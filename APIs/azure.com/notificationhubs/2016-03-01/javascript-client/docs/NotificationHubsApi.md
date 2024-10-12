# NotificationHubsManagementClient.NotificationHubsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationHubsCheckAvailability**](NotificationHubsApi.md#notificationHubsCheckAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/checkNotificationHubAvailability | 
[**notificationHubsCreateOrUpdate**](NotificationHubsApi.md#notificationHubsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName} | 
[**notificationHubsCreateOrUpdateAuthorizationRule**](NotificationHubsApi.md#notificationHubsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName} | 
[**notificationHubsDelete**](NotificationHubsApi.md#notificationHubsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName} | 
[**notificationHubsDeleteAuthorizationRule**](NotificationHubsApi.md#notificationHubsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName} | 
[**notificationHubsGet**](NotificationHubsApi.md#notificationHubsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName} | 
[**notificationHubsGetAuthorizationRule**](NotificationHubsApi.md#notificationHubsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName} | 
[**notificationHubsGetPnsCredentials**](NotificationHubsApi.md#notificationHubsGetPnsCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/pnsCredentials | 
[**notificationHubsList**](NotificationHubsApi.md#notificationHubsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs | 
[**notificationHubsListAuthorizationRules**](NotificationHubsApi.md#notificationHubsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules | 
[**notificationHubsListKeys**](NotificationHubsApi.md#notificationHubsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName}/listKeys | 
[**notificationHubsRegenerateKeys**](NotificationHubsApi.md#notificationHubsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName}/regenerateKeys | 



## notificationHubsCheckAvailability

> CheckAvailabilityResult notificationHubsCheckAvailability(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Checks the availability of the given notificationHub in a namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.CheckAvailabilityParameters(); // CheckAvailabilityParameters | The notificationHub name.
apiInstance.notificationHubsCheckAvailability(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**CheckAvailabilityParameters**](CheckAvailabilityParameters.md)| The notificationHub name. | 

### Return type

[**CheckAvailabilityResult**](CheckAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## notificationHubsCreateOrUpdate

> NotificationHubResource notificationHubsCreateOrUpdate(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, parameters)



Creates/Update a NotificationHub in a namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.NotificationHubCreateOrUpdateParameters(); // NotificationHubCreateOrUpdateParameters | Parameters supplied to the create/update a NotificationHub Resource.
apiInstance.notificationHubsCreateOrUpdate(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NotificationHubCreateOrUpdateParameters**](NotificationHubCreateOrUpdateParameters.md)| Parameters supplied to the create/update a NotificationHub Resource. | 

### Return type

[**NotificationHubResource**](NotificationHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## notificationHubsCreateOrUpdateAuthorizationRule

> SharedAccessAuthorizationRuleResource notificationHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates/Updates an authorization rule for a NotificationHub

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let authorizationRuleName = "authorizationRuleName_example"; // String | Authorization Rule Name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access authorization rule.
apiInstance.notificationHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **authorizationRuleName** | **String**| Authorization Rule Name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access authorization rule. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## notificationHubsDelete

> notificationHubsDelete(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Deletes a notification hub associated with a namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsDelete(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationHubsDeleteAuthorizationRule

> notificationHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a notificationHub authorization rule

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let authorizationRuleName = "authorizationRuleName_example"; // String | Authorization Rule Name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
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


## notificationHubsGet

> NotificationHubResource notificationHubsGet(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Lists the notification hubs associated with a namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsGet(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NotificationHubResource**](NotificationHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## notificationHubsGetAuthorizationRule

> SharedAccessAuthorizationRuleResource notificationHubsGetAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a NotificationHub by name.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let authorizationRuleName = "authorizationRuleName_example"; // String | authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsGetAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **authorizationRuleName** | **String**| authorization rule name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## notificationHubsGetPnsCredentials

> PnsCredentialsResource notificationHubsGetPnsCredentials(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Lists the PNS Credentials associated with a notification hub .

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsGetPnsCredentials(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PnsCredentialsResource**](PnsCredentialsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## notificationHubsList

> NotificationHubListResult notificationHubsList(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Lists the notification hubs associated with a namespace.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsList(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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

[**NotificationHubListResult**](NotificationHubListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## notificationHubsListAuthorizationRules

> SharedAccessAuthorizationRuleListResult notificationHubsListAuthorizationRules(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Gets the authorization rules for a NotificationHub.

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsListAuthorizationRules(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## notificationHubsListKeys

> ResourceListKeys notificationHubsListKeys(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets the Primary and Secondary ConnectionStrings to the NotificationHub 

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The connection string of the NotificationHub for the specified authorizationRule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.notificationHubsListKeys(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **authorizationRuleName** | **String**| The connection string of the NotificationHub for the specified authorizationRule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## notificationHubsRegenerateKeys

> ResourceListKeys notificationHubsRegenerateKeys(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the Primary/Secondary Keys to the NotificationHub Authorization Rule

### Example

```javascript
import NotificationHubsManagementClient from 'notification_hubs_management_client';
let defaultClient = NotificationHubsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NotificationHubsManagementClient.NotificationHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let namespaceName = "namespaceName_example"; // String | The namespace name.
let notificationHubName = "notificationHubName_example"; // String | The notification hub name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The connection string of the NotificationHub for the specified authorizationRule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NotificationHubsManagementClient.PolicykeyResource(); // PolicykeyResource | Parameters supplied to regenerate the NotificationHub Authorization Rule Key.
apiInstance.notificationHubsRegenerateKeys(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **notificationHubName** | **String**| The notification hub name. | 
 **authorizationRuleName** | **String**| The connection string of the NotificationHub for the specified authorizationRule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PolicykeyResource**](PolicykeyResource.md)| Parameters supplied to regenerate the NotificationHub Authorization Rule Key. | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

