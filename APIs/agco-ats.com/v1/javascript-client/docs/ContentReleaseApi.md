# AgcoApi.ContentReleaseApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2ContentReleasesContentReleaseIdGet**](ContentReleaseApi.md#apiV2ContentReleasesContentReleaseIdGet) | **GET** /api/v2/ContentReleases/{ContentReleaseId} | Get a Content Release Version by ID
[**contentReleaseDeleteContentReleaseVersionn**](ContentReleaseApi.md#contentReleaseDeleteContentReleaseVersionn) | **DELETE** /api/v2/ContentReleases/{ContentReleaseId} | Delete a ContentReleaseVersion
[**contentReleaseGetContentReleaseVersion**](ContentReleaseApi.md#contentReleaseGetContentReleaseVersion) | **GET** /api/v2/ContentReleases | Get ContentReleaseVersion
[**contentReleasePostContentRelease**](ContentReleaseApi.md#contentReleasePostContentRelease) | **POST** /api/v2/ContentReleases | Create a ContentReleaseVersion
[**contentReleasePutContentDefinition**](ContentReleaseApi.md#contentReleasePutContentDefinition) | **PUT** /api/v2/ContentReleases/{ContentReleaseId} | Update a ContentReleaseVersion



## apiV2ContentReleasesContentReleaseIdGet

> ContentSubmissionSharedBusinessEntitiesContentReleaseVersion apiV2ContentReleasesContentReleaseIdGet(contentReleaseId)

Get a Content Release Version by ID

Gets a ContentReleaseVersion by ID. When successful, the response is the requested ContentReleaseVersion.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentReleaseApi();
let contentReleaseId = 56; // Number | The ID of the ContentReleaseVersion to get.
apiInstance.apiV2ContentReleasesContentReleaseIdGet(contentReleaseId, (error, data, response) => {
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
 **contentReleaseId** | **Number**| The ID of the ContentReleaseVersion to get. | 

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## contentReleaseDeleteContentReleaseVersionn

> contentReleaseDeleteContentReleaseVersionn(contentReleaseId)

Delete a ContentReleaseVersion

Deletes an ContentReleaseVersion. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentReleaseApi();
let contentReleaseId = 56; // Number | The ID of the ContentReleaseVersion to delete
apiInstance.contentReleaseDeleteContentReleaseVersionn(contentReleaseId, (error, data, response) => {
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
 **contentReleaseId** | **Number**| The ID of the ContentReleaseVersion to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentReleaseGetContentReleaseVersion

> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion contentReleaseGetContentReleaseVersion(opts)

Get ContentReleaseVersion

Gets a collection of ContentReleaseVersion. When successful, the response is a PagedResponse of ContentReleaseVersion.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentReleaseApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'deleted': true, // Boolean | Optional. Filter by deleted.
  'releaseID': 56, // Number | Optional. Filter by releaseID.
  'userId': 56, // Number | Optional. Filter by UserID.
  'contentDefinitionID': 56, // Number | Optional. Filter by ContentDefinitionID.
  'version': 56 // Number | Optional. Filter by Version.
};
apiInstance.contentReleaseGetContentReleaseVersion(opts, (error, data, response) => {
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
 **deleted** | **Boolean**| Optional. Filter by deleted. | [optional] 
 **releaseID** | **Number**| Optional. Filter by releaseID. | [optional] 
 **userId** | **Number**| Optional. Filter by UserID. | [optional] 
 **contentDefinitionID** | **Number**| Optional. Filter by ContentDefinitionID. | [optional] 
 **version** | **Number**| Optional. Filter by Version. | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## contentReleasePostContentRelease

> Number contentReleasePostContentRelease(contentSubmissionSharedBusinessEntitiesContentReleaseVersion)

Create a ContentReleaseVersion

Creates a ContentReleaseVersion.  The body of the POST is the ContentReleaseVersion to create.              The ContentReleaseId will be assigned on creation of the Job.  When successful, the response              is the contentReleaseId.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentReleaseApi();
let contentSubmissionSharedBusinessEntitiesContentReleaseVersion = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentReleaseVersion(); // ContentSubmissionSharedBusinessEntitiesContentReleaseVersion | The ContentReleaseVersion to create.
apiInstance.contentReleasePostContentRelease(contentSubmissionSharedBusinessEntitiesContentReleaseVersion, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesContentReleaseVersion** | [**ContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)| The ContentReleaseVersion to create. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## contentReleasePutContentDefinition

> contentReleasePutContentDefinition(contentReleaseId, contentSubmissionSharedBusinessEntitiesContentReleaseVersion)

Update a ContentReleaseVersion

Updates a ContentReleaseVersion.  The body of the PUT is the updated ContentReleaseVersion.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentReleaseApi();
let contentReleaseId = 56; // Number | The ID of the ContentReleaseVersion to update
let contentSubmissionSharedBusinessEntitiesContentReleaseVersion = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentReleaseVersion(); // ContentSubmissionSharedBusinessEntitiesContentReleaseVersion | The updated ContentReleaseVersion
apiInstance.contentReleasePutContentDefinition(contentReleaseId, contentSubmissionSharedBusinessEntitiesContentReleaseVersion, (error, data, response) => {
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
 **contentReleaseId** | **Number**| The ID of the ContentReleaseVersion to update | 
 **contentSubmissionSharedBusinessEntitiesContentReleaseVersion** | [**ContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)| The updated ContentReleaseVersion | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

