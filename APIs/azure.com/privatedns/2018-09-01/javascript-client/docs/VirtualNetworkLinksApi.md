# PrivateDnsManagementClient.VirtualNetworkLinksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkLinksCreateOrUpdate**](VirtualNetworkLinksApi.md#virtualNetworkLinksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} | 
[**virtualNetworkLinksDelete**](VirtualNetworkLinksApi.md#virtualNetworkLinksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} | 
[**virtualNetworkLinksGet**](VirtualNetworkLinksApi.md#virtualNetworkLinksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} | 
[**virtualNetworkLinksList**](VirtualNetworkLinksApi.md#virtualNetworkLinksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks | 
[**virtualNetworkLinksUpdate**](VirtualNetworkLinksApi.md#virtualNetworkLinksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} | 



## virtualNetworkLinksCreateOrUpdate

> VirtualNetworkLink virtualNetworkLinksCreateOrUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, opts)



Creates or updates a virtual network link to the specified Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.VirtualNetworkLinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new PrivateDnsManagementClient.VirtualNetworkLink(); // VirtualNetworkLink | Parameters supplied to the CreateOrUpdate operation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new virtual network link to the Private DNS zone to be created, but to prevent updating an existing link. Other values will be ignored.
};
apiInstance.virtualNetworkLinksCreateOrUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **virtualNetworkLinkName** | **String**| The name of the virtual network link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkLink**](VirtualNetworkLink.md)| Parameters supplied to the CreateOrUpdate operation. | 
 **ifMatch** | **String**| The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new virtual network link to the Private DNS zone to be created, but to prevent updating an existing link. Other values will be ignored. | [optional] 

### Return type

[**VirtualNetworkLink**](VirtualNetworkLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkLinksDelete

> virtualNetworkLinksDelete(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, opts)



Deletes a virtual network link to the specified Private DNS zone. WARNING: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.VirtualNetworkLinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the virtual network link to the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
};
apiInstance.virtualNetworkLinksDelete(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **virtualNetworkLinkName** | **String**| The name of the virtual network link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **ifMatch** | **String**| The ETag of the virtual network link to the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkLinksGet

> VirtualNetworkLink virtualNetworkLinksGet(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId)



Gets a virtual network link to the specified Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.VirtualNetworkLinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkLinksGet(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkLinkName** | **String**| The name of the virtual network link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkLink**](VirtualNetworkLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkLinksList

> VirtualNetworkLinkListResult virtualNetworkLinksList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, opts)



Lists the virtual network links to the specified Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.VirtualNetworkLinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | The maximum number of virtual network links to return. If not specified, returns up to 100 virtual network links.
};
apiInstance.virtualNetworkLinksList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| The maximum number of virtual network links to return. If not specified, returns up to 100 virtual network links. | [optional] 

### Return type

[**VirtualNetworkLinkListResult**](VirtualNetworkLinkListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkLinksUpdate

> VirtualNetworkLink virtualNetworkLinksUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, opts)



Updates a virtual network link to the specified Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.VirtualNetworkLinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new PrivateDnsManagementClient.VirtualNetworkLink(); // VirtualNetworkLink | Parameters supplied to the Update operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
};
apiInstance.virtualNetworkLinksUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **virtualNetworkLinkName** | **String**| The name of the virtual network link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkLink**](VirtualNetworkLink.md)| Parameters supplied to the Update operation. | 
 **ifMatch** | **String**| The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] 

### Return type

[**VirtualNetworkLink**](VirtualNetworkLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

