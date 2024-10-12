from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_time_option import AddTimeOption
from openapi_server.models.attachment import Attachment
from openapi_server.models.comment import Comment
from openapi_server.models.create_issue_comment_option import CreateIssueCommentOption
from openapi_server.models.create_issue_option import CreateIssueOption
from openapi_server.models.create_label_option import CreateLabelOption
from openapi_server.models.create_milestone_option import CreateMilestoneOption
from openapi_server.models.edit_attachment_options import EditAttachmentOptions
from openapi_server.models.edit_deadline_option import EditDeadlineOption
from openapi_server.models.edit_issue_comment_option import EditIssueCommentOption
from openapi_server.models.edit_issue_option import EditIssueOption
from openapi_server.models.edit_label_option import EditLabelOption
from openapi_server.models.edit_milestone_option import EditMilestoneOption
from openapi_server.models.edit_reaction_option import EditReactionOption
from openapi_server.models.issue import Issue
from openapi_server.models.issue_deadline import IssueDeadline
from openapi_server.models.issue_labels_option import IssueLabelsOption
from openapi_server.models.issue_meta import IssueMeta
from openapi_server.models.label import Label
from openapi_server.models.milestone import Milestone
from openapi_server.models.reaction import Reaction
from openapi_server.models.timeline_comment import TimelineComment
from openapi_server.models.tracked_time import TrackedTime
from openapi_server.models.user import User
from openapi_server.models.watch_info import WatchInfo
from openapi_server import util


async def issue_add_label(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Add a label to an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssueLabelsOption.from_dict(body)
    return web.Response(status=200)


async def issue_add_subscription(request: web.Request, owner, repo, index, user) -> web.Response:
    """Subscribe user to issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param user: user to subscribe
    :type user: str

    """
    return web.Response(status=200)


async def issue_add_time(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Add tracked time to a issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddTimeOption.from_dict(body)
    return web.Response(status=200)


async def issue_check_subscription(request: web.Request, owner, repo, index) -> web.Response:
    """Check if user is subscribed to an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int

    """
    return web.Response(status=200)


async def issue_clear_labels(request: web.Request, owner, repo, index) -> web.Response:
    """Remove all labels from an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int

    """
    return web.Response(status=200)


async def issue_create_comment(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Add a comment to an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = CreateIssueCommentOption.from_dict(body)
    return web.Response(status=200)


async def issue_create_issue(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateIssueOption.from_dict(body)
    return web.Response(status=200)


async def issue_create_issue_attachment(request: web.Request, owner, repo, index, attachment, name=None) -> web.Response:
    """Create an issue attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param attachment: attachment to upload
    :type attachment: str
    :param name: name of the attachment
    :type name: str

    """
    return web.Response(status=200)


async def issue_create_issue_blocking(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Block the issue given in the body by the issue in path

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueMeta.from_dict(body)
    return web.Response(status=200)


async def issue_create_issue_comment_attachment(request: web.Request, owner, repo, id, attachment, name=None) -> web.Response:
    """Create a comment attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment
    :type id: int
    :param attachment: attachment to upload
    :type attachment: str
    :param name: name of the attachment
    :type name: str

    """
    return web.Response(status=200)


async def issue_create_issue_dependencies(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Make the issue in the url depend on the issue in the form.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueMeta.from_dict(body)
    return web.Response(status=200)


async def issue_create_label(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a label

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateLabelOption.from_dict(body)
    return web.Response(status=200)


async def issue_create_milestone(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a milestone

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateMilestoneOption.from_dict(body)
    return web.Response(status=200)


async def issue_delete(request: web.Request, owner, repo, index) -> web.Response:
    """Delete an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of issue to delete
    :type index: int

    """
    return web.Response(status=200)


async def issue_delete_comment(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a comment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of comment to delete
    :type id: int

    """
    return web.Response(status=200)


async def issue_delete_comment_deprecated(request: web.Request, owner, repo, index, id) -> web.Response:
    """Delete a comment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: this parameter is ignored
    :type index: int
    :param id: id of comment to delete
    :type id: int

    """
    return web.Response(status=200)


async def issue_delete_comment_reaction(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Remove a reaction from a comment of an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditReactionOption.from_dict(body)
    return web.Response(status=200)


async def issue_delete_issue_attachment(request: web.Request, owner, repo, index, attachment_id) -> web.Response:
    """Delete an issue attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param attachment_id: id of the attachment to delete
    :type attachment_id: int

    """
    return web.Response(status=200)


async def issue_delete_issue_comment_attachment(request: web.Request, owner, repo, id, attachment_id) -> web.Response:
    """Delete a comment attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment
    :type id: int
    :param attachment_id: id of the attachment to delete
    :type attachment_id: int

    """
    return web.Response(status=200)


async def issue_delete_issue_reaction(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Remove a reaction from an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditReactionOption.from_dict(body)
    return web.Response(status=200)


async def issue_delete_label(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a label

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the label to delete
    :type id: int

    """
    return web.Response(status=200)


async def issue_delete_milestone(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a milestone

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: the milestone to delete, identified by ID and if not available by name
    :type id: str

    """
    return web.Response(status=200)


async def issue_delete_stop_watch(request: web.Request, owner, repo, index) -> web.Response:
    """Delete an issue&#39;s existing stopwatch.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to stop the stopwatch on
    :type index: int

    """
    return web.Response(status=200)


async def issue_delete_subscription(request: web.Request, owner, repo, index, user) -> web.Response:
    """Unsubscribe user from issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param user: user witch unsubscribe
    :type user: str

    """
    return web.Response(status=200)


async def issue_delete_time(request: web.Request, owner, repo, index, id) -> web.Response:
    """Delete specific tracked time

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param id: id of time to delete
    :type id: int

    """
    return web.Response(status=200)


async def issue_edit_comment(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Edit a comment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditIssueCommentOption.from_dict(body)
    return web.Response(status=200)


async def issue_edit_comment_deprecated(request: web.Request, owner, repo, index, id, body=None) -> web.Response:
    """Edit a comment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: this parameter is ignored
    :type index: int
    :param id: id of the comment to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditIssueCommentOption.from_dict(body)
    return web.Response(status=200)


async def issue_edit_issue(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to edit
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditIssueOption.from_dict(body)
    return web.Response(status=200)


async def issue_edit_issue_attachment(request: web.Request, owner, repo, index, attachment_id, body=None) -> web.Response:
    """Edit an issue attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param attachment_id: id of the attachment to edit
    :type attachment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditAttachmentOptions.from_dict(body)
    return web.Response(status=200)


async def issue_edit_issue_comment_attachment(request: web.Request, owner, repo, id, attachment_id, body=None) -> web.Response:
    """Edit a comment attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment
    :type id: int
    :param attachment_id: id of the attachment to edit
    :type attachment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditAttachmentOptions.from_dict(body)
    return web.Response(status=200)


async def issue_edit_issue_deadline(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to create or update a deadline on
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditDeadlineOption.from_dict(body)
    return web.Response(status=200)


async def issue_edit_label(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Update a label

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the label to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditLabelOption.from_dict(body)
    return web.Response(status=200)


async def issue_edit_milestone(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Update a milestone

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: the milestone to edit, identified by ID and if not available by name
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditMilestoneOption.from_dict(body)
    return web.Response(status=200)


async def issue_get_comment(request: web.Request, owner, repo, id) -> web.Response:
    """Get a comment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment
    :type id: int

    """
    return web.Response(status=200)


async def issue_get_comment_reactions(request: web.Request, owner, repo, id) -> web.Response:
    """Get a list of reactions from a comment of an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment to edit
    :type id: int

    """
    return web.Response(status=200)


async def issue_get_comments(request: web.Request, owner, repo, index, since=None, before=None) -> web.Response:
    """List all comments on an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param since: if provided, only comments updated since the specified time are returned.
    :type since: str
    :param before: if provided, only comments updated before the provided time are returned.
    :type before: str

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def issue_get_comments_and_timeline(request: web.Request, owner, repo, index, since=None, page=None, limit=None, before=None) -> web.Response:
    """List all comments and events on an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param since: if provided, only comments updated since the specified time are returned.
    :type since: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int
    :param before: if provided, only comments updated before the provided time are returned.
    :type before: str

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def issue_get_issue(request: web.Request, owner, repo, index) -> web.Response:
    """Get an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to get
    :type index: int

    """
    return web.Response(status=200)


async def issue_get_issue_attachment(request: web.Request, owner, repo, index, attachment_id) -> web.Response:
    """Get an issue attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param attachment_id: id of the attachment to get
    :type attachment_id: int

    """
    return web.Response(status=200)


async def issue_get_issue_comment_attachment(request: web.Request, owner, repo, id, attachment_id) -> web.Response:
    """Get a comment attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment
    :type id: int
    :param attachment_id: id of the attachment to get
    :type attachment_id: int

    """
    return web.Response(status=200)


async def issue_get_issue_reactions(request: web.Request, owner, repo, index, page=None, limit=None) -> web.Response:
    """Get a list reactions of an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def issue_get_label(request: web.Request, owner, repo, id) -> web.Response:
    """Get a single label

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the label to get
    :type id: int

    """
    return web.Response(status=200)


async def issue_get_labels(request: web.Request, owner, repo, index) -> web.Response:
    """Get an issue&#39;s labels

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int

    """
    return web.Response(status=200)


async def issue_get_milestone(request: web.Request, owner, repo, id) -> web.Response:
    """Get a milestone

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: the milestone to get, identified by ID and if not available by name
    :type id: str

    """
    return web.Response(status=200)


async def issue_get_milestones_list(request: web.Request, owner, repo, state=None, name=None, page=None, limit=None) -> web.Response:
    """Get all of a repository&#39;s opened milestones

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param state: Milestone state, Recognized values are open, closed and all. Defaults to \&quot;open\&quot;
    :type state: str
    :param name: filter by milestone name
    :type name: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def issue_get_repo_comments(request: web.Request, owner, repo, since=None, before=None, page=None, limit=None) -> web.Response:
    """List all comments in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param since: if provided, only comments updated since the provided time are returned.
    :type since: str
    :param before: if provided, only comments updated before the provided time are returned.
    :type before: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def issue_list_blocks(request: web.Request, owner, repo, index, page=None, limit=None) -> web.Response:
    """List issues that are blocked by this issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def issue_list_issue_attachments(request: web.Request, owner, repo, index) -> web.Response:
    """List issue&#39;s attachments

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int

    """
    return web.Response(status=200)


async def issue_list_issue_comment_attachments(request: web.Request, owner, repo, id) -> web.Response:
    """List comment&#39;s attachments

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment
    :type id: int

    """
    return web.Response(status=200)


async def issue_list_issue_dependencies(request: web.Request, owner, repo, index, page=None, limit=None) -> web.Response:
    """List an issue&#39;s dependencies, i.e all issues that block this issue.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def issue_list_issues(request: web.Request, owner, repo, state=None, labels=None, q=None, type=None, milestones=None, since=None, before=None, created_by=None, assigned_by=None, mentioned_by=None, page=None, limit=None) -> web.Response:
    """List a repository&#39;s issues

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param state: whether issue is open or closed
    :type state: str
    :param labels: comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded
    :type labels: str
    :param q: search string
    :type q: str
    :param type: filter by type (issues / pulls) if set
    :type type: str
    :param milestones: comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded
    :type milestones: str
    :param since: Only show items updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show items updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str
    :param created_by: Only show items which were created by the the given user
    :type created_by: str
    :param assigned_by: Only show items for which the given user is assigned
    :type assigned_by: str
    :param mentioned_by: Only show items in which the given user was mentioned
    :type mentioned_by: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def issue_list_labels(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """Get all of a repository&#39;s labels

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def issue_post_comment_reaction(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Add a reaction to a comment of an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the comment to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditReactionOption.from_dict(body)
    return web.Response(status=200)


async def issue_post_issue_reaction(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Add a reaction to an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditReactionOption.from_dict(body)
    return web.Response(status=200)


async def issue_remove_issue_blocking(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Unblock the issue given in the body by the issue in path

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueMeta.from_dict(body)
    return web.Response(status=200)


async def issue_remove_issue_dependencies(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Remove an issue dependency

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueMeta.from_dict(body)
    return web.Response(status=200)


async def issue_remove_label(request: web.Request, owner, repo, index, id) -> web.Response:
    """Remove a label from an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param id: id of the label to remove
    :type id: int

    """
    return web.Response(status=200)


async def issue_replace_labels(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Replace an issue&#39;s labels

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssueLabelsOption.from_dict(body)
    return web.Response(status=200)


async def issue_reset_time(request: web.Request, owner, repo, index) -> web.Response:
    """Reset a tracked time of an issue

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to add tracked time to
    :type index: int

    """
    return web.Response(status=200)


async def issue_search_issues(request: web.Request, state=None, labels=None, milestones=None, q=None, priority_repo_id=None, type=None, since=None, before=None, assigned=None, created=None, mentioned=None, review_requested=None, reviewed=None, owner=None, team=None, page=None, limit=None) -> web.Response:
    """Search for issues across the repositories that the user has access to

    

    :param state: whether issue is open or closed
    :type state: str
    :param labels: comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded
    :type labels: str
    :param milestones: comma separated list of milestone names. Fetch only issues that have any of this milestones. Non existent are discarded
    :type milestones: str
    :param q: search string
    :type q: str
    :param priority_repo_id: repository to prioritize in the results
    :type priority_repo_id: int
    :param type: filter by type (issues / pulls) if set
    :type type: str
    :param since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str
    :param assigned: filter (issues / pulls) assigned to you, default is false
    :type assigned: bool
    :param created: filter (issues / pulls) created by you, default is false
    :type created: bool
    :param mentioned: filter (issues / pulls) mentioning you, default is false
    :type mentioned: bool
    :param review_requested: filter pulls requesting your review, default is false
    :type review_requested: bool
    :param reviewed: filter pulls reviewed by you, default is false
    :type reviewed: bool
    :param owner: filter by owner
    :type owner: str
    :param team: filter by team (requires organization owner parameter to be provided)
    :type team: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def issue_start_stop_watch(request: web.Request, owner, repo, index) -> web.Response:
    """Start stopwatch on an issue.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to create the stopwatch on
    :type index: int

    """
    return web.Response(status=200)


async def issue_stop_stop_watch(request: web.Request, owner, repo, index) -> web.Response:
    """Stop an issue&#39;s existing stopwatch.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue to stop the stopwatch on
    :type index: int

    """
    return web.Response(status=200)


async def issue_subscriptions(request: web.Request, owner, repo, index, page=None, limit=None) -> web.Response:
    """Get users who subscribed on an issue.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def issue_tracked_times(request: web.Request, owner, repo, index, user=None, since=None, before=None, page=None, limit=None) -> web.Response:
    """List an issue&#39;s tracked times

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the issue
    :type index: int
    :param user: optional filter by user (available for issue managers)
    :type user: str
    :param since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)
