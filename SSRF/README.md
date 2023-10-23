# Server-side request forgery (SSRF)
Falsificação de solicitação do lado do servidor (SSRF)


## 📚 Aprenda sobre SSRF

**CWE-918**
___

[Mitre](https://cwe.mitre.org/data/definitions/918.html)

[OWASP](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)

[Portswigger Academy](https://portswigger.net/web-security/ssrf)

[TryHackMe](https://tryhackme.com/room/ssrfqi)


## ⚠️ Vulnerabilidades neste laboratório 🚨
### Softwares desatualizados
- Python;
- Flask;

### Server Information Disclosure 
- **Endpoint:** localhost:56733/static

### SSRF
1. **Endpoint:** localhost:56733/param/<backdoor>

2. **Endpoint:** localhost:56733/args?target=<backdoor>?

___
## 🏗️ Referências para a construção deste lab
- https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04

- https://codeql.github.com/codeql-query-help/python/py-full-ssrf/

- https://docs.boostsecurity.io/rules/code-ssrf.html