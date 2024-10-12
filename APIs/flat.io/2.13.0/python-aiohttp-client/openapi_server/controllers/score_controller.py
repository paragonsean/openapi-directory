from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment_submission import AssignmentSubmission
from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.resource_collaborator import ResourceCollaborator
from openapi_server.models.resource_collaborator_creation import ResourceCollaboratorCreation
from openapi_server.models.score_comment import ScoreComment
from openapi_server.models.score_comment_creation import ScoreCommentCreation
from openapi_server.models.score_comment_update import ScoreCommentUpdate
from openapi_server.models.score_creation import ScoreCreation
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.score_fork import ScoreFork
from openapi_server.models.score_modification import ScoreModification
from openapi_server.models.score_revision import ScoreRevision
from openapi_server.models.score_revision_creation import ScoreRevisionCreation
from openapi_server.models.score_track import ScoreTrack
from openapi_server.models.score_track_creation import ScoreTrackCreation
from openapi_server.models.score_track_update import ScoreTrackUpdate
from openapi_server import util


async def add_score_collaborator(request: web.Request, score, body) -> web.Response:
    """Add a new collaborator

    Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a resource. - To add an existing Flat user to the resource, specify its unique identifier in the &#x60;user&#x60; property. - To invite an external user to the resource, specify its email in the &#x60;userEmail&#x60; property. - To add a Flat group to the resource, specify its unique identifier in the &#x60;group&#x60; property. - To update an existing collaborator, process the same request with different rights. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResourceCollaboratorCreation.from_dict(body)
    return web.Response(status=200)


async def add_score_track(request: web.Request, score, body) -> web.Response:
    """Add a new video or audio track to the score

    Use this method to add new track to the score. This track can then be played on flat.io or in an embedded score. This API method support medias hosted on SoundCloud, YouTube and Vimeo. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScoreTrackCreation.from_dict(body)
    return web.Response(status=200)


async def create_score(request: web.Request, body) -> web.Response:
    """Create a new score

    Use this API method to **create a new music score in the current User account**. You will need a MusicXML 3 (&#x60;vnd.recordare.musicxml&#x60; or &#x60;vnd.recordare.musicxml+xml&#x60;), a MIDI (&#x60;audio/midi&#x60;), Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar, or MuseScore file to create the new Flat document.  This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (&#x60;POST /v2/scores/{score}/revisions/{revision}&#x60;).  The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups).  If no &#x60;collection&#x60; is specified, the API will create the score in the most appropriate collection. This can be the &#x60;root&#x60; collection or a different collection based on the user&#39;s settings or API authentication method. If a &#x60;collection&#x60; is specified and this one has more public privacy settings than the score (e.g. &#x60;public&#x60; vs &#x60;private&#x60; for the score), the privacy settings of the created score will be adjusted to the collection ones. You can check the adjusted privacy settings in the returned score &#x60;privacy&#x60;, and optionally adjust these settings if needed using &#x60;PUT /scores/{score}&#x60;. 

    :param body: 
    :type body: dict | bytes

    """
    body = ScoreCreation.from_dict(body)
    return web.Response(status=200)


async def create_score_revision(request: web.Request, score, body) -> web.Response:
    """Create a new revision

    Update a score by uploading a new revision for this one. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScoreRevisionCreation.from_dict(body)
    return web.Response(status=200)


async def delete_score(request: web.Request, score, now=None) -> web.Response:
    """Delete a score

    This method can be used by the owner/admin (&#x60;aclAdmin&#x60; rights) of a score as well as regular collaborators.  When called by an owner/admin, it will schedule the deletion of the score, its revisions, and complete history. The score won&#39;t be accessible anymore after calling this method and the user&#39;s quota will directly be updated.  When called by a regular collaborator (&#x60;aclRead&#x60; / &#x60;aclWrite&#x60;), the score will be unshared (i.e. removed from the account &amp; own collections). 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param now: If &#x60;true&#x60;, the score deletion will be scheduled to be done ASAP
    :type now: bool

    """
    return web.Response(status=200)


async def delete_score_comment(request: web.Request, score, comment, sharing_key=None) -> web.Response:
    """Delete a comment

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param comment: Unique identifier of a sheet music comment 
    :type comment: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def delete_score_track(request: web.Request, score, track) -> web.Response:
    """Remove an audio or video track linked to the score

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param track: Unique identifier of a score audio track 
    :type track: str

    """
    return web.Response(status=200)


async def edit_score(request: web.Request, score, body=None) -> web.Response:
    """Edit a score&#39;s metadata

    This API method allows you to change the metadata of a score document (e.g. its &#x60;title&#x60; or &#x60;privacy&#x60;), all the properties are optional.  To edit the file itself, create a new revision using the appropriate method (&#x60;POST /v2/scores/{score}/revisions/{revision}&#x60;).  When editing the &#x60;title&#x60;, &#x60;subtitle&#x60;, &#x60;composer&#x60;, &#x60;lyricist&#x60;, &#x60;arranger&#x60; or &#x60;licenseText&#x60;, the metadatas will be instantly be updated, and a real-time action will be pushed to update the document lazily. This pending document modification will be automatically be saved as a new version by either a connected client or our internal versioning service. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScoreModification.from_dict(body)
    return web.Response(status=200)


async def fork_score(request: web.Request, score, body, sharing_key=None) -> web.Response:
    """Fork a score

    This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to &#x60;private&#x60;.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    body = ScoreFork.from_dict(body)
    return web.Response(status=200)


async def ger_user_likes_0(request: web.Request, user, ids=None) -> web.Response:
    """List liked scores

    

    :param user: Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user. 
    :type user: str
    :param ids: Return only the identifiers of the scores
    :type ids: bool

    """
    return web.Response(status=200)


async def get_group_scores_0(request: web.Request, group, parent=None) -> web.Response:
    """List group&#39;s scores

    Get the list of scores shared with a group. 

    :param group: Unique identifier of a Flat group 
    :type group: str
    :param parent: Filter the score forked from the score id &#x60;parent&#x60;
    :type parent: str

    """
    return web.Response(status=200)


async def get_score(request: web.Request, score, sharing_key=None) -> web.Response:
    """Get a score&#39;s metadata

    Get the details of a score identified by the &#x60;score&#x60; parameter in the URL. The currently authenticated user must have at least a read access to the document to use this API call. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def get_score_collaborator(request: web.Request, score, collaborator, sharing_key=None) -> web.Response:
    """Get a collaborator

    Get the information about a collaborator (User or Group). 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param collaborator: Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
    :type collaborator: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def get_score_collaborators(request: web.Request, score, sharing_key=None) -> web.Response:
    """List the collaborators

    This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.  Collaborators can be a single user (the object &#x60;user&#x60; will be populated) or a group (the object &#x60;group&#x60; will be populated). 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def get_score_comments(request: web.Request, score, sharing_key=None, type=None, sort=None, direction=None) -> web.Response:
    """List comments

    This method lists the different comments added on a music score (documents and inline) sorted by their post dates.

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str
    :param type: Filter the comments by type
    :type type: str
    :param sort: Sort
    :type sort: str
    :param direction: Sort direction
    :type direction: str

    """
    return web.Response(status=200)


async def get_score_revision(request: web.Request, score, revision, sharing_key=None) -> web.Response:
    """Get a score revision

    When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific revision metadata. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param revision: Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created. 
    :type revision: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def get_score_revision_data(request: web.Request, score, revision, format, sharing_key=None, parts=None, only_cached=None, url=None) -> web.Response:
    """Get a score revision data

    Retrieve the file corresponding to a score revision (the following formats are available): Flat JSON/Adagio JSON &#x60;json&#x60;, MusicXML &#x60;mxl&#x60;/&#x60;xml&#x60;, MP3 &#x60;mp3&#x60;, WAV &#x60;wav&#x60;, MIDI &#x60;midi&#x60;, a tumbnail of the first page &#x60;thumbnail.png&#x60; or auto sync points &#x60;synchronizationPoints&#x60;. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param revision: Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created. 
    :type revision: str
    :param format: The format of the file you will retrieve
    :type format: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str
    :param parts: An optional a set of parts uuid to be exported. This parameter must be composed of parts uuids separated by commas. For example \&quot;59df645f-bb1c-f1b4-b573-d2afc4491f94,34ef645f-1aef-f3bc-1564-34cca4492b87\&quot;. 
    :type parts: str
    :param only_cached: Only return files already generated and cached in Flat&#39;s production cache. If the file is not availabe, a 404 will be returned 
    :type only_cached: bool
    :param url: Returns a json with the &#x60;url&#x60; in it instead of redirecting 
    :type url: bool

    """
    return web.Response(status=200)


async def get_score_revisions(request: web.Request, score, sharing_key=None) -> web.Response:
    """List the revisions

    When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.  Depending the plan of the account, this list can be trunked to the few last revisions. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def get_score_submissions(request: web.Request, score) -> web.Response:
    """List submissions related to the score

    This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str

    """
    return web.Response(status=200)


async def get_score_track(request: web.Request, score, track, sharing_key=None) -> web.Response:
    """Retrieve the details of an audio or video track linked to a score

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param track: Unique identifier of a score audio track 
    :type track: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def get_user_scores_0(request: web.Request, user, parent=None) -> web.Response:
    """List user&#39;s scores

    Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

    :param user: Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user. 
    :type user: str
    :param parent: Filter the score forked from the score id &#x60;parent&#x60;
    :type parent: str

    """
    return web.Response(status=200)


async def list_score_tracks(request: web.Request, score, sharing_key=None, assignment=None, list_auto_track=None) -> web.Response:
    """List the audio or video tracks linked to a score

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str
    :param assignment: An assignment id with which all the tracks returned will be related to 
    :type assignment: str
    :param list_auto_track: If true, and if available, return last automatically synchronized Flat&#39;s mp3 export as an additional track 
    :type list_auto_track: bool

    """
    return web.Response(status=200)


async def mark_score_comment_resolved(request: web.Request, score, comment, sharing_key=None) -> web.Response:
    """Mark the comment as resolved

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param comment: Unique identifier of a sheet music comment 
    :type comment: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def mark_score_comment_unresolved(request: web.Request, score, comment, sharing_key=None) -> web.Response:
    """Mark the comment as unresolved

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param comment: Unique identifier of a sheet music comment 
    :type comment: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def post_score_comment(request: web.Request, score, body, sharing_key=None) -> web.Response:
    """Post a new comment

    Post a document or a contextualized comment on a document.  Please note that this method includes an anti-spam system for public scores. We don&#39;t guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a &#x60;403&#x60; HTTP error and hidden from other users when the &#x60;spam&#x60; property is &#x60;true&#x60;. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    body = ScoreCommentCreation.from_dict(body)
    return web.Response(status=200)


async def remove_score_collaborator(request: web.Request, score, collaborator) -> web.Response:
    """Delete a collaborator

    Remove the specified collaborator from the score 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param collaborator: Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
    :type collaborator: str

    """
    return web.Response(status=200)


async def untrash_score(request: web.Request, score) -> web.Response:
    """Untrash a score

    This method will remove the score from the &#x60;trash&#x60; collection and from the deletion queue, and add it back to the original collections. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str

    """
    return web.Response(status=200)


async def update_score_comment(request: web.Request, score, comment, body, sharing_key=None) -> web.Response:
    """Update an existing comment

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param comment: Unique identifier of a sheet music comment 
    :type comment: str
    :param body: 
    :type body: dict | bytes
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    body = ScoreCommentUpdate.from_dict(body)
    return web.Response(status=200)


async def update_score_track(request: web.Request, score, track, body) -> web.Response:
    """Update an audio or video track linked to a score

    

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param track: Unique identifier of a score audio track 
    :type track: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScoreTrackUpdate.from_dict(body)
    return web.Response(status=200)
