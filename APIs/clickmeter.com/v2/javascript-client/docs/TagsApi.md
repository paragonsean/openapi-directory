# ClickMeterApi.TagsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsCount**](TagsApi.md#tagsCount) | **GET** /tags/count | List of all the groups associated to the user filtered by this tag.
[**tagsDelete**](TagsApi.md#tagsDelete) | **DELETE** /tags/{tagId} | Delete a tag
[**tagsDeleteRelatedDatapoints**](TagsApi.md#tagsDeleteRelatedDatapoints) | **DELETE** /tags/{tagId}/datapoints | Delete the association of this tag with all datapoints
[**tagsDeleteRelatedGroups**](TagsApi.md#tagsDeleteRelatedGroups) | **DELETE** /tags/{tagId}/groups | Delete the association of this tag with all groups
[**tagsGet**](TagsApi.md#tagsGet) | **GET** /tags | List of all the groups associated to the user filtered by this tag.
[**tagsGetDatapoints**](TagsApi.md#tagsGetDatapoints) | **GET** /tags/{tagId}/datapoints | List of all the datapoints associated to the user filtered by this tag
[**tagsGetDatapointsCount**](TagsApi.md#tagsGetDatapointsCount) | **GET** /tags/{tagId}/datapoints/count | Count the datapoints associated to the user filtered by this tag
[**tagsGetGroups**](TagsApi.md#tagsGetGroups) | **GET** /tags/{tagId}/groups | List of all the groups associated to the user filtered by this tag.
[**tagsGetGroupsCount**](TagsApi.md#tagsGetGroupsCount) | **GET** /tags/{tagId}/groups/count | Count the groups associated to the user filtered by this tag
[**tagsPatchDataPoint**](TagsApi.md#tagsPatchDataPoint) | **PUT** /tags/{tagId}/datapoints/patch | Associate/Deassociate a tag with a datapoint
[**tagsPatchGroup**](TagsApi.md#tagsPatchGroup) | **PUT** /tags/{tagId}/groups/patch | Associate/Deassociate a tag with a group
[**tagsPatchTagName**](TagsApi.md#tagsPatchTagName) | **PUT** /tags/{tagId}/name | Fast patch a tag name
[**tagsPut**](TagsApi.md#tagsPut) | **POST** /tags | Create a tag
[**tagsTagIdGet**](TagsApi.md#tagsTagIdGet) | **GET** /tags/{tagId} | Retrieve a tag



## tagsCount

> Object tagsCount(opts)

List of all the groups associated to the user filtered by this tag.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let opts = {
  'name': "name_example", // String | Name of the tag
  'datapoints': "datapoints_example", // String | Comma separated list of datapoints id to filter by
  'groups': "groups_example", // String | Comma separated list of groups id to filter by
  'type': "type_example" // String | Type of entity related to the tag
};
apiInstance.tagsCount(opts, (error, data, response) => {
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
 **name** | **String**| Name of the tag | [optional] 
 **datapoints** | **String**| Comma separated list of datapoints id to filter by | [optional] 
 **groups** | **String**| Comma separated list of groups id to filter by | [optional] 
 **type** | **String**| Type of entity related to the tag | [optional] 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## tagsDelete

> Object tagsDelete(tagId)

Delete a tag

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
apiInstance.tagsDelete(tagId, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## tagsDeleteRelatedDatapoints

> ApiCoreResponsesEntityUriSystemInt64 tagsDeleteRelatedDatapoints(tagId)

Delete the association of this tag with all datapoints

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
apiInstance.tagsDeleteRelatedDatapoints(tagId, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsDeleteRelatedGroups

> ApiCoreResponsesEntityUriSystemInt64 tagsDeleteRelatedGroups(tagId)

Delete the association of this tag with all groups

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
apiInstance.tagsDeleteRelatedGroups(tagId, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsGet

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 tagsGet(opts)

List of all the groups associated to the user filtered by this tag.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20, // Number | Maximum elements to retrieve. Default to 20 if not specified.
  'name': "name_example", // String | Name of the tag
  'datapoints': "datapoints_example", // String | Comma separated list of datapoints id to filter by
  'groups': "groups_example", // String | Comma separated list of groups id to filter by
  'type': "type_example" // String | Type of entity related to the tag
};
apiInstance.tagsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0]
 **limit** | **Number**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20]
 **name** | **String**| Name of the tag | [optional] 
 **datapoints** | **String**| Comma separated list of datapoints id to filter by | [optional] 
 **groups** | **String**| Comma separated list of groups id to filter by | [optional] 
 **type** | **String**| Type of entity related to the tag | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## tagsGetDatapoints

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 tagsGetDatapoints(tagId, opts)

List of all the datapoints associated to the user filtered by this tag

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag.
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20, // Number | Maximum elements to retrieve. Default to 20 if not specified.
  'type': "type_example", // String | Type of the datapoint (\"tp\"/\"tl\")
  'status': "status_example", // String | Status of the datapoint
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.tagsGetDatapoints(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag. | 
 **offset** | **Number**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0]
 **limit** | **Number**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20]
 **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] 
 **status** | **String**| Status of the datapoint | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## tagsGetDatapointsCount

> ApiCoreResponsesCountResponce tagsGetDatapointsCount(tagId, opts)

Count the datapoints associated to the user filtered by this tag

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag.
let opts = {
  'type': "type_example", // String | Type of the datapoint (\"tp\"/\"tl\")
  'status': "status_example", // String | Status of the datapoint
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.tagsGetDatapointsCount(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag. | 
 **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] 
 **status** | **String**| Status of the datapoint | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsGetGroups

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 tagsGetGroups(tagId, opts)

List of all the groups associated to the user filtered by this tag.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag.
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20, // Number | Maximum elements to retrieve. Default to 20 if not specified.
  'status': "status_example", // String | Status of the datapoint
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude groups created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude groups created after this date (YYYYMMDD)
};
apiInstance.tagsGetGroups(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag. | 
 **offset** | **Number**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0]
 **limit** | **Number**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20]
 **status** | **String**| Status of the datapoint | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## tagsGetGroupsCount

> ApiCoreResponsesCountResponce tagsGetGroupsCount(tagId, opts)

Count the groups associated to the user filtered by this tag

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag.
let opts = {
  'status': "status_example", // String | Status of the datapoint
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude groups created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude groups created after this date (YYYYMMDD)
};
apiInstance.tagsGetGroupsCount(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag. | 
 **status** | **String**| Status of the datapoint | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsPatchDataPoint

> ApiCoreResponsesEntityUriSystemInt64 tagsPatchDataPoint(tagId, apiCoreRequestsPatchBody)

Associate/Deassociate a tag with a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
let apiCoreRequestsPatchBody = new ClickMeterApi.ApiCoreRequestsPatchBody(); // ApiCoreRequestsPatchBody | The body patch
apiInstance.tagsPatchDataPoint(tagId, apiCoreRequestsPatchBody, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 
 **apiCoreRequestsPatchBody** | [**ApiCoreRequestsPatchBody**](ApiCoreRequestsPatchBody.md)| The body patch | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsPatchGroup

> ApiCoreResponsesEntityUriSystemInt64 tagsPatchGroup(tagId, apiCoreRequestsPatchBody)

Associate/Deassociate a tag with a group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
let apiCoreRequestsPatchBody = new ClickMeterApi.ApiCoreRequestsPatchBody(); // ApiCoreRequestsPatchBody | The body patch
apiInstance.tagsPatchGroup(tagId, apiCoreRequestsPatchBody, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 
 **apiCoreRequestsPatchBody** | [**ApiCoreRequestsPatchBody**](ApiCoreRequestsPatchBody.md)| The body patch | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsPatchTagName

> ApiCoreResponsesEntityUriSystemInt64 tagsPatchTagName(tagId, apiCoreRequestsGenericTextPatch)

Fast patch a tag name

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
let apiCoreRequestsGenericTextPatch = new ClickMeterApi.ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | The body patch
apiInstance.tagsPatchTagName(tagId, apiCoreRequestsGenericTextPatch, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 
 **apiCoreRequestsGenericTextPatch** | [**ApiCoreRequestsGenericTextPatch**](ApiCoreRequestsGenericTextPatch.md)| The body patch | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsPut

> ApiCoreResponsesEntityUriSystemInt64 tagsPut(apiCoreDtoTagsTag)

Create a tag

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let apiCoreDtoTagsTag = new ClickMeterApi.ApiCoreDtoTagsTag(); // ApiCoreDtoTagsTag | The body of the tag
apiInstance.tagsPut(apiCoreDtoTagsTag, (error, data, response) => {
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
 **apiCoreDtoTagsTag** | [**ApiCoreDtoTagsTag**](ApiCoreDtoTagsTag.md)| The body of the tag | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## tagsTagIdGet

> ApiCoreDtoTagsTag tagsTagIdGet(tagId)

Retrieve a tag

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.TagsApi();
let tagId = 789; // Number | Id of the tag
apiInstance.tagsTagIdGet(tagId, (error, data, response) => {
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
 **tagId** | **Number**| Id of the tag | 

### Return type

[**ApiCoreDtoTagsTag**](ApiCoreDtoTagsTag.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

