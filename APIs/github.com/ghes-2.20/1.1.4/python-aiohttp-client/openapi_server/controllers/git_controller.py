from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.blob import Blob
from openapi_server.models.git_commit import GitCommit
from openapi_server.models.git_create_blob_request import GitCreateBlobRequest
from openapi_server.models.git_create_commit_request import GitCreateCommitRequest
from openapi_server.models.git_create_ref_request import GitCreateRefRequest
from openapi_server.models.git_create_tag_request import GitCreateTagRequest
from openapi_server.models.git_create_tree_request import GitCreateTreeRequest
from openapi_server.models.git_ref import GitRef
from openapi_server.models.git_tag import GitTag
from openapi_server.models.git_tree import GitTree
from openapi_server.models.git_update_ref_request import GitUpdateRefRequest
from openapi_server.models.short_blob import ShortBlob
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def git_create_blob(request: web.Request, owner, repo, body) -> web.Response:
    """Create a blob

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = GitCreateBlobRequest.from_dict(body)
    return web.Response(status=200)


async def git_create_commit(request: web.Request, owner, repo, body) -> web.Response:
    """Create a commit

    Creates a new Git [commit object](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects#Commit-Objects).  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = GitCreateCommitRequest.from_dict(body)
    return web.Response(status=200)


async def git_create_ref(request: web.Request, owner, repo, body) -> web.Response:
    """Create a reference

    Creates a reference for your repository. You are unable to create new references for empty repositories, even if the commit SHA-1 hash used exists. Empty repositories are repositories without branches.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = GitCreateRefRequest.from_dict(body)
    return web.Response(status=200)


async def git_create_tag(request: web.Request, owner, repo, body) -> web.Response:
    """Create a tag object

    Note that creating a tag object does not create the reference that makes a tag in Git. If you want to create an annotated tag in Git, you have to do this call to create the tag object, and then [create](https://docs.github.com/enterprise-server@2.20/rest/reference/git#create-a-reference) the &#x60;refs/tags/[tag]&#x60; reference. If you want to create a lightweight tag, you only have to [create](https://docs.github.com/enterprise-server@2.20/rest/reference/git#create-a-reference) the tag reference - this call would be unnecessary.  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = GitCreateTagRequest.from_dict(body)
    return web.Response(status=200)


async def git_create_tree(request: web.Request, owner, repo, body) -> web.Response:
    """Create a tree

    The tree creation API accepts nested entries. If you specify both a tree and a nested path modifying that tree, this endpoint will overwrite the contents of the tree with the new path contents, and create a new tree structure.  If you use this endpoint to add, delete, or modify the file contents in a tree, you will need to commit the tree and then update a branch to point to the commit. For more information see \&quot;[Create a commit](https://docs.github.com/enterprise-server@2.20/rest/reference/git#create-a-commit)\&quot; and \&quot;[Update a reference](https://docs.github.com/enterprise-server@2.20/rest/reference/git#update-a-reference).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = GitCreateTreeRequest.from_dict(body)
    return web.Response(status=200)


async def git_delete_ref(request: web.Request, owner, repo, ref) -> web.Response:
    """Delete a reference

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str

    """
    return web.Response(status=200)


async def git_get_blob(request: web.Request, owner, repo, file_sha) -> web.Response:
    """Get a blob

    The &#x60;content&#x60; in the response will always be Base64 encoded.  _Note_: This API supports blobs up to 100 megabytes in size.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param file_sha: 
    :type file_sha: str

    """
    return web.Response(status=200)


async def git_get_commit(request: web.Request, owner, repo, commit_sha) -> web.Response:
    """Get a commit

    Gets a Git [commit object](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects#Commit-Objects).  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param commit_sha: commit_sha parameter
    :type commit_sha: str

    """
    return web.Response(status=200)


async def git_get_ref(request: web.Request, owner, repo, ref) -> web.Response:
    """Get a reference

    Returns a single reference from your Git database. The &#x60;:ref&#x60; in the URL must be formatted as &#x60;heads/&lt;branch name&gt;&#x60; for branches and &#x60;tags/&lt;tag name&gt;&#x60; for tags. If the &#x60;:ref&#x60; doesn&#39;t match an existing ref, a &#x60;404&#x60; is returned.  **Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see \&quot;[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@2.20/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)\&quot;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str

    """
    return web.Response(status=200)


async def git_get_tag(request: web.Request, owner, repo, tag_sha) -> web.Response:
    """Get a tag

    **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param tag_sha: 
    :type tag_sha: str

    """
    return web.Response(status=200)


async def git_get_tree(request: web.Request, owner, repo, tree_sha, recursive=None) -> web.Response:
    """Get a tree

    Returns a single tree using the SHA1 value for that tree.  If &#x60;truncated&#x60; is &#x60;true&#x60; in the response then the number of items in the &#x60;tree&#x60; array exceeded our maximum limit. If you need to fetch more items, use the non-recursive method of fetching trees, and fetch one sub-tree at a time.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param tree_sha: 
    :type tree_sha: str
    :param recursive: Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in &#x60;:tree_sha&#x60;. For example, setting &#x60;recursive&#x60; to any of the following will enable returning objects or subtrees: &#x60;0&#x60;, &#x60;1&#x60;, &#x60;\&quot;true\&quot;&#x60;, and &#x60;\&quot;false\&quot;&#x60;. Omit this parameter to prevent recursively returning objects or subtrees.
    :type recursive: str

    """
    return web.Response(status=200)


async def git_list_matching_refs(request: web.Request, owner, repo, ref, per_page=None, page=None) -> web.Response:
    """List matching references

    Returns an array of references from your Git database that match the supplied name. The &#x60;:ref&#x60; in the URL must be formatted as &#x60;heads/&lt;branch name&gt;&#x60; for branches and &#x60;tags/&lt;tag name&gt;&#x60; for tags. If the &#x60;:ref&#x60; doesn&#39;t exist in the repository, but existing refs start with &#x60;:ref&#x60;, they will be returned as an array.  When you use this endpoint without providing a &#x60;:ref&#x60;, it will return an array of all the references from your Git database, including notes and stashes if they exist on the server. Anything in the namespace is returned, not just &#x60;heads&#x60; and &#x60;tags&#x60;.  **Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see \&quot;[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@2.20/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)\&quot;.  If you request matching references for a branch named &#x60;feature&#x60; but the branch &#x60;feature&#x60; doesn&#39;t exist, the response can still include other matching head refs that start with the word &#x60;feature&#x60;, such as &#x60;featureA&#x60; and &#x60;featureB&#x60;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def git_update_ref(request: web.Request, owner, repo, ref, body) -> web.Response:
    """Update a reference

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param body: 
    :type body: dict | bytes

    """
    body = GitUpdateRefRequest.from_dict(body)
    return web.Response(status=200)
