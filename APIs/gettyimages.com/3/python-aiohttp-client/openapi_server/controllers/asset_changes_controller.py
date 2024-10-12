from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset_changes import AssetChanges
from openapi_server.models.channel import Channel
from openapi_server import util


async def v3_asset_changes_change_sets_change_set_id_delete(request: web.Request, change_set_id) -> web.Response:
    """Confirm asset change notifications.

    # Delete Asset Changes  Confirm asset changes acknowledges receipt of asset changes (from the PUT asset-changes endpoint).  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.  Use the change_set_id from the PUT asset-changes/change-sets endpoint to confirm receipt of notifications. 

    :param change_set_id: Specify the change-set-id associated with a transaction resource whose receipt you want to confirm.
    :type change_set_id: int

    """
    return web.Response(status=200)


async def v3_asset_changes_change_sets_put(request: web.Request, channel_id=None, batch_size=None) -> web.Response:
    """Get asset change notifications.

    # Asset Changes  Get notifications about new, updated or deleted assets for a specific channel.  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.   Maximum batch size is 2200.  Change-sets must be confirmed before a new batch of notifications can be retrieved from this endpoint. Use the DELETE asset-changes/change-sets/{change-set-id} endpoint to confirm reciept of these notifications.  Values returned for asset_type include Image, Film, and null. Values returned for asset_lifecycle include New, Update, and Delete.  Delete notifications may be provided for asset ids that have not previously been received as New or Update notifications. Delete notifications may return null for the asset_type.  If there are no notifications in the channel an empty response body will be returned.  Notifications older than 60 days will be removed from partner channels. 

    :param channel_id: Specifies the id of the channel for the asset data. Valid channel ids can be found in the results of the Get Partner Channel query.
    :type channel_id: int
    :param batch_size: Specifies the number of assets to return. The default is 2200; maximum is 2200.
    :type batch_size: int

    """
    return web.Response(status=200)


async def v3_asset_changes_channels_get(request: web.Request, ) -> web.Response:
    """Get a list of asset change notification channels.

    # Get Partner Channels  Retrieves the channel data for the partner. This data can be used to populate the channel_id parameter in the Put Asset Changes query.  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.  Partners who have a channel that has been removed should contact their sales representative to be set up again.  


    """
    return web.Response(status=200)
