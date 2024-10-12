# PrivateDnsManagementClient.PrivateZonesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateZonesCreateOrUpdate**](PrivateZonesApi.md#privateZonesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} | 
[**privateZonesDelete**](PrivateZonesApi.md#privateZonesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} | 
[**privateZonesGet**](PrivateZonesApi.md#privateZonesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} | 
[**privateZonesList**](PrivateZonesApi.md#privateZonesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/privateDnsZones | 
[**privateZonesListByResourceGroup**](PrivateZonesApi.md#privateZonesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones | 
[**privateZonesUpdate**](PrivateZonesApi.md#privateZonesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} | 



## privateZonesCreateOrUpdate

> PrivateZone privateZonesCreateOrUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, opts)



Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.PrivateZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new PrivateDnsManagementClient.PrivateZone(); // PrivateZone | Parameters supplied to the CreateOrUpdate operation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new Private DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.
};
apiInstance.privateZonesCreateOrUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PrivateZone**](PrivateZone.md)| Parameters supplied to the CreateOrUpdate operation. | 
 **ifMatch** | **String**| The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new Private DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. | [optional] 

### Return type

[**PrivateZone**](PrivateZone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateZonesDelete

> privateZonesDelete(resourceGroupName, privateZoneName, apiVersion, subscriptionId, opts)



Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.PrivateZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
};
apiInstance.privateZonesDelete(resourceGroupName, privateZoneName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **ifMatch** | **String**| The ETag of the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateZonesGet

> PrivateZone privateZonesGet(resourceGroupName, privateZoneName, apiVersion, subscriptionId)



Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.PrivateZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.privateZonesGet(resourceGroupName, privateZoneName, apiVersion, subscriptionId, (error, data, response) => {
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
 **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PrivateZone**](PrivateZone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateZonesList

> PrivateZoneListResult privateZonesList(apiVersion, subscriptionId, opts)



Lists the Private DNS zones in all resource groups in a subscription.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.PrivateZonesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | The maximum number of Private DNS zones to return. If not specified, returns up to 100 zones.
};
apiInstance.privateZonesList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| The maximum number of Private DNS zones to return. If not specified, returns up to 100 zones. | [optional] 

### Return type

[**PrivateZoneListResult**](PrivateZoneListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateZonesListByResourceGroup

> PrivateZoneListResult privateZonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Lists the Private DNS zones within a resource group.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.PrivateZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
};
apiInstance.privateZonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 

### Return type

[**PrivateZoneListResult**](PrivateZoneListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateZonesUpdate

> PrivateZone privateZonesUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, opts)



Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.PrivateZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new PrivateDnsManagementClient.PrivateZone(); // PrivateZone | Parameters supplied to the Update operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
};
apiInstance.privateZonesUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PrivateZone**](PrivateZone.md)| Parameters supplied to the Update operation. | 
 **ifMatch** | **String**| The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] 

### Return type

[**PrivateZone**](PrivateZone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

