from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_env_vars_request_inner import CreateEnvVarsRequestInner
from openapi_server.models.env_var import EnvVar
from openapi_server.models.error import Error
from openapi_server.models.set_env_var_value_request import SetEnvVarValueRequest
from openapi_server import util


async def create_env_vars(request: web.Request, account_id, site_id=None, env_vars=None) -> web.Response:
    """create_env_vars

    Creates new environment variables. Granular scopes are available on Pro plans and above.  To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param site_id: If provided, create an environment variable on the site level, not the account level
    :type site_id: str
    :param env_vars: 
    :type env_vars: list | bytes

    """
    env_vars = [CreateEnvVarsRequestInner.from_dict(d) for d in env_vars]
    return web.Response(status=200)


async def delete_env_var(request: web.Request, account_id, key, site_id=None) -> web.Response:
    """delete_env_var

    Deletes an environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param key: The environment variable key (case-sensitive)
    :type key: str
    :param site_id: If provided, delete the environment variable from this site
    :type site_id: str

    """
    return web.Response(status=200)


async def delete_env_var_value(request: web.Request, account_id, id, key, site_id=None) -> web.Response:
    """delete_env_var_value

    Deletes a specific environment variable value. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param id: The environment variable value&#39;s ID
    :type id: str
    :param key: The environment variable key name (case-sensitive)
    :type key: str
    :param site_id: If provided, delete the value from an environment variable on this site
    :type site_id: str

    """
    return web.Response(status=200)


async def get_env_var(request: web.Request, account_id, key, site_id=None) -> web.Response:
    """get_env_var

    Returns an individual environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param key: The environment variable key (case-sensitive)
    :type key: str
    :param site_id: If provided, return the environment variable for a specific site (no merging is performed)
    :type site_id: str

    """
    return web.Response(status=200)


async def get_env_vars(request: web.Request, account_id, context_name=None, scope=None, site_id=None) -> web.Response:
    """get_env_vars

    Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param context_name: Filter by deploy context
    :type context_name: str
    :param scope: Filter by scope
    :type scope: str
    :param site_id: If specified, only return environment variables set on this site
    :type site_id: str

    """
    return web.Response(status=200)


async def set_env_var_value(request: web.Request, account_id, key, site_id=None, env_var=None) -> web.Response:
    """set_env_var_value

    Updates or creates a new value for an existing environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param key: The existing environment variable key name (case-sensitive)
    :type key: str
    :param site_id: If provided, update an environment variable set on this site
    :type site_id: str
    :param env_var: 
    :type env_var: dict | bytes

    """
    env_var = SetEnvVarValueRequest.from_dict(env_var)
    return web.Response(status=200)


async def update_env_var(request: web.Request, account_id, key, site_id=None, env_var=None) -> web.Response:
    """update_env_var

    Updates an existing environment variable and all of its values. Existing values will be replaced by values provided. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

    :param account_id: Scope response to account_id
    :type account_id: str
    :param key: The existing environment variable key name (case-sensitive)
    :type key: str
    :param site_id: If provided, update an environment variable set on this site
    :type site_id: str
    :param env_var: 
    :type env_var: dict | bytes

    """
    env_var = CreateEnvVarsRequestInner.from_dict(env_var)
    return web.Response(status=200)
