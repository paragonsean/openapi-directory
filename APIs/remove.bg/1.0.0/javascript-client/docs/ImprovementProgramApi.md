# BackgroundRemovalApi.ImprovementProgramApi

All URIs are relative to *https://api.remove.bg/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**improvePost**](ImprovementProgramApi.md#improvePost) | **POST** /improve | 



## improvePost

> ImprovementProgramJsonResponse improvePost(improvementProgramJson)



Submit an image to the remove.bg Improvement program * Contribute an image that remove.bg is currently not able to remove the background from properly * Help us make remove.bg better * Get better results for similiar images in the future  Notes:   * By submitting images through the API you agree to the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener\&quot; href&#x3D;\&quot;/ipc\&quot;&gt;Improvement Program Conditions&lt;/a&gt;   * File size: up to 12MB   * up to 100 files per day. &lt;br&gt; Higher Rate Limits are available for Enterprise customers &lt;a href&#x3D;\&quot;/support/contact?subject&#x3D;Improvement+Program+Rate+Limit\&quot;&gt;upon request&lt;/a&gt;.  Requires either an API Key to be provided in the &#x60;X-API-Key&#x60; request header or an OAuth 2.0 access token to be provided in the &#x60;Authorization&#x60; request header.  Please note that submissions are used on a best-effort basis and the extent of expected improvement varies depending on many factors, including the number of provided images, their complexity and visual similarity. Improvements usually take several weeks to become effective. 

### Example

```javascript
import BackgroundRemovalApi from 'background_removal_api';
let defaultClient = BackgroundRemovalApi.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new BackgroundRemovalApi.ImprovementProgramApi();
let improvementProgramJson = new BackgroundRemovalApi.ImprovementProgramJson(); // ImprovementProgramJson | 
apiInstance.improvePost(improvementProgramJson, (error, data, response) => {
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
 **improvementProgramJson** | [**ImprovementProgramJson**](ImprovementProgramJson.md)|  | 

### Return type

[**ImprovementProgramJsonResponse**](ImprovementProgramJsonResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: */*

