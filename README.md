# py-multiapi

a python library for api.itayki.com


### Installation
 ```pip3 install py-multiapi```

### Example
   ```
from py_multiapi import multiapi
import asyncio
async def main():
    print(await multiapi.exec_code(lang="python3", code="print('Hello World')"))
asyncio.run(main())
```
## links

[pypi](https://pypi.org/project/py-multiapi)
