from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def add_changeset_to_review(request: web.Request, id) -> web.Response:
    """add_changeset_to_review

    

    :param id: the perm id of the review to add the changeset to
    :type id: str

    """
    return web.Response(status=200)


async def add_file(request: web.Request, id) -> web.Response:
    """add_file

    

    :param id: the review perma id to add the file
    :type id: str

    """
    return web.Response(status=200)


async def add_fisheye_review_item(request: web.Request, id) -> web.Response:
    """add_fisheye_review_item

    Add the changes between two files in a fisheye repository to the review.

    :param id: the id of the review (e.g. \&quot;CR-362\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def add_general_comment(request: web.Request, id) -> web.Response:
    """add_general_comment

    Add a general comment to the review.

    :param id: the review perma-id
    :type id: str

    """
    return web.Response(status=200)


async def add_patch_review0(request: web.Request, id) -> web.Response:
    """add_patch_review0

    Old, non-restful name. Kept for backwards compatibility. Exactly the same as POSTing to /{id}/patch

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def add_patch_to_review(request: web.Request, id) -> web.Response:
    """add_patch_to_review

    Add the revisions in a patch to an existing review.

    :param id: the review id to get the patches for
    :type id: str

    """
    return web.Response(status=200)


async def add_reply(request: web.Request, id, c_id) -> web.Response:
    """add_reply

    Adds a reply to the given comment. This call includes the  repsonse header that  contains the URL of the newly created entity.

    :param id: the review perma-id (e.g. \&quot;CR-45\&quot;).
    :type id: str
    :param c_id: the comment to reply to
    :type c_id: str

    """
    return web.Response(status=200)


async def add_review_item(request: web.Request, id) -> web.Response:
    """add_review_item

    Adds the given review item to the review. This will always create a new review item, even if there is an existing  one with the same data in the review (in which case the existing item will be replaced).

    :param id: the id of the review (e.g. \&quot;CR-362\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def add_review_item_revisions(request: web.Request, ri_id, id, rev=None) -> web.Response:
    """add_review_item_revisions

    Adds the given list of revisions to the supplied review item, merging if required. For example, if the review  item for  contains revisions 3 to 6, and if:

    :param ri_id: the id of the review item (e.g. \&quot;CFR-5622\&quot;).
    :type ri_id: str
    :param id: the id of the review (e.g. \&quot;CR-345\&quot;).
    :type id: str
    :param rev: a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored.
    :type rev: str

    """
    return web.Response(status=200)


async def add_review_items(request: web.Request, id) -> web.Response:
    """add_review_items

    Adds a review item for each of the supplied crucibleRevisionData elements.

    :param id: the id of the review (e.g. \&quot;CR-362\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def add_reviewers(request: web.Request, id) -> web.Response:
    """add_reviewers

    Adds the given list of reviewers to the review.

    :param id: the id of the review to add to
    :type id: str

    """
    return web.Response(status=200)


async def add_versioned_comment(request: web.Request, ri_id, id) -> web.Response:
    """add_versioned_comment

    This call includes the  repsonse header that contains the URL of the newly created entity.

    :param ri_id: the review item id.
    :type ri_id: str
    :param id: the review perma id
    :type id: str

    """
    return web.Response(status=200)


async def browse(request: web.Request, path, repository) -> web.Response:
    """browse

    Lists the contents of the specified directory.

    :param path: path to a directory. When path represents a file name, the result is unspecified.
    :type path: str
    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str

    """
    return web.Response(status=200)


async def change(request: web.Request, repository, revision) -> web.Response:
    """change

    Represents a particular changeset.

    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str
    :param revision: the SCM revision string.
    :type revision: str

    """
    return web.Response(status=200)


async def change_state(request: web.Request, id, action=None, ignore_warnings=None) -> web.Response:
    """change_state

    Change the state of a review by performing an action on it.

    :param id: the review perma-id (e.g. \&quot;CR-45\&quot;).
    :type id: str
    :param action: the string representation of the action to perform. Valid actions are:    Note:
    :type action: str
    :param ignore_warnings: if  then condition failure warnings will be ignored
    :type ignore_warnings: bool

    """
    return web.Response(status=200)


async def changes(request: web.Request, path, repository, oldest_csid=None, include_oldest=None, newest_csid=None, include_newest=None, max=None) -> web.Response:
    """changes

    Represents a sorted list of changesets, newest first.

    :param path: only show change sets which contain at least one revision with a path under this path.  Changesets with some revisions outside this path still include all revisions.  i.e. Revisions outside the path are *not* excluded from the change set.
    :type path: str
    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str
    :param oldest_csid: only return change sets after this change set. If omitted there is no restriction.
    :type oldest_csid: str
    :param include_oldest: include the change set with id \&quot;from\&quot; in the change sets returned.
    :type include_oldest: bool
    :param newest_csid: only return change sets before this change set. If omitted there is no restriction.
    :type newest_csid: str
    :param include_newest: include the change set with id \&quot;to\&quot; in the change sets returned.
    :type include_newest: bool
    :param max: return only the newest change sets, to a maximum of maxChangesets.
    :type max: int

    """
    return web.Response(status=200)


async def close_review_with_comment(request: web.Request, id) -> web.Response:
    """close_review_with_comment

    Closes the given review with the summary given.

    :param id: the review perma id to close. it should be in the open state.
    :type id: str

    """
    return web.Response(status=200)


async def complete_review(request: web.Request, id, ignore_warnings=None) -> web.Response:
    """complete_review

    Completes the review for the current user

    :param id: the review perma id
    :type id: str
    :param ignore_warnings: if {@code ignoreWarnings&#x3D;&#x3D;true} then condition failure warnings will be ignored
    :type ignore_warnings: bool

    """
    return web.Response(status=200)


async def create_review(request: web.Request, ) -> web.Response:
    """create_review

    


    """
    return web.Response(status=200)


async def delete_review(request: web.Request, id) -> web.Response:
    """delete_review

    Permanently deletes the specified review.  The review must have been abandoned.

    :param id: the permId of the review to delete (e.g. \&quot;CR-45\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def details(request: web.Request, path, repository, revision) -> web.Response:
    """details

    

    :param path: the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins).
    :type path: str
    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str
    :param revision: the SCM revision string.
    :type revision: str

    """
    return web.Response(status=200)


async def get_all_comments(request: web.Request, id, render=None) -> web.Response:
    """get_all_comments

    Return all the comments visible to the requesting user for the review.

    :param id: the review perma-id
    :type id: str
    :param render: indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html.
    :type render: bool

    """
    return web.Response(status=200)


async def get_all_detailed_reviews(request: web.Request, state=None) -> web.Response:
    """get_all_detailed_reviews

    Retrieves all reviews that are in one of the the specified states. For each review all details are included (review items + comments). The  wiki rendered comments will be available via the &lt;messageAsHtml&gt; element

    :param state: the review states to match.
    :type state: str

    """
    return web.Response(status=200)


async def get_all_projects(request: web.Request, exclude_allowed_reviewers=None) -> web.Response:
    """get_all_projects

    Get the list of projects that the authenticated user is entitled to access.

    :param exclude_allowed_reviewers: if set to true, user data (e.g. allowedReviewers) which is expensive  to compute, will not be included in the response data. Defaults to false so allowedReviewers are included in the response.
    :type exclude_allowed_reviewers: bool

    """
    return web.Response(status=200)


async def get_all_repositories(request: web.Request, name=None, enabled=None, available=None, type=None, limit=None) -> web.Response:
    """get_all_repositories

    Returns a list of all repositories. This includes plugin provided repositories

    :param name: filter repositories by the repository key, only repositories of keys containing this value  would be returned if value was provided.  Case insensitive.
    :type name: str
    :param enabled: filter repositories by enabled flag.  Only enabled/disabled repositories would be returned  accordingly if value was provided.
    :type enabled: bool
    :param available: filter repositories by its availability.  Only available/unavailable repositories would be returned  accordingly if value was provided.
    :type available: bool
    :param type: filter repositories by type.  Allowed values: cvs, svn, p4, git, hg, plugin (for light SCM repositories).  Parameter can be specified more than once.
    :type type: str
    :param limit: maximum number of repositories to be returned.
    :type limit: int

    """
    return web.Response(status=200)


async def get_all_reviews(request: web.Request, state=None) -> web.Response:
    """get_all_reviews

    

    :param state: only return reviews that are in these states.
    :type state: str

    """
    return web.Response(status=200)


async def get_available_actions(request: web.Request, id) -> web.Response:
    """get_available_actions

    Get a list of the actions which the current user is allowed to perform  on the review.

    :param id: the permId of the a review (e.g. \&quot;CR-45\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def get_available_transitions(request: web.Request, id) -> web.Response:
    """get_available_transitions

    Get a list of the actions which the current user can perform on this  review, given its current state and the user&#39;s permissions.

    :param id: the permId of the a review (e.g. \&quot;CR-45\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def get_comment(request: web.Request, id, c_id, render=None) -> web.Response:
    """get_comment

    Gets the given comment.

    :param id: the perma id of the review
    :type id: str
    :param c_id: the id of the comment
    :type c_id: str
    :param render: true if the wiki text should be rendered into html, into the field &lt;messageAsHtml&gt;.
    :type render: bool

    """
    return web.Response(status=200)


async def get_completed_reviewers(request: web.Request, id) -> web.Response:
    """get_completed_reviewers

    Gets a list of completed reviewers.

    :param id: the review perma id to retrieve reviewers
    :type id: str

    """
    return web.Response(status=200)


async def get_contents(request: web.Request, path, repository, revision) -> web.Response:
    """get_contents

    Returns the raw content of the specified file revision as a binary  stream. No attempt is made to identify the content type and no mime  type is provided.

    :param path: the path of a file.
    :type path: str
    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str
    :param revision: the SCM revision string.
    :type revision: str

    """
    return web.Response(status=200)


async def get_custom_filter_reviews(request: web.Request, title=None, author=None, moderator=None, creator=None, states=None, reviewer=None, or_roles=None, complete=None, all_reviewers_complete=None, project=None, from_date=None, to_date=None) -> web.Response:
    """get_custom_filter_reviews

    To ignore a property, omit it from the query string.

    :param title: a string that will be searched for in review titles.
    :type title: str
    :param author: reviews authored by this user.
    :type author: str
    :param moderator: reviews moderated by this user.
    :type moderator: str
    :param creator: reviews created by this user.
    :type creator: str
    :param states: comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown).
    :type states: str
    :param reviewer: reviews reviewed by this user.
    :type reviewer: str
    :param or_roles: whether the value of , ,   and  should be OR&#39;d  () or AND&#39;d ()  together.
    :type or_roles: bool
    :param complete: reviews that the specified reviewer has completed.
    :type complete: bool
    :param all_reviewers_complete: Reviews that all reviewers have completed.
    :type all_reviewers_complete: bool
    :param project: reviews for the specified project.
    :type project: str
    :param from_date: reviews with last activity date after the specified timestamp, in milliseconds. Inclusive.
    :type from_date: int
    :param to_date: reviews with last activity date before the specified timestamp, in milliseconds. Inclusive.
    :type to_date: int

    """
    return web.Response(status=200)


async def get_detailed_custom_filter_reviews(request: web.Request, title=None, author=None, moderator=None, creator=None, states=None, reviewer=None, or_roles=None, complete=None, all_reviewers_complete=None, project=None, from_date=None, to_date=None) -> web.Response:
    """get_detailed_custom_filter_reviews

    To ignore a property, omit it from the query string.

    :param title: a string that will be searched for in review titles.
    :type title: str
    :param author: reviews authored by this user.
    :type author: str
    :param moderator: reviews moderated by this user.
    :type moderator: str
    :param creator: reviews created by this user.
    :type creator: str
    :param states: comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown).
    :type states: str
    :param reviewer: reviews reviewed by this user.
    :type reviewer: str
    :param or_roles: whether the value of , ,   and  should be OR&#39;d  () or AND&#39;d ()  together.
    :type or_roles: bool
    :param complete: reviews that the specified reviewer has completed.
    :type complete: bool
    :param all_reviewers_complete: Reviews that all reviewers have completed.
    :type all_reviewers_complete: bool
    :param project: reviews for the specified project.
    :type project: str
    :param from_date: reviews with last activity date after the specified timestamp, in milliseconds. Inclusive.
    :type from_date: int
    :param to_date: reviews with last activity date before the specified timestamp, in milliseconds. Inclusive.
    :type to_date: int

    """
    return web.Response(status=200)


async def get_detailed_filtered_reviews_for_user(request: web.Request, filter) -> web.Response:
    """get_detailed_filtered_reviews_for_user

    Gets a list of all the reviews that match the specified filter criteria.

    :param filter: a predefined filter type.
    :type filter: str

    """
    return web.Response(status=200)


async def get_detailed_review(request: web.Request, id) -> web.Response:
    """get_detailed_review

    Returns the specified review.

    :param id: the permId of the review (e.g. \&quot;CR-45\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def get_filtered_reviews_for_user(request: web.Request, filter) -> web.Response:
    """get_filtered_reviews_for_user

    Get all the reviews which match the given filter, for the current user.

    :param filter: a predefined filter type.
    :type filter: str

    """
    return web.Response(status=200)


async def get_general_comments(request: web.Request, id, render=None) -> web.Response:
    """get_general_comments

    

    :param id: review perma-id
    :type id: str
    :param render: indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html.
    :type render: bool

    """
    return web.Response(status=200)


async def get_mapped_user(request: web.Request, repository, username) -> web.Response:
    """get_mapped_user

    Returns the user details of the user mapped to a committer in a repository.

    :param repository: the key of the repository
    :type repository: str
    :param username: the name of the committer
    :type username: str

    """
    return web.Response(status=200)


async def get_metrics(request: web.Request, version) -> web.Response:
    """get_metrics

    Get comment metrics metadata for the specified metrics version.

    :param version: a metrics version.
    :type version: str

    """
    return web.Response(status=200)


async def get_project(request: web.Request, key, exclude_allowed_reviewers=None) -> web.Response:
    """get_project

    Returns a project description.

    :param key: the key of a Crucible project.
    :type key: str
    :param exclude_allowed_reviewers: 
    :type exclude_allowed_reviewers: bool

    """
    return web.Response(status=200)


async def get_replies(request: web.Request, id, c_id, render=None) -> web.Response:
    """get_replies

    Gets the replies to the given comment.

    :param id: the review perma-id (e.g. \&quot;CR-45\&quot;).
    :type id: str
    :param c_id: the comment to reply to
    :type c_id: str
    :param render: true if the comments should also be rendered into html, into the element &lt;messageAsHtml&gt;
    :type render: bool

    """
    return web.Response(status=200)


async def get_repository_details(request: web.Request, repository) -> web.Response:
    """get_repository_details

    

    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str

    """
    return web.Response(status=200)


async def get_review(request: web.Request, id) -> web.Response:
    """get_review

    Get a single review by its permId (e.g. \&quot;CR-45\&quot;).  If the review does not exist, a 404 is returned.    The moderator element may not exist if the review does not have a Moderator.

    :param id: the permId of the review to delete (e.g. \&quot;CR-45\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def get_review_item(request: web.Request, ri_id, id) -> web.Response:
    """get_review_item

    Returns detailed information for a specific review item.

    :param ri_id: review item id (e.g. \&quot;CFR-6312\&quot;).
    :type ri_id: str
    :param id: review id (e.g. \&quot;CR-345\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def get_review_items_comments(request: web.Request, ri_id, id, render=None) -> web.Response:
    """get_review_items_comments

    

    :param ri_id: the review item id.
    :type ri_id: str
    :param id: the review perma id
    :type id: str
    :param render: indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html.
    :type render: bool

    """
    return web.Response(status=200)


async def get_review_items_for_review(request: web.Request, id) -> web.Response:
    """get_review_items_for_review

    Returns a list of all the items in a review.

    :param id: the id of the review (e.g. \&quot;CR-362\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def get_review_patches(request: web.Request, id) -> web.Response:
    """get_review_patches

    Get a list of patches and their details for the given review

    :param id: the review id to get the patches for
    :type id: str

    """
    return web.Response(status=200)


async def get_reviewers(request: web.Request, id) -> web.Response:
    """get_reviewers

    Get a list of reviewers in the review given by the permaid id.

    :param id: the id of the review to add to
    :type id: str

    """
    return web.Response(status=200)


async def get_reviews_details_for_path(request: web.Request, repository, path=None) -> web.Response:
    """get_reviews_details_for_path

    Return a list of Reviews which include a particular file.

    :param repository: the key of the repository to search for file.
    :type repository: str
    :param path: path to find in reviews.
    :type path: str

    """
    return web.Response(status=200)


async def get_reviews_for_issue_key(request: web.Request, jira_key=None, max_return=None) -> web.Response:
    """get_reviews_for_issue_key

    Get a list of all reviews that have been linked to the specified JIRA issue key.

    :param jira_key: a Jira issue key (e.g. \&quot;FOO-3453\&quot;)
    :type jira_key: str
    :param max_return: the maximum number of reviews to return.
    :type max_return: str

    """
    return web.Response(status=200)


async def get_reviews_for_path(request: web.Request, repository, path=None) -> web.Response:
    """get_reviews_for_path

    Return a list of Reviews which include a particular file.

    :param repository: the key of the repository to search for file
    :type repository: str
    :param path: path to find in reviews
    :type path: str

    """
    return web.Response(status=200)


async def get_reviews_for_term(request: web.Request, term=None, max_return=None) -> web.Response:
    """get_reviews_for_term

    Search for reviews where the name, description, state or permaId contain the specified term.

    :param term: a search term.
    :type term: str
    :param max_return: the maximum number of reviews to return.
    :type max_return: str

    """
    return web.Response(status=200)


async def get_svn_repository_details(request: web.Request, repository) -> web.Response:
    """get_svn_repository_details

    For backward compatibility we provide this method, but repositories should be referred to just by their key.

    :param repository: the key of a FishEye or Crucible SCM plugin repository
    :type repository: str

    """
    return web.Response(status=200)


async def get_uncompleted_reviewers(request: web.Request, id) -> web.Response:
    """get_uncompleted_reviewers

    Gets a list of reviewers that have not completed the review.

    :param id: the review perma id to retrieve reviewers
    :type id: str

    """
    return web.Response(status=200)


async def get_user_profile(request: web.Request, username) -> web.Response:
    """get_user_profile

    Returns the user&#39;s profile details.

    :param username: the username of the user
    :type username: str

    """
    return web.Response(status=200)


async def get_users(request: web.Request, username=None) -> web.Response:
    """get_users

    Get a list of all the users. You can also ask for a set of users.

    :param username: a username (or a few) to limit the number of returned entries. It will return only existing users.
    :type username: str

    """
    return web.Response(status=200)


async def get_version_info(request: web.Request, ) -> web.Response:
    """get_version_info

    Returns Crucible version information.


    """
    return web.Response(status=200)


async def get_versioned_comments(request: web.Request, id, render=None) -> web.Response:
    """get_versioned_comments

    

    :param id: review perma-id
    :type id: str
    :param render: indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html.
    :type render: bool

    """
    return web.Response(status=200)


async def history(request: web.Request, path, repository, revision) -> web.Response:
    """history

    Represents the history of a versioned entity.

    :param path: the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins).
    :type path: str
    :param repository: the key of the Crucible SCM plugin repository.
    :type repository: str
    :param revision: the SCM revision string.
    :type revision: str

    """
    return web.Response(status=200)


async def login(request: web.Request, user_name=None, password=None) -> web.Response:
    """login

    Get the user authentication token.    This is a legacy version of the login request. Using GET is deprecated as your password is likely to appear in logs which record request URLs.  Use the POST version instead.

    :param user_name: the username of the user to get the token for
    :type user_name: str
    :param password: the password for the user to get the token for
    :type password: str

    """
    return web.Response(status=200)


async def login_post(request: web.Request, ) -> web.Response:
    """login_post

    Get the user authentication token.


    """
    return web.Response(status=200)


async def mark_all_comments_as_read(request: web.Request, id) -> web.Response:
    """mark_all_comments_as_read

    For the effective user, mark all comments in a review as read (except  those marked as leave unread).

    :param id: the review perma-id (e.g. \&quot;CR-45\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def mark_comment_as_leave_unread(request: web.Request, id, c_id) -> web.Response:
    """mark_comment_as_leave_unread

    Marks the comment as leave unread to the current user - it will not automatically be marked as read by crucible.

    :param id: the review perma id for the comment
    :type id: str
    :param c_id: the comment perma id
    :type c_id: str

    """
    return web.Response(status=200)


async def mark_comment_as_read(request: web.Request, id, c_id) -> web.Response:
    """mark_comment_as_read

    Mark the given comment as read for the user used to make this POST.

    :param id: the review perma id
    :type id: str
    :param c_id: the comment perma id.
    :type c_id: str

    """
    return web.Response(status=200)


async def post_custom_filter_reviews(request: web.Request, ) -> web.Response:
    """post_custom_filter_reviews

    This method should no longer be used, as it uses a POST for a read-only  retrieval operation and is provided for backward compatibility only.


    """
    return web.Response(status=200)


async def post_detailed_custom_filter_reviews(request: web.Request, ) -> web.Response:
    """post_detailed_custom_filter_reviews

    This method should no longer be used, as it uses a POST for a read-only  retrieval operation and is provided for backward compatibility only.


    """
    return web.Response(status=200)


async def publish_all_comments(request: web.Request, id) -> web.Response:
    """publish_all_comments

    Publishes all the draft comments of the current user.

    :param id: the review perma id to look for draft comments
    :type id: str

    """
    return web.Response(status=200)


async def publish_comment(request: web.Request, id, c_id) -> web.Response:
    """publish_comment

    publishes the given draft comment.

    :param id: the review perma id
    :type id: str
    :param c_id: the comment perma id
    :type c_id: str

    """
    return web.Response(status=200)


async def remind_incomplete_reviewers(request: web.Request, id) -> web.Response:
    """remind_incomplete_reviewers

    Immediately send a reminder to incomplete reviewers about the given review.

    :param id: the review perma id to remind about. it should be in the open state.
    :type id: str

    """
    return web.Response(status=200)


async def remove_comment(request: web.Request, id, c_id) -> web.Response:
    """remove_comment

    Deletes the given comment.

    :param id: the perma id of the review
    :type id: str
    :param c_id: the id of the comment
    :type c_id: str

    """
    return web.Response(status=200)


async def remove_patch(request: web.Request, patch_id, id) -> web.Response:
    """remove_patch

    Removes the patch with the given id from the review. All of the revisions provided by the patch will be removed as well.

    :param patch_id: the id of the patch (as returned by the &#39;{id}/patch&#39; resource)
    :type patch_id: int
    :param id: the permaId of the review
    :type id: str

    """
    return web.Response(status=200)


async def remove_reply(request: web.Request, id, r_id, c_id) -> web.Response:
    """remove_reply

    Deletes the reply.

    :param id: The review perma id
    :type id: str
    :param r_id: the perma id of the reply to delete
    :type r_id: str
    :param c_id: the reply&#39;s parent comment perma id
    :type c_id: str

    """
    return web.Response(status=200)


async def remove_review_item(request: web.Request, ri_id, id) -> web.Response:
    """remove_review_item

    Removes an item from a review.

    :param ri_id: review item id (e.g. \&quot;CFR-6312\&quot;).
    :type ri_id: str
    :param id: review id (e.g. \&quot;CR-345\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def remove_review_item_revisions(request: web.Request, ri_id, id, rev=None) -> web.Response:
    """remove_review_item_revisions

    Removes the revisions given from the review item in the review specified by the id. If the review item has no  more revisions left, it is automatically deleted.

    :param ri_id: the id of the review item (e.g. \&quot;CFR-5622\&quot;).
    :type ri_id: str
    :param id: the id of the review (e.g. \&quot;CR-345\&quot;).
    :type id: str
    :param rev: a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored.
    :type rev: str

    """
    return web.Response(status=200)


async def remove_reviewer(request: web.Request, id, username) -> web.Response:
    """remove_reviewer

    Removes the reviewer from the review.

    :param id: the perma id of the review
    :type id: str
    :param username: the name of the reviewer.
    :type username: str

    """
    return web.Response(status=200)


async def set_review_item(request: web.Request, ri_id, id) -> web.Response:
    """set_review_item

    Sets the review item specified by itemId with the given reviewItem. The old review item is discarded. Can only  perform this operation if the old review item specified by itemId can be deleted. The old review item&#39;s permId is  not changed.

    :param ri_id: a valid review item id (e.g. \&quot;CFR-5622\&quot;).
    :type ri_id: str
    :param id: a valid review id (e.g. \&quot;CR-345\&quot;).
    :type id: str

    """
    return web.Response(status=200)


async def uncomplete_review(request: web.Request, id, ignore_warnings=None) -> web.Response:
    """uncomplete_review

    Uncompletes the review for the current user.

    :param id: the review perma id
    :type id: str
    :param ignore_warnings: if {@code ignoreWarnings&#x3D;&#x3D;true} then condition failure warnings will be ignored
    :type ignore_warnings: bool

    """
    return web.Response(status=200)


async def update_comment(request: web.Request, id, c_id) -> web.Response:
    """update_comment

    Updates the comment given by the perma id to the new comment posted.

    :param id: the perma id of the review
    :type id: str
    :param c_id: the id of the comment
    :type c_id: str

    """
    return web.Response(status=200)


async def update_reply(request: web.Request, id, r_id, c_id) -> web.Response:
    """update_reply

    Updates a reply with the given newComment.

    :param id: The review perma id
    :type id: str
    :param r_id: the perma id of the reply to delete
    :type r_id: str
    :param c_id: the reply&#39;s parent comment perma id
    :type c_id: str

    """
    return web.Response(status=200)
