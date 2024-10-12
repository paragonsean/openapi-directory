# FabricAdminClient.ScaleUnitsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scaleUnitsCreateFromJson**](ScaleUnitsApi.md#scaleUnitsCreateFromJson) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/createFromJson | 
[**scaleUnitsGet**](ScaleUnitsApi.md#scaleUnitsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit} | 
[**scaleUnitsList**](ScaleUnitsApi.md#scaleUnitsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits | 
[**scaleUnitsScaleOut**](ScaleUnitsApi.md#scaleUnitsScaleOut) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/scaleOut | 



## scaleUnitsCreateFromJson

> scaleUnitsCreateFromJson(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, creationData)



Add a new scale unit.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.ScaleUnitsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
let creationData = new FabricAdminClient.CreateFromJsonScaleUnitParametersList(); // CreateFromJsonScaleUnitParametersList | A list of input data that allows for creating the new scale unit.
apiInstance.scaleUnitsCreateFromJson(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, creationData, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **scaleUnit** | **String**| Name of the scale units. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]
 **creationData** | [**CreateFromJsonScaleUnitParametersList**](CreateFromJsonScaleUnitParametersList.md)| A list of input data that allows for creating the new scale unit. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## scaleUnitsGet

> ScaleUnit scaleUnitsGet(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion)



Returns the requested scale unit.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.ScaleUnitsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.scaleUnitsGet(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **scaleUnit** | **String**| Name of the scale units. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**ScaleUnit**](ScaleUnit.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scaleUnitsList

> ScaleUnitList scaleUnitsList(subscriptionId, resourceGroupName, location, apiVersion, opts)



Returns a list of all scale units at a location.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.ScaleUnitsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
let opts = {
  'filter': "filter_example" // String | OData filter parameter.
};
apiInstance.scaleUnitsList(subscriptionId, resourceGroupName, location, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]
 **filter** | **String**| OData filter parameter. | [optional] 

### Return type

[**ScaleUnitList**](ScaleUnitList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scaleUnitsScaleOut

> scaleUnitsScaleOut(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, scaleUnitNodeParameters)



Scales out a scale unit.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.ScaleUnitsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
let scaleUnitNodeParameters = new FabricAdminClient.ScaleOutScaleUnitParametersList(); // ScaleOutScaleUnitParametersList | A list of input data that allows for adding a set of scale unit nodes.
apiInstance.scaleUnitsScaleOut(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, scaleUnitNodeParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **scaleUnit** | **String**| Name of the scale units. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]
 **scaleUnitNodeParameters** | [**ScaleOutScaleUnitParametersList**](ScaleOutScaleUnitParametersList.md)| A list of input data that allows for adding a set of scale unit nodes. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

