from typing import List, Dict
from aiohttp import web

from openapi_server.models.parserequest import Parserequest
from openapi_server import util


async def parse(request: web.Request, body) -> web.Response:
    """Extract structured data from web pages

    Dataflow kit uses CSS selectors to find HTML elements in web pages for later data extraction.  Open [visual point-and-click toolkit](https://dataflowkit.com/dfk) and click desired elements on a page to specify extracting data.     Then you can send generated payload to &#x60;/parse&#x60; endpoint. We crawl web pages and extract data like text, links, or images for you following the specified rules.    Extracted data is returned in CSV, MS Excel, JSON, JSON(Lines) or XML format. 

    :param body: ### Field types and attributes    - **Text**. Extract human-readable text from the selected element and all its child elements. HTML tags are stripped, and only text returned.      - **Link**. Capture link &#x60;href&#x60; attribute and link text. Or specify a special _Path_ option for website navigation. When Path option is true, all other selectors ignored, and no results from the current page returned.      - **Image**. Image type extracts &#x60;src&#x60; (URL) and &#x60;alt&#x60; attributes of an image   *** ### Filters Filters are used to manipulate text data when extracting.  Here is the list of available filters   - **Trim** removes leading and trailing white spaces from the _field text or attribute_  - **Normal** leaves the case and capitalization of text/ attribute exactly as is.  - **UPPERCASE** makes all of the letters in the Field&#39;s text/ attribute uppercase.  - **lowercase** makes all of the letters in the Field&#39;s text/ attribute lowercase.  - **Capitalize** capitalizes the first letter of each word in the Field&#39;s text/ attribute  - **Concatinate** joins text array element into a single string  *** ### Regular Expressions  For more advanced text formatting regular expression can be used. Some useful examples are listed below   | Input text | Regex | Result | | ---------- | ----- | ------ | | price- 10.99€ | &lt;code&gt;[0-9]+\\.[0-9]+&lt;/code&gt; | 10.99 | | phone- 0 (944) 244-18-22 | &lt;code&gt;\\w+&lt;/code&gt; | 09442441822 |   *** ### Details. Chaining. The Link field type serves as a navigation link to a details page containing more data. A special _Path_ option is used for navigation only. When the Path option specified, no results from the current page returned. But grouped results from details pages will be pulled instead. You can use chaining functionality of Dataflow Kit scraper to retrieve all the detail page data at the same time. 
    :type body: dict | bytes

    """
    body = Parserequest.from_dict(body)
    return web.Response(status=200)
