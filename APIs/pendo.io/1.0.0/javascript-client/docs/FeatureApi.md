# PendoFeedbackApi.FeatureApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**featuresGet**](FeatureApi.md#featuresGet) | **GET** /features | Query features
[**featuresIdGet**](FeatureApi.md#featuresIdGet) | **GET** /features/{id} | Get a Feature by ID
[**featuresIdTagsDelete**](FeatureApi.md#featuresIdTagsDelete) | **DELETE** /features/{id}/tags | Delete custom Feature tags
[**featuresIdTagsGet**](FeatureApi.md#featuresIdTagsGet) | **GET** /features/{id}/tags | Get custom Feature tags
[**featuresIdTagsPost**](FeatureApi.md#featuresIdTagsPost) | **POST** /features/{id}/tags | Overwrite current custom Feature tags with the given tags
[**searchGet**](FeatureApi.md#searchGet) | **GET** /search | Search features



## featuresGet

> [Feature] featuresGet(opts)

Query features

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.FeatureApi();
let opts = {
  'limit': 3.4, // Number | Limit the number of records returned
  'start': 3.4, // Number | Offset to start at
  'orderDir': "orderDir_example", // String | The sort direction
  'isPrivate': true, // Boolean | Filter by whether the features are shown/hidden from customer, if supplied.
  'wantedBy': 56, // Number | Filter by User ID, if supplied.
  'orderBy': "orderBy_example", // String | The field to use for sort
  'tags': "tags_example", // String | Tags to limit results by. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \"....&tags=TagExample,Multi:TagThis,Multi:TagThat\".
  'products': "products_example" // String | Products to limit results by. Comma delimeted string of either ids or names. E.g. \"...&products=1,2,3\" or \"...products=Product1,Product2\".
};
apiInstance.featuresGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit the number of records returned | [optional] 
 **start** | **Number**| Offset to start at | [optional] 
 **orderDir** | **String**| The sort direction | [optional] 
 **isPrivate** | **Boolean**| Filter by whether the features are shown/hidden from customer, if supplied. | [optional] 
 **wantedBy** | **Number**| Filter by User ID, if supplied. | [optional] 
 **orderBy** | **String**| The field to use for sort | [optional] 
 **tags** | **String**| Tags to limit results by. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \&quot;....&amp;tags&#x3D;TagExample,Multi:TagThis,Multi:TagThat\&quot;. | [optional] 
 **products** | **String**| Products to limit results by. Comma delimeted string of either ids or names. E.g. \&quot;...&amp;products&#x3D;1,2,3\&quot; or \&quot;...products&#x3D;Product1,Product2\&quot;. | [optional] 

### Return type

[**[Feature]**](Feature.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresIdGet

> Feature featuresIdGet(id)

Get a Feature by ID

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.FeatureApi();
let id = 56; // Number | ID of the feature
apiInstance.featuresIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the feature | 

### Return type

[**Feature**](Feature.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresIdTagsDelete

> featuresIdTagsDelete(id)

Delete custom Feature tags

Removes all custom tags associated with the Feature

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.FeatureApi();
let id = 3.4; // Number | Feedback's Feature ID
apiInstance.featuresIdTagsDelete(id, (error, data, response) => {
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
 **id** | **Number**| Feedback&#39;s Feature ID | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## featuresIdTagsGet

> featuresIdTagsGet(id)

Get custom Feature tags

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.FeatureApi();
let id = 3.4; // Number | Account ID (generated by Feedback)
apiInstance.featuresIdTagsGet(id, (error, data, response) => {
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
 **id** | **Number**| Account ID (generated by Feedback) | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## featuresIdTagsPost

> featuresIdTagsPost(id, tags)

Overwrite current custom Feature tags with the given tags

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.FeatureApi();
let id = 3.4; // Number | Feedback's Feature ID
let tags = {key: null}; // Object | 
apiInstance.featuresIdTagsPost(id, tags, (error, data, response) => {
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
 **id** | **Number**| Feedback&#39;s Feature ID | 
 **tags** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchGet

> [Feature] searchGet(scope, q, opts)

Search features

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.FeatureApi();
let scope = "scope_example"; // String | Specifies the type of entity being searched for. Must be set to 'feature'
let q = "q_example"; // String | The search term.
let opts = {
  'status': "status_example", // String | A comma seperated list of status values to filter by, if required. Valid values: 'new', 'waiting', 'planned', 'developing', 'released', 'declined'.
  'tags': "tags_example", // String | Tags to limit results by - only applies when scope is 'case' or 'feature'. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \"....&tags=TagExample,Multi:TagThis,Multi:TagThat\".
  'products': "products_example" // String | Products to limit results by. Comma delimeted string of either ids or names. E.g. \"...&products=1,2,3\" or \"...products=Product1,Product2\".
};
apiInstance.searchGet(scope, q, opts, (error, data, response) => {
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
 **scope** | **String**| Specifies the type of entity being searched for. Must be set to &#39;feature&#39; | 
 **q** | **String**| The search term. | 
 **status** | **String**| A comma seperated list of status values to filter by, if required. Valid values: &#39;new&#39;, &#39;waiting&#39;, &#39;planned&#39;, &#39;developing&#39;, &#39;released&#39;, &#39;declined&#39;. | [optional] 
 **tags** | **String**| Tags to limit results by - only applies when scope is &#39;case&#39; or &#39;feature&#39;. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \&quot;....&amp;tags&#x3D;TagExample,Multi:TagThis,Multi:TagThat\&quot;. | [optional] 
 **products** | **String**| Products to limit results by. Comma delimeted string of either ids or names. E.g. \&quot;...&amp;products&#x3D;1,2,3\&quot; or \&quot;...products&#x3D;Product1,Product2\&quot;. | [optional] 

### Return type

[**[Feature]**](Feature.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

