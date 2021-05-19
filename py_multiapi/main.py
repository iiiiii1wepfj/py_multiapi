import httpx
from typing import Optional, Union

http = httpx.AsyncClient(http2=True)

api_url = "https://api.itayki.com"


class multiapi:
    @staticmethod
    async def get_exec_langs():
        a = (await http.get(f"{api_url}/execlangs")).json()
        await http.aclose()
        return a["langs"]

    @staticmethod
    async def exec_code(lang: str, code: str):
        if not (lang or code):
            return "please specify the code or the language"
        a = (
            await http.get(f"{api_url}/exec", params=dict(lang=lang, code=code))
        ).json()
        await http.aclose()
        if "Errors" in a:
            return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Errors:\n\n {a['Errors']}"
        elif "Stats" in a:
            return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Stats:\n\n {a['Stats']}"
        else:
            return a["langs"]

    @staticmethod
    async def ocr(url: str):
        if not url:
            return "please specify the url"
        a = (await http.get(f"{api_url}/ocr", params=dict(url=url))).json()
        await http.aclose()
        if "ocr" in a:
            return f"ocr: {a['ocr']}"
        elif "error" in a:
            return f"Error: {a['error']}"

    @staticmethod
    async def translate(
        text: str, fromlang: Optional[str] = None, lang: Optional[str] = "en"
    ):
        if not text:
            return "please specify the url"
        a = (
            (await http.get(f"{api_url}/tr", params=dict(text=text, lang=lang))).json()
            if not fromlang
            else (
                await http.get(
                    f"{api_url}/tr?text",
                    params=dict(text=text, fromlang=fromlang, lang=lang),
                )
            ).json()
        )
        await http.aclose()
        return f"Text: \n\n{a['text']}\n\nfrom language: {a['from_language']}\n\nto language: {a['to_language']}"

    @staticmethod
    async def urban(query: str):
        if not query:
            return "please specify the query"
        a = {
            x["term"]: x["preview"]
            for x in (await http.get(f"{api_url}/ud", params=dict(query=query))).json()[
                "results"
            ]
        }
        await http.aclose()
        return a

    @staticmethod
    async def webshot(
        url: str,
        width: Optional[int] = 1280,
        height: Optional[int] = 720,
    ):
        if not url:
            return "please specify the url"
        a = await http.get(
            f"{api_url}/print", params=dict(url=url, width=width, height=height)
        )
        await http.aclose()
        a = a.read()
        return a

    @staticmethod
    async def random_number(min: Union[int, str] = 1, max: Union[int, str] = 100):
        if not (min or max):
            return "please specify the min and max"
        a = (await http.get(f"{api_url}/random", params=dict(min=min, max=max))).json()
        await http.aclose()
        return a["number"]
