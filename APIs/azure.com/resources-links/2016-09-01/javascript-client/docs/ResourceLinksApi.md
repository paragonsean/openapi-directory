# ManagementLinkClient.ResourceLinksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceLinksCreateOrUpdate**](ResourceLinksApi.md#resourceLinksCreateOrUpdate) | **PUT** /{linkId} | 
[**resourceLinksDelete**](ResourceLinksApi.md#resourceLinksDelete) | **DELETE** /{linkId} | 
[**resourceLinksGet**](ResourceLinksApi.md#resourceLinksGet) | **GET** /{linkId} | 
[**resourceLinksListAtSourceScope**](ResourceLinksApi.md#resourceLinksListAtSourceScope) | **GET** /{scope}/providers/Microsoft.Resources/links | 
[**resourceLinksListAtSubscription**](ResourceLinksApi.md#resourceLinksListAtSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/links | 



## resourceLinksCreateOrUpdate

> ResourceLink resourceLinksCreateOrUpdate(linkId, apiVersion, parameters)



Creates or updates a resource link between the specified resources.

### Example

```javascript
import ManagementLinkClient from 'management_link_client';
let defaultClient = ManagementLinkClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLinkClient.ResourceLinksApi();
let linkId = "linkId_example"; // String | The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let parameters = new ManagementLinkClient.ResourceLink(); // ResourceLink | Parameters for creating or updating a resource link.
apiInstance.resourceLinksCreateOrUpdate(linkId, apiVersion, parameters, (error, data, response) => {
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
 **linkId** | **String**| The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**ResourceLink**](ResourceLink.md)| Parameters for creating or updating a resource link. | 

### Return type

[**ResourceLink**](ResourceLink.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourceLinksDelete

> resourceLinksDelete(linkId, apiVersion)



Deletes a resource link with the specified ID.

### Example

```javascript
import ManagementLinkClient from 'management_link_client';
let defaultClient = ManagementLinkClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLinkClient.ResourceLinksApi();
let linkId = "linkId_example"; // String | The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.resourceLinksDelete(linkId, apiVersion, (error, data, response) => {
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
 **linkId** | **String**| The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resourceLinksGet

> ResourceLink resourceLinksGet(linkId, apiVersion)



Gets a resource link with the specified ID.

### Example

```javascript
import ManagementLinkClient from 'management_link_client';
let defaultClient = ManagementLinkClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLinkClient.ResourceLinksApi();
let linkId = "linkId_example"; // String | The fully qualified Id of the resource link. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.resourceLinksGet(linkId, apiVersion, (error, data, response) => {
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
 **linkId** | **String**| The fully qualified Id of the resource link. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**ResourceLink**](ResourceLink.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceLinksListAtSourceScope

> ResourceLinkResult resourceLinksListAtSourceScope(scope, apiVersion, opts)



Gets a list of resource links at and below the specified source scope.

### Example

```javascript
import ManagementLinkClient from 'management_link_client';
let defaultClient = ManagementLinkClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLinkClient.ResourceLinksApi();
let scope = "scope_example"; // String | The fully qualified ID of the scope for getting the resource links. For example, to list resource links at and under a resource group, set the scope to /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply when getting resource links. To get links only at the specified scope (not below the scope), use Filter.atScope().
};
apiInstance.resourceLinksListAtSourceScope(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The fully qualified ID of the scope for getting the resource links. For example, to list resource links at and under a resource group, set the scope to /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **filter** | **String**| The filter to apply when getting resource links. To get links only at the specified scope (not below the scope), use Filter.atScope(). | [optional] 

### Return type

[**ResourceLinkResult**](ResourceLinkResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceLinksListAtSubscription

> ResourceLinkResult resourceLinksListAtSubscription(apiVersion, subscriptionId, opts)



Gets all the linked resources for the subscription.

### Example

```javascript
import ManagementLinkClient from 'management_link_client';
let defaultClient = ManagementLinkClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLinkClient.ResourceLinksApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the list resource links operation. The supported filter for list resource links is targetId. For example, $filter=targetId eq {value}
};
apiInstance.resourceLinksListAtSubscription(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the list resource links operation. The supported filter for list resource links is targetId. For example, $filter&#x3D;targetId eq {value} | [optional] 

### Return type

[**ResourceLinkResult**](ResourceLinkResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

