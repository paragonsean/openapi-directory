# DevTestLabsClient.ArmTemplatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**armTemplatesGet**](ArmTemplatesApi.md#armTemplatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/armtemplates/{name} | 
[**armTemplatesList**](ArmTemplatesApi.md#armTemplatesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/armtemplates | 



## armTemplatesGet

> ArmTemplate armTemplatesGet(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, opts)



Get azure resource manager template.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArmTemplatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let name = "name_example"; // String | The name of the azure resource manager template.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=displayName)'
};
apiInstance.armTemplatesGet(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| The name of the azure resource manager template. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39; | [optional] 

### Return type

[**ArmTemplate**](ArmTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## armTemplatesList

> ArmTemplateList armTemplatesList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, opts)



List azure resource manager templates in a given artifact source.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ArmTemplatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=displayName)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.armTemplatesList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] 

### Return type

[**ArmTemplateList**](ArmTemplateList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

