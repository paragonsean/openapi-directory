from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def add_allowed_reviewer_group(request: web.Request, key) -> web.Response:
    """add_allowed_reviewer_group

    Add group to project&#39;s allowed reviewer group list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def add_allowed_reviewer_user(request: web.Request, key) -> web.Response:
    """add_allowed_reviewer_user

    Add user to project&#39;s allowed reviewer users list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def add_default_reviewer_group(request: web.Request, key) -> web.Response:
    """add_default_reviewer_group

    Add group to project&#39;s default reviewer group list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def add_default_reviewer_user(request: web.Request, key) -> web.Response:
    """add_default_reviewer_user

    Add user to project&#39;s default reviewer users list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def add_group_to_permissions(request: web.Request, repository) -> web.Response:
    """add_group_to_permissions

    Note: use /rest-service-fecru/admin/repository-permissions/ endpoint for full repository permission administration functionality  Adds group to repository allowed groups

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def add_permission_scheme_anonymous_users(request: web.Request, name) -> web.Response:
    """add_permission_scheme_anonymous_users

    Add anonymous-user permission [action name] to given permission scheme  List of available action names:

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def add_permission_scheme_group(request: web.Request, name) -> web.Response:
    """add_permission_scheme_group

    Add group permission [group name, action name] to given permission scheme  List of available action names:

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def add_permission_scheme_logged_users(request: web.Request, name) -> web.Response:
    """add_permission_scheme_logged_users

    Add logged-in-users permission [action name] to given permission scheme  List of available action names:

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def add_permission_scheme_review_role(request: web.Request, name) -> web.Response:
    """add_permission_scheme_review_role

    Add review-role permission [role name, action name] to given permission scheme  List of available action names:     List of available role names:

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def add_permission_scheme_user(request: web.Request, name) -> web.Response:
    """add_permission_scheme_user

    Add user permission [username, action name] to given permission scheme  List of available action names:

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def add_repository(request: web.Request, ) -> web.Response:
    """add_repository

    Adds repository


    """
    return web.Response(status=200)


async def allowed_reviewer_groups(request: web.Request, key) -> web.Response:
    """allowed_reviewer_groups

    Retrieves project&#39;s allowed reviewer groups

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def allowed_reviewer_users(request: web.Request, key) -> web.Response:
    """allowed_reviewer_users

    Retrieves project&#39;s allowed reviewer users

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def default_permissions(request: web.Request, ) -> web.Response:
    """default_permissions

    Retrieve default repository permissions properties.


    """
    return web.Response(status=200)


async def default_reviewer_groups(request: web.Request, key) -> web.Response:
    """default_reviewer_groups

    Retrieves project&#39;s default reviewer groups

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def delete_allowed_reviewer_group(request: web.Request, key) -> web.Response:
    """delete_allowed_reviewer_group

    Delete group from project&#39;s allowed reviewer group list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def delete_allowed_reviewer_user(request: web.Request, key) -> web.Response:
    """delete_allowed_reviewer_user

    Remove user from project&#39;s allowed reviewer users list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def delete_default_reviewer_group(request: web.Request, key) -> web.Response:
    """delete_default_reviewer_group

    Delete group from project&#39;s default reviewer group list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def delete_default_reviewer_user(request: web.Request, key) -> web.Response:
    """delete_default_reviewer_user

    Remove user from project&#39;s default reviewer users list

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def delete_permission_scheme_anonymous_users(request: web.Request, name) -> web.Response:
    """delete_permission_scheme_anonymous_users

    Removes anonymous-user permission [action name] from given permission scheme

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def delete_permission_scheme_group(request: web.Request, name) -> web.Response:
    """delete_permission_scheme_group

    Removes group permission [group name, action name] from given permission scheme

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def delete_permission_scheme_logged_users(request: web.Request, name) -> web.Response:
    """delete_permission_scheme_logged_users

    Removes logged-in-users permission [action name] from given permission scheme

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def delete_permission_scheme_role(request: web.Request, name) -> web.Response:
    """delete_permission_scheme_role

    Removes review-role permission [role name, action name] from given permission scheme

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def delete_permission_scheme_user(request: web.Request, name) -> web.Response:
    """delete_permission_scheme_user

    Removes user permission [username, action name] from given permission scheme

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def delete_repository(request: web.Request, repository) -> web.Response:
    """delete_repository

    Deletes repository.  Warning: you can not undo this operation

    :param repository: the key of the repository to delete
    :type repository: str

    """
    return web.Response(status=200)


async def disable_repository(request: web.Request, repository) -> web.Response:
    """disable_repository

    Disables repository.

    :param repository: the key of the repository to disable
    :type repository: str

    """
    return web.Response(status=200)


async def do_review_revision_reindex(request: web.Request, repository, synchronous=None) -> web.Response:
    """do_review_revision_reindex

    Re-indexes all the Crucible revision data (which revisions have been reviewed)

    :param repository: the key of the repository to reindex
    :type repository: str
    :param synchronous: if true will wait for the indexing to finish before returning
    :type synchronous: bool

    """
    return web.Response(status=200)


async def do_share_content(request: web.Request, ) -> web.Response:
    """do_share_content

    


    """
    return web.Response(status=200)


async def enable_repository(request: web.Request, repository) -> web.Response:
    """enable_repository

    Enables repository.

    :param repository: the key of the repository to enable
    :type repository: str

    """
    return web.Response(status=200)


async def full_incremental_index(request: web.Request, repository) -> web.Response:
    """full_incremental_index

    Runs an full incremental repository index.  For CVS: scans the whole CVS repository for any changes since the last scan.  For other repository types will trigger an incremental index.

    :param repository: the key of the repository to scan
    :type repository: str

    """
    return web.Response(status=200)


async def get_global_pref(request: web.Request, _property) -> web.Response:
    """get_global_pref

    Getting user&#39;s global preference

    :param _property: the property(preference) name
    :type _property: str

    """
    return web.Response(status=200)


async def get_info(request: web.Request, ) -> web.Response:
    """get_info

    Provides general information about the server&#39;s configuration.


    """
    return web.Response(status=200)


async def get_recent(request: web.Request, ) -> web.Response:
    """get_recent

    Get a list of recently visited items for the currently logged in user.


    """
    return web.Response(status=200)


async def get_recent_detailed(request: web.Request, ) -> web.Response:
    """get_recent_detailed

    Get a list of recently visisted items for the currently logged in user, including the detailed entities.


    """
    return web.Response(status=200)


async def get_recent_projects(request: web.Request, ) -> web.Response:
    """get_recent_projects

    Get a list of recently visited projects for the currently logged in user.


    """
    return web.Response(status=200)


async def get_recent_projects_detailed(request: web.Request, ) -> web.Response:
    """get_recent_projects_detailed

    Get a list of recently visited projects for the currently logged in Project, including the detailed entities.


    """
    return web.Response(status=200)


async def get_recent_repositories(request: web.Request, ) -> web.Response:
    """get_recent_repositories

    Get a list of recently visited repositories for the currently logged in user.


    """
    return web.Response(status=200)


async def get_recent_repositories_detailed(request: web.Request, ) -> web.Response:
    """get_recent_repositories_detailed

    Get a list of recently visisted repositories for the currently logged in user, including the detailed entities.


    """
    return web.Response(status=200)


async def get_recent_reviews(request: web.Request, ) -> web.Response:
    """get_recent_reviews

    Get a list of recently visited reviews for the currently logged in user.


    """
    return web.Response(status=200)


async def get_recent_reviews_detailed(request: web.Request, ) -> web.Response:
    """get_recent_reviews_detailed

    Get a list of recently visited reviews for the currently logged in user, including the detailed entities.


    """
    return web.Response(status=200)


async def get_recent_snippets(request: web.Request, ) -> web.Response:
    """get_recent_snippets

    Get a list of recently visited snippets for the currently logged in user.


    """
    return web.Response(status=200)


async def get_recent_snippets_detailed(request: web.Request, ) -> web.Response:
    """get_recent_snippets_detailed

    Get a list of recently visited snippets for the currently logged in user, including the detailed entities.


    """
    return web.Response(status=200)


async def get_recent_users(request: web.Request, ) -> web.Response:
    """get_recent_users

    Get a list of recently visited users for the currently logged in user.


    """
    return web.Response(status=200)


async def get_recent_users_detailed(request: web.Request, ) -> web.Response:
    """get_recent_users_detailed

    Get a list of recently visited users for the currently logged in user, including the detailed entities.


    """
    return web.Response(status=200)


async def get_repo_pref(request: web.Request, _property, repository) -> web.Response:
    """get_repo_pref

    Getting user&#39;s preference related to a certain repository

    :param _property: the property(preference) name
    :type _property: str
    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def incremental_index(request: web.Request, repository, wait=None) -> web.Response:
    """incremental_index

    Runs an incremental repository index.  This is the same operation as triggered by scheduled indexing.  Can be called using the REST API Token to authorize.

    :param repository: the key of the repository to stop
    :type repository: str
    :param wait: if true will wait for the indexing to finish before returning
    :type wait: bool

    """
    return web.Response(status=200)


async def list_anonymous_users_principal_association(request: web.Request, name, action=None) -> web.Response:
    """list_anonymous_users_principal_association

    Retrieve a page of anonymous users permissions [action name] for given permission scheme.

    :param name: permission scheme name
    :type name: str
    :param action: action name
    :type action: str

    """
    return web.Response(status=200)


async def list_default_reviewer_users(request: web.Request, key) -> web.Response:
    """list_default_reviewer_users

    Retrieves project&#39;s default reviewer users

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def list_group_principal_association(request: web.Request, name, name2=None, action=None) -> web.Response:
    """list_group_principal_association

    Retrieve a page of group permissions [group name, action name] for given permission scheme.

    :param name: permission scheme name
    :type name: str
    :param name2: group name
    :type name2: str
    :param action: action name
    :type action: str

    """
    return web.Response(status=200)


async def list_group_users(request: web.Request, name) -> web.Response:
    """list_group_users

    Lists group&#39;s user names

    :param name: group name
    :type name: str

    """
    return web.Response(status=200)


async def list_logged_users_principal_association(request: web.Request, name, action=None) -> web.Response:
    """list_logged_users_principal_association

    Retrieve a page of logged in users permissions [action name] for given permission scheme.

    :param name: permission scheme name
    :type name: str
    :param action: action name
    :type action: str

    """
    return web.Response(status=200)


async def list_projects(request: web.Request, name) -> web.Response:
    """list_projects

    Retrieve a page of projects for given permission scheme.

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def list_roles_principal_association(request: web.Request, name, name2=None, action=None) -> web.Response:
    """list_roles_principal_association

    Retrieve a page of review-roles permissions [role name, action name] for given permission scheme.

    :param name: permission scheme name
    :type name: str
    :param name2: role name
    :type name2: str
    :param action: action name
    :type action: str

    """
    return web.Response(status=200)


async def list_user_groups(request: web.Request, name) -> web.Response:
    """list_user_groups

    Lists user&#39;s group names

    :param name: user name
    :type name: str

    """
    return web.Response(status=200)


async def list_user_principal_association(request: web.Request, name, name2=None, action=None) -> web.Response:
    """list_user_principal_association

    Retrieve a page of user permissions [username, action name] for given permission scheme.

    :param name: permission scheme name
    :type name: str
    :param name2: permission scheme name
    :type name2: str
    :param action: action name
    :type action: str

    """
    return web.Response(status=200)


async def login(request: web.Request, ) -> web.Response:
    """login

    Get the user authentication token.


    """
    return web.Response(status=200)


async def move_all_reviews(request: web.Request, source_project_key, destination_project_key) -> web.Response:
    """move_all_reviews

    Move reviews and snippets from source project to destination project

    :param source_project_key: project key of reviews and snippets source project
    :type source_project_key: str
    :param destination_project_key: project key of reviews and snippets destination project
    :type destination_project_key: str

    """
    return web.Response(status=200)


async def permissions(request: web.Request, repository) -> web.Response:
    """permissions

    Retrieve repository permissions properties.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def permissions_groups(request: web.Request, repository) -> web.Response:
    """permissions_groups

    Note: use /rest-service-fecru/admin/repository-permissions/ endpoint for full repository permission administration functionality  Lists groups allowed to access repository.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def rebuild_search_index(request: web.Request, repository) -> web.Response:
    """rebuild_search_index

    Rebuilds the search index data for the given repository. This will rebuild the data used to search by path,  commit message and comitter, also used for activity streams and JIRA integration.

    :param repository: the key of the repository to re-index.
    :type repository: str

    """
    return web.Response(status=200)


async def reindex_changeset_comments(request: web.Request, repository) -> web.Response:
    """reindex_changeset_comments

    Rebuilds the changeset discussion index for the specified repository. The index is used to display changeset  discussions in activity streams.

    :param repository: the key of the repository to perform the operation for
    :type repository: str

    """
    return web.Response(status=200)


async def reindex_changeset_discussion(request: web.Request, repository) -> web.Response:
    """reindex_changeset_discussion

    Rebuilds the changeset discussion index for the specified repository. The index is used to display changeset  discussions in activity streams.

    :param repository: the key of the repository to perform the operation for
    :type repository: str

    """
    return web.Response(status=200)


async def reindex_reviews(request: web.Request, repository) -> web.Response:
    """reindex_reviews

    Re-indexes all the Crucible revision data (which revisions have been reviewed)

    :param repository: the key of the repository to reindex
    :type repository: str

    """
    return web.Response(status=200)


async def reindex_search(request: web.Request, repository) -> web.Response:
    """reindex_search

    Rebuilds the search index data for the given repository. This will rebuild the data used to search by path,  commit message and committer, also used for activity streams and JIRA integration.

    :param repository: the key of the repository to re-index.
    :type repository: str

    """
    return web.Response(status=200)


async def remove_group_to_permissions(request: web.Request, repository) -> web.Response:
    """remove_group_to_permissions

    Delete group from repository allowed groups

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def repository_updates(request: web.Request, repository) -> web.Response:
    """repository_updates

    Retrieves repository updates properties.

    :param repository: repository key
    :type repository: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_get(request: web.Request, prefix=None) -> web.Response:
    """rest_service_fecru_admin_groups_get

    Retrieve a page of groups.

    :param prefix: filter groups by name prefix
    :type prefix: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_name_delete(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_groups_name_delete

    Deletes a group by name

    :param name: group name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_name_get(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_groups_name_get

    Retrieve a group by name.

    :param name: group name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_name_put(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_groups_name_put

    Updates an existing group.

    :param name: group name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_name_users_delete(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_groups_name_users_delete

    Removes user from group

    :param name: group name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_name_users_put(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_groups_name_users_put

    Adds user to group

    :param name: group name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_groups_post(request: web.Request, ) -> web.Response:
    """rest_service_fecru_admin_groups_post

    Creates a new user group.


    """
    return web.Response(status=200)


async def rest_service_fecru_admin_permission_schemes_get(request: web.Request, name=None) -> web.Response:
    """rest_service_fecru_admin_permission_schemes_get

    Retrieve a page of permission schemes.

    :param name: permission scheme name part filter, case insensitive, optional
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_permission_schemes_name_delete(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_permission_schemes_name_delete

    Deletes a permission scheme by name

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_permission_schemes_name_get(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_permission_schemes_name_get

    Retrieve a permission scheme by name

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_permission_schemes_name_put(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_permission_schemes_name_put

    Updates an existing permission scheme.

    :param name: permission scheme name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_permission_schemes_post(request: web.Request, copy_from=None) -> web.Response:
    """rest_service_fecru_admin_permission_schemes_post

    Creates a new permission scheme. The new permission scheme is blank or can be created from another existing permission scheme.

    :param copy_from: if set, the new permission scheme will be a copy of permissionSchemeName
    :type copy_from: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_projects_get(request: web.Request, name=None, key=None, default_repository_name=None, permission_scheme_name=None) -> web.Response:
    """rest_service_fecru_admin_projects_get

    Retrieve a page of projects.

    :param name: project&#39;s name part filter, optional
    :type name: str
    :param key: project&#39;s key part filter, optional
    :type key: str
    :param default_repository_name: project&#39;s default repository key part filter, optional
    :type default_repository_name: str
    :param permission_scheme_name: project&#39;s permission scheme pare name filter, optional
    :type permission_scheme_name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_projects_key_delete(request: web.Request, key, delete_project_reviews=None) -> web.Response:
    """rest_service_fecru_admin_projects_key_delete

    Deletes a project by key (including all reviews in this project).  Use   to move reviews to another project.

    :param key: project key
    :type key: str
    :param delete_project_reviews: if true deletes reviews in project
    :type delete_project_reviews: bool

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_projects_key_get(request: web.Request, key) -> web.Response:
    """rest_service_fecru_admin_projects_key_get

    Retrieve a project by key.

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_projects_key_put(request: web.Request, key) -> web.Response:
    """rest_service_fecru_admin_projects_key_put

    Updates an existing project.

    :param key: project key
    :type key: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_projects_post(request: web.Request, ) -> web.Response:
    """rest_service_fecru_admin_projects_post

    Creates a new project.


    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_get(request: web.Request, type=None, enabled=None, started=None) -> web.Response:
    """rest_service_fecru_admin_repositories_get

    Retrieve a page of repositories. Repository properties with default values may not be returned.

    :param type: filter repositories by repository type: svn, git, hg, cvs, p4, ...
    :type type: str
    :param enabled: filter repositories by enabled flag
    :type enabled: bool
    :param started: filter repositories by started flag
    :type started: bool

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_post(request: web.Request, ) -> web.Response:
    """rest_service_fecru_admin_repositories_post

    Creates a repository.


    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_repository_delete(request: web.Request, repository) -> web.Response:
    """rest_service_fecru_admin_repositories_repository_delete

    Deletes a repository by key

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_repository_get(request: web.Request, repository) -> web.Response:
    """rest_service_fecru_admin_repositories_repository_get

    Retrieve a repository by key. Repository properties with default values may not be returned.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_repository_put(request: web.Request, repository) -> web.Response:
    """rest_service_fecru_admin_repositories_repository_put

    Updates an existing repository.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_repository_reindex_linecount_put(request: web.Request, repository) -> web.Response:
    """rest_service_fecru_admin_repositories_repository_reindex_linecount_put

    Re-indexes the linecount data used to generate the LOC graphs. The linecount data will be recalculated in daily  buckets based on the server timezone.

    :param repository: the key of the repository to re-index
    :type repository: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_repository_reindex_source_put(request: web.Request, repository, clone=None) -> web.Response:
    """rest_service_fecru_admin_repositories_repository_reindex_source_put

    Deletes the existing cache and re-indexes the repository from scratch.  For large or slow repositories this may take some time, during which some functionality will be unavailable.  This action will also restart the repository.

    :param repository: the key of the repository to reindex
    :type repository: str
    :param clone: if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository before re-indexing
    :type clone: bool

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_repository_rescan_metadata_put(request: web.Request, repository, _from=None, to=None) -> web.Response:
    """rest_service_fecru_admin_repositories_repository_rescan_metadata_put

    Re-scans the repository metadata. Only valid for Perforce and SVN repositories.

    :param repository: the key of the repository to re-scan
    :type repository: str
    :param _from: the revision number to start at
    :type _from: str
    :param to: the revision number to end at
    :type to: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_v1_repository_reindex_linecount_post(request: web.Request, repository) -> web.Response:
    """rest_service_fecru_admin_repositories_v1_repository_reindex_linecount_post

    Re-indexes the linecount data used to generate the LOC graphs. The linecount data will be recalculated in daily  buckets based on the server timezone.

    :param repository: the key of the repository to re-index
    :type repository: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_v1_repository_reindex_source_post(request: web.Request, repository, clone=None) -> web.Response:
    """rest_service_fecru_admin_repositories_v1_repository_reindex_source_post

    Deletes the existing cache and re-indexes the repository from scratch.  For large or slow repositories this may take some time, during which some functionality will be unavailable.  This action will also restart the repository.

    :param repository: the key of the repository to reindex
    :type repository: str
    :param clone: if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository  before re-indexing
    :type clone: bool

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_repositories_v1_repository_rescan_metadata_post(request: web.Request, repository, _from=None, to=None) -> web.Response:
    """rest_service_fecru_admin_repositories_v1_repository_rescan_metadata_post

    Re-scans the repository metadata for SVN and Perforce repositories. Only valid for Perforce and SVN repositories.

    :param repository: the key of the repository to re-scan
    :type repository: str
    :param _from: the revision number to start at
    :type _from: int
    :param to: the revision number to end at
    :type to: int

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_get(request: web.Request, ) -> web.Response:
    """rest_service_fecru_admin_users_get

    Retrieve a page of users.


    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_name_delete(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_users_name_delete

    Deletes a user by name

    :param name: user name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_name_get(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_users_name_get

    Retrieve a user by name.

    :param name: user name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_name_groups_delete(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_users_name_groups_delete

    Removes user from group

    :param name: user name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_name_groups_put(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_users_name_groups_put

    Adds user to group

    :param name: user name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_name_put(request: web.Request, name) -> web.Response:
    """rest_service_fecru_admin_users_name_put

    Updates an existing user.

    :param name: user name
    :type name: str

    """
    return web.Response(status=200)


async def rest_service_fecru_admin_users_post(request: web.Request, ) -> web.Response:
    """rest_service_fecru_admin_users_post

    Creates a new user. Tries to add the user to fisheye-users and crucible-users groups if those exist.


    """
    return web.Response(status=200)


async def rest_service_fecru_indexing_status_v1_status_repository_get(request: web.Request, repository) -> web.Response:
    """rest_service_fecru_indexing_status_v1_status_repository_get

    Returns indexing status of given repository.

    :param repository: the key of the repository to get status of
    :type repository: str

    """
    return web.Response(status=200)


async def scan(request: web.Request, repository, synchronous=None) -> web.Response:
    """scan

    Runs an incremental repository index now.  This is the same operation as triggered by scheduled indexing.  Can be called using the REST Api Token to authorize.

    :param repository: the key of the repository to run scan for
    :type repository: str
    :param synchronous: if true will wait for the indexing to finish before returning
    :type synchronous: bool

    """
    return web.Response(status=200)


async def scan_cvs(request: web.Request, repository) -> web.Response:
    """scan_cvs

    Scans the whole CVS repository for any changes since the last scan. Only valid for CVS repositories.

    :param repository: the key of the repository to scan
    :type repository: str

    """
    return web.Response(status=200)


async def set_pref(request: web.Request, ) -> web.Response:
    """set_pref

    Using POST method to set a user preference.  If repo is not set, the preference will be recognised as a global preference.


    """
    return web.Response(status=200)


async def start(request: web.Request, repository) -> web.Response:
    """start

    Starts repository. Does not wait for the repository to start before returning.

    :param repository: the key of the repository to start
    :type repository: str

    """
    return web.Response(status=200)


async def start_repository(request: web.Request, repository) -> web.Response:
    """start_repository

    Starts the repository.

    :param repository: the key of the repository to start
    :type repository: str

    """
    return web.Response(status=200)


async def stop(request: web.Request, repository) -> web.Response:
    """stop

    Stops repository. Does not wait for the repository to stop before returning.

    :param repository: the key of the repository to stop
    :type repository: str

    """
    return web.Response(status=200)


async def stop_repository(request: web.Request, repository) -> web.Response:
    """stop_repository

    Stops the repository. Does not wait for the repository to stop before returning.

    :param repository: the key of the repository to stop
    :type repository: str

    """
    return web.Response(status=200)


async def update_default_permissions(request: web.Request, ) -> web.Response:
    """update_default_permissions

    Updates default repository permissions properties.   Valid permission settings: any combination of allowAnonymous, allowLoggedIn


    """
    return web.Response(status=200)


async def update_permissions(request: web.Request, repository) -> web.Response:
    """update_permissions

    Updates repository permissions properties.   Valid permission settings: any combination of useDefaults, allowAnonymous, allowLoggedIn.

    :param repository: the key of the repository
    :type repository: str

    """
    return web.Response(status=200)


async def update_repository_updates(request: web.Request, repository) -> web.Response:
    """update_repository_updates

    

    :param repository: repository key
    :type repository: str

    """
    return web.Response(status=200)
