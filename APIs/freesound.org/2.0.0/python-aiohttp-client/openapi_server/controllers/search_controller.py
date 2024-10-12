from typing import List, Dict
from aiohttp import web

from openapi_server.models.sound import Sound
from openapi_server import util


async def search_text(request: web.Request, query=None, filter=None, sort=None, group_by_pack=None, page=None, page_size=None) -> web.Response:
    """Search sounds

    This resource allows searching sounds in Freesound by matching their tags and other kinds of metadata.

    :param query: The query! The query is the main parameter used to define a query. You can type several terms separated by spaces or phrases wrapped inside quote ‘”’ characters. For every term, you can also use ‘+’ and ‘-‘ modifier characters to indicate that a term is “mandatory” or “prohibited” (by default, terms are considered to be “mandatory”). For example, in a query such as query&#x3D;term_a -term_b, sounds including term_b will not match the search criteria. The query does a weighted search over some sound properties including sound tags, the sound name, its description, pack name and the sound id. Therefore, searching for query&#x3D;123 will find you sounds with id 1234, sounds that have 1234 in the description, in the tags, etc. You’ll find some examples below. Using an empty query (query&#x3D; or query&#x3D;\&quot;\&quot;) will return all Freeosund sounds.
    :type query: str
    :param filter: Allows filtering query results. See below for more information.
    :type filter: str
    :param sort: Indicates how query results should be sorted. See below for a list of the sorting options. By default &#x60;sort&#x3D;score&#x60;. &lt;p&gt; &lt;table&gt;   &lt;tr&gt;     &lt;th&gt;Option&lt;/th&gt;     &lt;th&gt;Explanation&lt;/th&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;score&lt;/td&gt;     &lt;td&gt;Sort by a relevance score returned by our search engine (default).&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;duration_desc     &lt;td&gt;Sort by the duration of the sounds, longest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;duration_asc     &lt;td&gt;Same as above, but shortest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;created_desc     &lt;td&gt;Sort by the date of when the sound was added. newest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;created_asc     &lt;td&gt;Same as above, but oldest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;downloads_desc     &lt;td&gt;Sort by the number of downloads, most downloaded sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;downloads_asc     &lt;td&gt;Same as above, but least downloaded sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;rating_desc     &lt;td&gt;Sort by the average rating given to the sounds, highest rated first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;rating_asc     &lt;td&gt;Same as above, but lowest rated sounds first.   &lt;/tr&gt; &lt;/table&gt; &lt;/p&gt;
    :type sort: str
    :param group_by_pack: This parameter represents a boolean option to indicate whether to collapse results belonging to sounds of the same pack into single entries in the results list. If &#x60;group_by_pack&#x3D;1&#x60; and search results contain more than one sound that belongs to the same pack, only one sound for each distinct pack is returned (sounds with no packs are returned as well). However, the returned sound will feature two extra properties to access these other sounds omitted from the results list: &#x60;n_from_same_pack&#x60;: indicates how many other results belong to the same pack (and have not been returned) &#x60;more_from_same_pack&#x60;: uri pointing to the list of omitted sound results of the same pack (also including the result which has already been returned). See examples below. By default &#x60;group_by_pack&#x3D;0&#x60;.
    :type group_by_pack: int
    :param page: Query results are paginated, this parameter indicates what page should be returned. By default &#x60;page&#x3D;1&#x60;.
    :type page: int
    :param page_size: Indicates the number of sounds per page to include in the result. By default &#x60;page_size&#x3D;15&#x60;, and the maximum is &#x60;page_size&#x3D;150&#x60;. Not that with bigger &#x60;page_size&#x60;, more data will need to be transferred.
    :type page_size: int

    """
    return web.Response(status=200)
