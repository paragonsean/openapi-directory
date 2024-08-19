# AmazonLocationService.DefaultApi

All URIs are relative to *http://geo.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateTrackerConsumer**](DefaultApi.md#associateTrackerConsumer) | **POST** /tracking/v0/trackers/{TrackerName}/consumers | 
[**batchDeleteDevicePositionHistory**](DefaultApi.md#batchDeleteDevicePositionHistory) | **POST** /tracking/v0/trackers/{TrackerName}/delete-positions | 
[**batchDeleteGeofence**](DefaultApi.md#batchDeleteGeofence) | **POST** /geofencing/v0/collections/{CollectionName}/delete-geofences | 
[**batchEvaluateGeofences**](DefaultApi.md#batchEvaluateGeofences) | **POST** /geofencing/v0/collections/{CollectionName}/positions | 
[**batchGetDevicePosition**](DefaultApi.md#batchGetDevicePosition) | **POST** /tracking/v0/trackers/{TrackerName}/get-positions | 
[**batchPutGeofence**](DefaultApi.md#batchPutGeofence) | **POST** /geofencing/v0/collections/{CollectionName}/put-geofences | 
[**batchUpdateDevicePosition**](DefaultApi.md#batchUpdateDevicePosition) | **POST** /tracking/v0/trackers/{TrackerName}/positions | 
[**calculateRoute**](DefaultApi.md#calculateRoute) | **POST** /routes/v0/calculators/{CalculatorName}/calculate/route | 
[**calculateRouteMatrix**](DefaultApi.md#calculateRouteMatrix) | **POST** /routes/v0/calculators/{CalculatorName}/calculate/route-matrix | 
[**createGeofenceCollection**](DefaultApi.md#createGeofenceCollection) | **POST** /geofencing/v0/collections | 
[**createKey**](DefaultApi.md#createKey) | **POST** /metadata/v0/keys | 
[**createMap**](DefaultApi.md#createMap) | **POST** /maps/v0/maps | 
[**createPlaceIndex**](DefaultApi.md#createPlaceIndex) | **POST** /places/v0/indexes | 
[**createRouteCalculator**](DefaultApi.md#createRouteCalculator) | **POST** /routes/v0/calculators | 
[**createTracker**](DefaultApi.md#createTracker) | **POST** /tracking/v0/trackers | 
[**deleteGeofenceCollection**](DefaultApi.md#deleteGeofenceCollection) | **DELETE** /geofencing/v0/collections/{CollectionName} | 
[**deleteKey**](DefaultApi.md#deleteKey) | **DELETE** /metadata/v0/keys/{KeyName} | 
[**deleteMap**](DefaultApi.md#deleteMap) | **DELETE** /maps/v0/maps/{MapName} | 
[**deletePlaceIndex**](DefaultApi.md#deletePlaceIndex) | **DELETE** /places/v0/indexes/{IndexName} | 
[**deleteRouteCalculator**](DefaultApi.md#deleteRouteCalculator) | **DELETE** /routes/v0/calculators/{CalculatorName} | 
[**deleteTracker**](DefaultApi.md#deleteTracker) | **DELETE** /tracking/v0/trackers/{TrackerName} | 
[**describeGeofenceCollection**](DefaultApi.md#describeGeofenceCollection) | **GET** /geofencing/v0/collections/{CollectionName} | 
[**describeKey**](DefaultApi.md#describeKey) | **GET** /metadata/v0/keys/{KeyName} | 
[**describeMap**](DefaultApi.md#describeMap) | **GET** /maps/v0/maps/{MapName} | 
[**describePlaceIndex**](DefaultApi.md#describePlaceIndex) | **GET** /places/v0/indexes/{IndexName} | 
[**describeRouteCalculator**](DefaultApi.md#describeRouteCalculator) | **GET** /routes/v0/calculators/{CalculatorName} | 
[**describeTracker**](DefaultApi.md#describeTracker) | **GET** /tracking/v0/trackers/{TrackerName} | 
[**disassociateTrackerConsumer**](DefaultApi.md#disassociateTrackerConsumer) | **DELETE** /tracking/v0/trackers/{TrackerName}/consumers/{ConsumerArn} | 
[**getDevicePosition**](DefaultApi.md#getDevicePosition) | **GET** /tracking/v0/trackers/{TrackerName}/devices/{DeviceId}/positions/latest | 
[**getDevicePositionHistory**](DefaultApi.md#getDevicePositionHistory) | **POST** /tracking/v0/trackers/{TrackerName}/devices/{DeviceId}/list-positions | 
[**getGeofence**](DefaultApi.md#getGeofence) | **GET** /geofencing/v0/collections/{CollectionName}/geofences/{GeofenceId} | 
[**getMapGlyphs**](DefaultApi.md#getMapGlyphs) | **GET** /maps/v0/maps/{MapName}/glyphs/{FontStack}/{FontUnicodeRange} | 
[**getMapSprites**](DefaultApi.md#getMapSprites) | **GET** /maps/v0/maps/{MapName}/sprites/{FileName} | 
[**getMapStyleDescriptor**](DefaultApi.md#getMapStyleDescriptor) | **GET** /maps/v0/maps/{MapName}/style-descriptor | 
[**getMapTile**](DefaultApi.md#getMapTile) | **GET** /maps/v0/maps/{MapName}/tiles/{Z}/{X}/{Y} | 
[**getPlace**](DefaultApi.md#getPlace) | **GET** /places/v0/indexes/{IndexName}/places/{PlaceId} | 
[**listDevicePositions**](DefaultApi.md#listDevicePositions) | **POST** /tracking/v0/trackers/{TrackerName}/list-positions | 
[**listGeofenceCollections**](DefaultApi.md#listGeofenceCollections) | **POST** /geofencing/v0/list-collections | 
[**listGeofences**](DefaultApi.md#listGeofences) | **POST** /geofencing/v0/collections/{CollectionName}/list-geofences | 
[**listKeys**](DefaultApi.md#listKeys) | **POST** /metadata/v0/list-keys | 
[**listMaps**](DefaultApi.md#listMaps) | **POST** /maps/v0/list-maps | 
[**listPlaceIndexes**](DefaultApi.md#listPlaceIndexes) | **POST** /places/v0/list-indexes | 
[**listRouteCalculators**](DefaultApi.md#listRouteCalculators) | **POST** /routes/v0/list-calculators | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**listTrackerConsumers**](DefaultApi.md#listTrackerConsumers) | **POST** /tracking/v0/trackers/{TrackerName}/list-consumers | 
[**listTrackers**](DefaultApi.md#listTrackers) | **POST** /tracking/v0/list-trackers | 
[**putGeofence**](DefaultApi.md#putGeofence) | **PUT** /geofencing/v0/collections/{CollectionName}/geofences/{GeofenceId} | 
[**searchPlaceIndexForPosition**](DefaultApi.md#searchPlaceIndexForPosition) | **POST** /places/v0/indexes/{IndexName}/search/position | 
[**searchPlaceIndexForSuggestions**](DefaultApi.md#searchPlaceIndexForSuggestions) | **POST** /places/v0/indexes/{IndexName}/search/suggestions | 
[**searchPlaceIndexForText**](DefaultApi.md#searchPlaceIndexForText) | **POST** /places/v0/indexes/{IndexName}/search/text | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateGeofenceCollection**](DefaultApi.md#updateGeofenceCollection) | **PATCH** /geofencing/v0/collections/{CollectionName} | 
[**updateKey**](DefaultApi.md#updateKey) | **PATCH** /metadata/v0/keys/{KeyName} | 
[**updateMap**](DefaultApi.md#updateMap) | **PATCH** /maps/v0/maps/{MapName} | 
[**updatePlaceIndex**](DefaultApi.md#updatePlaceIndex) | **PATCH** /places/v0/indexes/{IndexName} | 
[**updateRouteCalculator**](DefaultApi.md#updateRouteCalculator) | **PATCH** /routes/v0/calculators/{CalculatorName} | 
[**updateTracker**](DefaultApi.md#updateTracker) | **PATCH** /tracking/v0/trackers/{TrackerName} | 



## associateTrackerConsumer

> Object associateTrackerConsumer(trackerName, associateTrackerConsumerRequest, opts)



&lt;p&gt;Creates an association between a geofence collection and a tracker resource. This allows the tracker resource to communicate location data to the linked geofence collection. &lt;/p&gt; &lt;p&gt;You can associate up to five geofence collections to each tracker resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Currently not supported — Cross-account configurations, such as creating associations between a tracker resource in one account and a geofence collection in another account.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The name of the tracker resource to be associated with a geofence collection.
let associateTrackerConsumerRequest = new AmazonLocationService.AssociateTrackerConsumerRequest(); // AssociateTrackerConsumerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateTrackerConsumer(trackerName, associateTrackerConsumerRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The name of the tracker resource to be associated with a geofence collection. | 
 **associateTrackerConsumerRequest** | [**AssociateTrackerConsumerRequest**](AssociateTrackerConsumerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteDevicePositionHistory

> BatchDeleteDevicePositionHistoryResponse batchDeleteDevicePositionHistory(trackerName, batchDeleteDevicePositionHistoryRequest, opts)



Deletes the position history of one or more devices from a tracker resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The name of the tracker resource to delete the device position history from.
let batchDeleteDevicePositionHistoryRequest = new AmazonLocationService.BatchDeleteDevicePositionHistoryRequest(); // BatchDeleteDevicePositionHistoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteDevicePositionHistory(trackerName, batchDeleteDevicePositionHistoryRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The name of the tracker resource to delete the device position history from. | 
 **batchDeleteDevicePositionHistoryRequest** | [**BatchDeleteDevicePositionHistoryRequest**](BatchDeleteDevicePositionHistoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteDevicePositionHistoryResponse**](BatchDeleteDevicePositionHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteGeofence

> BatchDeleteGeofenceResponse batchDeleteGeofence(collectionName, batchDeleteGeofenceRequest, opts)



&lt;p&gt;Deletes a batch of geofences from a geofence collection.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The geofence collection storing the geofences to be deleted.
let batchDeleteGeofenceRequest = new AmazonLocationService.BatchDeleteGeofenceRequest(); // BatchDeleteGeofenceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteGeofence(collectionName, batchDeleteGeofenceRequest, opts, (error, data, response) => {
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
 **collectionName** | **String**| The geofence collection storing the geofences to be deleted. | 
 **batchDeleteGeofenceRequest** | [**BatchDeleteGeofenceRequest**](BatchDeleteGeofenceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteGeofenceResponse**](BatchDeleteGeofenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchEvaluateGeofences

> BatchEvaluateGeofencesResponse batchEvaluateGeofences(collectionName, batchEvaluateGeofencesRequest, opts)



&lt;p&gt;Evaluates device positions against the geofence geometries from a given geofence collection.&lt;/p&gt; &lt;p&gt;This operation always returns an empty response because geofences are asynchronously evaluated. The evaluation determines if the device has entered or exited a geofenced area, and then publishes one of the following events to Amazon EventBridge:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ENTER&lt;/code&gt; if Amazon Location determines that the tracked device has entered a geofenced area.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EXIT&lt;/code&gt; if Amazon Location determines that the tracked device has exited a geofenced area.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The last geofence that a device was observed within is tracked for 30 days after the most recent device position update.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Geofence evaluation uses the given device position. It does not account for the optional &lt;code&gt;Accuracy&lt;/code&gt; of a &lt;code&gt;DevicePositionUpdate&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;DeviceID&lt;/code&gt; is used as a string to represent the device. You do not need to have a &lt;code&gt;Tracker&lt;/code&gt; associated with the &lt;code&gt;DeviceID&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The geofence collection used in evaluating the position of devices against its geofences.
let batchEvaluateGeofencesRequest = new AmazonLocationService.BatchEvaluateGeofencesRequest(); // BatchEvaluateGeofencesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchEvaluateGeofences(collectionName, batchEvaluateGeofencesRequest, opts, (error, data, response) => {
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
 **collectionName** | **String**| The geofence collection used in evaluating the position of devices against its geofences. | 
 **batchEvaluateGeofencesRequest** | [**BatchEvaluateGeofencesRequest**](BatchEvaluateGeofencesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchEvaluateGeofencesResponse**](BatchEvaluateGeofencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetDevicePosition

> BatchGetDevicePositionResponse batchGetDevicePosition(trackerName, batchGetDevicePositionRequest, opts)



Lists the latest device positions for requested devices.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The tracker resource retrieving the device position.
let batchGetDevicePositionRequest = new AmazonLocationService.BatchGetDevicePositionRequest(); // BatchGetDevicePositionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetDevicePosition(trackerName, batchGetDevicePositionRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The tracker resource retrieving the device position. | 
 **batchGetDevicePositionRequest** | [**BatchGetDevicePositionRequest**](BatchGetDevicePositionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetDevicePositionResponse**](BatchGetDevicePositionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchPutGeofence

> BatchPutGeofenceResponse batchPutGeofence(collectionName, batchPutGeofenceRequest, opts)



A batch request for storing geofence geometries into a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The geofence collection storing the geofences.
let batchPutGeofenceRequest = new AmazonLocationService.BatchPutGeofenceRequest(); // BatchPutGeofenceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchPutGeofence(collectionName, batchPutGeofenceRequest, opts, (error, data, response) => {
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
 **collectionName** | **String**| The geofence collection storing the geofences. | 
 **batchPutGeofenceRequest** | [**BatchPutGeofenceRequest**](BatchPutGeofenceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchPutGeofenceResponse**](BatchPutGeofenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdateDevicePosition

> BatchUpdateDevicePositionResponse batchUpdateDevicePosition(trackerName, batchUpdateDevicePositionRequest, opts)



&lt;p&gt;Uploads position update data for one or more devices to a tracker resource (up to 10 devices per batch). Amazon Location uses the data when it reports the last known device position and position history. Amazon Location retains location data for 30 days.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Position updates are handled based on the &lt;code&gt;PositionFiltering&lt;/code&gt; property of the tracker. When &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;TimeBased&lt;/code&gt;, updates are evaluated against linked geofence collections, and location data is stored at a maximum of one position per 30 second interval. If your update frequency is more often than every 30 seconds, only one update per 30 seconds is stored for each unique device ID.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;DistanceBased&lt;/code&gt; filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than 30 m (98.4 ft).&lt;/p&gt; &lt;p&gt;When &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;AccuracyBased&lt;/code&gt; filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than the measured accuracy. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is neither stored or evaluated if the device has moved less than 15 m. If &lt;code&gt;PositionFiltering&lt;/code&gt; is set to &lt;code&gt;AccuracyBased&lt;/code&gt; filtering, Amazon Location uses the default value &lt;code&gt;{ \&quot;Horizontal\&quot;: 0}&lt;/code&gt; when accuracy is not provided on a &lt;code&gt;DevicePositionUpdate&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The name of the tracker resource to update.
let batchUpdateDevicePositionRequest = new AmazonLocationService.BatchUpdateDevicePositionRequest(); // BatchUpdateDevicePositionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateDevicePosition(trackerName, batchUpdateDevicePositionRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The name of the tracker resource to update. | 
 **batchUpdateDevicePositionRequest** | [**BatchUpdateDevicePositionRequest**](BatchUpdateDevicePositionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateDevicePositionResponse**](BatchUpdateDevicePositionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## calculateRoute

> CalculateRouteResponse calculateRoute(calculatorName, calculateRouteRequest, opts)



&lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/calculate-route.html\&quot;&gt;Calculates a route&lt;/a&gt; given the following required parameters: &lt;code&gt;DeparturePosition&lt;/code&gt; and &lt;code&gt;DestinationPosition&lt;/code&gt;. Requires that you first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html\&quot;&gt;create a route calculator resource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;By default, a request that doesn&#39;t specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.&lt;/p&gt; &lt;p&gt;Additional options include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/departure-time.html\&quot;&gt;Specifying a departure time&lt;/a&gt; using either &lt;code&gt;DepartureTime&lt;/code&gt; or &lt;code&gt;DepartNow&lt;/code&gt;. This calculates a route based on predictive traffic data at the given time. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t specify both &lt;code&gt;DepartureTime&lt;/code&gt; and &lt;code&gt;DepartNow&lt;/code&gt; in a single request. Specifying both parameters returns a validation error.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/travel-mode.html\&quot;&gt;Specifying a travel mode&lt;/a&gt; using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in &lt;code&gt;CarModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Car&lt;/code&gt;, or &lt;code&gt;TruckModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Truck&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you specify &lt;code&gt;walking&lt;/code&gt; for the travel mode and your data provider is Esri, the start and destination must be within 40km.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let calculatorName = "calculatorName_example"; // String | The name of the route calculator resource that you want to use to calculate the route. 
let calculateRouteRequest = new AmazonLocationService.CalculateRouteRequest(); // CalculateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.calculateRoute(calculatorName, calculateRouteRequest, opts, (error, data, response) => {
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
 **calculatorName** | **String**| The name of the route calculator resource that you want to use to calculate the route.  | 
 **calculateRouteRequest** | [**CalculateRouteRequest**](CalculateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**CalculateRouteResponse**](CalculateRouteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## calculateRouteMatrix

> CalculateRouteMatrixResponse calculateRouteMatrix(calculatorName, calculateRouteMatrixRequest, opts)



&lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html\&quot;&gt; Calculates a route matrix&lt;/a&gt; given the following required parameters: &lt;code&gt;DeparturePositions&lt;/code&gt; and &lt;code&gt;DestinationPositions&lt;/code&gt;. &lt;code&gt;CalculateRouteMatrix&lt;/code&gt; calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, &lt;code&gt;CalculateRouteMatrix&lt;/code&gt; will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of &lt;code&gt;DeparturePositions&lt;/code&gt; times the number of &lt;code&gt;DestinationPositions&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Your account is charged for each route calculated, not the number of requests.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Requires that you first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html\&quot;&gt;create a route calculator resource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;By default, a request that doesn&#39;t specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.&lt;/p&gt; &lt;p&gt;Additional options include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/departure-time.html\&quot;&gt; Specifying a departure time&lt;/a&gt; using either &lt;code&gt;DepartureTime&lt;/code&gt; or &lt;code&gt;DepartNow&lt;/code&gt;. This calculates routes based on predictive traffic data at the given time. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t specify both &lt;code&gt;DepartureTime&lt;/code&gt; and &lt;code&gt;DepartNow&lt;/code&gt; in a single request. Specifying both parameters returns a validation error.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/travel-mode.html\&quot;&gt;Specifying a travel mode&lt;/a&gt; using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in &lt;code&gt;CarModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Car&lt;/code&gt;, or &lt;code&gt;TruckModeOptions&lt;/code&gt; if traveling by &lt;code&gt;Truck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let calculatorName = "calculatorName_example"; // String | The name of the route calculator resource that you want to use to calculate the route matrix. 
let calculateRouteMatrixRequest = new AmazonLocationService.CalculateRouteMatrixRequest(); // CalculateRouteMatrixRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.calculateRouteMatrix(calculatorName, calculateRouteMatrixRequest, opts, (error, data, response) => {
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
 **calculatorName** | **String**| The name of the route calculator resource that you want to use to calculate the route matrix.  | 
 **calculateRouteMatrixRequest** | [**CalculateRouteMatrixRequest**](CalculateRouteMatrixRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**CalculateRouteMatrixResponse**](CalculateRouteMatrixResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGeofenceCollection

> CreateGeofenceCollectionResponse createGeofenceCollection(createGeofenceCollectionRequest, opts)



Creates a geofence collection, which manages and stores geofences.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let createGeofenceCollectionRequest = new AmazonLocationService.CreateGeofenceCollectionRequest(); // CreateGeofenceCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createGeofenceCollection(createGeofenceCollectionRequest, opts, (error, data, response) => {
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
 **createGeofenceCollectionRequest** | [**CreateGeofenceCollectionRequest**](CreateGeofenceCollectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateGeofenceCollectionResponse**](CreateGeofenceCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createKey

> CreateKeyResponse createKey(createKeyRequest, opts)



&lt;p&gt;Creates an API key resource in your Amazon Web Services account, which lets you grant actions for Amazon Location resources to the API key bearer.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;Using API keys&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let createKeyRequest = new AmazonLocationService.CreateKeyRequest(); // CreateKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createKey(createKeyRequest, opts, (error, data, response) => {
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
 **createKeyRequest** | [**CreateKeyRequest**](CreateKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateKeyResponse**](CreateKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMap

> CreateMapResponse createMap(createMapRequest, opts)



&lt;p&gt;Creates a map resource in your Amazon Web Services account, which provides map tiles of different styles sourced from global location data providers.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms\&quot;&gt;Amazon Web Services service terms&lt;/a&gt; for more details.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let createMapRequest = new AmazonLocationService.CreateMapRequest(); // CreateMapRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMap(createMapRequest, opts, (error, data, response) => {
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
 **createMapRequest** | [**CreateMapRequest**](CreateMapRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMapResponse**](CreateMapResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPlaceIndex

> CreatePlaceIndexResponse createPlaceIndex(createPlaceIndexRequest, opts)



&lt;p&gt;Creates a place index resource in your Amazon Web Services account. Use a place index resource to geocode addresses and other text queries by using the &lt;code&gt;SearchPlaceIndexForText&lt;/code&gt; operation, and reverse geocode coordinates by using the &lt;code&gt;SearchPlaceIndexForPosition&lt;/code&gt; operation, and enable autosuggestions by using the &lt;code&gt;SearchPlaceIndexForSuggestions&lt;/code&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms\&quot;&gt;Amazon Web Services service terms&lt;/a&gt; for more details.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let createPlaceIndexRequest = new AmazonLocationService.CreatePlaceIndexRequest(); // CreatePlaceIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPlaceIndex(createPlaceIndexRequest, opts, (error, data, response) => {
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
 **createPlaceIndexRequest** | [**CreatePlaceIndexRequest**](CreatePlaceIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePlaceIndexResponse**](CreatePlaceIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRouteCalculator

> CreateRouteCalculatorResponse createRouteCalculator(createRouteCalculatorRequest, opts)



&lt;p&gt;Creates a route calculator resource in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms\&quot;&gt;Amazon Web Services service terms&lt;/a&gt; for more details.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let createRouteCalculatorRequest = new AmazonLocationService.CreateRouteCalculatorRequest(); // CreateRouteCalculatorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRouteCalculator(createRouteCalculatorRequest, opts, (error, data, response) => {
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
 **createRouteCalculatorRequest** | [**CreateRouteCalculatorRequest**](CreateRouteCalculatorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRouteCalculatorResponse**](CreateRouteCalculatorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTracker

> CreateTrackerResponse createTracker(createTrackerRequest, opts)



Creates a tracker resource in your Amazon Web Services account, which lets you retrieve current and historical location of devices.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let createTrackerRequest = new AmazonLocationService.CreateTrackerRequest(); // CreateTrackerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTracker(createTrackerRequest, opts, (error, data, response) => {
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
 **createTrackerRequest** | [**CreateTrackerRequest**](CreateTrackerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTrackerResponse**](CreateTrackerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGeofenceCollection

> Object deleteGeofenceCollection(collectionName, opts)



&lt;p&gt;Deletes a geofence collection from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently. If the geofence collection is the target of a tracker resource, the devices will no longer be monitored.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The name of the geofence collection to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGeofenceCollection(collectionName, opts, (error, data, response) => {
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
 **collectionName** | **String**| The name of the geofence collection to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteKey

> Object deleteKey(keyName, opts)



Deletes the specified API key. The API key must have been deactivated more than 90 days previously.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let keyName = "keyName_example"; // String | The name of the API key to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteKey(keyName, opts, (error, data, response) => {
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
 **keyName** | **String**| The name of the API key to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMap

> Object deleteMap(mapName, opts)



&lt;p&gt;Deletes a map resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently. If the map is being used in an application, the map may not render.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let mapName = "mapName_example"; // String | The name of the map resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMap(mapName, opts, (error, data, response) => {
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
 **mapName** | **String**| The name of the map resource to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePlaceIndex

> Object deletePlaceIndex(indexName, opts)



&lt;p&gt;Deletes a place index resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePlaceIndex(indexName, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRouteCalculator

> Object deleteRouteCalculator(calculatorName, opts)



&lt;p&gt;Deletes a route calculator resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let calculatorName = "calculatorName_example"; // String | The name of the route calculator resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRouteCalculator(calculatorName, opts, (error, data, response) => {
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
 **calculatorName** | **String**| The name of the route calculator resource to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTracker

> Object deleteTracker(trackerName, opts)



&lt;p&gt;Deletes a tracker resource from your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the resource permanently. If the tracker resource is in use, you may encounter an error. Make sure that the target resource isn&#39;t a dependency for your applications.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The name of the tracker resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTracker(trackerName, opts, (error, data, response) => {
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
 **trackerName** | **String**| The name of the tracker resource to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeGeofenceCollection

> DescribeGeofenceCollectionResponse describeGeofenceCollection(collectionName, opts)



Retrieves the geofence collection details.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The name of the geofence collection.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeGeofenceCollection(collectionName, opts, (error, data, response) => {
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
 **collectionName** | **String**| The name of the geofence collection. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeGeofenceCollectionResponse**](DescribeGeofenceCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeKey

> DescribeKeyResponse describeKey(keyName, opts)



Retrieves the API key resource details.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let keyName = "keyName_example"; // String | The name of the API key resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeKey(keyName, opts, (error, data, response) => {
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
 **keyName** | **String**| The name of the API key resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeKeyResponse**](DescribeKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeMap

> DescribeMapResponse describeMap(mapName, opts)



Retrieves the map resource details.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let mapName = "mapName_example"; // String | The name of the map resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMap(mapName, opts, (error, data, response) => {
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
 **mapName** | **String**| The name of the map resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMapResponse**](DescribeMapResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describePlaceIndex

> DescribePlaceIndexResponse describePlaceIndex(indexName, opts)



Retrieves the place index resource details.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePlaceIndex(indexName, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePlaceIndexResponse**](DescribePlaceIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRouteCalculator

> DescribeRouteCalculatorResponse describeRouteCalculator(calculatorName, opts)



Retrieves the route calculator resource details.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let calculatorName = "calculatorName_example"; // String | The name of the route calculator resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRouteCalculator(calculatorName, opts, (error, data, response) => {
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
 **calculatorName** | **String**| The name of the route calculator resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRouteCalculatorResponse**](DescribeRouteCalculatorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTracker

> DescribeTrackerResponse describeTracker(trackerName, opts)



Retrieves the tracker resource details.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The name of the tracker resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTracker(trackerName, opts, (error, data, response) => {
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
 **trackerName** | **String**| The name of the tracker resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTrackerResponse**](DescribeTrackerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateTrackerConsumer

> Object disassociateTrackerConsumer(consumerArn, trackerName, opts)



&lt;p&gt;Removes the association between a tracker resource and a geofence collection.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Once you unlink a tracker resource from a geofence collection, the tracker positions will no longer be automatically evaluated against geofences.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let consumerArn = "consumerArn_example"; // String | <p>The Amazon Resource Name (ARN) for the geofence collection to be disassociated from the tracker resource. Used when you need to specify a resource across all Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer</code> </p> </li> </ul>
let trackerName = "trackerName_example"; // String | The name of the tracker resource to be dissociated from the consumer.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateTrackerConsumer(consumerArn, trackerName, opts, (error, data, response) => {
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
 **consumerArn** | **String**| &lt;p&gt;The Amazon Resource Name (ARN) for the geofence collection to be disassociated from the tracker resource. Used when you need to specify a resource across all Amazon Web Services. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **trackerName** | **String**| The name of the tracker resource to be dissociated from the consumer. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDevicePosition

> GetDevicePositionResponse getDevicePosition(deviceId, trackerName, opts)



&lt;p&gt;Retrieves a device&#39;s most recent position according to its sample time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Device positions are deleted after 30 days.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let deviceId = "deviceId_example"; // String | The device whose position you want to retrieve.
let trackerName = "trackerName_example"; // String | The tracker resource receiving the position update.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDevicePosition(deviceId, trackerName, opts, (error, data, response) => {
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
 **deviceId** | **String**| The device whose position you want to retrieve. | 
 **trackerName** | **String**| The tracker resource receiving the position update. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDevicePositionResponse**](GetDevicePositionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDevicePositionHistory

> GetDevicePositionHistoryResponse getDevicePositionHistory(deviceId, trackerName, getDevicePositionHistoryRequest, opts)



&lt;p&gt;Retrieves the device position history from a tracker resource within a specified range of time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Device positions are deleted after 30 days.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let deviceId = "deviceId_example"; // String | The device whose position history you want to retrieve.
let trackerName = "trackerName_example"; // String | The tracker resource receiving the request for the device position history.
let getDevicePositionHistoryRequest = new AmazonLocationService.GetDevicePositionHistoryRequest(); // GetDevicePositionHistoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getDevicePositionHistory(deviceId, trackerName, getDevicePositionHistoryRequest, opts, (error, data, response) => {
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
 **deviceId** | **String**| The device whose position history you want to retrieve. | 
 **trackerName** | **String**| The tracker resource receiving the request for the device position history. | 
 **getDevicePositionHistoryRequest** | [**GetDevicePositionHistoryRequest**](GetDevicePositionHistoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetDevicePositionHistoryResponse**](GetDevicePositionHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getGeofence

> GetGeofenceResponse getGeofence(collectionName, geofenceId, opts)



Retrieves the geofence details from a geofence collection.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The geofence collection storing the target geofence.
let geofenceId = "geofenceId_example"; // String | The geofence you're retrieving details for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGeofence(collectionName, geofenceId, opts, (error, data, response) => {
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
 **collectionName** | **String**| The geofence collection storing the target geofence. | 
 **geofenceId** | **String**| The geofence you&#39;re retrieving details for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGeofenceResponse**](GetGeofenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMapGlyphs

> GetMapGlyphsResponse getMapGlyphs(fontStack, fontUnicodeRange, mapName, opts)



Retrieves glyphs used to display labels on a map.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let fontStack = "fontStack_example"; // String | <p>A comma-separated list of fonts to load glyphs from in order of preference. For example, <code>Noto Sans Regular, Arial Unicode</code>.</p> <p>Valid fonts stacks for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/esri.html\">Esri</a> styles: </p> <ul> <li> <p>VectorEsriDarkGrayCanvas – <code>Ubuntu Medium Italic</code> | <code>Ubuntu Medium</code> | <code>Ubuntu Italic</code> | <code>Ubuntu Regular</code> | <code>Ubuntu Bold</code> </p> </li> <li> <p>VectorEsriLightGrayCanvas – <code>Ubuntu Italic</code> | <code>Ubuntu Regular</code> | <code>Ubuntu Light</code> | <code>Ubuntu Bold</code> </p> </li> <li> <p>VectorEsriTopographic – <code>Noto Sans Italic</code> | <code>Noto Sans Regular</code> | <code>Noto Sans Bold</code> | <code>Noto Serif Regular</code> | <code>Roboto Condensed Light Italic</code> </p> </li> <li> <p>VectorEsriStreets – <code>Arial Regular</code> | <code>Arial Italic</code> | <code>Arial Bold</code> </p> </li> <li> <p>VectorEsriNavigation – <code>Arial Regular</code> | <code>Arial Italic</code> | <code>Arial Bold</code> </p> </li> </ul> <p>Valid font stacks for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/HERE.html\">HERE Technologies</a> styles:</p> <ul> <li> <p>VectorHereContrast – <code>Fira GO Regular</code> | <code>Fira GO Bold</code> </p> </li> <li> <p>VectorHereExplore, VectorHereExploreTruck, HybridHereExploreSatellite – <code>Fira GO Italic</code> | <code>Fira GO Map</code> | <code>Fira GO Map Bold</code> | <code>Noto Sans CJK JP Bold</code> | <code>Noto Sans CJK JP Light</code> | <code>Noto Sans CJK JP Regular</code> </p> </li> </ul> <p>Valid font stacks for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/grab.html\">GrabMaps</a> styles:</p> <ul> <li> <p>VectorGrabStandardLight, VectorGrabStandardDark – <code>Noto Sans Regular</code> | <code>Noto Sans Medium</code> | <code>Noto Sans Bold</code> </p> </li> </ul> <p>Valid font stacks for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/open-data.html\">Open Data</a> styles:</p> <ul> <li> <p>VectorOpenDataStandardLight, VectorOpenDataStandardDark, VectorOpenDataVisualizationLight, VectorOpenDataVisualizationDark – <code>Amazon Ember Regular,Noto Sans Regular</code> | <code>Amazon Ember Bold,Noto Sans Bold</code> | <code>Amazon Ember Medium,Noto Sans Medium</code> | <code>Amazon Ember Regular Italic,Noto Sans Italic</code> | <code>Amazon Ember Condensed RC Regular,Noto Sans Regular</code> | <code>Amazon Ember Condensed RC Bold,Noto Sans Bold</code> | <code>Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular</code> | <code>Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold</code> | <code>Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold</code> | <code>Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular</code> | <code>Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular</code> | <code>Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium</code> </p> </li> </ul> <note> <p>The fonts used by the Open Data map styles are combined fonts that use <code>Amazon Ember</code> for most glyphs but <code>Noto Sans</code> for glyphs unsupported by <code>Amazon Ember</code>.</p> </note>
let fontUnicodeRange = "fontUnicodeRange_example"; // String | A Unicode range of characters to download glyphs for. Each response will contain 256 characters. For example, 0–255 includes all characters from range <code>U+0000</code> to <code>00FF</code>. Must be aligned to multiples of 256.
let mapName = "mapName_example"; // String | The map resource associated with the glyph ﬁle.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.getMapGlyphs(fontStack, fontUnicodeRange, mapName, opts, (error, data, response) => {
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
 **fontStack** | **String**| &lt;p&gt;A comma-separated list of fonts to load glyphs from in order of preference. For example, &lt;code&gt;Noto Sans Regular, Arial Unicode&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Valid fonts stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/esri.html\&quot;&gt;Esri&lt;/a&gt; styles: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorEsriDarkGrayCanvas – &lt;code&gt;Ubuntu Medium Italic&lt;/code&gt; | &lt;code&gt;Ubuntu Medium&lt;/code&gt; | &lt;code&gt;Ubuntu Italic&lt;/code&gt; | &lt;code&gt;Ubuntu Regular&lt;/code&gt; | &lt;code&gt;Ubuntu Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriLightGrayCanvas – &lt;code&gt;Ubuntu Italic&lt;/code&gt; | &lt;code&gt;Ubuntu Regular&lt;/code&gt; | &lt;code&gt;Ubuntu Light&lt;/code&gt; | &lt;code&gt;Ubuntu Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriTopographic – &lt;code&gt;Noto Sans Italic&lt;/code&gt; | &lt;code&gt;Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Noto Sans Bold&lt;/code&gt; | &lt;code&gt;Noto Serif Regular&lt;/code&gt; | &lt;code&gt;Roboto Condensed Light Italic&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriStreets – &lt;code&gt;Arial Regular&lt;/code&gt; | &lt;code&gt;Arial Italic&lt;/code&gt; | &lt;code&gt;Arial Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorEsriNavigation – &lt;code&gt;Arial Regular&lt;/code&gt; | &lt;code&gt;Arial Italic&lt;/code&gt; | &lt;code&gt;Arial Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid font stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/HERE.html\&quot;&gt;HERE Technologies&lt;/a&gt; styles:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorHereContrast – &lt;code&gt;Fira GO Regular&lt;/code&gt; | &lt;code&gt;Fira GO Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VectorHereExplore, VectorHereExploreTruck, HybridHereExploreSatellite – &lt;code&gt;Fira GO Italic&lt;/code&gt; | &lt;code&gt;Fira GO Map&lt;/code&gt; | &lt;code&gt;Fira GO Map Bold&lt;/code&gt; | &lt;code&gt;Noto Sans CJK JP Bold&lt;/code&gt; | &lt;code&gt;Noto Sans CJK JP Light&lt;/code&gt; | &lt;code&gt;Noto Sans CJK JP Regular&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid font stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html\&quot;&gt;GrabMaps&lt;/a&gt; styles:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorGrabStandardLight, VectorGrabStandardDark – &lt;code&gt;Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Noto Sans Medium&lt;/code&gt; | &lt;code&gt;Noto Sans Bold&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid font stacks for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/open-data.html\&quot;&gt;Open Data&lt;/a&gt; styles:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VectorOpenDataStandardLight, VectorOpenDataStandardDark, VectorOpenDataVisualizationLight, VectorOpenDataVisualizationDark – &lt;code&gt;Amazon Ember Regular,Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Bold,Noto Sans Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Medium,Noto Sans Medium&lt;/code&gt; | &lt;code&gt;Amazon Ember Regular Italic,Noto Sans Italic&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Regular,Noto Sans Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Bold,Noto Sans Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold&lt;/code&gt; | &lt;code&gt;Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular&lt;/code&gt; | &lt;code&gt;Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The fonts used by the Open Data map styles are combined fonts that use &lt;code&gt;Amazon Ember&lt;/code&gt; for most glyphs but &lt;code&gt;Noto Sans&lt;/code&gt; for glyphs unsupported by &lt;code&gt;Amazon Ember&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; | 
 **fontUnicodeRange** | **String**| A Unicode range of characters to download glyphs for. Each response will contain 256 characters. For example, 0–255 includes all characters from range &lt;code&gt;U+0000&lt;/code&gt; to &lt;code&gt;00FF&lt;/code&gt;. Must be aligned to multiples of 256. | 
 **mapName** | **String**| The map resource associated with the glyph ﬁle. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**GetMapGlyphsResponse**](GetMapGlyphsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMapSprites

> GetMapSpritesResponse getMapSprites(fileName, mapName, opts)



Retrieves the sprite sheet corresponding to a map resource. The sprite sheet is a PNG image paired with a JSON document describing the offsets of individual icons that will be displayed on a rendered map.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let fileName = "fileName_example"; // String | <p>The name of the sprite ﬁle. Use the following ﬁle names for the sprite sheet:</p> <ul> <li> <p> <code>sprites.png</code> </p> </li> <li> <p> <code>sprites@2x.png</code> for high pixel density displays</p> </li> </ul> <p>For the JSON document containing image offsets. Use the following ﬁle names:</p> <ul> <li> <p> <code>sprites.json</code> </p> </li> <li> <p> <code>sprites@2x.json</code> for high pixel density displays</p> </li> </ul>
let mapName = "mapName_example"; // String | The map resource associated with the sprite ﬁle.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.getMapSprites(fileName, mapName, opts, (error, data, response) => {
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
 **fileName** | **String**| &lt;p&gt;The name of the sprite ﬁle. Use the following ﬁle names for the sprite sheet:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites.png&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites@2x.png&lt;/code&gt; for high pixel density displays&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For the JSON document containing image offsets. Use the following ﬁle names:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites.json&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sprites@2x.json&lt;/code&gt; for high pixel density displays&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **mapName** | **String**| The map resource associated with the sprite ﬁle. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**GetMapSpritesResponse**](GetMapSpritesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMapStyleDescriptor

> GetMapStyleDescriptorResponse getMapStyleDescriptor(mapName, opts)



&lt;p&gt;Retrieves the map style descriptor from a map resource. &lt;/p&gt; &lt;p&gt;The style descriptor contains speciﬁcations on how features render on a map. For example, what data to display, what order to display the data in, and the style for the data. Style descriptors follow the Mapbox Style Specification.&lt;/p&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let mapName = "mapName_example"; // String | The map resource to retrieve the style descriptor from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.getMapStyleDescriptor(mapName, opts, (error, data, response) => {
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
 **mapName** | **String**| The map resource to retrieve the style descriptor from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**GetMapStyleDescriptorResponse**](GetMapStyleDescriptorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMapTile

> GetMapTileResponse getMapTile(mapName, X, Y, Z, opts)



&lt;p&gt;Retrieves a vector data tile from the map resource. Map tiles are used by clients to render a map. they&#39;re addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level. &lt;/p&gt; &lt;p&gt;The origin (0, 0) is the top left of the map. Increasing the zoom level by 1 doubles both the X and Y dimensions, so a tile containing data for the entire world at (0/0/0) will be split into 4 tiles at zoom 1 (1/0/0, 1/0/1, 1/1/0, 1/1/1).&lt;/p&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let mapName = "mapName_example"; // String | The map resource to retrieve the map tiles from.
let X = "X_example"; // String | The X axis value for the map tile.
let Y = "Y_example"; // String | The Y axis value for the map tile. 
let Z = "Z_example"; // String | The zoom value for the map tile.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.getMapTile(mapName, X, Y, Z, opts, (error, data, response) => {
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
 **mapName** | **String**| The map resource to retrieve the map tiles from. | 
 **X** | **String**| The X axis value for the map tile. | 
 **Y** | **String**| The Y axis value for the map tile.  | 
 **Z** | **String**| The zoom value for the map tile. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**GetMapTileResponse**](GetMapTileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlace

> GetPlaceResponse getPlace(indexName, placeId, opts)



&lt;p&gt;Finds a place by its unique ID. A &lt;code&gt;PlaceId&lt;/code&gt; is returned by other search operations.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A PlaceId is valid only if all of the following are the same in the original search request and the call to &lt;code&gt;GetPlace&lt;/code&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Customer Amazon Web Services account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services Region&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data provider specified in the place index resource&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource that you want to use for the search.
let placeId = "placeId_example"; // String | The identifier of the place to find.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example", // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
  'language': "language_example" // String | <p>The preferred language used to return results. The value must be a valid <a href=\"https://tools.ietf.org/search/bcp47\">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
};
apiInstance.getPlace(indexName, placeId, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource that you want to use for the search. | 
 **placeId** | **String**| The identifier of the place to find. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 
 **language** | **String**| &lt;p&gt;The preferred language used to return results. The value must be a valid &lt;a href&#x3D;\&quot;https://tools.ietf.org/search/bcp47\&quot;&gt;BCP 47&lt;/a&gt; language tag, for example, &lt;code&gt;en&lt;/code&gt; for English.&lt;/p&gt; &lt;p&gt;This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.&lt;/p&gt; &lt;p&gt;For an example, we&#39;ll use the Greek language. You search for a location around Athens, Greece, with the &lt;code&gt;language&lt;/code&gt; parameter set to &lt;code&gt;en&lt;/code&gt;. The &lt;code&gt;city&lt;/code&gt; in the results will most likely be returned as &lt;code&gt;Athens&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you set the &lt;code&gt;language&lt;/code&gt; parameter to &lt;code&gt;el&lt;/code&gt;, for Greek, then the &lt;code&gt;city&lt;/code&gt; in the results will more likely be returned as &lt;code&gt;Αθήνα&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the data provider does not have a value for Greek, the result will be in a language that the provider does support.&lt;/p&gt; | [optional] 

### Return type

[**GetPlaceResponse**](GetPlaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDevicePositions

> ListDevicePositionsResponse listDevicePositions(trackerName, listDevicePositionsRequest, opts)



A batch request to retrieve all device positions.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The tracker resource containing the requested devices.
let listDevicePositionsRequest = new AmazonLocationService.ListDevicePositionsRequest(); // ListDevicePositionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listDevicePositions(trackerName, listDevicePositionsRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The tracker resource containing the requested devices. | 
 **listDevicePositionsRequest** | [**ListDevicePositionsRequest**](ListDevicePositionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListDevicePositionsResponse**](ListDevicePositionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGeofenceCollections

> ListGeofenceCollectionsResponse listGeofenceCollections(listGeofenceCollectionsRequest, opts)



Lists geofence collections in your Amazon Web Services account.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let listGeofenceCollectionsRequest = new AmazonLocationService.ListGeofenceCollectionsRequest(); // ListGeofenceCollectionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listGeofenceCollections(listGeofenceCollectionsRequest, opts, (error, data, response) => {
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
 **listGeofenceCollectionsRequest** | [**ListGeofenceCollectionsRequest**](ListGeofenceCollectionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListGeofenceCollectionsResponse**](ListGeofenceCollectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGeofences

> ListGeofencesResponse listGeofences(collectionName, listGeofencesRequest, opts)



Lists geofences stored in a given geofence collection.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The name of the geofence collection storing the list of geofences.
let listGeofencesRequest = new AmazonLocationService.ListGeofencesRequest(); // ListGeofencesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listGeofences(collectionName, listGeofencesRequest, opts, (error, data, response) => {
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
 **collectionName** | **String**| The name of the geofence collection storing the list of geofences. | 
 **listGeofencesRequest** | [**ListGeofencesRequest**](ListGeofencesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListGeofencesResponse**](ListGeofencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listKeys

> ListKeysResponse listKeys(listKeysRequest, opts)



Lists API key resources in your Amazon Web Services account.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let listKeysRequest = new AmazonLocationService.ListKeysRequest(); // ListKeysRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listKeys(listKeysRequest, opts, (error, data, response) => {
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
 **listKeysRequest** | [**ListKeysRequest**](ListKeysRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListKeysResponse**](ListKeysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listMaps

> ListMapsResponse listMaps(listMapsRequest, opts)



Lists map resources in your Amazon Web Services account.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let listMapsRequest = new AmazonLocationService.ListMapsRequest(); // ListMapsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listMaps(listMapsRequest, opts, (error, data, response) => {
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
 **listMapsRequest** | [**ListMapsRequest**](ListMapsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListMapsResponse**](ListMapsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPlaceIndexes

> ListPlaceIndexesResponse listPlaceIndexes(listPlaceIndexesRequest, opts)



Lists place index resources in your Amazon Web Services account.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let listPlaceIndexesRequest = new AmazonLocationService.ListPlaceIndexesRequest(); // ListPlaceIndexesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listPlaceIndexes(listPlaceIndexesRequest, opts, (error, data, response) => {
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
 **listPlaceIndexesRequest** | [**ListPlaceIndexesRequest**](ListPlaceIndexesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListPlaceIndexesResponse**](ListPlaceIndexesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRouteCalculators

> ListRouteCalculatorsResponse listRouteCalculators(listRouteCalculatorsRequest, opts)



Lists route calculator resources in your Amazon Web Services account.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let listRouteCalculatorsRequest = new AmazonLocationService.ListRouteCalculatorsRequest(); // ListRouteCalculatorsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listRouteCalculators(listRouteCalculatorsRequest, opts, (error, data, response) => {
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
 **listRouteCalculatorsRequest** | [**ListRouteCalculatorsRequest**](ListRouteCalculatorsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListRouteCalculatorsResponse**](ListRouteCalculatorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Returns a list of tags that are applied to the specified Amazon Location resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| &lt;p&gt;The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:resourcetype/ExampleResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrackerConsumers

> ListTrackerConsumersResponse listTrackerConsumers(trackerName, listGeofenceCollectionsRequest, opts)



Lists geofence collections currently associated to the given tracker resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The tracker resource whose associated geofence collections you want to list.
let listGeofenceCollectionsRequest = new AmazonLocationService.ListGeofenceCollectionsRequest(); // ListGeofenceCollectionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTrackerConsumers(trackerName, listGeofenceCollectionsRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The tracker resource whose associated geofence collections you want to list. | 
 **listGeofenceCollectionsRequest** | [**ListGeofenceCollectionsRequest**](ListGeofenceCollectionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTrackerConsumersResponse**](ListTrackerConsumersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTrackers

> ListTrackersResponse listTrackers(listGeofenceCollectionsRequest, opts)



Lists tracker resources in your Amazon Web Services account.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let listGeofenceCollectionsRequest = new AmazonLocationService.ListGeofenceCollectionsRequest(); // ListGeofenceCollectionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTrackers(listGeofenceCollectionsRequest, opts, (error, data, response) => {
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
 **listGeofenceCollectionsRequest** | [**ListGeofenceCollectionsRequest**](ListGeofenceCollectionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTrackersResponse**](ListTrackersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putGeofence

> PutGeofenceResponse putGeofence(collectionName, geofenceId, putGeofenceRequest, opts)



Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request. 

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The geofence collection to store the geofence in.
let geofenceId = "geofenceId_example"; // String | An identifier for the geofence. For example, <code>ExampleGeofence-1</code>.
let putGeofenceRequest = new AmazonLocationService.PutGeofenceRequest(); // PutGeofenceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putGeofence(collectionName, geofenceId, putGeofenceRequest, opts, (error, data, response) => {
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
 **collectionName** | **String**| The geofence collection to store the geofence in. | 
 **geofenceId** | **String**| An identifier for the geofence. For example, &lt;code&gt;ExampleGeofence-1&lt;/code&gt;. | 
 **putGeofenceRequest** | [**PutGeofenceRequest**](PutGeofenceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutGeofenceResponse**](PutGeofenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchPlaceIndexForPosition

> SearchPlaceIndexForPositionResponse searchPlaceIndexForPosition(indexName, searchPlaceIndexForPositionRequest, opts)



Reverse geocodes a given coordinate and returns a legible address. Allows you to search for Places or points of interest near a given position.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource you want to use for the search.
let searchPlaceIndexForPositionRequest = new AmazonLocationService.SearchPlaceIndexForPositionRequest(); // SearchPlaceIndexForPositionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.searchPlaceIndexForPosition(indexName, searchPlaceIndexForPositionRequest, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource you want to use for the search. | 
 **searchPlaceIndexForPositionRequest** | [**SearchPlaceIndexForPositionRequest**](SearchPlaceIndexForPositionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**SearchPlaceIndexForPositionResponse**](SearchPlaceIndexForPositionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchPlaceIndexForSuggestions

> SearchPlaceIndexForSuggestionsResponse searchPlaceIndexForSuggestions(indexName, searchPlaceIndexForSuggestionsRequest, opts)



&lt;p&gt;Generates suggestions for addresses and points of interest based on partial or misspelled free-form text. This operation is also known as autocomplete, autosuggest, or fuzzy matching.&lt;/p&gt; &lt;p&gt;Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can search for suggested place names near a specified position by using &lt;code&gt;BiasPosition&lt;/code&gt;, or filter results within a bounding box by using &lt;code&gt;FilterBBox&lt;/code&gt;. These parameters are mutually exclusive; using both &lt;code&gt;BiasPosition&lt;/code&gt; and &lt;code&gt;FilterBBox&lt;/code&gt; in the same command returns an error.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource you want to use for the search.
let searchPlaceIndexForSuggestionsRequest = new AmazonLocationService.SearchPlaceIndexForSuggestionsRequest(); // SearchPlaceIndexForSuggestionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.searchPlaceIndexForSuggestions(indexName, searchPlaceIndexForSuggestionsRequest, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource you want to use for the search. | 
 **searchPlaceIndexForSuggestionsRequest** | [**SearchPlaceIndexForSuggestionsRequest**](SearchPlaceIndexForSuggestionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**SearchPlaceIndexForSuggestionsResponse**](SearchPlaceIndexForSuggestionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchPlaceIndexForText

> SearchPlaceIndexForTextResponse searchPlaceIndexForText(indexName, searchPlaceIndexForTextRequest, opts)



&lt;p&gt;Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest. &lt;/p&gt; &lt;p&gt;Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can search for places near a given position using &lt;code&gt;BiasPosition&lt;/code&gt;, or filter results within a bounding box using &lt;code&gt;FilterBBox&lt;/code&gt;. Providing both parameters simultaneously returns an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Search results are returned in order of highest to lowest relevance.&lt;/p&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource you want to use for the search.
let searchPlaceIndexForTextRequest = new AmazonLocationService.SearchPlaceIndexForTextRequest(); // SearchPlaceIndexForTextRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'key': "key_example" // String | The optional <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\">API key</a> to authorize the request.
};
apiInstance.searchPlaceIndexForText(indexName, searchPlaceIndexForTextRequest, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource you want to use for the search. | 
 **searchPlaceIndexForTextRequest** | [**SearchPlaceIndexForTextRequest**](SearchPlaceIndexForTextRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **key** | **String**| The optional &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html\&quot;&gt;API key&lt;/a&gt; to authorize the request. | [optional] 

### Return type

[**SearchPlaceIndexForTextResponse**](SearchPlaceIndexForTextResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; operation with an Amazon Location Service resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the tags already associated with the resource. If you specify a tag key that&#39;s already associated with the resource, the new tag value that you specify replaces the previous value for that tag. &lt;/p&gt; &lt;p&gt;You can associate up to 50 tags with a resource.&lt;/p&gt;

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The Amazon Resource Name (ARN) of the resource whose tags you want to update.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
let tagResourceRequest = new AmazonLocationService.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| &lt;p&gt;The Amazon Resource Name (ARN) of the resource whose tags you want to update.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:resourcetype/ExampleResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes one or more tags from the specified Amazon Location resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
let tagKeys = ["null"]; // [String] | The list of tag keys to remove from the specified resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| &lt;p&gt;The Amazon Resource Name (ARN) of the resource from which you want to remove tags.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Format example: &lt;code&gt;arn:aws:geo:region:account-id:resourcetype/ExampleResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **tagKeys** | [**[String]**](String.md)| The list of tag keys to remove from the specified resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateGeofenceCollection

> UpdateGeofenceCollectionResponse updateGeofenceCollection(collectionName, updateGeofenceCollectionRequest, opts)



Updates the specified properties of a given geofence collection.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let collectionName = "collectionName_example"; // String | The name of the geofence collection to update.
let updateGeofenceCollectionRequest = new AmazonLocationService.UpdateGeofenceCollectionRequest(); // UpdateGeofenceCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGeofenceCollection(collectionName, updateGeofenceCollectionRequest, opts, (error, data, response) => {
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
 **collectionName** | **String**| The name of the geofence collection to update. | 
 **updateGeofenceCollectionRequest** | [**UpdateGeofenceCollectionRequest**](UpdateGeofenceCollectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGeofenceCollectionResponse**](UpdateGeofenceCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateKey

> UpdateKeyResponse updateKey(keyName, updateKeyRequest, opts)



Updates the specified properties of a given API key resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let keyName = "keyName_example"; // String | The name of the API key resource to update.
let updateKeyRequest = new AmazonLocationService.UpdateKeyRequest(); // UpdateKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateKey(keyName, updateKeyRequest, opts, (error, data, response) => {
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
 **keyName** | **String**| The name of the API key resource to update. | 
 **updateKeyRequest** | [**UpdateKeyRequest**](UpdateKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateKeyResponse**](UpdateKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMap

> UpdateMapResponse updateMap(mapName, updateMapRequest, opts)



Updates the specified properties of a given map resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let mapName = "mapName_example"; // String | The name of the map resource to update.
let updateMapRequest = new AmazonLocationService.UpdateMapRequest(); // UpdateMapRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMap(mapName, updateMapRequest, opts, (error, data, response) => {
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
 **mapName** | **String**| The name of the map resource to update. | 
 **updateMapRequest** | [**UpdateMapRequest**](UpdateMapRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMapResponse**](UpdateMapResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePlaceIndex

> UpdatePlaceIndexResponse updatePlaceIndex(indexName, updatePlaceIndexRequest, opts)



Updates the specified properties of a given place index resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let indexName = "indexName_example"; // String | The name of the place index resource to update.
let updatePlaceIndexRequest = new AmazonLocationService.UpdatePlaceIndexRequest(); // UpdatePlaceIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePlaceIndex(indexName, updatePlaceIndexRequest, opts, (error, data, response) => {
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
 **indexName** | **String**| The name of the place index resource to update. | 
 **updatePlaceIndexRequest** | [**UpdatePlaceIndexRequest**](UpdatePlaceIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePlaceIndexResponse**](UpdatePlaceIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRouteCalculator

> UpdateRouteCalculatorResponse updateRouteCalculator(calculatorName, updateRouteCalculatorRequest, opts)



Updates the specified properties for a given route calculator resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let calculatorName = "calculatorName_example"; // String | The name of the route calculator resource to update.
let updateRouteCalculatorRequest = new AmazonLocationService.UpdateRouteCalculatorRequest(); // UpdateRouteCalculatorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRouteCalculator(calculatorName, updateRouteCalculatorRequest, opts, (error, data, response) => {
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
 **calculatorName** | **String**| The name of the route calculator resource to update. | 
 **updateRouteCalculatorRequest** | [**UpdateRouteCalculatorRequest**](UpdateRouteCalculatorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRouteCalculatorResponse**](UpdateRouteCalculatorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTracker

> UpdateTrackerResponse updateTracker(trackerName, updateTrackerRequest, opts)



Updates the specified properties of a given tracker resource.

### Example

```javascript
import AmazonLocationService from 'amazon_location_service';
let defaultClient = AmazonLocationService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLocationService.DefaultApi();
let trackerName = "trackerName_example"; // String | The name of the tracker resource to update.
let updateTrackerRequest = new AmazonLocationService.UpdateTrackerRequest(); // UpdateTrackerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTracker(trackerName, updateTrackerRequest, opts, (error, data, response) => {
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
 **trackerName** | **String**| The name of the tracker resource to update. | 
 **updateTrackerRequest** | [**UpdateTrackerRequest**](UpdateTrackerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTrackerResponse**](UpdateTrackerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

