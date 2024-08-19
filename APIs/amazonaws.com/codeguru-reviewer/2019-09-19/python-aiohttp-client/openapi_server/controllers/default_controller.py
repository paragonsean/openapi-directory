from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_repository_request import AssociateRepositoryRequest
from openapi_server.models.associate_repository_response import AssociateRepositoryResponse
from openapi_server.models.create_code_review_request import CreateCodeReviewRequest
from openapi_server.models.create_code_review_response import CreateCodeReviewResponse
from openapi_server.models.describe_code_review_response import DescribeCodeReviewResponse
from openapi_server.models.describe_recommendation_feedback_response import DescribeRecommendationFeedbackResponse
from openapi_server.models.describe_repository_association_response import DescribeRepositoryAssociationResponse
from openapi_server.models.disassociate_repository_response import DisassociateRepositoryResponse
from openapi_server.models.job_state import JobState
from openapi_server.models.list_code_reviews_response import ListCodeReviewsResponse
from openapi_server.models.list_recommendation_feedback_response import ListRecommendationFeedbackResponse
from openapi_server.models.list_recommendations_response import ListRecommendationsResponse
from openapi_server.models.list_repository_associations_response import ListRepositoryAssociationsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.provider_type import ProviderType
from openapi_server.models.put_recommendation_feedback_request import PutRecommendationFeedbackRequest
from openapi_server.models.repository_association_state import RepositoryAssociationState
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server import util


async def associate_repository(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_repository

    &lt;p&gt;Use to associate an Amazon Web Services CodeCommit repository or a repository managed by Amazon Web Services CodeStar Connections with Amazon CodeGuru Reviewer. When you associate a repository, CodeGuru Reviewer reviews source code changes in the repository&#39;s pull requests and provides automatic recommendations. You can view recommendations using the CodeGuru Reviewer console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendations.html\&quot;&gt;Recommendations in Amazon CodeGuru Reviewer&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;If you associate a CodeCommit or S3 repository, it must be in the same Amazon Web Services Region and Amazon Web Services account where its CodeGuru Reviewer code reviews are configured.&lt;/p&gt; &lt;p&gt;Bitbucket and GitHub Enterprise Server repositories are managed by Amazon Web Services CodeStar Connections to connect to CodeGuru Reviewer. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-associate-repository.html\&quot;&gt;Associate a repository&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide.&lt;/i&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot use the CodeGuru Reviewer SDK or the Amazon Web Services CLI to associate a GitHub repository with Amazon CodeGuru Reviewer. To associate a GitHub repository, use the console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-with-guru.html\&quot;&gt;Getting started with CodeGuru Reviewer&lt;/a&gt; in the &lt;i&gt;CodeGuru Reviewer User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/note&gt;

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
    body = AssociateRepositoryRequest.from_dict(body)
    return web.Response(status=200)


async def create_code_review(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_code_review

    Use to create a code review with a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html\&quot;&gt;CodeReviewType&lt;/a&gt; of &lt;code&gt;RepositoryAnalysis&lt;/code&gt;. This type of code review analyzes all code under a specified branch in an associated repository. &lt;code&gt;PullRequest&lt;/code&gt; code reviews are automatically triggered by a pull request.

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
    body = CreateCodeReviewRequest.from_dict(body)
    return web.Response(status=200)


async def describe_code_review(request: web.Request, code_review_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_code_review

    Returns the metadata associated with the code review along with its status.

    :param code_review_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object. 
    :type code_review_arn: str
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
    return web.Response(status=200)


async def describe_recommendation_feedback(request: web.Request, code_review_arn, recommendation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, user_id=None) -> web.Response:
    """describe_recommendation_feedback

    Describes the customer feedback for a CodeGuru Reviewer recommendation.

    :param code_review_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object. 
    :type code_review_arn: str
    :param recommendation_id: The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.
    :type recommendation_id: str
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
    :param user_id: &lt;p&gt;Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.&lt;/p&gt; &lt;p&gt; The &lt;code&gt;UserId&lt;/code&gt; is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\&quot;&gt; Specifying a Principal&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt;
    :type user_id: str

    """
    return web.Response(status=200)


async def describe_repository_association(request: web.Request, association_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_repository_association

    Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object that contains information about the requested repository association.

    :param association_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;.
    :type association_arn: str
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
    return web.Response(status=200)


async def disassociate_repository(request: web.Request, association_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_repository

    Removes the association between Amazon CodeGuru Reviewer and a repository.

    :param association_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;.
    :type association_arn: str
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
    return web.Response(status=200)


async def list_code_reviews(request: web.Request, type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, provider_types=None, states=None, repository_names=None, max_results=None, next_token=None) -> web.Response:
    """list_code_reviews

    Lists all the code reviews that the customer has created in the past 90 days.

    :param type: The type of code reviews to list in the response.
    :type type: str
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
    :param provider_types: List of provider types for filtering that needs to be applied before displaying the result. For example, &lt;code&gt;providerTypes&#x3D;[GitHub]&lt;/code&gt; lists code reviews from GitHub.
    :type provider_types: list | bytes
    :param states: &lt;p&gt;List of states for filtering that needs to be applied before displaying the result. For example, &lt;code&gt;states&#x3D;[Pending]&lt;/code&gt; lists code reviews in the Pending state.&lt;/p&gt; &lt;p&gt;The valid code review states are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Completed&lt;/code&gt;: The code review is complete.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Pending&lt;/code&gt;: The code review started and has not completed or failed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Failed&lt;/code&gt;: The code review failed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Deleting&lt;/code&gt;: The code review is being deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type states: list | bytes
    :param repository_names: List of repository names for filtering that needs to be applied before displaying the result.
    :type repository_names: List[str]
    :param max_results: The maximum number of results that are returned per call. The default is 100.
    :type max_results: int
    :param next_token: If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
    :type next_token: str

    """
    provider_types = [ProviderType.from_dict(d) for d in provider_types]
    states = [JobState.from_dict(d) for d in states]
    return web.Response(status=200)


async def list_recommendation_feedback(request: web.Request, code_review_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, user_ids=None, recommendation_ids=None) -> web.Response:
    """list_recommendation_feedback

    Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedbackSummary.html\&quot;&gt;RecommendationFeedbackSummary&lt;/a&gt; objects that contain customer recommendation feedback for all CodeGuru Reviewer users.

    :param code_review_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object. 
    :type code_review_arn: str
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
    :param next_token: If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
    :type next_token: str
    :param max_results: The maximum number of results that are returned per call. The default is 100.
    :type max_results: int
    :param user_ids: &lt;p&gt;An Amazon Web Services user&#39;s account ID or Amazon Resource Name (ARN). Use this ID to query the recommendation feedback for a code review from that user.&lt;/p&gt; &lt;p&gt; The &lt;code&gt;UserId&lt;/code&gt; is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\&quot;&gt; Specifying a Principal&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt;
    :type user_ids: List[str]
    :param recommendation_ids: Used to query the recommendation feedback for a given recommendation.
    :type recommendation_ids: List[str]

    """
    return web.Response(status=200)


async def list_recommendations(request: web.Request, code_review_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_recommendations

    Returns the list of all recommendations for a completed code review.

    :param code_review_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object. 
    :type code_review_arn: str
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
    :param next_token: Pagination token.
    :type next_token: str
    :param max_results: The maximum number of results that are returned per call. The default is 100.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_repository_associations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, provider_type=None, state=None, name=None, owner=None, max_results=None, next_token=None) -> web.Response:
    """list_repository_associations

    Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html\&quot;&gt;RepositoryAssociationSummary&lt;/a&gt; objects that contain summary information about a repository association. You can filter the returned list by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-ProviderType\&quot;&gt;ProviderType&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Name\&quot;&gt;Name&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-State\&quot;&gt;State&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Owner\&quot;&gt;Owner&lt;/a&gt;.

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
    :param provider_type: List of provider types to use as a filter.
    :type provider_type: list | bytes
    :param state: &lt;p&gt;List of repository association states to use as a filter.&lt;/p&gt; &lt;p&gt;The valid repository association states are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Associated&lt;/b&gt;: The repository association is complete.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Associating&lt;/b&gt;: CodeGuru Reviewer is:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your repository &lt;code&gt;ProviderType&lt;/code&gt; is &lt;code&gt;GitHub&lt;/code&gt;, &lt;code&gt;GitHub Enterprise Server&lt;/code&gt;, or &lt;code&gt;Bitbucket&lt;/code&gt;, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Failed&lt;/b&gt;: The repository failed to associate or disassociate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Disassociating&lt;/b&gt;: CodeGuru Reviewer is removing the repository&#39;s pull request notifications and source code access.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Disassociated&lt;/b&gt;: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html\&quot;&gt;Using tags to control access to associated repositories&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type state: list | bytes
    :param name: List of repository names to use as a filter.
    :type name: List[str]
    :param owner: List of owners to use as a filter. For Amazon Web Services CodeCommit, it is the name of the CodeCommit account that was used to associate the repository. For other repository source providers, such as Bitbucket and GitHub Enterprise Server, this is name of the account that was used to associate the repository. 
    :type owner: List[str]
    :param max_results: The maximum number of repository association results returned by &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If this parameter is not used, &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. 
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Treat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str

    """
    provider_type = [ProviderType.from_dict(d) for d in provider_type]
    state = [RepositoryAssociationState.from_dict(d) for d in state]
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns the list of tags associated with an associated repository resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;.
    :type resource_arn: str
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
    return web.Response(status=200)


async def put_recommendation_feedback(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_recommendation_feedback

    Stores customer feedback for a CodeGuru Reviewer recommendation. When this API is called again with different reactions the previous feedback is overwritten.

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
    body = PutRecommendationFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more tags to an associated repository.

    :param resource_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;.
    :type resource_arn: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes a tag from an associated repository.

    :param resource_arn: The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;.
    :type resource_arn: str
    :param tag_keys: A list of the keys for each tag you want to remove from an associated repository.
    :type tag_keys: List[str]
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
    return web.Response(status=200)
