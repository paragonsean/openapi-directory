# Bufferapp.DefaultApi

All URIs are relative to *https://api.bufferapp.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infoConfigurationmediaTypeExtensionGet**](DefaultApi.md#infoConfigurationmediaTypeExtensionGet) | **GET** /info/configuration{mediaTypeExtension} | 
[**linksSharesmediaTypeExtensionGet**](DefaultApi.md#linksSharesmediaTypeExtensionGet) | **GET** /links/shares{mediaTypeExtension} | 
[**profilesIdSchedulesUpdatemediaTypeExtensionPost**](DefaultApi.md#profilesIdSchedulesUpdatemediaTypeExtensionPost) | **POST** /profiles/{id}/schedules/update{mediaTypeExtension} | 
[**profilesIdSchedulesmediaTypeExtensionGet**](DefaultApi.md#profilesIdSchedulesmediaTypeExtensionGet) | **GET** /profiles/{id}/schedules{mediaTypeExtension} | 
[**profilesIdUpdatesPendingmediaTypeExtensionGet**](DefaultApi.md#profilesIdUpdatesPendingmediaTypeExtensionGet) | **GET** /profiles/{id}/updates/pending{mediaTypeExtension} | 
[**profilesIdUpdatesReordermediaTypeExtensionPost**](DefaultApi.md#profilesIdUpdatesReordermediaTypeExtensionPost) | **POST** /profiles/{id}/updates/reorder{mediaTypeExtension} | 
[**profilesIdUpdatesSentmediaTypeExtensionGet**](DefaultApi.md#profilesIdUpdatesSentmediaTypeExtensionGet) | **GET** /profiles/{id}/updates/sent{mediaTypeExtension} | 
[**profilesIdUpdatesShufflemediaTypeExtensionPost**](DefaultApi.md#profilesIdUpdatesShufflemediaTypeExtensionPost) | **POST** /profiles/{id}/updates/shuffle{mediaTypeExtension} | 
[**profilesIdmediaTypeExtensionGet**](DefaultApi.md#profilesIdmediaTypeExtensionGet) | **GET** /profiles/{id}{mediaTypeExtension} | 
[**profilesmediaTypeExtensionGet**](DefaultApi.md#profilesmediaTypeExtensionGet) | **GET** /profiles{mediaTypeExtension} | 
[**updatesCreatemediaTypeExtensionPost**](DefaultApi.md#updatesCreatemediaTypeExtensionPost) | **POST** /updates/create{mediaTypeExtension} | 
[**updatesIdDestroymediaTypeExtensionPost**](DefaultApi.md#updatesIdDestroymediaTypeExtensionPost) | **POST** /updates/{id}/destroy{mediaTypeExtension} | 
[**updatesIdInteractionsmediaTypeExtensionGet**](DefaultApi.md#updatesIdInteractionsmediaTypeExtensionGet) | **GET** /updates/{id}/interactions{mediaTypeExtension} | 
[**updatesIdMoveToTopmediaTypeExtensionPost**](DefaultApi.md#updatesIdMoveToTopmediaTypeExtensionPost) | **POST** /updates/{id}/move_to_top{mediaTypeExtension} | 
[**updatesIdSharemediaTypeExtensionPost**](DefaultApi.md#updatesIdSharemediaTypeExtensionPost) | **POST** /updates/{id}/share{mediaTypeExtension} | 
[**updatesIdUpdatemediaTypeExtensionPost**](DefaultApi.md#updatesIdUpdatemediaTypeExtensionPost) | **POST** /updates/{id}/update{mediaTypeExtension} | 
[**updatesIdmediaTypeExtensionGet**](DefaultApi.md#updatesIdmediaTypeExtensionGet) | **GET** /updates/{id}{mediaTypeExtension} | 
[**usermediaTypeExtensionGet**](DefaultApi.md#usermediaTypeExtensionGet) | **GET** /user{mediaTypeExtension} | 



## infoConfigurationmediaTypeExtensionGet

> Configuration infoConfigurationmediaTypeExtensionGet(mediaTypeExtension)



Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.infoConfigurationmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Configuration**](Configuration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## linksSharesmediaTypeExtensionGet

> Shares linksSharesmediaTypeExtensionGet(mediaTypeExtension, url)



Returns an object with a the numbers of shares a link has had using Buffer.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
let url = "url_example"; // String | URL-encoded URL of the page for which the number of shares is requested.
apiInstance.linksSharesmediaTypeExtensionGet(mediaTypeExtension, url, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 
 **url** | **String**| URL-encoded URL of the page for which the number of shares is requested. | 

### Return type

[**Shares**](Shares.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdSchedulesUpdatemediaTypeExtensionPost

> Success profilesIdSchedulesUpdatemediaTypeExtensionPost(id, mediaTypeExtension)



\&quot;Set the posting schedules for the specified social media profile. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.profilesIdSchedulesUpdatemediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdSchedulesmediaTypeExtensionGet

> Schedules profilesIdSchedulesmediaTypeExtensionGet(id, mediaTypeExtension)



Returns details of the posting schedules associated with a social media profile.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.profilesIdSchedulesmediaTypeExtensionGet(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Schedules**](Schedules.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdUpdatesPendingmediaTypeExtensionGet

> UpdatesArray profilesIdUpdatesPendingmediaTypeExtensionGet(id, mediaTypeExtension, opts)



\&quot;Returns an array of updates that are currently in the buffer for an individual social media profile. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
let opts = {
  'page': 56, // Number | Specifies the page of status updates to receive. If not specified the first page of results will be returned.
  'count': 56, // Number | Specifies the number of status updates to receive. If provided, must be between 1 and 100.
  'since': new Date("2013-10-20"), // Date | Specifies a unix timestamp which only status updates created after this time will be retrieved.
  'utc': true // Boolean | If utc is set times will be returned relative to UTC rather than the users associated timezone.
};
apiInstance.profilesIdUpdatesPendingmediaTypeExtensionGet(id, mediaTypeExtension, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 
 **page** | **Number**| Specifies the page of status updates to receive. If not specified the first page of results will be returned. | [optional] 
 **count** | **Number**| Specifies the number of status updates to receive. If provided, must be between 1 and 100. | [optional] 
 **since** | **Date**| Specifies a unix timestamp which only status updates created after this time will be retrieved. | [optional] 
 **utc** | **Boolean**| If utc is set times will be returned relative to UTC rather than the users associated timezone. | [optional] 

### Return type

[**UpdatesArray**](UpdatesArray.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdUpdatesReordermediaTypeExtensionPost

> Shuffle profilesIdUpdatesReordermediaTypeExtensionPost(id, mediaTypeExtension)



Edit the order at which statuses for the specified social media profile will be sent out of the buffer. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.profilesIdUpdatesReordermediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Shuffle**](Shuffle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdUpdatesSentmediaTypeExtensionGet

> UpdatesArray profilesIdUpdatesSentmediaTypeExtensionGet(id, mediaTypeExtension, opts)



Returns an array of updates that have been sent from the buffer for an individual social media profile. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
let opts = {
  'page': 56, // Number | Specifies the page of status updates to receive. If not specified the first page of results will be returned.
  'count': 56, // Number | Specifies the number of status updates to receive. If provided, must be between 1 and 100.
  'since': new Date("2013-10-20"), // Date | Specifies a unix timestamp which only status updates created after this time will be retrieved.
  'utc': true // Boolean | If utc is set times will be returned relative to UTC rather than the users associated timezone.
};
apiInstance.profilesIdUpdatesSentmediaTypeExtensionGet(id, mediaTypeExtension, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 
 **page** | **Number**| Specifies the page of status updates to receive. If not specified the first page of results will be returned. | [optional] 
 **count** | **Number**| Specifies the number of status updates to receive. If provided, must be between 1 and 100. | [optional] 
 **since** | **Date**| Specifies a unix timestamp which only status updates created after this time will be retrieved. | [optional] 
 **utc** | **Boolean**| If utc is set times will be returned relative to UTC rather than the users associated timezone. | [optional] 

### Return type

[**UpdatesArray**](UpdatesArray.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdUpdatesShufflemediaTypeExtensionPost

> Shuffle profilesIdUpdatesShufflemediaTypeExtensionPost(id, mediaTypeExtension)



Randomize the order at which statuses for the specified social media profile will be sent out of the buffer. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.profilesIdUpdatesShufflemediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Shuffle**](Shuffle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesIdmediaTypeExtensionGet

> Profile profilesIdmediaTypeExtensionGet(mediaTypeExtension, id)



Returns details of the single specified social media profile.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
let id = "id_example"; // String | 
apiInstance.profilesIdmediaTypeExtensionGet(mediaTypeExtension, id, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesmediaTypeExtensionGet

> [ProfilesInner] profilesmediaTypeExtensionGet(mediaTypeExtension)



Returns an array of social media profiles connected to a users account.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.profilesmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 

### Return type

[**[ProfilesInner]**](ProfilesInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesCreatemediaTypeExtensionPost

> NewUpdate updatesCreatemediaTypeExtensionPost(mediaTypeExtension)



Create one or more new status updates. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.updatesCreatemediaTypeExtensionPost(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 

### Return type

[**NewUpdate**](NewUpdate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesIdDestroymediaTypeExtensionPost

> Success updatesIdDestroymediaTypeExtensionPost(id, mediaTypeExtension)



Permanently delete an existing status update.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.updatesIdDestroymediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesIdInteractionsmediaTypeExtensionGet

> Interactions updatesIdInteractionsmediaTypeExtensionGet(id, mediaTypeExtension, event, opts)



Returns the detailed information on individual interactions with the social media update such as favorites, retweets and likes. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
let event = "event_example"; // String | Specifies a type of event to be retrieved, for example \"retweet\", \"like\", \"comment\", \"mention\" or \"reshare\". They can also be plural (e.g., \"reshares\"). Plurality has no effect other than visual semantics. See /info/configuration for more information on supported interaction events. 
let opts = {
  'page': 56, // Number | Specifies the page of status updates to receive. If not specified the first page of results will be returned.
  'count': 56 // Number | Specifies the number of status updates to receive. If provided, must be between 1 and 100.
};
apiInstance.updatesIdInteractionsmediaTypeExtensionGet(id, mediaTypeExtension, event, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 
 **event** | **String**| Specifies a type of event to be retrieved, for example \&quot;retweet\&quot;, \&quot;like\&quot;, \&quot;comment\&quot;, \&quot;mention\&quot; or \&quot;reshare\&quot;. They can also be plural (e.g., \&quot;reshares\&quot;). Plurality has no effect other than visual semantics. See /info/configuration for more information on supported interaction events.  | 
 **page** | **Number**| Specifies the page of status updates to receive. If not specified the first page of results will be returned. | [optional] 
 **count** | **Number**| Specifies the number of status updates to receive. If provided, must be between 1 and 100. | [optional] 

### Return type

[**Interactions**](Interactions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesIdMoveToTopmediaTypeExtensionPost

> Update updatesIdMoveToTopmediaTypeExtensionPost(id, mediaTypeExtension)



Move an existing status update to the top of the queue and recalculate times for all updates in the queue. Returns the update with its new posting time.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.updatesIdMoveToTopmediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Update**](Update.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesIdSharemediaTypeExtensionPost

> Success updatesIdSharemediaTypeExtensionPost(id, mediaTypeExtension)



Immediately shares a single pending update and recalculates times for updates remaining in the queue.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.updatesIdSharemediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesIdUpdatemediaTypeExtensionPost

> IndividualUpdate updatesIdUpdatemediaTypeExtensionPost(id, mediaTypeExtension)



Edit an existing, individual status update. 

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let id = "id_example"; // String | 
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.updatesIdUpdatemediaTypeExtensionPost(id, mediaTypeExtension, (error, data, response) => {
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
 **id** | **String**|  | 
 **mediaTypeExtension** | **String**|  | 

### Return type

[**IndividualUpdate**](IndividualUpdate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatesIdmediaTypeExtensionGet

> Update updatesIdmediaTypeExtensionGet(mediaTypeExtension, id)



Returns a single social media update.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
let id = "id_example"; // String | 
apiInstance.updatesIdmediaTypeExtensionGet(mediaTypeExtension, id, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**Update**](Update.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usermediaTypeExtensionGet

> User usermediaTypeExtensionGet(mediaTypeExtension)



Returns a single user.

### Example

```javascript
import Bufferapp from 'bufferapp';

let apiInstance = new Bufferapp.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | 
apiInstance.usermediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

