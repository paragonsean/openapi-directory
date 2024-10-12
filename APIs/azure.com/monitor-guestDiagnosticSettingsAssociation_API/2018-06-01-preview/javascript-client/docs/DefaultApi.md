# GuestDiagnosticSettingsAssociation.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guestDiagnosticsSettingsAssociationList**](DefaultApi.md#guestDiagnosticsSettingsAssociationList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/guestDiagnosticSettingsAssociations | 
[**guestDiagnosticsSettingsAssociationListByResourceGroup**](DefaultApi.md#guestDiagnosticsSettingsAssociationListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/guestDiagnosticSettingsAssociations | 
[**guestDiagnosticsSettingsAssociationUpdate**](DefaultApi.md#guestDiagnosticsSettingsAssociationUpdate) | **PATCH** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} | 



## guestDiagnosticsSettingsAssociationList

> GuestDiagnosticSettingsAssociationList guestDiagnosticsSettingsAssociationList(subscriptionId, apiVersion)



Get a list of all guest diagnostic settings association in a subscription.

### Example

```javascript
import GuestDiagnosticSettingsAssociation from 'guest_diagnostic_settings_association';
let defaultClient = GuestDiagnosticSettingsAssociation.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GuestDiagnosticSettingsAssociation.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.guestDiagnosticsSettingsAssociationList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GuestDiagnosticSettingsAssociationList**](GuestDiagnosticSettingsAssociationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## guestDiagnosticsSettingsAssociationListByResourceGroup

> GuestDiagnosticSettingsAssociationList guestDiagnosticsSettingsAssociationListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Get a list of all guest diagnostic settings association in a resource group.

### Example

```javascript
import GuestDiagnosticSettingsAssociation from 'guest_diagnostic_settings_association';
let defaultClient = GuestDiagnosticSettingsAssociation.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GuestDiagnosticSettingsAssociation.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.guestDiagnosticsSettingsAssociationListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GuestDiagnosticSettingsAssociationList**](GuestDiagnosticSettingsAssociationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## guestDiagnosticsSettingsAssociationUpdate

> GuestDiagnosticSettingsAssociationResource guestDiagnosticsSettingsAssociationUpdate(resourceUri, apiVersion, associationName, parameters)



Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use the CreateOrUpdate method

### Example

```javascript
import GuestDiagnosticSettingsAssociation from 'guest_diagnostic_settings_association';
let defaultClient = GuestDiagnosticSettingsAssociation.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GuestDiagnosticSettingsAssociation.DefaultApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let associationName = "associationName_example"; // String | The name of the diagnostic settings association.
let parameters = new GuestDiagnosticSettingsAssociation.GuestDiagnosticSettingsAssociationResourcePatch(); // GuestDiagnosticSettingsAssociationResourcePatch | Parameters supplied to the operation.
apiInstance.guestDiagnosticsSettingsAssociationUpdate(resourceUri, apiVersion, associationName, parameters, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. | 
 **apiVersion** | **String**| Client Api Version. | 
 **associationName** | **String**| The name of the diagnostic settings association. | 
 **parameters** | [**GuestDiagnosticSettingsAssociationResourcePatch**](GuestDiagnosticSettingsAssociationResourcePatch.md)| Parameters supplied to the operation. | 

### Return type

[**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

