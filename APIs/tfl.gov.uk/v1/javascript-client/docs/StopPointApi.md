# TransportForLondonUnifiedApi.StopPointApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stopPointArrivalDepartures**](StopPointApi.md#stopPointArrivalDepartures) | **GET** /StopPoint/{id}/ArrivalDepartures | Gets the list of arrival and departure predictions for the given stop point id (overground, Elizabeth line and thameslink only)
[**stopPointArrivals**](StopPointApi.md#stopPointArrivals) | **GET** /StopPoint/{id}/Arrivals | Gets the list of arrival predictions for the given stop point id
[**stopPointCrowding**](StopPointApi.md#stopPointCrowding) | **GET** /StopPoint/{id}/Crowding/{line} | Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction.
[**stopPointDirection**](StopPointApi.md#stopPointDirection) | **GET** /StopPoint/{id}/DirectionTo/{toStopPointId} | Returns the canonical direction, \&quot;inbound\&quot; or \&quot;outbound\&quot;, for a given pair of stop point Ids in the direction from -&amp;gt; to.
[**stopPointDisruption**](StopPointApi.md#stopPointDisruption) | **GET** /StopPoint/{ids}/Disruption | Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.
[**stopPointDisruptionByMode**](StopPointApi.md#stopPointDisruptionByMode) | **GET** /StopPoint/Mode/{modes}/Disruption | Gets a distinct list of disrupted stop points for the given modes
[**stopPointGet**](StopPointApi.md#stopPointGet) | **GET** /StopPoint/{ids} | Gets a list of StopPoints corresponding to the given list of stop ids.
[**stopPointGetByGeoPoint**](StopPointApi.md#stopPointGetByGeoPoint) | **GET** /StopPoint | Gets a list of StopPoints within {radius} by the specified criteria
[**stopPointGetByMode**](StopPointApi.md#stopPointGetByMode) | **GET** /StopPoint/Mode/{modes} | Gets a list of StopPoints filtered by the modes available at that StopPoint.
[**stopPointGetBySms**](StopPointApi.md#stopPointGetBySms) | **GET** /StopPoint/Sms/{id} | Gets a StopPoint for a given sms code.
[**stopPointGetByType**](StopPointApi.md#stopPointGetByType) | **GET** /StopPoint/Type/{types} | Gets all stop points of a given type
[**stopPointGetByTypeWithPagination**](StopPointApi.md#stopPointGetByTypeWithPagination) | **GET** /StopPoint/Type/{types}/page/{page} | Gets all the stop points of given type(s) with a page number
[**stopPointGetCarParksById**](StopPointApi.md#stopPointGetCarParksById) | **GET** /StopPoint/{stopPointId}/CarParks | Get car parks corresponding to the given stop point id.
[**stopPointGetServiceTypes**](StopPointApi.md#stopPointGetServiceTypes) | **GET** /StopPoint/ServiceTypes | Gets the service types for a given stoppoint
[**stopPointGetTaxiRanksByIds**](StopPointApi.md#stopPointGetTaxiRanksByIds) | **GET** /StopPoint/{stopPointId}/TaxiRanks | Gets a list of taxi ranks corresponding to the given stop point id.
[**stopPointIdPlaceTypesGet**](StopPointApi.md#stopPointIdPlaceTypesGet) | **GET** /StopPoint/{id}/placeTypes | Get a list of places corresponding to a given id and place types.
[**stopPointMetaCategories**](StopPointApi.md#stopPointMetaCategories) | **GET** /StopPoint/Meta/Categories | Gets the list of available StopPoint additional information categories
[**stopPointMetaModes**](StopPointApi.md#stopPointMetaModes) | **GET** /StopPoint/Meta/Modes | Gets the list of available StopPoint modes
[**stopPointMetaStopTypes**](StopPointApi.md#stopPointMetaStopTypes) | **GET** /StopPoint/Meta/StopTypes | Gets the list of available StopPoint types
[**stopPointReachableFrom**](StopPointApi.md#stopPointReachableFrom) | **GET** /StopPoint/{id}/CanReachOnLine/{lineId} | Gets Stopoints that are reachable from a station/line combination.
[**stopPointRoute**](StopPointApi.md#stopPointRoute) | **GET** /StopPoint/{id}/Route | Returns the route sections for all the lines that service the given stop point ids
[**stopPointSearch**](StopPointApi.md#stopPointSearch) | **GET** /StopPoint/Search/{query} | Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.
[**stopPointSearchGet**](StopPointApi.md#stopPointSearchGet) | **GET** /StopPoint/Search | Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.



## stopPointArrivalDepartures

> [TflApiPresentationEntitiesArrivalDeparture] stopPointArrivalDepartures(id, lineIds)

Gets the list of arrival and departure predictions for the given stop point id (overground, Elizabeth line and thameslink only)

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let lineIds = ["null"]; // [String] | A comma-separated list of line ids e.g. elizabeth, london-overground, thameslink
apiInstance.stopPointArrivalDepartures(id, lineIds, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **lineIds** | [**[String]**](String.md)| A comma-separated list of line ids e.g. elizabeth, london-overground, thameslink | 

### Return type

[**[TflApiPresentationEntitiesArrivalDeparture]**](TflApiPresentationEntitiesArrivalDeparture.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointArrivals

> [TflApiPresentationEntitiesPrediction] stopPointArrivals(id)

Gets the list of arrival predictions for the given stop point id

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
apiInstance.stopPointArrivals(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 

### Return type

[**[TflApiPresentationEntitiesPrediction]**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointCrowding

> [TflApiPresentationEntitiesStopPoint] stopPointCrowding(id, line, direction)

Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | The Naptan id of the stop
let line = "line_example"; // String | A particular line e.g. victoria, circle, northern etc.
let direction = "direction_example"; // String | The direction of travel. Can be inbound or outbound.
apiInstance.stopPointCrowding(id, line, direction, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The Naptan id of the stop | 
 **line** | **String**| A particular line e.g. victoria, circle, northern etc. | 
 **direction** | **String**| The direction of travel. Can be inbound or outbound. | 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointDirection

> String stopPointDirection(id, toStopPointId, opts)

Returns the canonical direction, \&quot;inbound\&quot; or \&quot;outbound\&quot;, for a given pair of stop point Ids in the direction from -&amp;gt; to.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | Originating stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let toStopPointId = "toStopPointId_example"; // String | Destination stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let opts = {
  'lineId': "lineId_example" // String | Optional line id filter e.g. victoria
};
apiInstance.stopPointDirection(id, toStopPointId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Originating stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **toStopPointId** | **String**| Destination stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **lineId** | **String**| Optional line id filter e.g. victoria | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointDisruption

> [TflApiPresentationEntitiesDisruptedPoint] stopPointDisruption(ids, opts)

Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let ids = ["null"]; // [String] | A comma-seperated list of stop point ids. Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
let opts = {
  'getFamily': true, // Boolean | Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false.
  'includeRouteBlockedStops': true, // Boolean | 
  'flattenResponse': true // Boolean | Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true).
};
apiInstance.stopPointDisruption(ids, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[String]**](String.md)| A comma-seperated list of stop point ids. Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name. | 
 **getFamily** | **Boolean**| Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false. | [optional] 
 **includeRouteBlockedStops** | **Boolean**|  | [optional] 
 **flattenResponse** | **Boolean**| Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true). | [optional] 

### Return type

[**[TflApiPresentationEntitiesDisruptedPoint]**](TflApiPresentationEntitiesDisruptedPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointDisruptionByMode

> [TflApiPresentationEntitiesDisruptedPoint] stopPointDisruptionByMode(modes, opts)

Gets a distinct list of disrupted stop points for the given modes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let modes = ["null"]; // [String] | A comma-seperated list of modes e.g. tube,dlr
let opts = {
  'includeRouteBlockedStops': true // Boolean | 
};
apiInstance.stopPointDisruptionByMode(modes, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modes** | [**[String]**](String.md)| A comma-seperated list of modes e.g. tube,dlr | 
 **includeRouteBlockedStops** | **Boolean**|  | [optional] 

### Return type

[**[TflApiPresentationEntitiesDisruptedPoint]**](TflApiPresentationEntitiesDisruptedPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGet

> [TflApiPresentationEntitiesStopPoint] stopPointGet(ids, opts)

Gets a list of StopPoints corresponding to the given list of stop ids.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let ids = ["null"]; // [String] | A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
let opts = {
  'includeCrowdingData': true // Boolean | Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line}
};
apiInstance.stopPointGet(ids, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[String]**](String.md)| A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name. | 
 **includeCrowdingData** | **Boolean**| Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line} | [optional] 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetByGeoPoint

> TflApiPresentationEntitiesStopPointsResponse stopPointGetByGeoPoint(stopTypes, locationLat, locationLon, opts)

Gets a list of StopPoints within {radius} by the specified criteria

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let stopTypes = ["null"]; // [String] | a list of stopTypes that should be returned (a list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint)
let locationLat = 3.4; // Number | 
let locationLon = 3.4; // Number | 
let opts = {
  'radius': 56, // Number | the radius of the bounding circle in metres (default : 200)
  'useStopPointHierarchy': true, // Boolean | Re-arrange the output into a parent/child hierarchy
  'modes': ["null"], // [String] | the list of modes to search (comma separated mode names e.g. tube,dlr)
  'categories': ["null"], // [String] | an optional list of comma separated property categories to return in the StopPoint's property bag. If null or empty, all categories of property are returned. Pass the keyword \"none\" to return no properties (a valid list of categories can be obtained from the /StopPoint/Meta/categories endpoint)
  'returnLines': true // Boolean | true to return the lines that each stop point serves as a nested resource
};
apiInstance.stopPointGetByGeoPoint(stopTypes, locationLat, locationLon, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopTypes** | [**[String]**](String.md)| a list of stopTypes that should be returned (a list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint) | 
 **locationLat** | **Number**|  | 
 **locationLon** | **Number**|  | 
 **radius** | **Number**| the radius of the bounding circle in metres (default : 200) | [optional] 
 **useStopPointHierarchy** | **Boolean**| Re-arrange the output into a parent/child hierarchy | [optional] 
 **modes** | [**[String]**](String.md)| the list of modes to search (comma separated mode names e.g. tube,dlr) | [optional] 
 **categories** | [**[String]**](String.md)| an optional list of comma separated property categories to return in the StopPoint&#39;s property bag. If null or empty, all categories of property are returned. Pass the keyword \&quot;none\&quot; to return no properties (a valid list of categories can be obtained from the /StopPoint/Meta/categories endpoint) | [optional] 
 **returnLines** | **Boolean**| true to return the lines that each stop point serves as a nested resource | [optional] 

### Return type

[**TflApiPresentationEntitiesStopPointsResponse**](TflApiPresentationEntitiesStopPointsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetByMode

> TflApiPresentationEntitiesStopPointsResponse stopPointGetByMode(modes, opts)

Gets a list of StopPoints filtered by the modes available at that StopPoint.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let modes = ["null"]; // [String] | A comma-seperated list of modes e.g. tube,dlr
let opts = {
  'page': 56 // Number | The data set page to return. Page 1 equates to the first 1000 stop points, page 2 equates to 1001-2000 etc. Must be entered for bus mode as data set is too large.
};
apiInstance.stopPointGetByMode(modes, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modes** | [**[String]**](String.md)| A comma-seperated list of modes e.g. tube,dlr | 
 **page** | **Number**| The data set page to return. Page 1 equates to the first 1000 stop points, page 2 equates to 1001-2000 etc. Must be entered for bus mode as data set is too large. | [optional] 

### Return type

[**TflApiPresentationEntitiesStopPointsResponse**](TflApiPresentationEntitiesStopPointsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetBySms

> Object stopPointGetBySms(id, opts)

Gets a StopPoint for a given sms code.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | A 5-digit Countdown Bus Stop Code e.g. 73241, 50435, 56334.
let opts = {
  'output': "output_example" // String | If set to \"web\", a 302 redirect to relevant website bus stop page is returned. Valid values are : web. All other values are ignored.
};
apiInstance.stopPointGetBySms(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A 5-digit Countdown Bus Stop Code e.g. 73241, 50435, 56334. | 
 **output** | **String**| If set to \&quot;web\&quot;, a 302 redirect to relevant website bus stop page is returned. Valid values are : web. All other values are ignored. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetByType

> [TflApiPresentationEntitiesStopPoint] stopPointGetByType(types)

Gets all stop points of a given type

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let types = ["null"]; // [String] | A comma-separated list of the types to return. Max. approx. 12 types.               A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint.
apiInstance.stopPointGetByType(types, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**[String]**](String.md)| A comma-separated list of the types to return. Max. approx. 12 types.               A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint. | 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetByTypeWithPagination

> [TflApiPresentationEntitiesStopPoint] stopPointGetByTypeWithPagination(types, page)

Gets all the stop points of given type(s) with a page number

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let types = ["null"]; // [String] | 
let page = 56; // Number | 
apiInstance.stopPointGetByTypeWithPagination(types, page, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**[String]**](String.md)|  | 
 **page** | **Number**|  | 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetCarParksById

> [TflApiPresentationEntitiesPlace] stopPointGetCarParksById(stopPointId)

Get car parks corresponding to the given stop point id.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let stopPointId = "stopPointId_example"; // String | stopPointId is required to get the car parks.
apiInstance.stopPointGetCarParksById(stopPointId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopPointId** | **String**| stopPointId is required to get the car parks. | 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetServiceTypes

> [TflApiPresentationEntitiesLineServiceType] stopPointGetServiceTypes(id, opts)

Gets the service types for a given stoppoint

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | The Naptan id of the stop
let opts = {
  'lineIds': ["null"], // [String] | The lines which contain the given Naptan id (all lines relevant to the given stoppoint if empty)
  'modes': ["null"] // [String] | The modes which the lines are relevant to (all if empty)
};
apiInstance.stopPointGetServiceTypes(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The Naptan id of the stop | 
 **lineIds** | [**[String]**](String.md)| The lines which contain the given Naptan id (all lines relevant to the given stoppoint if empty) | [optional] 
 **modes** | [**[String]**](String.md)| The modes which the lines are relevant to (all if empty) | [optional] 

### Return type

[**[TflApiPresentationEntitiesLineServiceType]**](TflApiPresentationEntitiesLineServiceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointGetTaxiRanksByIds

> [TflApiPresentationEntitiesPlace] stopPointGetTaxiRanksByIds(stopPointId)

Gets a list of taxi ranks corresponding to the given stop point id.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let stopPointId = "stopPointId_example"; // String | stopPointId is required to get the taxi ranks.
apiInstance.stopPointGetTaxiRanksByIds(stopPointId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopPointId** | **String**| stopPointId is required to get the taxi ranks. | 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointIdPlaceTypesGet

> [TflApiPresentationEntitiesPlace] stopPointIdPlaceTypesGet(id, placeTypes)

Get a list of places corresponding to a given id and place types.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | A naptan id for a stop point (station naptan code e.g. 940GZZLUASL).
let placeTypes = ["null"]; // [String] | A comcomma-separated value representing the place types.
apiInstance.stopPointIdPlaceTypesGet(id, placeTypes, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A naptan id for a stop point (station naptan code e.g. 940GZZLUASL). | 
 **placeTypes** | [**[String]**](String.md)| A comcomma-separated value representing the place types. | 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointMetaCategories

> [TflApiPresentationEntitiesStopPointCategory] stopPointMetaCategories()

Gets the list of available StopPoint additional information categories

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
apiInstance.stopPointMetaCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesStopPointCategory]**](TflApiPresentationEntitiesStopPointCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointMetaModes

> [TflApiPresentationEntitiesMode] stopPointMetaModes()

Gets the list of available StopPoint modes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
apiInstance.stopPointMetaModes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesMode]**](TflApiPresentationEntitiesMode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointMetaStopTypes

> [String] stopPointMetaStopTypes()

Gets the list of available StopPoint types

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
apiInstance.stopPointMetaStopTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointReachableFrom

> [TflApiPresentationEntitiesStopPoint] stopPointReachableFrom(id, lineId, opts)

Gets Stopoints that are reachable from a station/line combination.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | The id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) of the stop point to filter by
let lineId = "lineId_example"; // String | Line id of the line to filter by (e.g. victoria)
let opts = {
  'serviceTypes': ["null"] // [String] | A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
};
apiInstance.stopPointReachableFrom(id, lineId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) of the stop point to filter by | 
 **lineId** | **String**| Line id of the line to filter by (e.g. victoria) | 
 **serviceTypes** | [**[String]**](String.md)| A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointRoute

> [TflApiPresentationEntitiesStopPointRouteSection] stopPointRoute(id, opts)

Returns the route sections for all the lines that service the given stop point ids

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let id = "id_example"; // String | A stop point id (station naptan codes e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let opts = {
  'serviceTypes': ["null"] // [String] | A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
};
apiInstance.stopPointRoute(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A stop point id (station naptan codes e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **serviceTypes** | [**[String]**](String.md)| A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 

### Return type

[**[TflApiPresentationEntitiesStopPointRouteSection]**](TflApiPresentationEntitiesStopPointRouteSection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointSearch

> TflApiPresentationEntitiesSearchResponse stopPointSearch(query, opts)

Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let query = "query_example"; // String | The query string, case-insensitive. Leading and trailing wildcards are applied automatically.
let opts = {
  'modes': ["null"], // [String] | An optional, parameter separated list of the modes to filter by
  'faresOnly': true, // Boolean | True to only return stations in that have Fares data available for single fares to another station.
  'maxResults': 56, // Number | An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items.
  'lines': ["null"], // [String] | An optional, parameter separated list of the lines to filter by
  'includeHubs': true, // Boolean | If true, returns results including HUBs.
  'tflOperatedNationalRailStationsOnly': true // Boolean | If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
};
apiInstance.stopPointSearch(query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| The query string, case-insensitive. Leading and trailing wildcards are applied automatically. | 
 **modes** | [**[String]**](String.md)| An optional, parameter separated list of the modes to filter by | [optional] 
 **faresOnly** | **Boolean**| True to only return stations in that have Fares data available for single fares to another station. | [optional] 
 **maxResults** | **Number**| An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items. | [optional] 
 **lines** | [**[String]**](String.md)| An optional, parameter separated list of the lines to filter by | [optional] 
 **includeHubs** | **Boolean**| If true, returns results including HUBs. | [optional] 
 **tflOperatedNationalRailStationsOnly** | **Boolean**| If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned | [optional] 

### Return type

[**TflApiPresentationEntitiesSearchResponse**](TflApiPresentationEntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stopPointSearchGet

> TflApiPresentationEntitiesSearchResponse stopPointSearchGet(query, opts)

Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.StopPointApi();
let query = "query_example"; // String | The query string, case-insensitive. Leading and trailing wildcards are applied automatically.
let opts = {
  'modes': ["null"], // [String] | An optional, parameter separated list of the modes to filter by
  'faresOnly': true, // Boolean | True to only return stations in that have Fares data available for single fares to another station.
  'maxResults': 56, // Number | An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items.
  'lines': ["null"], // [String] | An optional, parameter separated list of the lines to filter by
  'includeHubs': true, // Boolean | If true, returns results including HUBs.
  'tflOperatedNationalRailStationsOnly': true // Boolean | If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
};
apiInstance.stopPointSearchGet(query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| The query string, case-insensitive. Leading and trailing wildcards are applied automatically. | 
 **modes** | [**[String]**](String.md)| An optional, parameter separated list of the modes to filter by | [optional] 
 **faresOnly** | **Boolean**| True to only return stations in that have Fares data available for single fares to another station. | [optional] 
 **maxResults** | **Number**| An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items. | [optional] 
 **lines** | [**[String]**](String.md)| An optional, parameter separated list of the lines to filter by | [optional] 
 **includeHubs** | **Boolean**| If true, returns results including HUBs. | [optional] 
 **tflOperatedNationalRailStationsOnly** | **Boolean**| If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned | [optional] 

### Return type

[**TflApiPresentationEntitiesSearchResponse**](TflApiPresentationEntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

