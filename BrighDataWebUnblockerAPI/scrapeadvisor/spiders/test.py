import scrapy
import os
from urllib.parse import urlparse


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = []  # Will be set dynamically if needed
    start_urls = []
    DEFAULT_VALUE = "N/A"


    def __init__(self, input_file=None, output_file=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_file = output_file
        if input_file:
            with open(input_file, 'r') as f:
                self.start_urls = [line.strip() for line in f if line.strip()]

    def start_requests(self):
        """Generate requests with BrightData proxy configuration"""
        proxy = os.getenv("BD_UNBLOCKER_PROXY", "")
        
        for url in self.start_urls:
            website = self._identify_website(url)
            antibot_type = self._identify_antibot_type(url)
            
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={
                    'website': website,
                    'antibot_type': antibot_type,
                    'proxy': proxy
                }
            )

    def _identify_website(self, url):
        """Identify the specific website based on URL domain"""
        domain = urlparse(url).netloc.lower()
        
        # Extract the main domain (remove www, subdomains, etc.)
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Known websites for identification
        known_websites = [
            'gucci.com', 'farfetch.com', 'harrods.com', 'indeed.com',
            'loccitane.com', 'leboncoin.fr', 'canadagoose.com', 
            'realestate.com.au', 'ssense.com', 'walmart.com'
        ]
        
        # Return the specific website domain
        for website in known_websites:
            if website in domain:
                return website
        
        # Default fallback
        return 'gucci.com'

    def _identify_antibot_type(self, url):
        """Identify the anti-bot system based on URL patterns"""
        domain = urlparse(url).netloc.lower()
        
        # Akamai sites
        if any(site in domain for site in ['gucci.com', 'farfetch.com']):
            return 'akamai'
        
        # Cloudflare sites
        elif any(site in domain for site in ['harrods.com', 'indeed.com']):
            return 'cloudflare'
        
        # DataDome sites
        elif any(site in domain for site in ['loccitane.com', 'leboncoin.fr']):
            return 'datadome'
        
        # Kasada sites
        elif any(site in domain for site in ['canadagoose.com', 'realestate.com.au']):
            return 'kasada'
        
        # PerimeterX sites
        elif any(site in domain for site in ['ssense.com', 'walmart.com']):
            return 'perimeterx'
        
        # Default fallback
        else:
            return 'akamai'

    def parse(self, response):
        """Parse response based on the identified website and anti-bot system"""
        status_code = response.status
        website = response.meta.get('website', 'unknown')
        antibot_type = response.meta.get('antibot_type', 'unknown')
        check_field = self.DEFAULT_VALUE
        
        try:
            check_field = self._extract_check_field(response, antibot_type)
        except Exception as e:
            self.logger.warning(f"Failed to extract check field for {response.url}: {e}")
            check_field = self.DEFAULT_VALUE

        yield {
            'url': response.url,
            'website': website,
            'status_code': status_code,
            'antibot': antibot_type.upper(),
            'check_field': check_field,
            'proxy_used': response.meta.get('proxy', 'N/A')
        }

    def _extract_check_field(self, response, antibot_type):
        """Extract check field based on anti-bot system and specific site patterns"""
        url = response.url.lower()
        
        if antibot_type == 'kasada':
            if 'canadagoose' in url:
                return response.xpath('//h1/text()').extract_first().strip()
            elif 'realestate.com.au' in url:
                return response.xpath('//h1/text()').extract_first().strip()
        
        elif antibot_type == 'cloudflare':
            if 'indeed' in url:
                return response.xpath('//title/text()').extract_first().strip()
            elif 'harrods' in url:
                # Try multiple selectors for Harrods
                selectors = [
                    '//h1/span/a/text()',
                    '//h1/span/text()',
                    '//h1/text()'
                ]
                for selector in selectors:
                    result = response.xpath(selector).extract_first()
                    if result and result.strip():
                        return result.strip()
        
        elif antibot_type == 'perimeterx':
            if 'ssense' in url:
                return response.xpath('//h1/a/text()').extract_first().strip()
            elif 'walmart' in url:
                return response.xpath('//h1/text()').extract_first().strip()
        
        elif antibot_type == 'akamai':
            if 'farfetch' in url:
                return response.xpath('//title/text()').extract_first().strip()
            elif 'gucci.com' in url:
                return response.xpath('//h1/text()').extract_first().strip()
        
        elif antibot_type == 'datadome':
            if 'loccitane' in url:
                return response.xpath('//h1/div/text()').extract_first().strip()
            elif 'leboncoin' in url:
                return response.xpath('//h1/text()').extract_first().strip()
        
        return self.DEFAULT_VALUE 