# py-multiapi

a python library for api.itaykibotsonetwo.ml


### Installation
 ```pip3 install git+https://github.com/iiiiii1wepfj/py_multiapi.git```

### Example
   ```
from py_multiapi import multiapi
import asyncio
async def main():
    print(await multiapi.exec_code(lang="python3", code="print('Hello World')"))
asyncio.run(main())
