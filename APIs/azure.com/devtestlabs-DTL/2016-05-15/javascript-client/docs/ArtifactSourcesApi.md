# DevTestLabsClient.ArtifactSourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactSourcesCreateOrUpdate**](ArtifactSourcesApi.md#artifactSourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 
[**artifactSourcesDelete**](ArtifactSourcesApi.md#artifactSourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 
[**artifactSourcesGet**](ArtifactSourcesApi.md#artifactSourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 
[**artifactSourcesList**](ArtifactSourcesApi.md#artifactSourcesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources | 
[**artifactSourcesUpdate**](ArtifactSourcesApi.md#artifactSourcesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name} | 



## artifactSourcesCreateOrUpdate

> ArtifactSource artifactSourcesCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource)



Create or replace an existing artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let artifactSource = new DevTestLabsClient.ArtifactSource(); // ArtifactSource | Properties of an artifact source.
apiInstance.artifactSourcesCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **artifactSource** | [**ArtifactSource**](ArtifactSource.md)| Properties of an artifact source. | 

### Return type

[**ArtifactSource**](ArtifactSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactSourcesDelete

> artifactSourcesDelete(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2016-05-15'"; // String | Client API version.
apiInstance.artifactSourcesDelete(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactSourcesGet

> ArtifactSource artifactSourcesGet(subscriptionId, resourceGroupName, labName, name, apiVersion, opts)



Get artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=displayName)'
};
apiInstance.artifactSourcesGet(subscriptionId, resourceGroupName, labName, name, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39; | [optional] 

### Return type

[**ArtifactSource**](ArtifactSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactSourcesList

> ResponseWithContinuationArtifactSource artifactSourcesList(subscriptionId, resourceGroupName, labName, apiVersion, opts)



List artifact sources in a given lab.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=displayName)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.artifactSourcesList(subscriptionId, resourceGroupName, labName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationArtifactSource**](ResponseWithContinuationArtifactSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactSourcesUpdate

> ArtifactSource artifactSourcesUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource)



Modify properties of artifact sources.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArtifactSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the artifact source.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let artifactSource = new DevTestLabsClient.ArtifactSourceFragment(); // ArtifactSourceFragment | Properties of an artifact source.
apiInstance.artifactSourcesUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, artifactSource, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **artifactSource** | [**ArtifactSourceFragment**](ArtifactSourceFragment.md)| Properties of an artifact source. | 

### Return type

[**ArtifactSource**](ArtifactSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

