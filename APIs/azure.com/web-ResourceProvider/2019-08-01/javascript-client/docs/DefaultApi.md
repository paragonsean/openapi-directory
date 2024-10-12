# ApiClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkNameAvailability**](DefaultApi.md#checkNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/checknameavailability | Check if a resource name is available.
[**getPublishingUser**](DefaultApi.md#getPublishingUser) | **GET** /providers/Microsoft.Web/publishingUsers/web | Gets publishing user
[**getSourceControl**](DefaultApi.md#getSourceControl) | **GET** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Gets source control token
[**getSubscriptionDeploymentLocations**](DefaultApi.md#getSubscriptionDeploymentLocations) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/deploymentLocations | Gets list of available geo regions plus ministamps
[**listBillingMeters**](DefaultApi.md#listBillingMeters) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/billingMeters | Gets a list of meters for a given location.
[**listGeoRegions**](DefaultApi.md#listGeoRegions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/geoRegions | Get a list of available geographical regions.
[**listPremierAddOnOffers**](DefaultApi.md#listPremierAddOnOffers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/premieraddonoffers | List all premier add-on offers.
[**listSiteIdentifiersAssignedToHostName**](DefaultApi.md#listSiteIdentifiersAssignedToHostName) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/listSitesAssignedToHostName | List all apps that are assigned to a hostname.
[**listSkus**](DefaultApi.md#listSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/skus | List all SKUs.
[**listSourceControls**](DefaultApi.md#listSourceControls) | **GET** /providers/Microsoft.Web/sourcecontrols | Gets the source controls available for Azure websites.
[**move**](DefaultApi.md#move) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources | Move resources between resource groups.
[**updatePublishingUser**](DefaultApi.md#updatePublishingUser) | **PUT** /providers/Microsoft.Web/publishingUsers/web | Updates publishing user
[**updateSourceControl**](DefaultApi.md#updateSourceControl) | **PUT** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Updates source control token
[**validate**](DefaultApi.md#validate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/validate | Validate if a resource can be created.
[**validateMove**](DefaultApi.md#validateMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/validateMoveResources | Validate whether a resource can be moved.
[**verifyHostingEnvironmentVnet**](DefaultApi.md#verifyHostingEnvironmentVnet) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/verifyHostingEnvironmentVnet | Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.



## checkNameAvailability

> ResourceNameAvailability checkNameAvailability(subscriptionId, apiVersion, request)

Check if a resource name is available.

Description for Check if a resource name is available.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new ApiClient.ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | Name availability request.
apiInstance.checkNameAvailability(subscriptionId, apiVersion, request, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| Name availability request. | 

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPublishingUser

> GetPublishingUser200Response getPublishingUser(apiVersion)

Gets publishing user

Description for Gets publishing user

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.getPublishingUser(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**GetPublishingUser200Response**](GetPublishingUser200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourceControl

> SourceControl getSourceControl(sourceControlType, apiVersion)

Gets source control token

Description for Gets source control token

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let sourceControlType = "sourceControlType_example"; // String | Type of source control
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.getSourceControl(sourceControlType, apiVersion, (error, data, response) => {
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
 **sourceControlType** | **String**| Type of source control | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscriptionDeploymentLocations

> DeploymentLocations getSubscriptionDeploymentLocations(subscriptionId, apiVersion)

Gets list of available geo regions plus ministamps

Description for Gets list of available geo regions plus ministamps

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.getSubscriptionDeploymentLocations(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentLocations**](DeploymentLocations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBillingMeters

> BillingMeterCollection listBillingMeters(subscriptionId, apiVersion, opts)

Gets a list of meters for a given location.

Description for Gets a list of meters for a given location.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'billingLocation': "billingLocation_example", // String | Azure Location of billable resource
  'osType': "osType_example" // String | App Service OS type meters used for
};
apiInstance.listBillingMeters(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **billingLocation** | **String**| Azure Location of billable resource | [optional] 
 **osType** | **String**| App Service OS type meters used for | [optional] 

### Return type

[**BillingMeterCollection**](BillingMeterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGeoRegions

> GeoRegionCollection listGeoRegions(subscriptionId, apiVersion, opts)

Get a list of available geographical regions.

Description for Get a list of available geographical regions.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'sku': "sku_example", // String | Name of SKU used to filter the regions.
  'linuxWorkersEnabled': true, // Boolean | Specify <code>true</code> if you want to filter to only regions that support Linux workers.
  'xenonWorkersEnabled': true, // Boolean | Specify <code>true</code> if you want to filter to only regions that support Xenon workers.
  'linuxDynamicWorkersEnabled': true // Boolean | Specify <code>true</code> if you want to filter to only regions that support Linux Consumption Workers.
};
apiInstance.listGeoRegions(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **sku** | **String**| Name of SKU used to filter the regions. | [optional] 
 **linuxWorkersEnabled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Linux workers. | [optional] 
 **xenonWorkersEnabled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Xenon workers. | [optional] 
 **linuxDynamicWorkersEnabled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Linux Consumption Workers. | [optional] 

### Return type

[**GeoRegionCollection**](GeoRegionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPremierAddOnOffers

> PremierAddOnOfferCollection listPremierAddOnOffers(subscriptionId, apiVersion)

List all premier add-on offers.

Description for List all premier add-on offers.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.listPremierAddOnOffers(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PremierAddOnOfferCollection**](PremierAddOnOfferCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteIdentifiersAssignedToHostName

> ListSiteIdentifiersAssignedToHostName200Response listSiteIdentifiersAssignedToHostName(subscriptionId, apiVersion, nameIdentifier)

List all apps that are assigned to a hostname.

Description for List all apps that are assigned to a hostname.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let nameIdentifier = new ApiClient.ListSiteIdentifiersAssignedToHostNameRequest(); // ListSiteIdentifiersAssignedToHostNameRequest | Hostname information.
apiInstance.listSiteIdentifiersAssignedToHostName(subscriptionId, apiVersion, nameIdentifier, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **nameIdentifier** | [**ListSiteIdentifiersAssignedToHostNameRequest**](ListSiteIdentifiersAssignedToHostNameRequest.md)| Hostname information. | 

### Return type

[**ListSiteIdentifiersAssignedToHostName200Response**](ListSiteIdentifiersAssignedToHostName200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSkus

> SkuInfos listSkus(subscriptionId, apiVersion)

List all SKUs.

Description for List all SKUs.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.listSkus(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SkuInfos**](SkuInfos.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSourceControls

> SourceControlCollection listSourceControls(apiVersion)

Gets the source controls available for Azure websites.

Description for Gets the source controls available for Azure websites.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.listSourceControls(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**SourceControlCollection**](SourceControlCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## move

> move(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope)

Move resources between resource groups.

Description for Move resources between resource groups.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let moveResourceEnvelope = new ApiClient.CsmMoveResourceEnvelope(); // CsmMoveResourceEnvelope | Object that represents the resource to move.
apiInstance.move(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **moveResourceEnvelope** | [**CsmMoveResourceEnvelope**](CsmMoveResourceEnvelope.md)| Object that represents the resource to move. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePublishingUser

> GetPublishingUser200Response updatePublishingUser(apiVersion, userDetails)

Updates publishing user

Description for Updates publishing user

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | API Version
let userDetails = new ApiClient.GetPublishingUser200Response(); // GetPublishingUser200Response | Details of publishing user
apiInstance.updatePublishingUser(apiVersion, userDetails, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 
 **userDetails** | [**GetPublishingUser200Response**](GetPublishingUser200Response.md)| Details of publishing user | 

### Return type

[**GetPublishingUser200Response**](GetPublishingUser200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSourceControl

> SourceControl updateSourceControl(sourceControlType, apiVersion, requestMessage)

Updates source control token

Description for Updates source control token

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let sourceControlType = "sourceControlType_example"; // String | Type of source control
let apiVersion = "apiVersion_example"; // String | API Version
let requestMessage = new ApiClient.SourceControl(); // SourceControl | Source control token information
apiInstance.updateSourceControl(sourceControlType, apiVersion, requestMessage, (error, data, response) => {
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
 **sourceControlType** | **String**| Type of source control | 
 **apiVersion** | **String**| API Version | 
 **requestMessage** | [**SourceControl**](SourceControl.md)| Source control token information | 

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validate

> ValidateResponse validate(resourceGroupName, subscriptionId, apiVersion, validateRequest)

Validate if a resource can be created.

Description for Validate if a resource can be created.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let validateRequest = new ApiClient.ValidateRequest(); // ValidateRequest | Request with the resources to validate.
apiInstance.validate(resourceGroupName, subscriptionId, apiVersion, validateRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **validateRequest** | [**ValidateRequest**](ValidateRequest.md)| Request with the resources to validate. | 

### Return type

[**ValidateResponse**](ValidateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateMove

> validateMove(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope)

Validate whether a resource can be moved.

Description for Validate whether a resource can be moved.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let moveResourceEnvelope = new ApiClient.CsmMoveResourceEnvelope(); // CsmMoveResourceEnvelope | Object that represents the resource to move.
apiInstance.validateMove(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **moveResourceEnvelope** | [**CsmMoveResourceEnvelope**](CsmMoveResourceEnvelope.md)| Object that represents the resource to move. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## verifyHostingEnvironmentVnet

> VnetValidationFailureDetails verifyHostingEnvironmentVnet(subscriptionId, apiVersion, parameters)

Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

Description for Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

### Example

```javascript
import ApiClient from '_api_client';
let defaultClient = ApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let parameters = new ApiClient.VnetParameters(); // VnetParameters | VNET information
apiInstance.verifyHostingEnvironmentVnet(subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **parameters** | [**VnetParameters**](VnetParameters.md)| VNET information | 

### Return type

[**VnetValidationFailureDetails**](VnetValidationFailureDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

