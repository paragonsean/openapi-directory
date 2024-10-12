# NotificationHubsManagementClient.NamespacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**namespacesCheckAvailability**](NamespacesApi.md#namespacesCheckAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.NotificationHubs/checkNamespaceAvailability | 
[**namespacesCreateOrUpdate**](NamespacesApi.md#namespacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName} | 
[**namespacesCreateOrUpdateAuthorizationRule**](NamespacesApi.md#namespacesCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} | 
[**namespacesDelete**](NamespacesApi.md#namespacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName} | 
[**namespacesDeleteAuthorizationRule**](NamespacesApi.md#namespacesDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} | 
[**namespacesGet**](NamespacesApi.md#namespacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName} | 
[**namespacesGetAuthorizationRule**](NamespacesApi.md#namespacesGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} | 
[**namespacesList**](NamespacesApi.md#namespacesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces | 
[**namespacesListAll**](NamespacesApi.md#namespacesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.NotificationHubs/namespaces | 
[**namespacesListAuthorizationRules**](NamespacesApi.md#namespacesListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/AuthorizationRules | 
[**namespacesListKeys**](NamespacesApi.md#namespacesListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName}/listKeys | 
[**namespacesPatch**](NamespacesApi.md#namespacesPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName} | 
[**namespacesRegenerateKeys**](NamespacesApi.md#namespacesRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName}/regenerateKeys | 



## namespacesCheckAvailability

> CheckAvailabilityResult namespacesCheckAvailability(apiVersion, subscriptionId, parameters)



Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.CheckAvailabilityParameters(); // CheckAvailabilityParameters | The namespace name.
apiInstance.namespacesCheckAvailability(apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**CheckAvailabilityParameters**](CheckAvailabilityParameters.md)| The namespace name. | 

### Return type

[**CheckAvailabilityResult**](CheckAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## namespacesCreateOrUpdate

> NamespaceResource namespacesCreateOrUpdate(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Creates/Updates a service namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.NamespaceCreateOrUpdateParameters(); // NamespaceCreateOrUpdateParameters | Parameters supplied to create a Namespace Resource.
apiInstance.namespacesCreateOrUpdate(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NamespaceCreateOrUpdateParameters**](NamespaceCreateOrUpdateParameters.md)| Parameters supplied to create a Namespace Resource. | 

### Return type

[**NamespaceResource**](NamespaceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## namespacesCreateOrUpdateAuthorizationRule

> SharedAccessAuthorizationRuleResource namespacesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates an authorization rule for a namespace

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let authorizationRuleName = "authorizationRuleName_example"; // String | Authorization Rule Name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access authorization rule.
apiInstance.namespacesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **authorizationRuleName** | **String**| Authorization Rule Name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access authorization rule. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## namespacesDelete

> namespacesDelete(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesDelete(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namespacesDeleteAuthorizationRule

> namespacesDeleteAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a namespace authorization rule

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let authorizationRuleName = "authorizationRuleName_example"; // String | Authorization Rule Name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesDeleteAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **authorizationRuleName** | **String**| Authorization Rule Name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namespacesGet

> NamespaceResource namespacesGet(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Returns the description for the specified namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesGet(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NamespaceResource**](NamespaceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namespacesGetAuthorizationRule

> SharedAccessAuthorizationRuleResource namespacesGetAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a namespace by name.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name
let authorizationRuleName = "authorizationRuleName_example"; // String | Authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesGetAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name | 
 **authorizationRuleName** | **String**| Authorization rule name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namespacesList

> NamespaceListResult namespacesList(resourceGroupName, apiVersion, subscriptionId)



Lists the available namespaces within a resourceGroup.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. If resourceGroupName value is null the method lists all the namespaces within subscription
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. If resourceGroupName value is null the method lists all the namespaces within subscription | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NamespaceListResult**](NamespaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namespacesListAll

> NamespaceListResult namespacesListAll(apiVersion, subscriptionId)



Lists all the available namespaces within the subscription irrespective of the resourceGroups.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NamespaceListResult**](NamespaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namespacesListAuthorizationRules

> SharedAccessAuthorizationRuleListResult namespacesListAuthorizationRules(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets the authorization rules for a namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesListAuthorizationRules(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namespacesListKeys

> SharedAccessAuthorizationRuleListResult namespacesListKeys(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId)



Gets the Primary and Secondary ConnectionStrings to the namespace 

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The connection string of the namespace for the specified authorizationRule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.namespacesListKeys(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **authorizationRuleName** | **String**| The connection string of the namespace for the specified authorizationRule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namespacesPatch

> NamespaceResource namespacesPatch(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Patches the existing namespace

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.NamespacePatchParameters(); // NamespacePatchParameters | Parameters supplied to patch a Namespace Resource.
apiInstance.namespacesPatch(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NamespacePatchParameters**](NamespacePatchParameters.md)| Parameters supplied to patch a Namespace Resource. | 

### Return type

[**NamespaceResource**](NamespaceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## namespacesRegenerateKeys

> ResourceListKeys namespacesRegenerateKeys(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NamespacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The connection string of the namespace for the specified authorizationRule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.PolicykeyResource(); // PolicykeyResource | Parameters supplied to regenerate the Namespace Authorization Rule Key.
apiInstance.namespacesRegenerateKeys(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **namespaceName** | **String**| The namespace name. | 
 **authorizationRuleName** | **String**| The connection string of the namespace for the specified authorizationRule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PolicykeyResource**](PolicykeyResource.md)| Parameters supplied to regenerate the Namespace Authorization Rule Key. | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

