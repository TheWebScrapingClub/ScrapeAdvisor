# ScrapeAdvisor

ScrapeAdvisor, created by The Web Scraping Club, is an independent comparison platform for web scraping solutions. Our goal is to provide professionals with reliable, transparent, and actionable insights when choosing tools and services in this fast-evolving industry.

Unlike promotional reviews or vendor claims, ScrapeAdvisor is based on a standardized testing methodology. Each solution is evaluated within its category under comparable conditions, allowing results to be measured on equal terms. Key metrics include pricing, success rates, execution speed, and performance against various anti-bot technologies and websites.

All test procedures are designed to be as uniform and reproducible as possible. To ensure full transparency, the test code and datasets are publicly available on GitHub. This approach allows anyone to verify results, replicate experiments, or suggest improvements.

ScrapeAdvisor is built on the belief that better information leads to better decisions. By combining structured benchmarks with an open methodology, we aim to give developers, data teams, and organizations the clarity they need to select the most effective scraping solutions for their use cases.

## Test Categories

### Web Unblockers
Web unblockers are services that help bypass anti-bot protection and access websites that would otherwise block automated requests.

#### Tested Solutions:
- **Zyte API** - Cloud-based web scraping API with built-in anti-bot bypass capabilities

#### Test Methodology:
- **Anti-bot Systems Tested**: Akamai, Cloudflare, DataDome, Kasada, PerimeterX
- **Websites Tested**: 
  - Akamai: Gucci, Farfetch
  - Cloudflare: Harrods, Indeed
  - DataDome: L'Occitane, LeBonCoin
  - Kasada: Canada Goose, RealEstate.com.au
  - PerimeterX: SSENSE, Walmart
- **Metrics**: Success rates, execution times, response quality
- **Configuration**: Website-specific meta configurations optimized for each target

#### Results:
Test results are available in the respective output CSV files, with execution times tracked in `execution_times.txt`.
