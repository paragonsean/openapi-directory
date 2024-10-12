# EventHubManagementClient.EventHubsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventHubsCreateOrUpdate**](EventHubsApi.md#eventHubsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName} | 
[**eventHubsCreateOrUpdateAuthorizationRule**](EventHubsApi.md#eventHubsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} | 
[**eventHubsDelete**](EventHubsApi.md#eventHubsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName} | 
[**eventHubsDeleteAuthorizationRule**](EventHubsApi.md#eventHubsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} | 
[**eventHubsGet**](EventHubsApi.md#eventHubsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName} | 
[**eventHubsGetAuthorizationRule**](EventHubsApi.md#eventHubsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} | 
[**eventHubsListAll**](EventHubsApi.md#eventHubsListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs | 
[**eventHubsListAuthorizationRules**](EventHubsApi.md#eventHubsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules | 
[**eventHubsListKeys**](EventHubsApi.md#eventHubsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName}/ListKeys | 
[**eventHubsPostAuthorizationRule**](EventHubsApi.md#eventHubsPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} | 
[**eventHubsRegenerateKeys**](EventHubsApi.md#eventHubsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName}/regenerateKeys | 



## eventHubsCreateOrUpdate

> EventHubResource eventHubsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, parameters)



Creates or updates a new Event Hub as a nested resource within a Namespace.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new EventHubManagementClient.EventHubCreateOrUpdateParameters(); // EventHubCreateOrUpdateParameters | Parameters supplied to create an Event Hub resource.
apiInstance.eventHubsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**EventHubCreateOrUpdateParameters**](EventHubCreateOrUpdateParameters.md)| Parameters supplied to create an Event Hub resource. | 

### Return type

[**EventHubResource**](EventHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## eventHubsCreateOrUpdateAuthorizationRule

> SharedAccessAuthorizationRuleResource eventHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates or updates an AuthorizationRule for the specified Event Hub.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new EventHubManagementClient.SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access AuthorizationRule.
apiInstance.eventHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access AuthorizationRule. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## eventHubsDelete

> eventHubsDelete(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Deletes an Event Hub from the specified Namespace and resource group.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsDelete(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventHubsDeleteAuthorizationRule

> eventHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Deletes an Event Hub AuthorizationRule.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventHubsGet

> EventHubResource eventHubsGet(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Gets an Event Hubs description for the specified Event Hub.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsGet(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**EventHubResource**](EventHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubsGetAuthorizationRule

> SharedAccessAuthorizationRuleResource eventHubsGetAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets an AuthorizationRule for an Event Hub by rule name.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsGetAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubsListAll

> EventHubListResult eventHubsListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets all the Event Hubs in a Namespace.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**EventHubListResult**](EventHubListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubsListAuthorizationRules

> SharedAccessAuthorizationRuleListResult eventHubsListAuthorizationRules(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Gets the authorization rules for an Event Hub.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsListAuthorizationRules(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubsListKeys

> ResourceListKeys eventHubsListKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets the ACS and SAS connection strings for the Event Hub.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsListKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubsPostAuthorizationRule

> SharedAccessAuthorizationRuleResource eventHubsPostAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets an AuthorizationRule for an Event Hub by rule name.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubsPostAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubsRegenerateKeys

> ResourceListKeys eventHubsRegenerateKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the ACS and SAS connection strings for the Event Hub.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.EventHubsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new EventHubManagementClient.RegenerateKeysParameters(); // RegenerateKeysParameters | Parameters supplied to regenerate the AuthorizationRule Keys (PrimaryKey/SecondaryKey).
apiInstance.eventHubsRegenerateKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RegenerateKeysParameters**](RegenerateKeysParameters.md)| Parameters supplied to regenerate the AuthorizationRule Keys (PrimaryKey/SecondaryKey). | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

