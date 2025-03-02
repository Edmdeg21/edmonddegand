---

## 📜 2. metasploit-scan.sh (Bash Script)

```bash
#!/bin/bash

# Automated Metasploit auxiliary scan script
TARGET="192.168.1.100"

msfconsole -q -x "
use auxiliary/scanner/portscan/tcp;
set RHOSTS $TARGET;
set THREADS 10;
run;
use auxiliary/scanner/http/http_version;
set RHOSTS $TARGET;
run;
exit
"
