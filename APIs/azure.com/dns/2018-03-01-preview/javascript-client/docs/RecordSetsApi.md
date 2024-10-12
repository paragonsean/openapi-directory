# DnsManagementClient.RecordSetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recordSetsCreateOrUpdate**](RecordSetsApi.md#recordSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} | 
[**recordSetsDelete**](RecordSetsApi.md#recordSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} | 
[**recordSetsGet**](RecordSetsApi.md#recordSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} | 
[**recordSetsListAllByDnsZone**](RecordSetsApi.md#recordSetsListAllByDnsZone) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/all | 
[**recordSetsListByDnsZone**](RecordSetsApi.md#recordSetsListByDnsZone) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/recordsets | 
[**recordSetsListByType**](RecordSetsApi.md#recordSetsListByType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType} | 
[**recordSetsUpdate**](RecordSetsApi.md#recordSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} | 



## recordSetsCreateOrUpdate

> RecordSet recordSetsCreateOrUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, opts)



Creates or updates a record set within a DNS zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let recordType = "recordType_example"; // String | The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new DnsManagementClient.RecordSet(); // RecordSet | Parameters supplied to the CreateOrUpdate operation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.
};
apiInstance.recordSetsCreateOrUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created). | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the CreateOrUpdate operation. | 
 **ifMatch** | **String**| The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored. | [optional] 

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recordSetsDelete

> recordSetsDelete(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, opts)



Deletes a record set from a DNS zone. This operation cannot be undone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let recordType = "recordType_example"; // String | The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'ifMatch': "ifMatch_example" // String | The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
};
apiInstance.recordSetsDelete(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted). | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsGet

> RecordSet recordSetsGet(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId)



Gets a record set.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let recordType = "recordType_example"; // String | The type of DNS record in this record set.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.recordSetsGet(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, (error, data, response) => {
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
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **recordType** | **String**| The type of DNS record in this record set. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsListAllByDnsZone

> RecordSetListResult recordSetsListAllByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, opts)



Lists all record sets in a DNS zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56, // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
  'recordsetnamesuffix': "recordsetnamesuffix_example" // String | The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .<recordSetNameSuffix>
};
apiInstance.recordSetsListAllByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 
 **recordsetnamesuffix** | **String**| The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .&lt;recordSetNameSuffix&gt; | [optional] 

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsListByDnsZone

> RecordSetListResult recordSetsListByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, opts)



Lists all record sets in a DNS zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56, // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
  'recordsetnamesuffix': "recordsetnamesuffix_example" // String | The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .<recordSetNameSuffix>
};
apiInstance.recordSetsListByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 
 **recordsetnamesuffix** | **String**| The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .&lt;recordSetNameSuffix&gt; | [optional] 

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsListByType

> RecordSetListResult recordSetsListByType(resourceGroupName, zoneName, recordType, apiVersion, subscriptionId, opts)



Lists the record sets of a specified type in a DNS zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let recordType = "recordType_example"; // String | The type of record sets to enumerate.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56, // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
  'recordsetnamesuffix': "recordsetnamesuffix_example" // String | The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .<recordSetNameSuffix>
};
apiInstance.recordSetsListByType(resourceGroupName, zoneName, recordType, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **recordType** | **String**| The type of record sets to enumerate. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 
 **recordsetnamesuffix** | **String**| The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .&lt;recordSetNameSuffix&gt; | [optional] 

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsUpdate

> RecordSet recordSetsUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, opts)



Updates a record set within a DNS zone.

### Example

```javascript
import DnsManagementClient from 'dns_management_client';

let apiInstance = new DnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let recordType = "recordType_example"; // String | The type of DNS record in this record set.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new DnsManagementClient.RecordSet(); // RecordSet | Parameters supplied to the Update operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting concurrent changes.
};
apiInstance.recordSetsUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **recordType** | **String**| The type of DNS record in this record set. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the Update operation. | 
 **ifMatch** | **String**| The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting concurrent changes. | [optional] 

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

