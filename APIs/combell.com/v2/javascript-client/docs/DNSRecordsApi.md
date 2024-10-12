# PublicApi.DNSRecordsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsDomainNameRecordsGet**](DNSRecordsApi.md#dnsDomainNameRecordsGet) | **GET** /dns/{domainName}/records | Get records
[**dnsDomainNameRecordsPost**](DNSRecordsApi.md#dnsDomainNameRecordsPost) | **POST** /dns/{domainName}/records | Create a record
[**dnsDomainNameRecordsRecordIdDelete**](DNSRecordsApi.md#dnsDomainNameRecordsRecordIdDelete) | **DELETE** /dns/{domainName}/records/{recordId} | Delete a record
[**dnsDomainNameRecordsRecordIdGet**](DNSRecordsApi.md#dnsDomainNameRecordsRecordIdGet) | **GET** /dns/{domainName}/records/{recordId} | Get specific record
[**dnsDomainNameRecordsRecordIdPut**](DNSRecordsApi.md#dnsDomainNameRecordsRecordIdPut) | **PUT** /dns/{domainName}/records/{recordId} | Edit a record



## dnsDomainNameRecordsGet

> [DnsRecord] dnsDomainNameRecordsGet(domainName, domainName2, opts)

Get records

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DNSRecordsApi();
let domainName = "domainName_example"; // String | The domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56, // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
  'type': "type_example", // String | Filters records matching the type. Most other filters only apply when this filter is specified.
  'recordName': "recordName_example", // String | Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records.
  'service': "service_example" // String | Filters records for the service. This filter only applies to lookups of SRV records.
};
apiInstance.dnsDomainNameRecordsGet(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **domainName2** | **String**| Automatically added | 
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 
 **type** | **String**| Filters records matching the type. Most other filters only apply when this filter is specified. | [optional] 
 **recordName** | **String**| Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records. | [optional] 
 **service** | **String**| Filters records for the service. This filter only applies to lookups of SRV records. | [optional] 

### Return type

[**[DnsRecord]**](DnsRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsDomainNameRecordsPost

> dnsDomainNameRecordsPost(domainName, domainName2, opts)

Create a record

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DNSRecordsApi();
let domainName = "domainName_example"; // String | The domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'dnsRecord': new PublicApi.DnsRecord() // DnsRecord | The record to create
};
apiInstance.dnsDomainNameRecordsPost(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **domainName2** | **String**| Automatically added | 
 **dnsRecord** | [**DnsRecord**](DnsRecord.md)| The record to create | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## dnsDomainNameRecordsRecordIdDelete

> dnsDomainNameRecordsRecordIdDelete(domainName, recordId, domainName2, recordId2)

Delete a record

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DNSRecordsApi();
let domainName = "domainName_example"; // String | The domain name.
let recordId = "recordId_example"; // String | The id of the record.
let domainName2 = "domainName_example"; // String | Automatically added
let recordId2 = "recordId_example"; // String | Automatically added
apiInstance.dnsDomainNameRecordsRecordIdDelete(domainName, recordId, domainName2, recordId2, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **recordId** | **String**| The id of the record. | 
 **domainName2** | **String**| Automatically added | 
 **recordId2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dnsDomainNameRecordsRecordIdGet

> DnsRecord dnsDomainNameRecordsRecordIdGet(domainName, recordId, domainName2, recordId2)

Get specific record

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DNSRecordsApi();
let domainName = "domainName_example"; // String | The domain name.
let recordId = "recordId_example"; // String | The id of the record.
let domainName2 = "domainName_example"; // String | Automatically added
let recordId2 = "recordId_example"; // String | Automatically added
apiInstance.dnsDomainNameRecordsRecordIdGet(domainName, recordId, domainName2, recordId2, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **recordId** | **String**| The id of the record. | 
 **domainName2** | **String**| Automatically added | 
 **recordId2** | **String**| Automatically added | 

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsDomainNameRecordsRecordIdPut

> dnsDomainNameRecordsRecordIdPut(domainName, recordId, domainName2, recordId2, opts)

Edit a record

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DNSRecordsApi();
let domainName = "domainName_example"; // String | The domain name.
let recordId = "recordId_example"; // String | The id of the record.
let domainName2 = "domainName_example"; // String | Automatically added
let recordId2 = "recordId_example"; // String | Automatically added
let opts = {
  'dnsRecord': new PublicApi.DnsRecord() // DnsRecord | The record with updated values.
};
apiInstance.dnsDomainNameRecordsRecordIdPut(domainName, recordId, domainName2, recordId2, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **recordId** | **String**| The id of the record. | 
 **domainName2** | **String**| Automatically added | 
 **recordId2** | **String**| Automatically added | 
 **dnsRecord** | [**DnsRecord**](DnsRecord.md)| The record with updated values. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

