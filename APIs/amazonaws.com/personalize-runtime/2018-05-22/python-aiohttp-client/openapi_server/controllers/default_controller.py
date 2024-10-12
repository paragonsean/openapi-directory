from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_personalized_ranking_request import GetPersonalizedRankingRequest
from openapi_server.models.get_personalized_ranking_response import GetPersonalizedRankingResponse
from openapi_server.models.get_recommendations_request import GetRecommendationsRequest
from openapi_server.models.get_recommendations_response import GetRecommendationsResponse
from openapi_server import util


async def get_personalized_ranking(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_personalized_ranking

    &lt;p&gt;Re-ranks a list of recommended items for the given user. The first item in the list is deemed the most likely item to be of interest to the user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The solution backing the campaign must have been created using a recipe of type PERSONALIZED_RANKING.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetPersonalizedRankingRequest.from_dict(body)
    return web.Response(status=200)


async def get_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_recommendations

    &lt;p&gt;Returns a list of recommended items. For campaigns, the campaign&#39;s Amazon Resource Name (ARN) is required and the required user and item input depends on the recipe type used to create the solution backing the campaign as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;USER_PERSONALIZATION - &lt;code&gt;userId&lt;/code&gt; required, &lt;code&gt;itemId&lt;/code&gt; not used&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;RELATED_ITEMS - &lt;code&gt;itemId&lt;/code&gt; required, &lt;code&gt;userId&lt;/code&gt; not used&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Campaigns that are backed by a solution created using a recipe of type PERSONALIZED_RANKING use the API.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; For recommenders, the recommender&#39;s ARN is required and the required item and user input depends on the use case (domain-based recipe) backing the recommender. For information on use case requirements see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html\&quot;&gt;Choosing recommender use cases&lt;/a&gt;. &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetRecommendationsRequest.from_dict(body)
    return web.Response(status=200)
