from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_tracker_consumer_request import AssociateTrackerConsumerRequest
from openapi_server.models.batch_delete_device_position_history_request import BatchDeleteDevicePositionHistoryRequest
from openapi_server.models.batch_delete_device_position_history_response import BatchDeleteDevicePositionHistoryResponse
from openapi_server.models.batch_delete_geofence_request import BatchDeleteGeofenceRequest
from openapi_server.models.batch_delete_geofence_response import BatchDeleteGeofenceResponse
from openapi_server.models.batch_evaluate_geofences_request import BatchEvaluateGeofencesRequest
from openapi_server.models.batch_evaluate_geofences_response import BatchEvaluateGeofencesResponse
from openapi_server.models.batch_get_device_position_request import BatchGetDevicePositionRequest
from openapi_server.models.batch_get_device_position_response import BatchGetDevicePositionResponse
from openapi_server.models.batch_put_geofence_request import BatchPutGeofenceRequest
from openapi_server.models.batch_put_geofence_response import BatchPutGeofenceResponse
from openapi_server.models.batch_update_device_position_request import BatchUpdateDevicePositionRequest
from openapi_server.models.batch_update_device_position_response import BatchUpdateDevicePositionResponse
from openapi_server.models.calculate_route_matrix_request import CalculateRouteMatrixRequest
from openapi_server.models.calculate_route_matrix_response import CalculateRouteMatrixResponse
from openapi_server.models.calculate_route_request import CalculateRouteRequest
from openapi_server.models.calculate_route_response import CalculateRouteResponse
from openapi_server.models.create_geofence_collection_request import CreateGeofenceCollectionRequest
from openapi_server.models.create_geofence_collection_response import CreateGeofenceCollectionResponse
from openapi_server.models.create_key_request import CreateKeyRequest
from openapi_server.models.create_key_response import CreateKeyResponse
from openapi_server.models.create_map_request import CreateMapRequest
from openapi_server.models.create_map_response import CreateMapResponse
from openapi_server.models.create_place_index_request import CreatePlaceIndexRequest
from openapi_server.models.create_place_index_response import CreatePlaceIndexResponse
from openapi_server.models.create_route_calculator_request import CreateRouteCalculatorRequest
from openapi_server.models.create_route_calculator_response import CreateRouteCalculatorResponse
from openapi_server.models.create_tracker_request import CreateTrackerRequest
from openapi_server.models.create_tracker_response import CreateTrackerResponse
from openapi_server.models.describe_geofence_collection_response import DescribeGeofenceCollectionResponse
from openapi_server.models.describe_key_response import DescribeKeyResponse
from openapi_server.models.describe_map_response import DescribeMapResponse
from openapi_server.models.describe_place_index_response import DescribePlaceIndexResponse
from openapi_server.models.describe_route_calculator_response import DescribeRouteCalculatorResponse
from openapi_server.models.describe_tracker_response import DescribeTrackerResponse
from openapi_server.models.get_device_position_history_request import GetDevicePositionHistoryRequest
from openapi_server.models.get_device_position_history_response import GetDevicePositionHistoryResponse
from openapi_server.models.get_device_position_response import GetDevicePositionResponse
from openapi_server.models.get_geofence_response import GetGeofenceResponse
from openapi_server.models.get_map_glyphs_response import GetMapGlyphsResponse
from openapi_server.models.get_map_sprites_response import GetMapSpritesResponse
from openapi_server.models.get_map_style_descriptor_response import GetMapStyleDescriptorResponse
from openapi_server.models.get_map_tile_response import GetMapTileResponse
from openapi_server.models.get_place_response import GetPlaceResponse
from openapi_server.models.list_device_positions_request import ListDevicePositionsRequest
from openapi_server.models.list_device_positions_response import ListDevicePositionsResponse
from openapi_server.models.list_geofence_collections_request import ListGeofenceCollectionsRequest
from openapi_server.models.list_geofence_collections_response import ListGeofenceCollectionsResponse
from openapi_server.models.list_geofences_request import ListGeofencesRequest
from openapi_server.models.list_geofences_response import ListGeofencesResponse
from openapi_server.models.list_keys_request import ListKeysRequest
from openapi_server.models.list_keys_response import ListKeysResponse
from openapi_server.models.list_maps_request import ListMapsRequest
from openapi_server.models.list_maps_response import ListMapsResponse
from openapi_server.models.list_place_indexes_request import ListPlaceIndexesRequest
from openapi_server.models.list_place_indexes_response import ListPlaceIndexesResponse
from openapi_server.models.list_route_calculators_request import ListRouteCalculatorsRequest
from openapi_server.models.list_route_calculators_response import ListRouteCalculatorsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_tracker_consumers_response import ListTrackerConsumersResponse
from openapi_server.models.list_trackers_response import ListTrackersResponse
from openapi_server.models.put_geofence_request import PutGeofenceRequest
from openapi_server.models.put_geofence_response import PutGeofenceResponse
from openapi_server.models.search_place_index_for_position_request import SearchPlaceIndexForPositionRequest
from openapi_server.models.search_place_index_for_position_response import SearchPlaceIndexForPositionResponse
from openapi_server.models.search_place_index_for_suggestions_request import SearchPlaceIndexForSuggestionsRequest
from openapi_server.models.search_place_index_for_suggestions_response import SearchPlaceIndexForSuggestionsResponse
from openapi_server.models.search_place_index_for_text_request import SearchPlaceIndexForTextRequest
from openapi_server.models.search_place_index_for_text_response import SearchPlaceIndexForTextResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_geofence_collection_request import UpdateGeofenceCollectionRequest
from openapi_server.models.update_geofence_collection_response import UpdateGeofenceCollectionResponse
from openapi_server.models.update_key_request import UpdateKeyRequest
from openapi_server.models.update_key_response import UpdateKeyResponse
from openapi_server.models.update_map_request import UpdateMapRequest
from openapi_server.models.update_map_response import UpdateMapResponse
from openapi_server.models.update_place_index_request import UpdatePlaceIndexRequest
from openapi_server.models.update_place_index_response import UpdatePlaceIndexResponse
from openapi_server.models.update_route_calculator_request import UpdateRouteCalculatorRequest
from openapi_server.models.update_route_calculator_response import UpdateRouteCalculatorResponse
from openapi_server.models.update_tracker_request import UpdateTrackerRequest
from openapi_server.models.update_tracker_response import UpdateTrackerResponse
from openapi_server import util


async def associate_tracker_consumer(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_tracker_consumer

    &lt;p&gt;Creates an association between a geofence collection and a tracker resource. This allows the tracker resource to communicate location data to the linked geofence collection. &lt;/p&gt; &lt;p&gt;You can associate up to five geofence collections to each tracker resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Currently not supported — Cross-account configurations, such as creating associations between a tracker resource in one account and a geofence collection in another account.&lt;/p&gt; &lt;/note&gt;

    :param tracker_name: The name of the tracker resource to be associated with a geofence collection.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateTrackerConsumerRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_device_position_history(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_device_position_history

    Deletes the position history of one or more devices from a tracker resource.

    :param tracker_name: The name of the tracker resource to delete the device position history from.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDeleteDevicePositionHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_geofence(request: web.Request, collection_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_geofence

    &lt;p&gt;Deletes a batch of geofences from a geofence collection.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently.&lt;/p&gt; &lt;/note&gt;

    :param collection_name: The geofence collection storing the geofences to be deleted.
    :type collection_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDeleteGeofenceRequest.from_dict(body)
    return web.Response(status=200)


async def batch_evaluate_geofences(request: web.Request, collection_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_evaluate_geofences

    &lt;p&gt;Evaluates device positions against the geofence geometries from a given geofence collection.&lt;/p&gt; &lt;p&gt;This operation always returns an empty response because geofences are asynchronously evaluated. The evaluation determines if the device has entered or exited a geofenced area, and then publishes one of the following events to Amazon EventBridge:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ENTER&lt;/code&gt; if Amazon Location determines that the tracked device has entered a geofenced area.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EXIT&lt;/code&gt; if Amazon Location determines that the tracked device has exited a geofenced area.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The last geofence that a device was observed within is tracked for 30 days after the most recent device position update.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Geofence evaluation uses the given device position. It does not account for the optional &lt;code&gt;Accuracy&lt;/code&gt; of a &lt;code&gt;DevicePositionUpdate&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;DeviceID&lt;/code&gt; is used as a string to represent the device. You do not need to have a &lt;code&gt;Tracker&lt;/code&gt; associated with the &lt;code&gt;DeviceID&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param collection_name: The geofence collection used in evaluating the position of devices against its geofences.
    :type collection_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchEvaluateGeofencesRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_device_position(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_device_position

    Lists the latest device positions for requested devices.

    :param tracker_name: The tracker resource retrieving the device position.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGetDevicePositionRequest.from_dict(body)
    return web.Response(status=200)


async def batch_put_geofence(request: web.Request, collection_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_put_geofence

    A batch request for storing geofence geometries into a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.

    :param collection_name: The geofence collection storing the geofences.
    :type collection_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchPutGeofenceRequest.from_dict(body)
    return web.Response(status=200)


async def batch_update_device_position(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_device_position

    &lt;p&gt;Uploads position update data for one or more devices to a tracker resource (up to 10 devices per batch). Amazon Location uses the data when it reports the last known device position and position history. Amazon Location retains location data for 30 days.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Position updates are handled based on the &lt;code&gt;PositionFiltering&lt;/code&gt; property of the tracker. When &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;TimeBased&lt;/code&gt;, updates are evaluated against linked geofence collections, and location data is stored at a maximum of one position per 30 second interval. If your update frequency is more often than every 30 seconds, only one update per 30 seconds is stored for each unique device ID.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;DistanceBased&lt;/code&gt; filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than 30 m (98.4 ft).&lt;/p&gt; &lt;p&gt;When &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;AccuracyBased&lt;/code&gt; filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than the measured accuracy. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is neither stored or evaluated if the device has moved less than 15 m. If &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;AccuracyBased&lt;/code&gt; filtering, Amazon Location uses the default value &lt;code&gt;{ \&quot;Horizontal\&quot;: 0}&lt;/code&gt; when accuracy is not provided on a &lt;code&gt;DevicePositionUpdate&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param tracker_name: The name of the tracker resource to update.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchUpdateDevicePositionRequest.from_dict(body)
    return web.Response(status=200)


async def calculate_route(request: web.Request, calculator_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """calculate_route

    &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/calculate-route.html\&quot;&gt;Calculates a route&lt;/a&gt; given the following required parameters: &lt;code&gt;DeparturePosition&lt;/code&gt; and &lt;code&gt;DestinationPosition&lt;/code&gt;. Requires that you first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html\&quot;&gt;create a route calculator resource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;By default, a request that doesn&#39;t specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.&lt;/p&gt; &lt;p&gt;Additional options include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/departure-time.html\&quot;&gt;Specifying a departure time&lt;/a&gt; using either &lt;code&gt;DepartureTime&lt;/code&gt; or &lt;code&gt;DepartNow&lt;/code&gt;. This calculates a route based on predictive traffic data at the given time. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t specify both &lt;code&gt;DepartureTime&lt;/code&gt; and &lt;code&gt;DepartNow&lt;/code&gt; in a single request. Specifying both parameters returns a validation error.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/travel-mode.html\&quot;&gt;Specifying a travel mode&lt;/a&gt; using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in &lt;code&gt;CarModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Car&lt;/code&gt;, or &lt;code&gt;TruckModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Truck&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you specify &lt;code&gt;walking&lt;/code&gt; for the travel mode and your data provider is Esri, the start and destination must be within 40km.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt;

    :param calculator_name: The name of the route calculator resource that you want to use to calculate the route. 
    :type calculator_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    body = CalculateRouteRequest.from_dict(body)
    return web.Response(status=200)


async def calculate_route_matrix(request: web.Request, calculator_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """calculate_route_matrix

    &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html\&quot;&gt; Calculates a route matrix&lt;/a&gt; given the following required parameters: &lt;code&gt;DeparturePositions&lt;/code&gt; and &lt;code&gt;DestinationPositions&lt;/code&gt;. &lt;code&gt;CalculateRouteMatrix&lt;/code&gt; calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, &lt;code&gt;CalculateRouteMatrix&lt;/code&gt; will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of &lt;code&gt;DeparturePositions&lt;/code&gt; times the number of &lt;code&gt;DestinationPositions&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Your account is charged for each route calculated, not the number of requests.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Requires that you first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html\&quot;&gt;create a route calculator resource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;By default, a request that doesn&#39;t specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.&lt;/p&gt; &lt;p&gt;Additional options include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/departure-time.html\&quot;&gt; Specifying a departure time&lt;/a&gt; using either &lt;code&gt;DepartureTime&lt;/code&gt; or &lt;code&gt;DepartNow&lt;/code&gt;. This calculates routes based on predictive traffic data at the given time. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t specify both &lt;code&gt;DepartureTime&lt;/code&gt; and &lt;code&gt;DepartNow&lt;/code&gt; in a single request. Specifying both parameters returns a validation error.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/travel-mode.html\&quot;&gt;Specifying a travel mode&lt;/a&gt; using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in &lt;code&gt;CarModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Car&lt;/code&gt;, or &lt;code&gt;TruckModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Truck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param calculator_name: The name of the route calculator resource that you want to use to calculate the route matrix. 
    :type calculator_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    body = CalculateRouteMatrixRequest.from_dict(body)
    return web.Response(status=200)


async def create_geofence_collection(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_geofence_collection

    Creates a geofence collection, which manages and stores geofences.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateGeofenceCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def create_key(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_key

    &lt;p&gt;Creates an API key resource in your Amazon Web Services account, which lets you grant actions for Amazon Location resources to the API key bearer.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;Using API keys&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateKeyRequest.from_dict(body)
    return web.Response(status=200)


async def create_map(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_map

    &lt;p&gt;Creates a map resource in your Amazon Web Services account, which provides map tiles of different styles sourced from global location data providers.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms\&quot;&gt;Amazon Web Services service terms&lt;/a&gt; for more details.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateMapRequest.from_dict(body)
    return web.Response(status=200)


async def create_place_index(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_place_index

    &lt;p&gt;Creates a place index resource in your Amazon Web Services account. Use a place index resource to geocode addresses and other text queries by using the &lt;code&gt;SearchPlaceIndexForText&lt;/code&gt; operation, and reverse geocode coordinates by using the &lt;code&gt;SearchPlaceIndexForPosition&lt;/code&gt; operation, and enable autosuggestions by using the &lt;code&gt;SearchPlaceIndexForSuggestions&lt;/code&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms\&quot;&gt;Amazon Web Services service terms&lt;/a&gt; for more details.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePlaceIndexRequest.from_dict(body)
    return web.Response(status=200)


async def create_route_calculator(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_route_calculator

    &lt;p&gt;Creates a route calculator resource in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms\&quot;&gt;Amazon Web Services service terms&lt;/a&gt; for more details.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRouteCalculatorRequest.from_dict(body)
    return web.Response(status=200)


async def create_tracker(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tracker

    Creates a tracker resource in your Amazon Web Services account, which lets you retrieve current and historical location of devices.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTrackerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_geofence_collection(request: web.Request, collection_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_geofence_collection

    &lt;p&gt;Deletes a geofence collection from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently. If the geofence collection is the target of a tracker resource, the devices will no longer be monitored.&lt;/p&gt; &lt;/note&gt;

    :param collection_name: The name of the geofence collection to be deleted.
    :type collection_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_key(request: web.Request, key_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_key

    Deletes the specified API key. The API key must have been deactivated more than 90 days previously.

    :param key_name: The name of the API key to delete.
    :type key_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_map(request: web.Request, map_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_map

    &lt;p&gt;Deletes a map resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently. If the map is being used in an application, the map may not render.&lt;/p&gt; &lt;/note&gt;

    :param map_name: The name of the map resource to be deleted.
    :type map_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_place_index(request: web.Request, index_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_place_index

    &lt;p&gt;Deletes a place index resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently.&lt;/p&gt; &lt;/note&gt;

    :param index_name: The name of the place index resource to be deleted.
    :type index_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_route_calculator(request: web.Request, calculator_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_route_calculator

    &lt;p&gt;Deletes a route calculator resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently.&lt;/p&gt; &lt;/note&gt;

    :param calculator_name: The name of the route calculator resource to be deleted.
    :type calculator_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_tracker(request: web.Request, tracker_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tracker

    &lt;p&gt;Deletes a tracker resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently. If the tracker resource is in use, you may encounter an error. Make sure that the target resource isn&#39;t a dependency for your applications.&lt;/p&gt; &lt;/note&gt;

    :param tracker_name: The name of the tracker resource to be deleted.
    :type tracker_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_geofence_collection(request: web.Request, collection_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_geofence_collection

    Retrieves the geofence collection details.

    :param collection_name: The name of the geofence collection.
    :type collection_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_key(request: web.Request, key_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_key

    Retrieves the API key resource details.

    :param key_name: The name of the API key resource.
    :type key_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_map(request: web.Request, map_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_map

    Retrieves the map resource details.

    :param map_name: The name of the map resource.
    :type map_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_place_index(request: web.Request, index_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_place_index

    Retrieves the place index resource details.

    :param index_name: The name of the place index resource.
    :type index_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_route_calculator(request: web.Request, calculator_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_route_calculator

    Retrieves the route calculator resource details.

    :param calculator_name: The name of the route calculator resource.
    :type calculator_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_tracker(request: web.Request, tracker_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tracker

    Retrieves the tracker resource details.

    :param tracker_name: The name of the tracker resource.
    :type tracker_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def disassociate_tracker_consumer(request: web.Request, consumer_arn, tracker_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_tracker_consumer

    &lt;p&gt;Removes the association between a tracker resource and a geofence collection.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Once you unlink a tracker resource from a geofence collection, the tracker positions will no longer be automatically evaluated against geofences.&lt;/p&gt; &lt;/note&gt;

    :param consumer_arn: &lt;p&gt;The Amazon Resource Name (ARN) for the geofence collection to be disassociated from the tracker resource. Used when you need to specify a resource across all Amazon Web Services. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type consumer_arn: str
    :param tracker_name: The name of the tracker resource to be dissociated from the consumer.
    :type tracker_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_device_position(request: web.Request, device_id, tracker_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_device_position

    &lt;p&gt;Retrieves a device&#39;s most recent position according to its sample time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Device positions are deleted after 30 days.&lt;/p&gt; &lt;/note&gt;

    :param device_id: The device whose position you want to retrieve.
    :type device_id: str
    :param tracker_name: The tracker resource receiving the position update.
    :type tracker_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_device_position_history(request: web.Request, device_id, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_device_position_history

    &lt;p&gt;Retrieves the device position history from a tracker resource within a specified range of time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Device positions are deleted after 30 days.&lt;/p&gt; &lt;/note&gt;

    :param device_id: The device whose position history you want to retrieve.
    :type device_id: str
    :param tracker_name: The tracker resource receiving the request for the device position history.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetDevicePositionHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_geofence(request: web.Request, collection_name, geofence_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_geofence

    Retrieves the geofence details from a geofence collection.

    :param collection_name: The geofence collection storing the target geofence.
    :type collection_name: str
    :param geofence_id: The geofence you&#39;re retrieving details for.
    :type geofence_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_map_glyphs(request: web.Request, font_stack, font_unicode_range, map_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """get_map_glyphs

    Retrieves glyphs used to display labels on a map.

    :param font_stack: &lt;p&gt;A comma-separated list of fonts to load glyphs from in order of preference. For example, &lt;code&gt;Noto Sans Regular, Arial Unicode&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Valid fonts stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/esri.html\&quot;&gt;Esri&lt;/a&gt; styles: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorEsriDarkGrayCanvas – &lt;code&gt;Ubuntu Medium Italic&lt;/code&gt; | &lt;code&gt;Ubuntu Medium&lt;/code&gt; | &lt;code&gt;Ubuntu Italic&lt;/code&gt; | &lt;code&gt;Ubuntu Regular&lt;/code&gt; | &lt;code&gt;Ubuntu Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriLightGrayCanvas – &lt;code&gt;Ubuntu Italic&lt;/code&gt; | &lt;code&gt;Ubuntu Regular&lt;/code&gt; | &lt;code&gt;Ubuntu Light&lt;/code&gt; | &lt;code&gt;Ubuntu Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriTopographic – &lt;code&gt;Noto Sans Italic&lt;/code&gt; | &lt;code&gt;Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Noto Sans Bold&lt;/code&gt; | &lt;code&gt;Noto Serif Regular&lt;/code&gt; | &lt;code&gt;Roboto Condensed Light Italic&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriStreets – &lt;code&gt;Arial Regular&lt;/code&gt; | &lt;code&gt;Arial Italic&lt;/code&gt; | &lt;code&gt;Arial Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriNavigation – &lt;code&gt;Arial Regular&lt;/code&gt; | &lt;code&gt;Arial Italic&lt;/code&gt; | &lt;code&gt;Arial Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid font stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/HERE.html\&quot;&gt;HERE Technologies&lt;/a&gt; styles:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorHereContrast – &lt;code&gt;Fira GO Regular&lt;/code&gt; | &lt;code&gt;Fira GO Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorHereExplore, VectorHereExploreTruck, HybridHereExploreSatellite – &lt;code&gt;Fira GO Italic&lt;/code&gt; | &lt;code&gt;Fira GO Map&lt;/code&gt; | &lt;code&gt;Fira GO Map Bold&lt;/code&gt; | &lt;code&gt;Noto Sans CJK JP Bold&lt;/code&gt; | &lt;code&gt;Noto Sans CJK JP Light&lt;/code&gt; | &lt;code&gt;Noto Sans CJK JP Regular&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid font stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html\&quot;&gt;GrabMaps&lt;/a&gt; styles:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorGrabStandardLight, VectorGrabStandardDark – &lt;code&gt;Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Noto Sans Medium&lt;/code&gt; | &lt;code&gt;Noto Sans Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid font stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/open-data.html\&quot;&gt;Open Data&lt;/a&gt; styles:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorOpenDataStandardLight, VectorOpenDataStandardDark, VectorOpenDataVisualizationLight, VectorOpenDataVisualizationDark – &lt;code&gt;Amazon Ember Regular,Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Bold,Noto Sans Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Medium,Noto Sans Medium&lt;/code&gt; | &lt;code&gt;Amazon Ember Regular Italic,Noto Sans Italic&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Regular,Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Bold,Noto Sans Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The fonts used by the Open Data map styles are combined fonts that use &lt;code&gt;Amazon Ember&lt;/code&gt; for most glyphs but &lt;code&gt;Noto Sans&lt;/code&gt; for glyphs unsupported by &lt;code&gt;Amazon Ember&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type font_stack: str
    :param font_unicode_range: A Unicode range of characters to download glyphs for. Each response will contain 256 characters. For example, 0–255 includes all characters from range &lt;code&gt;U+0000&lt;/code&gt; to &lt;code&gt;00FF&lt;/code&gt;. Must be aligned to multiples of 256.
    :type font_unicode_range: str
    :param map_name: The map resource associated with the glyph ﬁle.
    :type map_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    return web.Response(status=200)


async def get_map_sprites(request: web.Request, file_name, map_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """get_map_sprites

    Retrieves the sprite sheet corresponding to a map resource. The sprite sheet is a PNG image paired with a JSON document describing the offsets of individual icons that will be displayed on a rendered map.

    :param file_name: &lt;p&gt;The name of the sprite ﬁle. Use the following ﬁle names for the sprite sheet:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites.png&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites@2x.png&lt;/code&gt; for high pixel density displays&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For the JSON document containing image offsets. Use the following ﬁle names:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites.json&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites@2x.json&lt;/code&gt; for high pixel density displays&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type file_name: str
    :param map_name: The map resource associated with the sprite ﬁle.
    :type map_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    return web.Response(status=200)


async def get_map_style_descriptor(request: web.Request, map_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """get_map_style_descriptor

    &lt;p&gt;Retrieves the map style descriptor from a map resource. &lt;/p&gt; &lt;p&gt;The style descriptor contains speciﬁcations on how features render on a map. For example, what data to display, what order to display the data in, and the style for the data. Style descriptors follow the Mapbox Style Specification.&lt;/p&gt;

    :param map_name: The map resource to retrieve the style descriptor from.
    :type map_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    return web.Response(status=200)


async def get_map_tile(request: web.Request, map_name, x, y, z, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """get_map_tile

    &lt;p&gt;Retrieves a vector data tile from the map resource. Map tiles are used by clients to render a map. they&#39;re addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level. &lt;/p&gt; &lt;p&gt;The origin (0, 0) is the top left of the map. Increasing the zoom level by 1 doubles both the X and Y dimensions, so a tile containing data for the entire world at (0/0/0) will be split into 4 tiles at zoom 1 (1/0/0, 1/0/1, 1/1/0, 1/1/1).&lt;/p&gt;

    :param map_name: The map resource to retrieve the map tiles from.
    :type map_name: str
    :param x: The X axis value for the map tile.
    :type x: str
    :param y: The Y axis value for the map tile. 
    :type y: str
    :param z: The zoom value for the map tile.
    :type z: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    return web.Response(status=200)


async def get_place(request: web.Request, index_name, place_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None, language=None) -> web.Response:
    """get_place

    &lt;p&gt;Finds a place by its unique ID. A &lt;code&gt;PlaceId&lt;/code&gt; is returned by other search operations.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A PlaceId is valid only if all of the following are the same in the original search request and the call to &lt;code&gt;GetPlace&lt;/code&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Customer Amazon Web Services account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services Region&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data provider specified in the place index resource&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param index_name: The name of the place index resource that you want to use for the search.
    :type index_name: str
    :param place_id: The identifier of the place to find.
    :type place_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str
    :param language: &lt;p&gt;The preferred language used to return results. The value must be a valid &lt;a href&#x3D;\&quot;https://tools.ietf.org/search/bcp47\&quot;&gt;BCP 47&lt;/a&gt; language tag, for example, &lt;code&gt;en&lt;/code&gt; for English.&lt;/p&gt; &lt;p&gt;This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.&lt;/p&gt; &lt;p&gt;For an example, we&#39;ll use the Greek language. You search for a location around Athens, Greece, with the &lt;code&gt;language&lt;/code&gt; parameter set to &lt;code&gt;en&lt;/code&gt;. The &lt;code&gt;city&lt;/code&gt; in the results will most likely be returned as &lt;code&gt;Athens&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you set the &lt;code&gt;language&lt;/code&gt; parameter to &lt;code&gt;el&lt;/code&gt;, for Greek, then the &lt;code&gt;city&lt;/code&gt; in the results will more likely be returned as &lt;code&gt;Αθήνα&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the data provider does not have a value for Greek, the result will be in a language that the provider does support.&lt;/p&gt;
    :type language: str

    """
    return web.Response(status=200)


async def list_device_positions(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_device_positions

    A batch request to retrieve all device positions.

    :param tracker_name: The tracker resource containing the requested devices.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDevicePositionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_geofence_collections(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_geofence_collections

    Lists geofence collections in your Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListGeofenceCollectionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_geofences(request: web.Request, collection_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_geofences

    Lists geofences stored in a given geofence collection.

    :param collection_name: The name of the geofence collection storing the list of geofences.
    :type collection_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListGeofencesRequest.from_dict(body)
    return web.Response(status=200)


async def list_keys(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_keys

    Lists API key resources in your Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListKeysRequest.from_dict(body)
    return web.Response(status=200)


async def list_maps(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_maps

    Lists map resources in your Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListMapsRequest.from_dict(body)
    return web.Response(status=200)


async def list_place_indexes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_place_indexes

    Lists place index resources in your Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPlaceIndexesRequest.from_dict(body)
    return web.Response(status=200)


async def list_route_calculators(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_route_calculators

    Lists route calculator resources in your Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRouteCalculatorsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of tags that are applied to the specified Amazon Location resource.

    :param resource_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:resourcetype/ExampleResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_tracker_consumers(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tracker_consumers

    Lists geofence collections currently associated to the given tracker resource.

    :param tracker_name: The tracker resource whose associated geofence collections you want to list.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListGeofenceCollectionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_trackers(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_trackers

    Lists tracker resources in your Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListGeofenceCollectionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_geofence(request: web.Request, collection_name, geofence_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_geofence

    Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request. 

    :param collection_name: The geofence collection to store the geofence in.
    :type collection_name: str
    :param geofence_id: An identifier for the geofence. For example, &lt;code&gt;ExampleGeofence-1&lt;/code&gt;.
    :type geofence_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutGeofenceRequest.from_dict(body)
    return web.Response(status=200)


async def search_place_index_for_position(request: web.Request, index_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """search_place_index_for_position

    Reverse geocodes a given coordinate and returns a legible address. Allows you to search for Places or points of interest near a given position.

    :param index_name: The name of the place index resource you want to use for the search.
    :type index_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    body = SearchPlaceIndexForPositionRequest.from_dict(body)
    return web.Response(status=200)


async def search_place_index_for_suggestions(request: web.Request, index_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """search_place_index_for_suggestions

    &lt;p&gt;Generates suggestions for addresses and points of interest based on partial or misspelled free-form text. This operation is also known as autocomplete, autosuggest, or fuzzy matching.&lt;/p&gt; &lt;p&gt;Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can search for suggested place names near a specified position by using &lt;code&gt;BiasPosition&lt;/code&gt;, or filter results within a bounding box by using &lt;code&gt;FilterBBox&lt;/code&gt;. These parameters are mutually exclusive; using both &lt;code&gt;BiasPosition&lt;/code&gt; and &lt;code&gt;FilterBBox&lt;/code&gt; in the same command returns an error.&lt;/p&gt; &lt;/note&gt;

    :param index_name: The name of the place index resource you want to use for the search.
    :type index_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    body = SearchPlaceIndexForSuggestionsRequest.from_dict(body)
    return web.Response(status=200)


async def search_place_index_for_text(request: web.Request, index_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key=None) -> web.Response:
    """search_place_index_for_text

    &lt;p&gt;Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest. &lt;/p&gt; &lt;p&gt;Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can search for places near a given position using &lt;code&gt;BiasPosition&lt;/code&gt;, or filter results within a bounding box using &lt;code&gt;FilterBBox&lt;/code&gt;. Providing both parameters simultaneously returns an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Search results are returned in order of highest to lowest relevance.&lt;/p&gt;

    :param index_name: The name of the place index resource you want to use for the search.
    :type index_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param key: The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request.
    :type key: str

    """
    body = SearchPlaceIndexForTextRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; operation with an Amazon Location Service resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the tags already associated with the resource. If you specify a tag key that&#39;s already associated with the resource, the new tag value that you specify replaces the previous value for that tag. &lt;/p&gt; &lt;p&gt;You can associate up to 50 tags with a resource.&lt;/p&gt;

    :param resource_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the resource whose tags you want to update.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:resourcetype/ExampleResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from the specified Amazon Location resource.

    :param resource_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the resource from which you want to remove tags.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:resourcetype/ExampleResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the specified resource.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_geofence_collection(request: web.Request, collection_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_geofence_collection

    Updates the specified properties of a given geofence collection.

    :param collection_name: The name of the geofence collection to update.
    :type collection_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateGeofenceCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_key(request: web.Request, key_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_key

    Updates the specified properties of a given API key resource.

    :param key_name: The name of the API key resource to update.
    :type key_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_map(request: web.Request, map_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_map

    Updates the specified properties of a given map resource.

    :param map_name: The name of the map resource to update.
    :type map_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateMapRequest.from_dict(body)
    return web.Response(status=200)


async def update_place_index(request: web.Request, index_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_place_index

    Updates the specified properties of a given place index resource.

    :param index_name: The name of the place index resource to update.
    :type index_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePlaceIndexRequest.from_dict(body)
    return web.Response(status=200)


async def update_route_calculator(request: web.Request, calculator_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_route_calculator

    Updates the specified properties for a given route calculator resource.

    :param calculator_name: The name of the route calculator resource to update.
    :type calculator_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRouteCalculatorRequest.from_dict(body)
    return web.Response(status=200)


async def update_tracker(request: web.Request, tracker_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_tracker

    Updates the specified properties of a given tracker resource.

    :param tracker_name: The name of the tracker resource to update.
    :type tracker_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTrackerRequest.from_dict(body)
    return web.Response(status=200)
