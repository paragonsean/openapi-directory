# DevTestLabsClient.ArtifactApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactGenerateArmTemplate**](ArtifactApi.md#artifactGenerateArmTemplate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name}/generateArmTemplate | 
[**artifactGetResource**](ArtifactApi.md#artifactGetResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name} | 
[**artifactList**](ArtifactApi.md#artifactList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts | 



## artifactGenerateArmTemplate

> ArmTemplateInfo artifactGenerateArmTemplate(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, generateArmTemplateRequest)



Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let name = "name_example"; // String | The name of the artifact.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let generateArmTemplateRequest = new DevTestLabsClient.GenerateArmTemplateRequest(); // GenerateArmTemplateRequest | 
apiInstance.artifactGenerateArmTemplate(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, generateArmTemplateRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **artifactSourceName** | **String**| The name of the artifact source. | 
 **name** | **String**| The name of the artifact. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **generateArmTemplateRequest** | [**GenerateArmTemplateRequest**](GenerateArmTemplateRequest.md)|  | 

### Return type

[**ArmTemplateInfo**](ArmTemplateInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## artifactGetResource

> Artifact artifactGetResource(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion)



Get artifact.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let name = "name_example"; // String | The name of the artifact.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
apiInstance.artifactGetResource(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **artifactSourceName** | **String**| The name of the artifact source. | 
 **name** | **String**| The name of the artifact. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]

### Return type

[**Artifact**](Artifact.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## artifactList

> ResponseWithContinuationArtifact artifactList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, opts)



List artifacts.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'orderBy': "orderBy_example" // String | 
};
apiInstance.artifactList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **artifactSourceName** | **String**| The name of the artifact source. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **orderBy** | **String**|  | [optional] 

### Return type

[**ResponseWithContinuationArtifact**](ResponseWithContinuationArtifact.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

