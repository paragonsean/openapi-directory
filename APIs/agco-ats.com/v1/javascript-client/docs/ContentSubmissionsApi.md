# AgcoApi.ContentSubmissionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentSubmissionsDeleteContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsDeleteContentSubmission) | **DELETE** /api/v2/ContentSubmissions/{contentSubmissionID} | Delete a ContentSubmission
[**contentSubmissionsDeleteContentSubmissionAttribute**](ContentSubmissionsApi.md#contentSubmissionsDeleteContentSubmissionAttribute) | **DELETE** /api/v2/ContentSubmissionAttributes/{contentSubmissionAttributeID} | Remove an Attribute from a ContentSubmission
[**contentSubmissionsGetContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmission) | **GET** /api/v2/ContentSubmissions/{contentSubmissionID} | Get a ContentSubmission by ID
[**contentSubmissionsGetContentSubmissionAttributes**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmissionAttributes) | **GET** /api/v2/ContentSubmissions/{contentSubmissionID}/Attributes | Get Attributes for a ContentSubmission
[**contentSubmissionsGetContentSubmissionStatus**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmissionStatus) | **GET** /api/v2/ContentSubmissions/{contentSubmissionID}/Status | Get the status of a ContentSubmission
[**contentSubmissionsGetContentSubmissions**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmissions) | **GET** /api/v2/ContentSubmissions | Get ContentSubmissions
[**contentSubmissionsPostContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsPostContentSubmission) | **POST** /api/v2/ContentSubmissions | Create a ContentSubmission
[**contentSubmissionsPostContentSubmissionAttribute**](ContentSubmissionsApi.md#contentSubmissionsPostContentSubmissionAttribute) | **POST** /api/v2/ContentSubmissions/{contentSubmissionID}/Attributes | Add an Attribute to a ContentSubmission
[**contentSubmissionsPostContentSubmissionAttributes**](ContentSubmissionsApi.md#contentSubmissionsPostContentSubmissionAttributes) | **POST** /api/v2/ContentSubmissions/{contentSubmissionID}/Attributes/Batch | No Documentation Found.
[**contentSubmissionsPutContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsPutContentSubmission) | **PUT** /api/v2/ContentSubmissions/{contentSubmissionID} | Update a ContentSubmission
[**contentSubmissionsPutContentSubmissionAttributeAsync**](ContentSubmissionsApi.md#contentSubmissionsPutContentSubmissionAttributeAsync) | **PUT** /api/v2/ContentSubmissionAttributes/{contentSubmissionAttributeID} | Update an Attribute for a ContentSubmission
[**contentSubmissionsPutContentSubmissionAttributes**](ContentSubmissionsApi.md#contentSubmissionsPutContentSubmissionAttributes) | **PUT** /api/v2/ContentSubmissionAttributes/Batch | No Documentation Found.



## contentSubmissionsDeleteContentSubmission

> contentSubmissionsDeleteContentSubmission(contentSubmissionID)

Delete a ContentSubmission

Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | The ID of the ContentSubmission to delete
apiInstance.contentSubmissionsDeleteContentSubmission(contentSubmissionID, (error, data, response) => {
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
 **contentSubmissionID** | **Number**| The ID of the ContentSubmission to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentSubmissionsDeleteContentSubmissionAttribute

> contentSubmissionsDeleteContentSubmissionAttribute(contentSubmissionAttributeID)

Remove an Attribute from a ContentSubmission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionAttributeID = 56; // Number | The ID of the Attribute to remove.
apiInstance.contentSubmissionsDeleteContentSubmissionAttribute(contentSubmissionAttributeID, (error, data, response) => {
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
 **contentSubmissionAttributeID** | **Number**| The ID of the Attribute to remove. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentSubmissionsGetContentSubmission

> ContentSubmissionSharedBusinessEntitiesContentSubmission contentSubmissionsGetContentSubmission(contentSubmissionID, opts)

Get a ContentSubmission by ID

Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | The ID of the ContentSubmission to get.
let opts = {
  'includeAttributes': "includeAttributes_example" // String | Names of Attributes to include when retrieving this submission. This should be a comma-separated list.
};
apiInstance.contentSubmissionsGetContentSubmission(contentSubmissionID, opts, (error, data, response) => {
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
 **contentSubmissionID** | **Number**| The ID of the ContentSubmission to get. | 
 **includeAttributes** | **String**| Names of Attributes to include when retrieving this submission. This should be a comma-separated list. | [optional] 

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentSubmission**](ContentSubmissionSharedBusinessEntitiesContentSubmission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionsGetContentSubmissionAttributes

> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute contentSubmissionsGetContentSubmissionAttributes(contentSubmissionID, opts)

Get Attributes for a ContentSubmission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | The ID of the ContentSubmission.
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'name': "name_example" // String | Optional. Filter the attributes by Name.
};
apiInstance.contentSubmissionsGetContentSubmissionAttributes(contentSubmissionID, opts, (error, data, response) => {
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
 **contentSubmissionID** | **Number**| The ID of the ContentSubmission. | 
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **name** | **String**| Optional. Filter the attributes by Name. | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## contentSubmissionsGetContentSubmissionStatus

> BuildSystemSharedInterfacesIJobRun contentSubmissionsGetContentSubmissionStatus(contentSubmissionID, opts)

Get the status of a ContentSubmission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | The ID of the ContentSubmission to get.
let opts = {
  'includeActivityRunDetails': true // Boolean | True to include all status details if JobRun. Defaults to false
};
apiInstance.contentSubmissionsGetContentSubmissionStatus(contentSubmissionID, opts, (error, data, response) => {
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
 **contentSubmissionID** | **Number**| The ID of the ContentSubmission to get. | 
 **includeActivityRunDetails** | **Boolean**| True to include all status details if JobRun. Defaults to false | [optional] 

### Return type

[**BuildSystemSharedInterfacesIJobRun**](BuildSystemSharedInterfacesIJobRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionsGetContentSubmissions

> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission contentSubmissionsGetContentSubmissions(opts)

Get ContentSubmissions

Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]&#x3D;Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'userID': 56, // Number | Optional. Filter by UserID.
  'contentDefinitionID': 56, // Number | Optional. Filter by ContentDefinitionID
  'includeAttributes': "includeAttributes_example", // String | Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
  'releaseID': 56, // Number | Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.
  'typeID': 56, // Number | Optional. Filter submissions by their ContentDefinition's Type ID.
  'version': 56, // Number | Optional. Filter submissions by their Version.
  'includeDefinition': true // Boolean | Optional. If true, includes the ContentDefinition for each submission.
};
apiInstance.contentSubmissionsGetContentSubmissions(opts, (error, data, response) => {
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
 **includeAttributes** | **String**| Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] 
 **releaseID** | **Number**| Optional. Filter the submissions by whether they are part of the Release with the specified Release ID. | [optional] 
 **typeID** | **Number**| Optional. Filter submissions by their ContentDefinition&#39;s Type ID. | [optional] 
 **version** | **Number**| Optional. Filter submissions by their Version. | [optional] 
 **includeDefinition** | **Boolean**| Optional. If true, includes the ContentDefinition for each submission. | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## contentSubmissionsPostContentSubmission

> Number contentSubmissionsPostContentSubmission(contentSubmissionSharedBusinessEntitiesContentSubmission)

Create a ContentSubmission

Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.              The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response              is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionSharedBusinessEntitiesContentSubmission = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission(); // ContentSubmissionSharedBusinessEntitiesContentSubmission | The ContentSubmission to create.
apiInstance.contentSubmissionsPostContentSubmission(contentSubmissionSharedBusinessEntitiesContentSubmission, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesContentSubmission** | [**ContentSubmissionSharedBusinessEntitiesContentSubmission**](ContentSubmissionSharedBusinessEntitiesContentSubmission.md)| The ContentSubmission to create. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionsPostContentSubmissionAttribute

> Number contentSubmissionsPostContentSubmissionAttribute(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

Add an Attribute to a ContentSubmission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | The ID of the ContentSubmission
let contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute | The Attribute to add.
apiInstance.contentSubmissionsPostContentSubmissionAttribute(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute, (error, data, response) => {
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
 **contentSubmissionID** | **Number**| The ID of the ContentSubmission | 
 **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)| The Attribute to add. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionsPostContentSubmissionAttributes

> contentSubmissionsPostContentSubmissionAttributes(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | 
let contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = [new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute()]; // [ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute] | 
apiInstance.contentSubmissionsPostContentSubmissionAttributes(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute, (error, data, response) => {
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
 **contentSubmissionID** | **Number**|  | 
 **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## contentSubmissionsPutContentSubmission

> contentSubmissionsPutContentSubmission(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmission)

Update a ContentSubmission

Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionID = 56; // Number | The ID of the ContentSubmission to update
let contentSubmissionSharedBusinessEntitiesContentSubmission = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission(); // ContentSubmissionSharedBusinessEntitiesContentSubmission | The updated ContentSubmission
apiInstance.contentSubmissionsPutContentSubmission(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmission, (error, data, response) => {
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
 **contentSubmissionID** | **Number**| The ID of the ContentSubmission to update | 
 **contentSubmissionSharedBusinessEntitiesContentSubmission** | [**ContentSubmissionSharedBusinessEntitiesContentSubmission**](ContentSubmissionSharedBusinessEntitiesContentSubmission.md)| The updated ContentSubmission | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## contentSubmissionsPutContentSubmissionAttributeAsync

> contentSubmissionsPutContentSubmissionAttributeAsync(contentSubmissionAttributeID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

Update an Attribute for a ContentSubmission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionAttributeID = 56; // Number | The ID of the Attribute to update.
let contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute | The Attribute to update.
apiInstance.contentSubmissionsPutContentSubmissionAttributeAsync(contentSubmissionAttributeID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute, (error, data, response) => {
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
 **contentSubmissionAttributeID** | **Number**| The ID of the Attribute to update. | 
 **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)| The Attribute to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## contentSubmissionsPutContentSubmissionAttributes

> contentSubmissionsPutContentSubmissionAttributes(contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionsApi();
let contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = [new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute()]; // [ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute] | 
apiInstance.contentSubmissionsPutContentSubmissionAttributes(contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

