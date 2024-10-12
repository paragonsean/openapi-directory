# CustomVisionTrainingClient.ImageRegionProposalApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getImageRegionProposals**](ImageRegionProposalApiApi.md#getImageRegionProposals) | **POST** /projects/{projectId}/images/{imageId}/regionproposals | Get region proposals for an image. Returns empty array if no proposals are found.



## getImageRegionProposals

> ImageRegionProposal getImageRegionProposals(projectId, imageId)

Get region proposals for an image. Returns empty array if no proposals are found.

This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ImageRegionProposalApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let imageId = "4d6eb844-42ee-42bc-bd6f-c32455ef07c9"; // String | The image id.
apiInstance.getImageRegionProposals(projectId, imageId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **imageId** | **String**| The image id. | 

### Return type

[**ImageRegionProposal**](ImageRegionProposal.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

