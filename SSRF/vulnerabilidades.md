### Server Information Disclosure 
- **Endpoint:** localhost:56733/static

### SSRF
1. **Endpoint:** localhost:56733/service_status/<backdoor>

2. **Endpoint:** localhost:56733/full_ssrf?target=<backdoor>?