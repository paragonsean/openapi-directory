# DevTestLabsClient.SecretsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secretsCreateOrUpdate**](SecretsApi.md#secretsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} | 
[**secretsDelete**](SecretsApi.md#secretsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} | 
[**secretsGet**](SecretsApi.md#secretsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} | 
[**secretsList**](SecretsApi.md#secretsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets | 
[**secretsUpdate**](SecretsApi.md#secretsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} | 



## secretsCreateOrUpdate

> Secret secretsCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret)



Create or replace an existing secret. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the secret.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let secret = new DevTestLabsClient.Secret(); // Secret | A secret.
apiInstance.secretsCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret, (error, data, response) => {
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
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **secret** | [**Secret**](Secret.md)| A secret. | 

### Return type

[**Secret**](Secret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsDelete

> secretsDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Delete secret.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the secret.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.secretsDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, (error, data, response) => {
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
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsGet

> Secret secretsGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, opts)



Get secret.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the secret.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=value)'
};
apiInstance.secretsGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, opts, (error, data, response) => {
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
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;value)&#39; | [optional] 

### Return type

[**Secret**](Secret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsList

> SecretList secretsList(subscriptionId, resourceGroupName, labName, userName, apiVersion, opts)



List secrets in a given user profile.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=value)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.secretsList(subscriptionId, resourceGroupName, labName, userName, apiVersion, opts, (error, data, response) => {
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
 **userName** | **String**| The name of the user profile. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;value)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] 

### Return type

[**SecretList**](SecretList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsUpdate

> Secret secretsUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret)



Allows modifying tags of secrets. All other properties will be ignored.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the secret.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let secret = new DevTestLabsClient.SecretFragment(); // SecretFragment | A secret.
apiInstance.secretsUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret, (error, data, response) => {
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
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **secret** | [**SecretFragment**](SecretFragment.md)| A secret. | 

### Return type

[**Secret**](Secret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

