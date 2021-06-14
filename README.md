# py-multiapi

a python library for api.itayki.com


### Installation
 ```pip3 install py-multiapi```

### Examples
execute code:

   ```
from py_multiapi import multiapi
import asyncio
async def main():
    print(await multiapi.exec_code(lang="python3", code="print('Hello World')"))
asyncio.run(main())
```
make web screenshot:

   ```
from py_multiapi import multiapi
import asyncio
async def main():
    a = await multiapi.webshot(url="duckduckgo.com")
    with open("test.png", "wb") as img:
        img.write(a)
asyncio.run(main())
```

get help from the function:

```
from py_multiapi import multiapi
def main_help():
    print(help(multiapi.exec_code))
main_help()
```


## links

[pypi](https://pypi.org/project/py-multiapi)


# versions in other languages
 nodejs https://github.com/AndrewLaneX/multiapi
 
 golang https://github.com/rojserbest/multiapi
