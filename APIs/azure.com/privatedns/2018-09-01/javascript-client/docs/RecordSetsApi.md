# PrivateDnsManagementClient.RecordSetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recordSetsCreateOrUpdate**](RecordSetsApi.md#recordSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} | 
[**recordSetsDelete**](RecordSetsApi.md#recordSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} | 
[**recordSetsGet**](RecordSetsApi.md#recordSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} | 
[**recordSetsList**](RecordSetsApi.md#recordSetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/ALL | 
[**recordSetsListByType**](RecordSetsApi.md#recordSetsListByType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType} | 
[**recordSetsUpdate**](RecordSetsApi.md#recordSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} | 



## recordSetsCreateOrUpdate

> RecordSet recordSetsCreateOrUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, opts)



Creates or updates a record set within a Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let recordType = "recordType_example"; // String | The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the Private DNS zone is created).
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new PrivateDnsManagementClient.RecordSet(); // RecordSet | Parameters supplied to the CreateOrUpdate operation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.
};
apiInstance.recordSetsCreateOrUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the Private DNS zone is created). | 
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the CreateOrUpdate operation. | 
 **ifMatch** | **String**| The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored. | [optional] 

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recordSetsDelete

> recordSetsDelete(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, opts)



Deletes a record set from a Private DNS zone. This operation cannot be undone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let recordType = "recordType_example"; // String | The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the Private DNS zone is deleted).
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the record set. Omit this value to always delete the current record set. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
};
apiInstance.recordSetsDelete(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the Private DNS zone is deleted). | 
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **ifMatch** | **String**| The ETag of the record set. Omit this value to always delete the current record set. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsGet

> RecordSet recordSetsGet(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId)



Gets a record set.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let recordType = "recordType_example"; // String | The type of DNS record in this record set.
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.recordSetsGet(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **recordType** | **String**| The type of DNS record in this record set. | 
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsList

> RecordSetListResult recordSetsList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, opts)



Lists all record sets in a Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56, // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
  'recordsetnamesuffix': "recordsetnamesuffix_example" // String | The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \".<recordsetnamesuffix>\".
};
apiInstance.recordSetsList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 
 **recordsetnamesuffix** | **String**| The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \&quot;.&lt;recordsetnamesuffix&gt;\&quot;. | [optional] 

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsListByType

> RecordSetListResult recordSetsListByType(resourceGroupName, privateZoneName, recordType, apiVersion, subscriptionId, opts)



Lists the record sets of a specified type in a Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let recordType = "recordType_example"; // String | The type of record sets to enumerate.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56, // Number | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
  'recordsetnamesuffix': "recordsetnamesuffix_example" // String | The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \".<recordsetnamesuffix>\".
};
apiInstance.recordSetsListByType(resourceGroupName, privateZoneName, recordType, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **recordType** | **String**| The type of record sets to enumerate. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] 
 **recordsetnamesuffix** | **String**| The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \&quot;.&lt;recordsetnamesuffix&gt;\&quot;. | [optional] 

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordSetsUpdate

> RecordSet recordSetsUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, opts)



Updates a record set within a Private DNS zone.

### Example

```javascript
import PrivateDnsManagementClient from 'private_dns_management_client';

let apiInstance = new PrivateDnsManagementClient.RecordSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
let recordType = "recordType_example"; // String | The type of DNS record in this record set.
let relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new PrivateDnsManagementClient.RecordSet(); // RecordSet | Parameters supplied to the Update operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
};
apiInstance.recordSetsUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **recordType** | **String**| The type of DNS record in this record set. | 
 **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the Update operation. | 
 **ifMatch** | **String**| The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

