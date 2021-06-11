import httpx
from typing import Optional, Union


api_url = "https://api.itayki.com"


class multiapi:
    @staticmethod
    async def get_exec_langs():
        """
        Get the list of the supported languages to execute code using tio.run.
        """
        async with httpx.AsyncClient(http2=True) as http:
            a = (await http.get(f"{api_url}/execlangs")).json()
            return a["langs"]

    @staticmethod
    async def exec_code(lang: str, code: str):
        """
        Execute code using tio.run.
        parameters:
        lang: the language to execute,
        code: the code to execute.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not (lang or code):
                return "please specify the code or the language"
            a = (
                await http.get(f"{api_url}/exec", params=dict(lang=lang, code=code))
            ).json()
            if "Errors" in a:
                return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Errors:\n\n {a['Errors']}"
            elif "Stats" in a:
                return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Stats:\n\n {a['Stats']}"
            else:
                return a["langs"]

    @staticmethod
    async def ocr(url: str):
        """
        Get the text from the image.
        parameters:
        url: the url of the image.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not url:
                return "please specify the url"
            a = (await http.get(f"{api_url}/ocr", params=dict(url=url))).json()
            if "ocr" in a:
                return f"ocr: {a['ocr']}"
            elif "error" in a:
                return f"Error: {a['error']}"

    @staticmethod
    async def translate(
        text: str, fromlang: Optional[str] = None, lang: Optional[str] = "en"
    ):
        """
        Translate the specified text.
        parameters:
        text: the text to translate,
        fromlang (optional): the language code of the text to translate (if not specified, this is auto detect the text),
        lang (optional): the language code of the translated text (the output text) (if not specified, this is translate to english).
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not text:
                return "please specify the url"
            a = (
                (
                    await http.get(f"{api_url}/tr", params=dict(text=text, lang=lang))
                ).json()
                if not fromlang
                else (
                    await http.get(
                        f"{api_url}/tr?text",
                        params=dict(text=text, fromlang=fromlang, lang=lang),
                    )
                ).json()
            )
            if "error" in a:
                return a
            else:
                return f"Text: \n\n{a['text']}\n\nfrom language: {a['from_language']}\n\nto language: {a['to_language']}"

    @staticmethod
    async def urban(query: str):
        """
        Get the results from urban dictionary api.
        parameters:
        query: the query to search.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not query:
                return "please specify the query"
            a = {
                x["term"]: x["preview"]
                for x in (
                    await http.get(f"{api_url}/ud", params=dict(query=query))
                ).json()["results"]
            }
            return a

    @staticmethod
    async def webshot(
        url: str,
        width: Optional[int] = 1280,
        height: Optional[int] = 720,
    ):
        """
        Returns a screenshot of the specified site.
        parameters:
        url: the url of the site to screenshot,
        width (optional): the width of the screenshot (default to 1280),
        height (optional): the height code of the screenshot (default to 720).
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not url:
                return "please specify the url"
            a = await http.get(
                f"{api_url}/print", params=dict(url=url, width=width, height=height)
            )
            if "error" in a.json():
                a = f"Error: {(a.json())['error']}"
            else:
                a = a.read()
            return a

    @staticmethod
    async def random_number(min: Union[int, str] = 1, max: Union[int, str] = 100):
        """
        Returns a random number from the min parameter to the max parameter.
        parameters:
        min (optional): the minimum number (default to 1),
        max (optional): the maximum number (default to 100).
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not (min or max):
                return "please specify the min and max"
            a = (
                await http.get(f"{api_url}/random", params=dict(min=min, max=max))
            ).json()
            return a["number"]

    @staticmethod
    async def pypi_search(package: str):
        """
        Search python packages on pypi.
        parameters:
        package: the name of the package.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not package:
                return "please specify package name"
            a = (await http.get(f"{api_url}/pypi", params=dict(package=package))).json()
            return a

    @staticmethodimport httpx
from typing import Optional, Union


api_url = "https://api.itayki.com"


class multiapi:
    @staticmethod
    async def get_exec_langs():
        """
        Get the list of the supported languages to execute code using tio.run.
        """
        async with httpx.AsyncClient(http2=True) as http:
            a = (await http.get(f"{api_url}/execlangs")).json()
            return a["langs"]

    @staticmethod
    async def exec_code(lang: str, code: str):
        """
        Execute code using tio.run.
        parameters:
        lang: the language to execute,
        code: the code to execute.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not (lang or code):
                return "please specify the code or the language"
            a = (
                await http.get(f"{api_url}/exec", params=dict(lang=lang, code=code))
            ).json()
            if "Errors" in a:
                return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Errors:\n\n {a['Errors']}"
            elif "Stats" in a:
                return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Stats:\n\n {a['Stats']}"
            else:
                return a["langs"]

    @staticmethod
    async def ocr(url: str):
        """
        Get the text from the image.
        parameters:
        url: the url of the image.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not url:
                return "please specify the url"
            a = (await http.get(f"{api_url}/ocr", params=dict(url=url))).json()
            if "ocr" in a:
                return f"ocr: {a['ocr']}"
            elif "error" in a:
                return f"Error: {a['error']}"

    @staticmethod
    async def translate(
        text: str, fromlang: Optional[str] = None, lang: Optional[str] = "en"
    ):
        """
        Translate the specified text.
        parameters:
        text: the text to translate,
        fromlang (optional): the language code of the text to translate (if not specified, this is auto detect the text),
        lang (optional): the language code of the translated text (the output text) (if not specified, this is translate to english).
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not text:
                return "please specify the url"
            a = (
                (
                    await http.get(f"{api_url}/tr", params=dict(text=text, lang=lang))
                ).json()
                if not fromlang
                else (
                    await http.get(
                        f"{api_url}/tr?text",
                        params=dict(text=text, fromlang=fromlang, lang=lang),
                    )
                ).json()
            )
            if "error" in a:
                return a
            else:
                return f"Text: \n\n{a['text']}\n\nfrom language: {a['from_language']}\n\nto language: {a['to_language']}"

    @staticmethod
    async def urban(query: str):
        """
        Get the results from urban dictionary api.
        parameters:
        query: the query to search.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not query:
                return "please specify the query"
            a = {
                x["term"]: x["preview"]
                for x in (
                    await http.get(f"{api_url}/ud", params=dict(query=query))
                ).json()["results"]
            }
            return a

    @staticmethod
    async def webshot(
        url: str,
        width: Optional[int] = 1280,
        height: Optional[int] = 720,
    ):
        """
        Returns a screenshot of the specified site.
        parameters:
        url: the url of the site to screenshot,
        width (optional): the width of the screenshot (default to 1280),
        height (optional): the height code of the screenshot (default to 720).
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not url:
                return "please specify the url"
            a = await http.get(
                f"{api_url}/print", params=dict(url=url, width=width, height=height)
            )
            if "error" in a.json():
                a = f"Error: {(a.json())['error']}"
            else:
                a = a.read()
            return a

    @staticmethod
    async def random_number(min: Union[int, str] = 1, max: Union[int, str] = 100):
        """
        Returns a random number from the min parameter to the max parameter.
        parameters:
        min (optional): the minimum number (default to 1),
        max (optional): the maximum number (default to 100).
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not (min or max):
                return "please specify the min and max"
            a = (
                await http.get(f"{api_url}/random", params=dict(min=min, max=max))
            ).json()
            return a["number"]

    @staticmethod
    async def pypi_search(package: str):
        """
        Search python packages on pypi.
        parameters:
        package: the name of the package.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not package:
                return "please specify package name"
            a = (await http.get(f"{api_url}/pypi", params=dict(package=package))).json()
            return a

    @staticmethod
    async def paste(
        content: str, title: Optional[str] = None, author: Optional[str] = None
    ):
        """
        Paste the text in nekobin.com.
        parameters:
        content: the text to paste,
        title (optional): the title,
        author (optional): the author.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not content:
                return "please specify the content"
            a = (
                await http.get(
                    f"{api_url}/paste",
                    params=dict(content=content, title=title, author=author),
                )
            ).json()
            return a

    @staticmethod
    async def get_paste(paste: str):
        """
        Get the paste data from nekobin.com.
        parameters:
        paste: the paste.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not paste:
                return "please specify the paste"
            a = (
                await http.get(f"{api_url}/get_paste", params=dict(paste=paste))
            ).json()
            return a
    async def paste(
        content: str, title: Optional[str] = None, author: Optional[str] = None
    ):
        """
        Paste the text in nekobin.com.
        parameters:
        content: the text to paste,
        title (optional): the title,
        author (optional): the author.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not content:
                return "please specify the content"
            a = (
                await http.get(
                    f"{api_url}/paste",
                    params=dict(content=content, title=title, author=author),
                )
            ).json()
            return a

    @staticmethod
    async def get_paste(paste: str):
        """
        Get the paste data from nekobin.com.
        parameters:
        paste: the paste.
        """
        async with httpx.AsyncClient(http2=True) as http:
            if not paste:
                return "please specify the paste"
            a = (
                await http.get(f"{api_url}/get_paste", params=dict(paste=paste))
            ).json()
            return a
