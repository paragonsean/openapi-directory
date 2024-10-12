from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def active_sessions(request: web.Request, ) -> web.Response:
    """&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    


    """
    return web.Response(status=200)


async def panic_terminate(request: web.Request, blazemeter_routing_v4_user_model5=None) -> web.Response:
    """&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param blazemeter_routing_v4_user_model5: &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;session_ids&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt;
    :type blazemeter_routing_v4_user_model5: 

    """
    return web.Response(status=200)


async def register(request: web.Request, blazemeter_routing_v4_user_model4) -> web.Response:
    """Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param blazemeter_routing_v4_user_model4: &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;firstName&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;lastName&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;email&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;password&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt;
    :type blazemeter_routing_v4_user_model4: 

    """
    return web.Response(status=200)


async def register_retrieve(request: web.Request, email, password, first_name=None, last_name=None) -> web.Response:
    """Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param email: Email address
    :type email: str
    :param password: Password
    :type password: str
    :param first_name: First name
    :type first_name: str
    :param last_name: Last name
    :type last_name: str

    """
    return web.Response(status=200)


async def retrieve_collections(request: web.Request, skip=None, limit=None) -> web.Response:
    """List organization multi-tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param skip: 
    :type skip: str
    :param limit: 
    :type limit: str

    """
    return web.Response(status=200)


async def retrieve_invites(request: web.Request, ) -> web.Response:
    """&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    


    """
    return web.Response(status=200)


async def retrieve_locations(request: web.Request, ) -> web.Response:
    """Get user available locations&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    


    """
    return web.Response(status=200)


async def retrieve_masters(request: web.Request, skip=None, limit=None) -> web.Response:
    """List user private masters&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param skip: 
    :type skip: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def retrieve_projects(request: web.Request, ) -> web.Response:
    """Get user projects&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    


    """
    return web.Response(status=200)


async def retrieve_tests(request: web.Request, skip=None, limit=None) -> web.Response:
    """List user private tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param skip: 
    :type skip: str
    :param limit: 
    :type limit: str

    """
    return web.Response(status=200)


async def top(request: web.Request, ) -> web.Response:
    """&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    


    """
    return web.Response(status=200)


async def user_password_patch(request: web.Request, blazemeter_routing_v4_user_model1) -> web.Response:
    """Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param blazemeter_routing_v4_user_model1: &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt;
    :type blazemeter_routing_v4_user_model1: 

    """
    return web.Response(status=200)


async def user_password_post(request: web.Request, blazemeter_routing_v4_user_model3) -> web.Response:
    """Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param blazemeter_routing_v4_user_model3: &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt;
    :type blazemeter_routing_v4_user_model3: 

    """
    return web.Response(status=200)


async def user_password_put(request: web.Request, blazemeter_routing_v4_user_model2) -> web.Response:
    """Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

    

    :param blazemeter_routing_v4_user_model2: &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt;
    :type blazemeter_routing_v4_user_model2: 

    """
    return web.Response(status=200)
