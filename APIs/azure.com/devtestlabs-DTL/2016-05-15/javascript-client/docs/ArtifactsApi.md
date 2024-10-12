# DevTestLabsClient.ArtifactsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactsGenerateArmTemplate**](ArtifactsApi.md#artifactsGenerateArmTemplate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name}/generateArmTemplate | 
[**artifactsGet**](ArtifactsApi.md#artifactsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name} | 
[**artifactsList**](ArtifactsApi.md#artifactsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts | 



## artifactsGenerateArmTemplate

> ArmTemplateInfo artifactsGenerateArmTemplate(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, generateArmTemplateRequest)



Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let name = "name_example"; // String | The name of the artifact.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let generateArmTemplateRequest = new DevTestLabsClient.GenerateArmTemplateRequest(); // GenerateArmTemplateRequest | Parameters for generating an ARM template for deploying artifacts.
apiInstance.artifactsGenerateArmTemplate(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, generateArmTemplateRequest, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **generateArmTemplateRequest** | [**GenerateArmTemplateRequest**](GenerateArmTemplateRequest.md)| Parameters for generating an ARM template for deploying artifacts. | 

### Return type

[**ArmTemplateInfo**](ArmTemplateInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsGet

> Artifact artifactsGet(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, opts)



Get artifact.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let name = "name_example"; // String | The name of the artifact.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=title)'
};
apiInstance.artifactsGet(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;title)&#39; | [optional] 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsList

> ResponseWithContinuationArtifact artifactsList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, opts)



List artifacts in a given artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=title)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.artifactsList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;title)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationArtifact**](ResponseWithContinuationArtifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

