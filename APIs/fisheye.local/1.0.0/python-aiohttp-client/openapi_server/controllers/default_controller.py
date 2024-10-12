from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def find_slice_data(request: web.Request, repository, branch=None, id=None, direction=None, size=None) -> web.Response:
    """find_slice_data

    finds slice data the query

    :param repository: the key of the repository to search
    :type repository: str
    :param branch: the set of branches to search. If not specified, will search all branches
    :type branch: str
    :param id: the id of the changeset which we are
    :type id: str
    :param direction: the direction to traverse. May be \&quot;before\&quot;, \&quot;after\&quot; or \&quot;around\&quot;
    :type direction: str
    :param size: the number of changesets to return in the slice
    :type size: int

    """
    return web.Response(status=200)


async def get_all_repositories(request: web.Request, ) -> web.Response:
    """get_all_repositories

    List all the repositories.


    """
    return web.Response(status=200)


async def get_changeset(request: web.Request, csid, repository) -> web.Response:
    """get_changeset

    

    :param csid: the ChangesetID of the changeset to return.
    :type csid: str
    :param repository: the key of the repository to query.
    :type repository: str

    """
    return web.Response(status=200)


async def get_changeset_details(request: web.Request, repository) -> web.Response:
    """get_changeset_details

    Retrieves detailed information about a set of changesets in a repository, designed to be used with the FishEye commit graph

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def get_changesets_for_text(request: web.Request, rep=None, path=None, committer=None, comment=None, p4_job_fixed=None, expand=None, before_csid=None) -> web.Response:
    """get_changesets_for_text

    List of changesets from a repository.

    :param rep: the key of the repository
    :type rep: str
    :param path: repository path
    :type path: str
    :param committer: ID of the committer
    :type committer: str
    :param comment: comment to match
    :type comment: str
    :param p4_job_fixed: Perforce option to select the changesets marked as fixing
    :type p4_job_fixed: str
    :param expand: expand query parameter to specify the maximum number of results
    :type expand: str
    :param before_csid: parent of the changesets
    :type before_csid: str

    """
    return web.Response(status=200)


async def get_cross_repository_query(request: web.Request, query=None, repository=None, expand=None) -> web.Response:
    """get_cross_repository_query

    Execute a query across repositories. By default, this will search all repositories.

    :param query: text to search for in commit message and p4 jobId. Must not be empty.
    :type query: str
    :param repository: restrict search to only these repositories (by their keys)
    :type repository: str
    :param expand: expand query parameter to specify the maximum number of results. Format is changesets[n:m].revisions[n:m],reviews         the default number of changesets returned is 30, the maximum returned is 100
    :type expand: str

    """
    return web.Response(status=200)


async def get_path_list(request: web.Request, repository, path=None) -> web.Response:
    """get_path_list

    Get a list of information about files and directories in a path.

    :param repository: the key of the repository to query.
    :type repository: str
    :param path: the path to query, with respect to the fisheye repository root.
    :type path: str

    """
    return web.Response(status=200)


async def get_query(request: web.Request, repository, query=None, max_return=None) -> web.Response:
    """get_query

    Execute a FishEye query against a specific repository.

    :param repository: the key of the repository
    :type repository: str
    :param query: FishEye query to execute
    :type query: str
    :param max_return: maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results)
    :type max_return: str

    """
    return web.Response(status=200)


async def get_query_as_rows(request: web.Request, repository, query=None, max_return=None) -> web.Response:
    """get_query_as_rows

    Execute a FishEye query (that contains a \&quot;return\&quot; statement) against a specific repository.

    :param repository: the key of the repository
    :type repository: str
    :param query: FishEye query to execute (which must contain a \&quot;return\&quot; statement)
    :type query: str
    :param max_return: maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results)
    :type max_return: str

    """
    return web.Response(status=200)


async def get_repository_info(request: web.Request, repository) -> web.Response:
    """get_repository_info

    Get the information about a repository.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def get_reviews_for_changeset(request: web.Request, repository) -> web.Response:
    """get_reviews_for_changeset

    Retrieve a list of reviews for a changeset in a given repository.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def get_reviews_for_changesets(request: web.Request, repository) -> web.Response:
    """get_reviews_for_changesets

    Retrieve a list of reviews for each given changeset in a given repository.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def get_revision_info(request: web.Request, repository, path=None, revision=None) -> web.Response:
    """get_revision_info

    

    :param repository: the key of the repository to query.
    :type repository: str
    :param path: the path of the filerevision, with respect to the fisheye repository root.
    :type path: str
    :param revision: the id of the filerevision to retrieve.
    :type revision: str

    """
    return web.Response(status=200)


async def list_changesets(request: web.Request, repository, path=None, start=None, end=None, max_return=None) -> web.Response:
    """list_changesets

    Get a list of changesets on a repository.

    :param repository: the key of the repository to query.
    :type repository: str
    :param path: restrict the changesets to those in this path, should be \&quot;/\&quot; to look at the whole repository.
    :type path: str
    :param start: only return changesets after this date.
    :type start: str
    :param end: only return changesets before this date.
    :type end: str
    :param max_return: the maximum number of changesets to return.
    :type max_return: str

    """
    return web.Response(status=200)


async def list_path_history(request: web.Request, repository, path=None) -> web.Response:
    """list_path_history

    Get a list of the file revisions for a specific path.

    :param repository: the key of the repository to query.
    :type repository: str
    :param path: the path to query.
    :type path: str

    """
    return web.Response(status=200)


async def list_tags_for_revision(request: web.Request, repository, path=None, revision=None) -> web.Response:
    """list_tags_for_revision

    

    :param repository: the key of the repository to query.
    :type repository: str
    :param path: the path of the filerevision, with respect to the fisheye repository root.
    :type path: str
    :param revision: the id of the filerevision to retrieve.
    :type revision: str

    """
    return web.Response(status=200)
