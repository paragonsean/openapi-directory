from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.commit import Commit
from openapi_server.models.diff_entry import DiffEntry
from openapi_server.models.enterprise_admin_update_org_name202_response import EnterpriseAdminUpdateOrgName202Response
from openapi_server.models.legacy_review_comment import LegacyReviewComment
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.pull_request import PullRequest
from openapi_server.models.pull_request_merge_result import PullRequestMergeResult
from openapi_server.models.pull_request_review import PullRequestReview
from openapi_server.models.pull_request_review_comment import PullRequestReviewComment
from openapi_server.models.pull_request_review_request import PullRequestReviewRequest
from openapi_server.models.pull_request_simple import PullRequestSimple
from openapi_server.models.pulls_create_reply_for_review_comment_request import PullsCreateReplyForReviewCommentRequest
from openapi_server.models.pulls_create_request import PullsCreateRequest
from openapi_server.models.pulls_create_review_comment_alternative_request import PullsCreateReviewCommentAlternativeRequest
from openapi_server.models.pulls_create_review_request import PullsCreateReviewRequest
from openapi_server.models.pulls_dismiss_review_request import PullsDismissReviewRequest
from openapi_server.models.pulls_merge_request import PullsMergeRequest
from openapi_server.models.pulls_remove_requested_reviewers_request import PullsRemoveRequestedReviewersRequest
from openapi_server.models.pulls_request_reviewers_request import PullsRequestReviewersRequest
from openapi_server.models.pulls_submit_review_request import PullsSubmitReviewRequest
from openapi_server.models.pulls_update_branch_request import PullsUpdateBranchRequest
from openapi_server.models.pulls_update_request import PullsUpdateRequest
from openapi_server.models.pulls_update_review_comment_request import PullsUpdateReviewCommentRequest
from openapi_server.models.pulls_update_review_request import PullsUpdateReviewRequest
from openapi_server.models.review_comment import ReviewComment
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple
from openapi_server import util


async def pulls_check_if_merged(request: web.Request, owner, repo, pull_number) -> web.Response:
    """Check if a pull request has been merged

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int

    """
    return web.Response(status=200)


async def pulls_create(request: web.Request, owner, repo, body) -> web.Response:
    """Create a pull request

    Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud. You can create a new pull request. This endpoint triggers [notifications](https://docs.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = PullsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_create_reply_for_review_comment(request: web.Request, owner, repo, pull_number, comment_id, body) -> web.Response:
    """Create a reply for a review comment

    Creates a reply to a review comment for a pull request. For the &#x60;comment_id&#x60;, provide the ID of the review comment you are replying to. This must be the ID of a _top-level review comment_, not a reply to that comment. Replies to replies are not supported.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsCreateReplyForReviewCommentRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_create_review(request: web.Request, owner, repo, pull_number, body=None) -> web.Response:
    """Create a review for a pull request

    This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  Pull request reviews created in the &#x60;PENDING&#x60; state do not include the &#x60;submitted_at&#x60; property in the response.  **Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API v3 offers the &#x60;application/vnd.github.v3.diff&#x60; [media type](https://docs.github.com/enterprise-server@2.18/rest/overview/media-types#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the &#x60;Accept&#x60; header of a call to the [single pull request](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#get-a-pull-request) endpoint.  The &#x60;position&#x60; value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsCreateReviewRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_create_review_comment_alternative(request: web.Request, owner, repo, pull_number, body) -> web.Response:
    """Create a review comment for a pull request (alternative)

    Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see \&quot;[Create an issue comment](https://docs.github.com/enterprise-server@2.18/rest/reference/issues#create-an-issue-comment).\&quot;  **Note:** The position value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsCreateReviewCommentAlternativeRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_delete_pending_review(request: web.Request, owner, repo, pull_number, review_id) -> web.Response:
    """Delete a pending review for a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param review_id: review_id parameter
    :type review_id: int

    """
    return web.Response(status=200)


async def pulls_delete_review_comment(request: web.Request, owner, repo, comment_id) -> web.Response:
    """Delete a review comment for a pull request

    Deletes a review comment.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def pulls_dismiss_review(request: web.Request, owner, repo, pull_number, review_id, body) -> web.Response:
    """Dismiss a review for a pull request

    **Note:** To dismiss a pull request review on a [protected branch](https://docs.github.com/enterprise-server@2.18/rest/reference/repos#branches), you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param review_id: review_id parameter
    :type review_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsDismissReviewRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_get(request: web.Request, owner, repo, pull_number) -> web.Response:
    """Get a pull request

    Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists details of a pull request by providing its number.  When you get, [create](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls/#create-a-pull-request), or [edit](https://docs.github.com/enterprise-server@2.18/rest/reference/pulls#update-a-pull-request) a pull request, GitHub Enterprise Server creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the &#x60;mergeable&#x60; key. For more information, see \&quot;[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@2.18/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)\&quot;.  The value of the &#x60;mergeable&#x60; attribute can be &#x60;true&#x60;, &#x60;false&#x60;, or &#x60;null&#x60;. If the value is &#x60;null&#x60;, then GitHub Enterprise Server has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-&#x60;null&#x60; value for the &#x60;mergeable&#x60; attribute in the response. If &#x60;mergeable&#x60; is &#x60;true&#x60;, then &#x60;merge_commit_sha&#x60; will be the SHA of the _test_ merge commit.  The value of the &#x60;merge_commit_sha&#x60; attribute changes depending on the state of the pull request. Before merging a pull request, the &#x60;merge_commit_sha&#x60; attribute holds the SHA of the _test_ merge commit. After merging a pull request, the &#x60;merge_commit_sha&#x60; attribute changes depending on how you merged the pull request:  *   If merged as a [merge commit](https://help.github.com/articles/about-merge-methods-on-github/), &#x60;merge_commit_sha&#x60; represents the SHA of the merge commit. *   If merged via a [squash](https://help.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits), &#x60;merge_commit_sha&#x60; represents the SHA of the squashed commit on the base branch. *   If [rebased](https://help.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), &#x60;merge_commit_sha&#x60; represents the commit that the base branch was updated to.  Pass the appropriate [media type](https://docs.github.com/enterprise-server@2.18/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int

    """
    return web.Response(status=200)


async def pulls_get_review(request: web.Request, owner, repo, pull_number, review_id) -> web.Response:
    """Get a review for a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param review_id: review_id parameter
    :type review_id: int

    """
    return web.Response(status=200)


async def pulls_get_review_comment(request: web.Request, owner, repo, comment_id) -> web.Response:
    """Get a review comment for a pull request

    Provides details for a review comment.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def pulls_list(request: web.Request, owner, repo, state=None, head=None, base=None, sort=None, direction=None, per_page=None, page=None) -> web.Response:
    """List pull requests

    Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param state: Either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60; to filter by state.
    :type state: str
    :param head: Filter pulls by head user or head organization and branch name in the format of &#x60;user:ref-name&#x60; or &#x60;organization:ref-name&#x60;. For example: &#x60;github:new-script-format&#x60; or &#x60;octocat:test-branch&#x60;.
    :type head: str
    :param base: Filter pulls by base branch name. Example: &#x60;gh-pages&#x60;.
    :type base: str
    :param sort: What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;popularity&#x60; (comment count) or &#x60;long-running&#x60; (age, filtering by pulls updated in the last month).
    :type sort: str
    :param direction: The direction of the sort. Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;desc&#x60; when sort is &#x60;created&#x60; or sort is not specified, otherwise &#x60;asc&#x60;.
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def pulls_list_comments_for_review(request: web.Request, owner, repo, pull_number, review_id, per_page=None, page=None) -> web.Response:
    """List comments for a pull request review

    List comments for a specific pull request review.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param review_id: review_id parameter
    :type review_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def pulls_list_commits(request: web.Request, owner, repo, pull_number, per_page=None, page=None) -> web.Response:
    """List commits on a pull request

    Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://docs.github.com/enterprise-server@2.18/rest/reference/repos#list-commits) endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def pulls_list_files(request: web.Request, owner, repo, pull_number, per_page=None, page=None) -> web.Response:
    """List pull requests files

    **Note:** Responses include a maximum of 3000 files. The paginated response returns 30 files per page by default.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def pulls_list_requested_reviewers(request: web.Request, owner, repo, pull_number, per_page=None, page=None) -> web.Response:
    """List requested reviewers for a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def pulls_list_review_comments(request: web.Request, owner, repo, pull_number, sort=None, direction=None, since=None, per_page=None, page=None) -> web.Response:
    """List review comments on a pull request

    Lists all review comments for a pull request. By default, review comments are in ascending order by ID.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param sort: One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to).
    :type sort: str
    :param direction: Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter.
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def pulls_list_review_comments_for_repo(request: web.Request, owner, repo, sort=None, direction=None, since=None, per_page=None, page=None) -> web.Response:
    """List review comments in a repository

    Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param sort: 
    :type sort: str
    :param direction: Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter.
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def pulls_list_reviews(request: web.Request, owner, repo, pull_number, per_page=None, page=None) -> web.Response:
    """List reviews for a pull request

    The list of reviews returns in chronological order.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def pulls_merge(request: web.Request, owner, repo, pull_number, body=None) -> web.Response:
    """Merge a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsMergeRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_remove_requested_reviewers(request: web.Request, owner, repo, pull_number, body) -> web.Response:
    """Remove requested reviewers from a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsRemoveRequestedReviewersRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_request_reviewers(request: web.Request, owner, repo, pull_number, body=None) -> web.Response:
    """Request reviewers for a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsRequestReviewersRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_submit_review(request: web.Request, owner, repo, pull_number, review_id, body) -> web.Response:
    """Submit a review for a pull request

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param review_id: review_id parameter
    :type review_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsSubmitReviewRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_update(request: web.Request, owner, repo, pull_number, body=None) -> web.Response:
    """Update a pull request

    Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_update_branch(request: web.Request, owner, repo, pull_number, body=None) -> web.Response:
    """Update a pull request branch

    Updates the pull request branch with the latest upstream changes by merging HEAD from the base branch into the pull request branch.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsUpdateBranchRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_update_review(request: web.Request, owner, repo, pull_number, review_id, body) -> web.Response:
    """Update a review for a pull request

    Update the review summary comment with new text.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pull_number: 
    :type pull_number: int
    :param review_id: review_id parameter
    :type review_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsUpdateReviewRequest.from_dict(body)
    return web.Response(status=200)


async def pulls_update_review_comment(request: web.Request, owner, repo, comment_id, body) -> web.Response:
    """Update a review comment for a pull request

    Enables you to edit a review comment.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullsUpdateReviewCommentRequest.from_dict(body)
    return web.Response(status=200)
