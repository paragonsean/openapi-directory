# DnsManagementClient.ZonesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zonesCreateOrUpdate**](ZonesApi.md#zonesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} | 
[**zonesDelete**](ZonesApi.md#zonesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} | 
[**zonesGet**](ZonesApi.md#zonesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} | 
[**zonesList**](ZonesApi.md#zonesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/dnszones | 
[**zonesListByResourceGroup**](ZonesApi.md#zonesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones | 



## zonesCreateOrUpdate

> Zone zonesCreateOrUpdate(resourceGroupName, zoneName, apiVersion, subscriptionId, parameters, opts)



Creates or updates a DNS zone. Does not modify DNS records within the zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.ZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new DnsManagementClient.Zone(); // Zone | Parameters supplied to the CreateOrUpdate operation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.
};
apiInstance.zonesCreateOrUpdate(resourceGroupName, zoneName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Zone**](Zone.md)| Parameters supplied to the CreateOrUpdate operation. | 
 **ifMatch** | **String**| The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. | [optional] 

### Return type

[**Zone**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## zonesDelete

> zonesDelete(resourceGroupName, zoneName, apiVersion, subscriptionId, opts)



Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.ZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'ifMatch': "ifMatch_example" // String | The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
};
apiInstance.zonesDelete(resourceGroupName, zoneName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## zonesGet

> Zone zonesGet(resourceGroupName, zoneName, apiVersion, subscriptionId)



Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.ZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.zonesGet(resourceGroupName, zoneName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**Zone**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## zonesList

> ZoneListResult zonesList(apiVersion, subscriptionId, opts)



Lists the DNS zones in all resource groups in a subscription.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.ZonesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56 // Number | The maximum number of DNS zones to return. If not specified, returns up to 100 zones.
};
apiInstance.zonesList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **top** | **Number**| The maximum number of DNS zones to return. If not specified, returns up to 100 zones. | [optional] 

### Return type

[**ZoneListResult**](ZoneListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## zonesListByResourceGroup

> ZoneListResult zonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Lists the DNS zones within a resource group.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.ZonesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56 // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
};
apiInstance.zonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 

### Return type

[**ZoneListResult**](ZoneListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

