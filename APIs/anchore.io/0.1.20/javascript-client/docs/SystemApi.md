# AnchoreEngineApiServer.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFeed**](SystemApi.md#deleteFeed) | **DELETE** /system/feeds/{feed} | 
[**deleteFeedGroup**](SystemApi.md#deleteFeedGroup) | **DELETE** /system/feeds/{feed}/{group} | 
[**deleteService**](SystemApi.md#deleteService) | **DELETE** /system/services/{servicename}/{hostid} | Delete the service config
[**describeErrorCodes**](SystemApi.md#describeErrorCodes) | **GET** /system/error_codes | Describe anchore engine error codes.
[**describePolicy**](SystemApi.md#describePolicy) | **GET** /system/policy_spec | Describe the policy language spec implemented by this service.
[**getServiceDetail**](SystemApi.md#getServiceDetail) | **GET** /system | System status
[**getServicesByName**](SystemApi.md#getServicesByName) | **GET** /system/services/{servicename} | Get a service configuration and state
[**getServicesByNameAndHost**](SystemApi.md#getServicesByNameAndHost) | **GET** /system/services/{servicename}/{hostid} | Get service config for a specific host
[**getStatus**](SystemApi.md#getStatus) | **GET** /status | Service status
[**getSystemFeeds**](SystemApi.md#getSystemFeeds) | **GET** /system/feeds | list feeds operations and information
[**listServices**](SystemApi.md#listServices) | **GET** /system/services | List system services
[**postSystemFeeds**](SystemApi.md#postSystemFeeds) | **POST** /system/feeds | trigger feeds operations
[**testWebhook**](SystemApi.md#testWebhook) | **POST** /system/webhooks/{webhook_type}/test | Adds the capabilities to test a webhook delivery for the given notification type
[**toggleFeedEnabled**](SystemApi.md#toggleFeedEnabled) | **PUT** /system/feeds/{feed} | 
[**toggleGroupEnabled**](SystemApi.md#toggleGroupEnabled) | **PUT** /system/feeds/{feed}/{group} | 



## deleteFeed

> deleteFeed(feed)



Delete the groups and data for the feed and disable the feed itself

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let feed = "feed_example"; // String | 
apiInstance.deleteFeed(feed, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFeedGroup

> deleteFeedGroup(feed, group)



Delete the group data and disable the group itself

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let feed = "feed_example"; // String | 
let group = "group_example"; // String | 
apiInstance.deleteFeedGroup(feed, group, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed** | **String**|  | 
 **group** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteService

> deleteService(servicename, hostid)

Delete the service config

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let servicename = "servicename_example"; // String | 
let hostid = "hostid_example"; // String | 
apiInstance.deleteService(servicename, hostid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servicename** | **String**|  | 
 **hostid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeErrorCodes

> [AnchoreErrorCode] describeErrorCodes()

Describe anchore engine error codes.

Describe anchore engine error codes.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
apiInstance.describeErrorCodes((error, data, response) => {
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

[**[AnchoreErrorCode]**](AnchoreErrorCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describePolicy

> [GateSpec] describePolicy()

Describe the policy language spec implemented by this service.

Get the policy language spec for this service

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
apiInstance.describePolicy((error, data, response) => {
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

[**[GateSpec]**](GateSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceDetail

> SystemStatusResponse getServiceDetail()

System status

Get the system status including queue lengths

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
apiInstance.getServiceDetail((error, data, response) => {
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

[**SystemStatusResponse**](SystemStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServicesByName

> [Service] getServicesByName(servicename)

Get a service configuration and state

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let servicename = "servicename_example"; // String | 
apiInstance.getServicesByName(servicename, (error, data, response) => {
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
 **servicename** | **String**|  | 

### Return type

[**[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServicesByNameAndHost

> [Service] getServicesByNameAndHost(servicename, hostid)

Get service config for a specific host

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let servicename = "servicename_example"; // String | 
let hostid = "hostid_example"; // String | 
apiInstance.getServicesByNameAndHost(servicename, hostid, (error, data, response) => {
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
 **servicename** | **String**|  | 
 **hostid** | **String**|  | 

### Return type

[**[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatus

> StatusResponse getStatus()

Service status

Get the API service status

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
apiInstance.getStatus((error, data, response) => {
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

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSystemFeeds

> [FeedMetadata] getSystemFeeds()

list feeds operations and information

Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
apiInstance.getSystemFeeds((error, data, response) => {
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

[**[FeedMetadata]**](FeedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServices

> [Service] listServices()

List system services

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
apiInstance.listServices((error, data, response) => {
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

[**[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postSystemFeeds

> [FeedSyncResult] postSystemFeeds(opts)

trigger feeds operations

Execute a synchronous feed sync operation. The response will block until complete, then return the result summary.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let opts = {
  'flush': true, // Boolean | instruct system to flush existing data feeds records from anchore-engine
  'sync': true // Boolean | instruct system to re-sync data feeds
};
apiInstance.postSystemFeeds(opts, (error, data, response) => {
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
 **flush** | **Boolean**| instruct system to flush existing data feeds records from anchore-engine | [optional] 
 **sync** | **Boolean**| instruct system to re-sync data feeds | [optional] 

### Return type

[**[FeedSyncResult]**](FeedSyncResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## testWebhook

> testWebhook(webhookType, opts)

Adds the capabilities to test a webhook delivery for the given notification type

Loads the Webhook configuration for webhook_type, and sends the notification out as a test

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let webhookType = "webhookType_example"; // String | The Webhook Type that we should test
let opts = {
  'notificationType': "'tag_update'" // String | What kind of Notification to send
};
apiInstance.testWebhook(webhookType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhookType** | **String**| The Webhook Type that we should test | 
 **notificationType** | **String**| What kind of Notification to send | [optional] [default to &#39;tag_update&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## toggleFeedEnabled

> FeedMetadata toggleFeedEnabled(feed, enabled)



Disable the feed so that it does not sync on subsequent sync operations

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let feed = "feed_example"; // String | 
let enabled = true; // Boolean | 
apiInstance.toggleFeedEnabled(feed, enabled, (error, data, response) => {
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
 **feed** | **String**|  | 
 **enabled** | **Boolean**|  | 

### Return type

[**FeedMetadata**](FeedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## toggleGroupEnabled

> [FeedMetadata] toggleGroupEnabled(feed, group, enabled)



Disable a specific group within a feed to not sync

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SystemApi();
let feed = "feed_example"; // String | 
let group = "group_example"; // String | 
let enabled = true; // Boolean | 
apiInstance.toggleGroupEnabled(feed, group, enabled, (error, data, response) => {
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
 **feed** | **String**|  | 
 **group** | **String**|  | 
 **enabled** | **Boolean**|  | 

### Return type

[**[FeedMetadata]**](FeedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

