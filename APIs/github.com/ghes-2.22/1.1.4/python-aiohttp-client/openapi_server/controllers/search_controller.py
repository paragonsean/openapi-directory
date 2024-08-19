from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.search_code200_response import SearchCode200Response
from openapi_server.models.search_commits200_response import SearchCommits200Response
from openapi_server.models.search_issues_and_pull_requests200_response import SearchIssuesAndPullRequests200Response
from openapi_server.models.search_labels200_response import SearchLabels200Response
from openapi_server.models.search_repos200_response import SearchRepos200Response
from openapi_server.models.search_topics200_response import SearchTopics200Response
from openapi_server.models.search_users200_response import SearchUsers200Response
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def search_code(request: web.Request, q, sort=None, order=None, per_page=None, page=None) -> web.Response:
    """Search code

    Searches for query terms inside of a file. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination).  When searching for code, you can get text match metadata for the file **content** and file **path** fields when you pass the &#x60;text-match&#x60; media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you want to find the definition of the &#x60;addClass&#x60; function inside [jQuery](https://github.com/jquery/jquery) repository, your query would look something like this:  &#x60;q&#x3D;addClass+in:file+language:js+repo:jquery/jquery&#x60;  This query searches for the keyword &#x60;addClass&#x60; within a file&#39;s contents. The query limits the search to files where the language is JavaScript in the &#x60;jquery/jquery&#x60; repository.  #### Considerations for code search  Due to the complexity of searching code, there are a few restrictions on how searches are performed:  *   Only the _default branch_ is considered. In most cases, this will be the &#x60;master&#x60; branch. *   Only files smaller than 384 KB are searchable. *   You must always include at least one search term when searching source code. For example, searching for [&#x60;language:go&#x60;](https://github.com/search?utf8&#x3D;%E2%9C%93&amp;q&#x3D;language%3Ago&amp;type&#x3D;Code) is not valid, while [&#x60;amazing language:go&#x60;](https://github.com/search?utf8&#x3D;%E2%9C%93&amp;q&#x3D;amazing+language%3Ago&amp;type&#x3D;Code) is.

    :param q: The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query). See \&quot;[Searching code](https://help.github.com/articles/searching-code/)\&quot; for a detailed list of qualifiers.
    :type q: str
    :param sort: Sorts the results of your query. Can only be &#x60;indexed&#x60;, which indicates how recently a file has been indexed by the GitHub Enterprise Server search infrastructure. Default: [best match](https://docs.github.com/enterprise-server@2.22/rest/reference/search#ranking-search-results)
    :type sort: str
    :param order: Determines whether the first search result returned is the highest number of matches (&#x60;desc&#x60;) or lowest number of matches (&#x60;asc&#x60;). This parameter is ignored unless you provide &#x60;sort&#x60;.
    :type order: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def search_commits(request: web.Request, q, sort=None, order=None, per_page=None, page=None) -> web.Response:
    """Search commits

    Find commits via various criteria on the default branch (usually &#x60;master&#x60;). This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination).  When searching for commits, you can get text match metadata for the **message** field when you provide the &#x60;text-match&#x60; media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you want to find commits related to CSS in the [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) repository. Your query would look something like this:  &#x60;q&#x3D;repo:octocat/Spoon-Knife+css&#x60;

    :param q: The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query). See \&quot;[Searching commits](https://help.github.com/articles/searching-commits/)\&quot; for a detailed list of qualifiers.
    :type q: str
    :param sort: Sorts the results of your query by &#x60;author-date&#x60; or &#x60;committer-date&#x60;. Default: [best match](https://docs.github.com/enterprise-server@2.22/rest/reference/search#ranking-search-results)
    :type sort: str
    :param order: Determines whether the first search result returned is the highest number of matches (&#x60;desc&#x60;) or lowest number of matches (&#x60;asc&#x60;). This parameter is ignored unless you provide &#x60;sort&#x60;.
    :type order: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def search_issues_and_pull_requests(request: web.Request, q, sort=None, order=None, per_page=None, page=None) -> web.Response:
    """Search issues and pull requests

    Find issues by state and keyword. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination).  When searching for issues, you can get text match metadata for the issue **title**, issue **body**, and issue **comment body** fields when you pass the &#x60;text-match&#x60; media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you want to find the oldest unresolved Python bugs on Windows. Your query might look something like this.  &#x60;q&#x3D;windows+label:bug+language:python+state:open&amp;sort&#x3D;created&amp;order&#x3D;asc&#x60;  This query searches for the keyword &#x60;windows&#x60;, within any open issue that is labeled as &#x60;bug&#x60;. The search runs across repositories whose primary language is Python. The results are sorted by creation date in ascending order, which means the oldest issues appear first in the search results.  **Note:** For [user-to-server](https://docs.github.com/developers/apps/identifying-and-authorizing-users-for-github-apps#user-to-server-requests) GitHub App requests, you can&#39;t retrieve a combination of issues and pull requests in a single query. Requests that don&#39;t include the &#x60;is:issue&#x60; or &#x60;is:pull-request&#x60; qualifier will receive an HTTP &#x60;422 Unprocessable Entity&#x60; response. To get results for both issues and pull requests, you must send separate queries for issues and pull requests. For more information about the &#x60;is&#x60; qualifier, see \&quot;[Searching only issues or pull requests](https://docs.github.com/github/searching-for-information-on-github/searching-issues-and-pull-requests#search-only-issues-or-pull-requests).\&quot;

    :param q: The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query). See \&quot;[Searching issues and pull requests](https://help.github.com/articles/searching-issues-and-pull-requests/)\&quot; for a detailed list of qualifiers.
    :type q: str
    :param sort: Sorts the results of your query by the number of &#x60;comments&#x60;, &#x60;reactions&#x60;, &#x60;reactions-+1&#x60;, &#x60;reactions--1&#x60;, &#x60;reactions-smile&#x60;, &#x60;reactions-thinking_face&#x60;, &#x60;reactions-heart&#x60;, &#x60;reactions-tada&#x60;, or &#x60;interactions&#x60;. You can also sort results by how recently the items were &#x60;created&#x60; or &#x60;updated&#x60;, Default: [best match](https://docs.github.com/enterprise-server@2.22/rest/reference/search#ranking-search-results)
    :type sort: str
    :param order: Determines whether the first search result returned is the highest number of matches (&#x60;desc&#x60;) or lowest number of matches (&#x60;asc&#x60;). This parameter is ignored unless you provide &#x60;sort&#x60;.
    :type order: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def search_labels(request: web.Request, repository_id, q, sort=None, order=None, per_page=None, page=None) -> web.Response:
    """Search labels

    Find labels in a repository with names or descriptions that match search keywords. Returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination).  When searching for labels, you can get text match metadata for the label **name** and **description** fields when you pass the &#x60;text-match&#x60; media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you want to find labels in the &#x60;linguist&#x60; repository that match &#x60;bug&#x60;, &#x60;defect&#x60;, or &#x60;enhancement&#x60;. Your query might look like this:  &#x60;q&#x3D;bug+defect+enhancement&amp;repository_id&#x3D;64778136&#x60;  The labels that best match the query appear first in the search results.

    :param repository_id: The id of the repository.
    :type repository_id: int
    :param q: The search keywords. This endpoint does not accept qualifiers in the query. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query).
    :type q: str
    :param sort: Sorts the results of your query by when the label was &#x60;created&#x60; or &#x60;updated&#x60;. Default: [best match](https://docs.github.com/enterprise-server@2.22/rest/reference/search#ranking-search-results)
    :type sort: str
    :param order: Determines whether the first search result returned is the highest number of matches (&#x60;desc&#x60;) or lowest number of matches (&#x60;asc&#x60;). This parameter is ignored unless you provide &#x60;sort&#x60;.
    :type order: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def search_repos(request: web.Request, q, sort=None, order=None, per_page=None, page=None) -> web.Response:
    """Search repositories

    Find repositories via various criteria. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination).  When searching for repositories, you can get text match metadata for the **name** and **description** fields when you pass the &#x60;text-match&#x60; media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you want to search for popular Tetris repositories written in assembly code, your query might look like this:  &#x60;q&#x3D;tetris+language:assembly&amp;sort&#x3D;stars&amp;order&#x3D;desc&#x60;  This query searches for repositories with the word &#x60;tetris&#x60; in the name, the description, or the README. The results are limited to repositories where the primary language is assembly. The results are sorted by stars in descending order, so that the most popular repositories appear first in the search results.  When you include the &#x60;mercy&#x60; preview header, you can also search for multiple topics by adding more &#x60;topic:&#x60; instances. For example, your query might look like this:  &#x60;q&#x3D;topic:ruby+topic:rails&#x60;

    :param q: The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query). See \&quot;[Searching for repositories](https://help.github.com/articles/searching-for-repositories/)\&quot; for a detailed list of qualifiers.
    :type q: str
    :param sort: Sorts the results of your query by number of &#x60;stars&#x60;, &#x60;forks&#x60;, or &#x60;help-wanted-issues&#x60; or how recently the items were &#x60;updated&#x60;. Default: [best match](https://docs.github.com/enterprise-server@2.22/rest/reference/search#ranking-search-results)
    :type sort: str
    :param order: Determines whether the first search result returned is the highest number of matches (&#x60;desc&#x60;) or lowest number of matches (&#x60;asc&#x60;). This parameter is ignored unless you provide &#x60;sort&#x60;.
    :type order: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def search_topics(request: web.Request, q, per_page=None, page=None) -> web.Response:
    """Search topics

    Find topics via various criteria. Results are sorted by best match. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination). See \&quot;[Searching topics](https://help.github.com/articles/searching-topics/)\&quot; for a detailed list of qualifiers.  When searching for topics, you can get text match metadata for the topic&#39;s **short\\_description**, **description**, **name**, or **display\\_name** field when you pass the &#x60;text-match&#x60; media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you want to search for topics related to Ruby that are featured on https://github.com/topics. Your query might look like this:  &#x60;q&#x3D;ruby+is:featured&#x60;  This query searches for topics with the keyword &#x60;ruby&#x60; and limits the results to find only topics that are featured. The topics that are the best match for the query appear first in the search results.

    :param q: The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query).
    :type q: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def search_users(request: web.Request, q, sort=None, order=None, per_page=None, page=None) -> web.Response:
    """Search users

    Find users via various criteria. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#pagination).  When searching for users, you can get text match metadata for the issue **login**, **email**, and **name** fields when you pass the &#x60;text-match&#x60; media type. For more details about highlighting search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata). For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@2.22/rest/reference/search#text-match-metadata).  For example, if you&#39;re looking for a list of popular users, you might try this query:  &#x60;q&#x3D;tom+repos:%3E42+followers:%3E1000&#x60;  This query searches for users with the name &#x60;tom&#x60;. The results are restricted to users with more than 42 repositories and over 1,000 followers.

    :param q: The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/enterprise-server@2.22/rest/reference/search#constructing-a-search-query). See \&quot;[Searching users](https://help.github.com/articles/searching-users/)\&quot; for a detailed list of qualifiers.
    :type q: str
    :param sort: Sorts the results of your query by number of &#x60;followers&#x60; or &#x60;repositories&#x60;, or when the person &#x60;joined&#x60; GitHub Enterprise Server. Default: [best match](https://docs.github.com/enterprise-server@2.22/rest/reference/search#ranking-search-results)
    :type sort: str
    :param order: Determines whether the first search result returned is the highest number of matches (&#x60;desc&#x60;) or lowest number of matches (&#x60;asc&#x60;). This parameter is ignored unless you provide &#x60;sort&#x60;.
    :type order: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)
