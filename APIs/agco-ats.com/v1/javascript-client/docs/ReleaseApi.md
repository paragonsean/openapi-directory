# AgcoApi.ReleaseApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**releaseDeleteReleaseBundle**](ReleaseApi.md#releaseDeleteReleaseBundle) | **DELETE** /api/v2/Releases/{ReleaseId}/Bundle/{BundleId} | Deletes the association between a release and a bundle.
[**releaseGetRelease**](ReleaseApi.md#releaseGetRelease) | **GET** /api/v2/Releases/{ReleaseId} | Get a  Release by ID
[**releaseGetReleases**](ReleaseApi.md#releaseGetReleases) | **GET** /api/v2/Releases | Get Release
[**releasePostRelease**](ReleaseApi.md#releasePostRelease) | **POST** /api/v2/Releases | Create a Release
[**releasePostReleaseBundle**](ReleaseApi.md#releasePostReleaseBundle) | **POST** /api/v2/Releases/{ReleaseId}/Bundle/{BundleId} | Associates the release with a bundle.
[**releasePutContentDefinition**](ReleaseApi.md#releasePutContentDefinition) | **PUT** /api/v2/Releases/{releaseId} | Update a Release



## releaseDeleteReleaseBundle

> releaseDeleteReleaseBundle(releaseId, bundleId)

Deletes the association between a release and a bundle.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReleaseApi();
let releaseId = 56; // Number | The release identifier.
let bundleId = "bundleId_example"; // String | The bundle identifier.
apiInstance.releaseDeleteReleaseBundle(releaseId, bundleId, (error, data, response) => {
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
 **releaseId** | **Number**| The release identifier. | 
 **bundleId** | **String**| The bundle identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## releaseGetRelease

> ContentSubmissionSharedBusinessEntitiesRelease releaseGetRelease(releaseId)

Get a  Release by ID

Gets a Release by ID. When successful, the response is the requested Release.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReleaseApi();
let releaseId = 56; // Number | The ID of the Release to get.
apiInstance.releaseGetRelease(releaseId, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the Release to get. | 

### Return type

[**ContentSubmissionSharedBusinessEntitiesRelease**](ContentSubmissionSharedBusinessEntitiesRelease.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## releaseGetReleases

> APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease releaseGetReleases(opts)

Get Release

Gets a collection of Release. When successful, the response is a PagedResponse of Release.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReleaseApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'visible': true, // Boolean | Optional. Filter by visible.
  'bundleID': "bundleID_example" // String | Optional. Filter by BundleID.
};
apiInstance.releaseGetReleases(opts, (error, data, response) => {
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
 **visible** | **Boolean**| Optional. Filter by visible. | [optional] 
 **bundleID** | **String**| Optional. Filter by BundleID. | [optional] 

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease**](APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## releasePostRelease

> Number releasePostRelease(contentSubmissionSharedBusinessEntitiesRelease)

Create a Release

Creates a Release.  The body of the POST is the Release to create.              The ReleaseId will be assigned on creation of the Job.  When successful, the response              is the Release Id.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReleaseApi();
let contentSubmissionSharedBusinessEntitiesRelease = new AgcoApi.ContentSubmissionSharedBusinessEntitiesRelease(); // ContentSubmissionSharedBusinessEntitiesRelease | The Release to create.
apiInstance.releasePostRelease(contentSubmissionSharedBusinessEntitiesRelease, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesRelease** | [**ContentSubmissionSharedBusinessEntitiesRelease**](ContentSubmissionSharedBusinessEntitiesRelease.md)| The Release to create. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## releasePostReleaseBundle

> releasePostReleaseBundle(releaseId, bundleId)

Associates the release with a bundle.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReleaseApi();
let releaseId = 56; // Number | The release identifier.
let bundleId = "bundleId_example"; // String | The bundle identifier.
apiInstance.releasePostReleaseBundle(releaseId, bundleId, (error, data, response) => {
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
 **releaseId** | **Number**| The release identifier. | 
 **bundleId** | **String**| The bundle identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## releasePutContentDefinition

> releasePutContentDefinition(releaseId, contentSubmissionSharedBusinessEntitiesRelease)

Update a Release

Updates a Release.  The body of the PUT is the updated Release.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReleaseApi();
let releaseId = 56; // Number | The ID of the Release to update
let contentSubmissionSharedBusinessEntitiesRelease = new AgcoApi.ContentSubmissionSharedBusinessEntitiesRelease(); // ContentSubmissionSharedBusinessEntitiesRelease | The updated Release
apiInstance.releasePutContentDefinition(releaseId, contentSubmissionSharedBusinessEntitiesRelease, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the Release to update | 
 **contentSubmissionSharedBusinessEntitiesRelease** | [**ContentSubmissionSharedBusinessEntitiesRelease**](ContentSubmissionSharedBusinessEntitiesRelease.md)| The updated Release | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

