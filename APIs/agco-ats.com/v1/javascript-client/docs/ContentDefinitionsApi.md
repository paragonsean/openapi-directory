# AgcoApi.ContentDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentDefinitionsDeleteContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsDeleteContentDefinition) | **DELETE** /api/v2/ContentDefinitions/{contentDefinitionID} | Delete a ContentDefinition
[**contentDefinitionsDeleteContentDefinitionAttribute**](ContentDefinitionsApi.md#contentDefinitionsDeleteContentDefinitionAttribute) | **DELETE** /api/v2/ContentDefinitionAttributes/{contentDefinitionAttributeID} | Remove an Attribute from a ContentDefinition
[**contentDefinitionsGetContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsGetContentDefinition) | **GET** /api/v2/ContentDefinitions/{contentDefinitionID} | Get a ContentDefinition by ID
[**contentDefinitionsGetContentDefinitionAttributes**](ContentDefinitionsApi.md#contentDefinitionsGetContentDefinitionAttributes) | **GET** /api/v2/ContentDefinitions/{contentDefinitionID}/Attributes | Get Attributes for a ContentDefinition
[**contentDefinitionsGetContentDefinitions**](ContentDefinitionsApi.md#contentDefinitionsGetContentDefinitions) | **GET** /api/v2/ContentDefinitions | Get ContentDefinitions
[**contentDefinitionsPostContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsPostContentDefinition) | **POST** /api/v2/ContentDefinitions | Create a ContentDefinition
[**contentDefinitionsPostContentDefinitionAttribute**](ContentDefinitionsApi.md#contentDefinitionsPostContentDefinitionAttribute) | **POST** /api/v2/ContentDefinitions/{contentDefinitionID}/Attributes | Add an Attribute to a ContentDefinition
[**contentDefinitionsPostContentDefinitionAttributes**](ContentDefinitionsApi.md#contentDefinitionsPostContentDefinitionAttributes) | **POST** /api/v2/ContentDefinitions/{contentDefinitionID}/Attributes/Batch | No Documentation Found.
[**contentDefinitionsPutContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsPutContentDefinition) | **PUT** /api/v2/ContentDefinitions/{contentDefinitionID} | Update a ContentDefinition
[**contentDefinitionsPutContentDefinitionAttributeAsync**](ContentDefinitionsApi.md#contentDefinitionsPutContentDefinitionAttributeAsync) | **PUT** /api/v2/ContentDefinitionAttributes/{contentDefinitionAttributeID} | Update an Attribute for a ContentDefinition
[**contentDefinitionsPutContentDefinitionAttributes**](ContentDefinitionsApi.md#contentDefinitionsPutContentDefinitionAttributes) | **PUT** /api/v2/ContentDefinitionAttributes/Batch | No Documentation Found.



## contentDefinitionsDeleteContentDefinition

> contentDefinitionsDeleteContentDefinition(contentDefinitionID)

Delete a ContentDefinition

Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionID = 56; // Number | The ID of the ContentDefinition to delete
apiInstance.contentDefinitionsDeleteContentDefinition(contentDefinitionID, (error, data, response) => {
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
 **contentDefinitionID** | **Number**| The ID of the ContentDefinition to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentDefinitionsDeleteContentDefinitionAttribute

> contentDefinitionsDeleteContentDefinitionAttribute(contentDefinitionAttributeID)

Remove an Attribute from a ContentDefinition

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionAttributeID = 56; // Number | The ID of the Attribute to remove.
apiInstance.contentDefinitionsDeleteContentDefinitionAttribute(contentDefinitionAttributeID, (error, data, response) => {
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
 **contentDefinitionAttributeID** | **Number**| The ID of the Attribute to remove. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentDefinitionsGetContentDefinition

> ContentSubmissionSharedBusinessEntitiesContentDefinition contentDefinitionsGetContentDefinition(contentDefinitionID, opts)

Get a ContentDefinition by ID

Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionID = 56; // Number | The ID of the ContentDefinition to get.
let opts = {
  'includeAttributes': "includeAttributes_example" // String | Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
};
apiInstance.contentDefinitionsGetContentDefinition(contentDefinitionID, opts, (error, data, response) => {
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
 **contentDefinitionID** | **Number**| The ID of the ContentDefinition to get. | 
 **includeAttributes** | **String**| Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] 

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## contentDefinitionsGetContentDefinitionAttributes

> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute contentDefinitionsGetContentDefinitionAttributes(contentDefinitionID, opts)

Get Attributes for a ContentDefinition

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionID = 56; // Number | The ID of the ContentDefinition.
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'name': "name_example" // String | Optional. Filter the attributes by Name.
};
apiInstance.contentDefinitionsGetContentDefinitionAttributes(contentDefinitionID, opts, (error, data, response) => {
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
 **contentDefinitionID** | **Number**| The ID of the ContentDefinition. | 
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **name** | **String**| Optional. Filter the attributes by Name. | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## contentDefinitionsGetContentDefinitions

> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition contentDefinitionsGetContentDefinitions(opts)

Get ContentDefinitions

Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'userID': 56, // Number | Optional. Filter by UserID.
  'includeAttributes': "includeAttributes_example", // String | Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
  'name': "name_example", // String | Optional. Filter by Name. Supports beginning and ending wildcard (*).
  'typeID': 56, // Number | Optional. Filter by TypeID.
  'packageTypeID': "packageTypeID_example" // String | Optional. Filter by PackageTypeID.
};
apiInstance.contentDefinitionsGetContentDefinitions(opts, (error, data, response) => {
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
 **includeAttributes** | **String**| Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] 
 **name** | **String**| Optional. Filter by Name. Supports beginning and ending wildcard (*). | [optional] 
 **typeID** | **Number**| Optional. Filter by TypeID. | [optional] 
 **packageTypeID** | **String**| Optional. Filter by PackageTypeID. | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## contentDefinitionsPostContentDefinition

> Number contentDefinitionsPostContentDefinition(contentSubmissionSharedBusinessEntitiesContentDefinition)

Create a ContentDefinition

Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.              The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the JobID.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentSubmissionSharedBusinessEntitiesContentDefinition = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinition(); // ContentSubmissionSharedBusinessEntitiesContentDefinition | The ContentDefinition to create.
apiInstance.contentDefinitionsPostContentDefinition(contentSubmissionSharedBusinessEntitiesContentDefinition, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesContentDefinition** | [**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md)| The ContentDefinition to create. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## contentDefinitionsPostContentDefinitionAttribute

> Number contentDefinitionsPostContentDefinitionAttribute(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

Add an Attribute to a ContentDefinition

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionID = 56; // Number | The ID of the ContentDefinition
let contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute | The Attribute to add.
apiInstance.contentDefinitionsPostContentDefinitionAttribute(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, (error, data, response) => {
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
 **contentDefinitionID** | **Number**| The ID of the ContentDefinition | 
 **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)| The Attribute to add. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## contentDefinitionsPostContentDefinitionAttributes

> contentDefinitionsPostContentDefinitionAttributes(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionID = 56; // Number | 
let contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = [new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute()]; // [ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute] | 
apiInstance.contentDefinitionsPostContentDefinitionAttributes(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, (error, data, response) => {
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
 **contentDefinitionID** | **Number**|  | 
 **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## contentDefinitionsPutContentDefinition

> contentDefinitionsPutContentDefinition(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinition)

Update a ContentDefinition

Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionID = 56; // Number | The ID of the ContentDefinition to update
let contentSubmissionSharedBusinessEntitiesContentDefinition = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinition(); // ContentSubmissionSharedBusinessEntitiesContentDefinition | The updated ContentDefinition
apiInstance.contentDefinitionsPutContentDefinition(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinition, (error, data, response) => {
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
 **contentDefinitionID** | **Number**| The ID of the ContentDefinition to update | 
 **contentSubmissionSharedBusinessEntitiesContentDefinition** | [**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md)| The updated ContentDefinition | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## contentDefinitionsPutContentDefinitionAttributeAsync

> contentDefinitionsPutContentDefinitionAttributeAsync(contentDefinitionAttributeID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

Update an Attribute for a ContentDefinition

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentDefinitionAttributeID = 56; // Number | The ID of the Attribute to update.
let contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute | The Attribute to update.
apiInstance.contentDefinitionsPutContentDefinitionAttributeAsync(contentDefinitionAttributeID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, (error, data, response) => {
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
 **contentDefinitionAttributeID** | **Number**| The ID of the Attribute to update. | 
 **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)| The Attribute to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## contentDefinitionsPutContentDefinitionAttributes

> contentDefinitionsPutContentDefinitionAttributes(contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentDefinitionsApi();
let contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = [new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute()]; // [ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute] | 
apiInstance.contentDefinitionsPutContentDefinitionAttributes(contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

