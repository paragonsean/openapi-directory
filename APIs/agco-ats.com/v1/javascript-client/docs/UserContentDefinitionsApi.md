# AgcoApi.UserContentDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userContentDefinitionsDeleteUserContentDefinition**](UserContentDefinitionsApi.md#userContentDefinitionsDeleteUserContentDefinition) | **DELETE** /api/v2/UserContentDefinitions/{userContentDefinitionID} | Delete a UserContentDefinition
[**userContentDefinitionsGetUserContentDefinition**](UserContentDefinitionsApi.md#userContentDefinitionsGetUserContentDefinition) | **GET** /api/v2/UserContentDefinitions/{userContentDefinitionID} | Get a UserContentDefinition by ID
[**userContentDefinitionsGetUserContentDefinitions**](UserContentDefinitionsApi.md#userContentDefinitionsGetUserContentDefinitions) | **GET** /api/v2/UserContentDefinitions | Get UserContentDefinitions
[**userContentDefinitionsPostUserContentDefinition**](UserContentDefinitionsApi.md#userContentDefinitionsPostUserContentDefinition) | **POST** /api/v2/UserContentDefinitions | Create a UserContentDefinition



## userContentDefinitionsDeleteUserContentDefinition

> userContentDefinitionsDeleteUserContentDefinition(userContentDefinitionID)

Delete a UserContentDefinition

Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserContentDefinitionsApi();
let userContentDefinitionID = 56; // Number | The ID of the UserContentDefinition to delete
apiInstance.userContentDefinitionsDeleteUserContentDefinition(userContentDefinitionID, (error, data, response) => {
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
 **userContentDefinitionID** | **Number**| The ID of the UserContentDefinition to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userContentDefinitionsGetUserContentDefinition

> ContentSubmissionSharedBusinessEntitiesUserContentDefinition userContentDefinitionsGetUserContentDefinition(userContentDefinitionID)

Get a UserContentDefinition by ID

Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserContentDefinitionsApi();
let userContentDefinitionID = 56; // Number | The ID of the UserContentDefinition to get.
apiInstance.userContentDefinitionsGetUserContentDefinition(userContentDefinitionID, (error, data, response) => {
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
 **userContentDefinitionID** | **Number**| The ID of the UserContentDefinition to get. | 

### Return type

[**ContentSubmissionSharedBusinessEntitiesUserContentDefinition**](ContentSubmissionSharedBusinessEntitiesUserContentDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## userContentDefinitionsGetUserContentDefinitions

> APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition userContentDefinitionsGetUserContentDefinitions(opts)

Get UserContentDefinitions

Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserContentDefinitionsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'userID': 56, // Number | Optional. Filter by UserID.
  'contentDefinitionID': 56 // Number | Optional. Filter by ContentDefinitionID
};
apiInstance.userContentDefinitionsGetUserContentDefinitions(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **userID** | **Number**| Optional. Filter by UserID. | [optional] 
 **contentDefinitionID** | **Number**| Optional. Filter by ContentDefinitionID | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition**](APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## userContentDefinitionsPostUserContentDefinition

> Number userContentDefinitionsPostUserContentDefinition(contentSubmissionSharedBusinessEntitiesUserContentDefinition)

Create a UserContentDefinition

Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.              The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserContentDefinitionsApi();
let contentSubmissionSharedBusinessEntitiesUserContentDefinition = new AgcoApi.ContentSubmissionSharedBusinessEntitiesUserContentDefinition(); // ContentSubmissionSharedBusinessEntitiesUserContentDefinition | The UserContentDefinition to create.
apiInstance.userContentDefinitionsPostUserContentDefinition(contentSubmissionSharedBusinessEntitiesUserContentDefinition, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesUserContentDefinition** | [**ContentSubmissionSharedBusinessEntitiesUserContentDefinition**](ContentSubmissionSharedBusinessEntitiesUserContentDefinition.md)| The UserContentDefinition to create. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

