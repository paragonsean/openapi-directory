# DevTestLabsClient.ArtifactSourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactSourceCreateOrUpdateResource**](ArtifactSourceApi.md#artifactSourceCreateOrUpdateResource) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 
[**artifactSourceDeleteResource**](ArtifactSourceApi.md#artifactSourceDeleteResource) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 
[**artifactSourceGetResource**](ArtifactSourceApi.md#artifactSourceGetResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 
[**artifactSourceList**](ArtifactSourceApi.md#artifactSourceList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources | 
[**artifactSourcePatchResource**](ArtifactSourceApi.md#artifactSourcePatchResource) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 



## artifactSourceCreateOrUpdateResource

> ArtifactSource artifactSourceCreateOrUpdateResource(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource)



Create or replace an existing artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourceApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let artifactSource = new DevTestLabsClient.ArtifactSource(); // ArtifactSource | 
apiInstance.artifactSourceCreateOrUpdateResource(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource, (error, data, response) => {
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
 **name** | **String**| The name of the artifact source. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **artifactSource** | [**ArtifactSource**](ArtifactSource.md)|  | 

### Return type

[**ArtifactSource**](ArtifactSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## artifactSourceDeleteResource

> artifactSourceDeleteResource(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourceApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
apiInstance.artifactSourceDeleteResource(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the artifact source. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## artifactSourceGetResource

> ArtifactSource artifactSourceGetResource(subscriptionId, resourceGroupName, labName, name, apiVersion)



Get artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourceApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
apiInstance.artifactSourceGetResource(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the artifact source. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]

### Return type

[**ArtifactSource**](ArtifactSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## artifactSourceList

> ResponseWithContinuationArtifactSource artifactSourceList(subscriptionId, resourceGroupName, labName, apiVersion, opts)



List artifact sources.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourceApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'orderBy': "orderBy_example" // String | 
};
apiInstance.artifactSourceList(subscriptionId, resourceGroupName, labName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **orderBy** | **String**|  | [optional] 

### Return type

[**ResponseWithContinuationArtifactSource**](ResponseWithContinuationArtifactSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## artifactSourcePatchResource

> ArtifactSource artifactSourcePatchResource(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource)



Modify properties of artifact sources.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourceApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let artifactSource = new DevTestLabsClient.ArtifactSource(); // ArtifactSource | 
apiInstance.artifactSourcePatchResource(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource, (error, data, response) => {
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
 **name** | **String**| The name of the artifact source. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **artifactSource** | [**ArtifactSource**](ArtifactSource.md)|  | 

### Return type

[**ArtifactSource**](ArtifactSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

