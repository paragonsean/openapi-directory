# NetlifysApiDocumentation.DnsZoneApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureDNSForSite**](DnsZoneApi.md#configureDNSForSite) | **PUT** /sites/{site_id}/dns | 
[**createDnsRecord**](DnsZoneApi.md#createDnsRecord) | **POST** /dns_zones/{zone_id}/dns_records | 
[**createDnsZone**](DnsZoneApi.md#createDnsZone) | **POST** /dns_zones | 
[**deleteDnsRecord**](DnsZoneApi.md#deleteDnsRecord) | **DELETE** /dns_zones/{zone_id}/dns_records/{dns_record_id} | 
[**deleteDnsZone**](DnsZoneApi.md#deleteDnsZone) | **DELETE** /dns_zones/{zone_id} | 
[**getDNSForSite**](DnsZoneApi.md#getDNSForSite) | **GET** /sites/{site_id}/dns | 
[**getDnsRecords**](DnsZoneApi.md#getDnsRecords) | **GET** /dns_zones/{zone_id}/dns_records | 
[**getDnsZone**](DnsZoneApi.md#getDnsZone) | **GET** /dns_zones/{zone_id} | 
[**getDnsZones**](DnsZoneApi.md#getDnsZones) | **GET** /dns_zones | 
[**getIndividualDnsRecord**](DnsZoneApi.md#getIndividualDnsRecord) | **GET** /dns_zones/{zone_id}/dns_records/{dns_record_id} | 
[**transferDnsZone**](DnsZoneApi.md#transferDnsZone) | **PUT** /dns_zones/{zone_id}/transfer | 



## configureDNSForSite

> [DnsZone] configureDNSForSite(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let siteId = "siteId_example"; // String | 
apiInstance.configureDNSForSite(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**[DnsZone]**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDnsRecord

> DnsRecord createDnsRecord(zoneId, dnsRecord)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
let dnsRecord = new NetlifysApiDocumentation.DnsRecordCreate(); // DnsRecordCreate | 
apiInstance.createDnsRecord(zoneId, dnsRecord, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **dnsRecord** | [**DnsRecordCreate**](DnsRecordCreate.md)|  | 

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDnsZone

> DnsZone createDnsZone(dnsZoneParams)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let dnsZoneParams = new NetlifysApiDocumentation.DnsZoneSetup(); // DnsZoneSetup | 
apiInstance.createDnsZone(dnsZoneParams, (error, data, response) => {
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
 **dnsZoneParams** | [**DnsZoneSetup**](DnsZoneSetup.md)|  | 

### Return type

[**DnsZone**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDnsRecord

> deleteDnsRecord(zoneId, dnsRecordId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
let dnsRecordId = "dnsRecordId_example"; // String | 
apiInstance.deleteDnsRecord(zoneId, dnsRecordId, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **dnsRecordId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDnsZone

> deleteDnsZone(zoneId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
apiInstance.deleteDnsZone(zoneId, (error, data, response) => {
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
 **zoneId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDNSForSite

> [DnsZone] getDNSForSite(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let siteId = "siteId_example"; // String | 
apiInstance.getDNSForSite(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**[DnsZone]**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDnsRecords

> [DnsRecord] getDnsRecords(zoneId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
apiInstance.getDnsRecords(zoneId, (error, data, response) => {
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
 **zoneId** | **String**|  | 

### Return type

[**[DnsRecord]**](DnsRecord.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDnsZone

> DnsZone getDnsZone(zoneId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
apiInstance.getDnsZone(zoneId, (error, data, response) => {
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
 **zoneId** | **String**|  | 

### Return type

[**DnsZone**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDnsZones

> [DnsZone] getDnsZones(opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let opts = {
  'accountSlug': "accountSlug_example" // String | 
};
apiInstance.getDnsZones(opts, (error, data, response) => {
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
 **accountSlug** | **String**|  | [optional] 

### Return type

[**[DnsZone]**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIndividualDnsRecord

> DnsRecord getIndividualDnsRecord(zoneId, dnsRecordId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
let dnsRecordId = "dnsRecordId_example"; // String | 
apiInstance.getIndividualDnsRecord(zoneId, dnsRecordId, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **dnsRecordId** | **String**|  | 

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transferDnsZone

> DnsZone transferDnsZone(zoneId, accountId, transferAccountId, transferUserId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DnsZoneApi();
let zoneId = "zoneId_example"; // String | 
let accountId = "accountId_example"; // String | the account of the dns zone
let transferAccountId = "transferAccountId_example"; // String | the account you want to transfer the dns zone to
let transferUserId = "transferUserId_example"; // String | the user you want to transfer the dns zone to
apiInstance.transferDnsZone(zoneId, accountId, transferAccountId, transferUserId, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **accountId** | **String**| the account of the dns zone | 
 **transferAccountId** | **String**| the account you want to transfer the dns zone to | 
 **transferUserId** | **String**| the user you want to transfer the dns zone to | 

### Return type

[**DnsZone**](DnsZone.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

