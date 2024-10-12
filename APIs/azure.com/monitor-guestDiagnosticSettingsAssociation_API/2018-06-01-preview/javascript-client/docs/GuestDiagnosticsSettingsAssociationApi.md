# GuestDiagnosticSettingsAssociation.GuestDiagnosticsSettingsAssociationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guestDiagnosticsSettingsAssociationCreateOrUpdate**](GuestDiagnosticsSettingsAssociationApi.md#guestDiagnosticsSettingsAssociationCreateOrUpdate) | **PUT** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} | 
[**guestDiagnosticsSettingsAssociationDelete**](GuestDiagnosticsSettingsAssociationApi.md#guestDiagnosticsSettingsAssociationDelete) | **DELETE** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} | 
[**guestDiagnosticsSettingsAssociationGet**](GuestDiagnosticsSettingsAssociationApi.md#guestDiagnosticsSettingsAssociationGet) | **GET** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} | 



## guestDiagnosticsSettingsAssociationCreateOrUpdate

> GuestDiagnosticSettingsAssociationResource guestDiagnosticsSettingsAssociationCreateOrUpdate(resourceUri, associationName, apiVersion, diagnosticSettingsAssociation)



Creates or updates guest diagnostics settings association.

### Example

```javascript
import GuestDiagnosticSettingsAssociation from 'guest_diagnostic_settings_association';
let defaultClient = GuestDiagnosticSettingsAssociation.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GuestDiagnosticSettingsAssociation.GuestDiagnosticsSettingsAssociationApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
let associationName = "associationName_example"; // String | The name of the diagnostic settings association.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let diagnosticSettingsAssociation = new GuestDiagnosticSettingsAssociation.GuestDiagnosticSettingsAssociationResource(); // GuestDiagnosticSettingsAssociationResource | The diagnostic settings association to create or update.
apiInstance.guestDiagnosticsSettingsAssociationCreateOrUpdate(resourceUri, associationName, apiVersion, diagnosticSettingsAssociation, (error, data, response) => {
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
 **associationName** | **String**| The name of the diagnostic settings association. | 
 **apiVersion** | **String**| Client Api Version. | 
 **diagnosticSettingsAssociation** | [**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)| The diagnostic settings association to create or update. | 

### Return type

[**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## guestDiagnosticsSettingsAssociationDelete

> guestDiagnosticsSettingsAssociationDelete(resourceUri, associationName, apiVersion)



Delete guest diagnostics association settings.

### Example

```javascript
import GuestDiagnosticSettingsAssociation from 'guest_diagnostic_settings_association';
let defaultClient = GuestDiagnosticSettingsAssociation.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GuestDiagnosticSettingsAssociation.GuestDiagnosticsSettingsAssociationApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
let associationName = "associationName_example"; // String | The name of the diagnostic settings association.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.guestDiagnosticsSettingsAssociationDelete(resourceUri, associationName, apiVersion, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. | 
 **associationName** | **String**| The name of the diagnostic settings association. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## guestDiagnosticsSettingsAssociationGet

> GuestDiagnosticSettingsAssociationResource guestDiagnosticsSettingsAssociationGet(resourceUri, associationName, apiVersion)



Gets guest diagnostics association settings.

### Example

```javascript
import GuestDiagnosticSettingsAssociation from 'guest_diagnostic_settings_association';
let defaultClient = GuestDiagnosticSettingsAssociation.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GuestDiagnosticSettingsAssociation.GuestDiagnosticsSettingsAssociationApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
let associationName = "associationName_example"; // String | The name of the diagnostic settings association.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.guestDiagnosticsSettingsAssociationGet(resourceUri, associationName, apiVersion, (error, data, response) => {
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
 **associationName** | **String**| The name of the diagnostic settings association. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

