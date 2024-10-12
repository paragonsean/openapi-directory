# DiscourseApiDocumentation.TopicsApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmarkTopic**](TopicsApi.md#bookmarkTopic) | **PUT** /t/{id}/bookmark.json | Bookmark topic
[**createTopicPostPM_0**](TopicsApi.md#createTopicPostPM_0) | **POST** /posts.json | Creates a new topic, a new post, or a private message
[**createTopicTimer**](TopicsApi.md#createTopicTimer) | **POST** /t/{id}/timer.json | Create topic timer
[**getSpecificPostsFromTopic**](TopicsApi.md#getSpecificPostsFromTopic) | **GET** /t/{id}/posts.json | Get specific posts from a topic
[**getTopic**](TopicsApi.md#getTopic) | **GET** /t/{id}.json | Get a single topic
[**getTopicByExternalId**](TopicsApi.md#getTopicByExternalId) | **GET** /t/external_id/{external_id}.json | Get topic by external_id
[**inviteToTopic**](TopicsApi.md#inviteToTopic) | **POST** /t/{id}/invite.json | Invite to topic
[**listLatestTopics**](TopicsApi.md#listLatestTopics) | **GET** /latest.json | Get the latest topics
[**listTopTopics**](TopicsApi.md#listTopTopics) | **GET** /top.json | Get the top topics filtered by period
[**removeTopic**](TopicsApi.md#removeTopic) | **DELETE** /t/{id}.json | Remove a topic
[**setNotificationLevel**](TopicsApi.md#setNotificationLevel) | **POST** /t/{id}/notifications.json | Set notification level
[**updateTopic**](TopicsApi.md#updateTopic) | **PUT** /t/-/{id}.json | Update a topic
[**updateTopicStatus**](TopicsApi.md#updateTopicStatus) | **PUT** /t/{id}/status.json | Update the status of a topic
[**updateTopicTimestamp**](TopicsApi.md#updateTopicTimestamp) | **PUT** /t/{id}/change-timestamp.json | Update topic timestamp



## bookmarkTopic

> bookmarkTopic(apiKey, apiUsername, id)

Bookmark topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
apiInstance.bookmarkTopic(apiKey, apiUsername, id, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createTopicPostPM_0

> CreateTopicPostPM200Response createTopicPostPM_0(opts)

Creates a new topic, a new post, or a private message

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let opts = {
  'createTopicPostPMRequest': new DiscourseApiDocumentation.CreateTopicPostPMRequest() // CreateTopicPostPMRequest | 
};
apiInstance.createTopicPostPM_0(opts, (error, data, response) => {
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
 **createTopicPostPMRequest** | [**CreateTopicPostPMRequest**](CreateTopicPostPMRequest.md)|  | [optional] 

### Return type

[**CreateTopicPostPM200Response**](CreateTopicPostPM200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTopicTimer

> CreateTopicTimer200Response createTopicTimer(apiKey, apiUsername, id, opts)

Create topic timer

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'createTopicTimerRequest': new DiscourseApiDocumentation.CreateTopicTimerRequest() // CreateTopicTimerRequest | 
};
apiInstance.createTopicTimer(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **createTopicTimerRequest** | [**CreateTopicTimerRequest**](CreateTopicTimerRequest.md)|  | [optional] 

### Return type

[**CreateTopicTimer200Response**](CreateTopicTimer200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSpecificPostsFromTopic

> GetSpecificPostsFromTopic200Response getSpecificPostsFromTopic(apiKey, apiUsername, id, opts)

Get specific posts from a topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'getSpecificPostsFromTopicRequest': new DiscourseApiDocumentation.GetSpecificPostsFromTopicRequest() // GetSpecificPostsFromTopicRequest | 
};
apiInstance.getSpecificPostsFromTopic(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **getSpecificPostsFromTopicRequest** | [**GetSpecificPostsFromTopicRequest**](GetSpecificPostsFromTopicRequest.md)|  | [optional] 

### Return type

[**GetSpecificPostsFromTopic200Response**](GetSpecificPostsFromTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTopic

> GetTopic200Response getTopic(apiKey, apiUsername, id)

Get a single topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getTopic(apiKey, apiUsername, id, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**GetTopic200Response**](GetTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTopicByExternalId

> getTopicByExternalId(externalId)

Get topic by external_id

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let externalId = "externalId_example"; // String | 
apiInstance.getTopicByExternalId(externalId, (error, data, response) => {
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
 **externalId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inviteToTopic

> InviteToTopic200Response inviteToTopic(apiKey, apiUsername, id, opts)

Invite to topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'inviteToTopicRequest': new DiscourseApiDocumentation.InviteToTopicRequest() // InviteToTopicRequest | 
};
apiInstance.inviteToTopic(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **inviteToTopicRequest** | [**InviteToTopicRequest**](InviteToTopicRequest.md)|  | [optional] 

### Return type

[**InviteToTopic200Response**](InviteToTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLatestTopics

> ListLatestTopics200Response listLatestTopics(apiKey, apiUsername, opts)

Get the latest topics

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let opts = {
  'order': "order_example", // String | Enum: `default`, `created`, `activity`, `views`, `posts`, `category`, `likes`, `op_likes`, `posters`
  'ascending': "ascending_example" // String | Defaults to `desc`, add `ascending=true` to sort asc
};
apiInstance.listLatestTopics(apiKey, apiUsername, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **order** | **String**| Enum: &#x60;default&#x60;, &#x60;created&#x60;, &#x60;activity&#x60;, &#x60;views&#x60;, &#x60;posts&#x60;, &#x60;category&#x60;, &#x60;likes&#x60;, &#x60;op_likes&#x60;, &#x60;posters&#x60; | [optional] 
 **ascending** | **String**| Defaults to &#x60;desc&#x60;, add &#x60;ascending&#x3D;true&#x60; to sort asc | [optional] 

### Return type

[**ListLatestTopics200Response**](ListLatestTopics200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTopTopics

> ListTopTopics200Response listTopTopics(apiKey, apiUsername, opts)

Get the top topics filtered by period

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let opts = {
  'period': "period_example" // String | Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`
};
apiInstance.listTopTopics(apiKey, apiUsername, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **period** | **String**| Enum: &#x60;all&#x60;, &#x60;yearly&#x60;, &#x60;quarterly&#x60;, &#x60;monthly&#x60;, &#x60;weekly&#x60;, &#x60;daily&#x60; | [optional] 

### Return type

[**ListTopTopics200Response**](ListTopTopics200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeTopic

> removeTopic(apiKey, apiUsername, id)

Remove a topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
apiInstance.removeTopic(apiKey, apiUsername, id, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setNotificationLevel

> UpdateGroup200Response setNotificationLevel(apiKey, apiUsername, id, opts)

Set notification level

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'setNotificationLevelRequest': new DiscourseApiDocumentation.SetNotificationLevelRequest() // SetNotificationLevelRequest | 
};
apiInstance.setNotificationLevel(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **setNotificationLevelRequest** | [**SetNotificationLevelRequest**](SetNotificationLevelRequest.md)|  | [optional] 

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTopic

> UpdateTopic200Response updateTopic(apiKey, apiUsername, id, opts)

Update a topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateTopicRequest': new DiscourseApiDocumentation.UpdateTopicRequest() // UpdateTopicRequest | 
};
apiInstance.updateTopic(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **updateTopicRequest** | [**UpdateTopicRequest**](UpdateTopicRequest.md)|  | [optional] 

### Return type

[**UpdateTopic200Response**](UpdateTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTopicStatus

> UpdateTopicStatus200Response updateTopicStatus(apiKey, apiUsername, id, opts)

Update the status of a topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateTopicStatusRequest': new DiscourseApiDocumentation.UpdateTopicStatusRequest() // UpdateTopicStatusRequest | 
};
apiInstance.updateTopicStatus(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **updateTopicStatusRequest** | [**UpdateTopicStatusRequest**](UpdateTopicStatusRequest.md)|  | [optional] 

### Return type

[**UpdateTopicStatus200Response**](UpdateTopicStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTopicTimestamp

> UpdateGroup200Response updateTopicTimestamp(apiKey, apiUsername, id, opts)

Update topic timestamp

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TopicsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateTopicTimestampRequest': new DiscourseApiDocumentation.UpdateTopicTimestampRequest() // UpdateTopicTimestampRequest | 
};
apiInstance.updateTopicTimestamp(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **updateTopicTimestampRequest** | [**UpdateTopicTimestampRequest**](UpdateTopicTimestampRequest.md)|  | [optional] 

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

