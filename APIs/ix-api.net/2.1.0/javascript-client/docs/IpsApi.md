# IxApi.IpsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipsCreate**](IpsApi.md#ipsCreate) | **POST** /ips | 
[**ipsList**](IpsApi.md#ipsList) | **GET** /ips | 
[**ipsPartialUpdate**](IpsApi.md#ipsPartialUpdate) | **PATCH** /ips/{id} | 
[**ipsRead**](IpsApi.md#ipsRead) | **GET** /ips/{id} | 
[**ipsUpdate**](IpsApi.md#ipsUpdate) | **PUT** /ips/{id} | 



## ipsCreate

> IpAddress ipsCreate(opts)



Add an ip host address or network prefix.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.IpsApi();
let opts = {
  'ipAddressRequest': new IxApi.IpAddressRequest() // IpAddressRequest | IP-Address / Prefix allocation Request
};
apiInstance.ipsCreate(opts, (error, data, response) => {
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
 **ipAddressRequest** | [**IpAddressRequest**](IpAddressRequest.md)| IP-Address / Prefix allocation Request | [optional] 

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipsList

> [IpAddress] ipsList(opts)



List all ip addresses (and prefixes).

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.IpsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'managingAccount': "managingAccount_example", // String | Filter by managing_account
  'consumingAccount': "consumingAccount_example", // String | Filter by consuming_account
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'networkService': "networkService_example", // String | Filter by network_service
  'networkServiceConfig': "networkServiceConfig_example", // String | Filter by network_service_config
  'networkFeature': "networkFeature_example", // String | Filter by network_feature
  'networkFeatureConfig': "networkFeatureConfig_example", // String | Filter by network_feature_config
  'version': 56, // Number | Filter by version
  'fqdn': "fqdn_example", // String | Filter by fqdn
  'prefixLength': 56, // Number | Filter by prefix_length
  'validNotBefore': "validNotBefore_example", // String | Filter by valid_not_before
  'validNotAfter': "validNotAfter_example" // String | Filter by valid_not_after
};
apiInstance.ipsList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **managingAccount** | **String**| Filter by managing_account | [optional] 
 **consumingAccount** | **String**| Filter by consuming_account | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 
 **networkService** | **String**| Filter by network_service | [optional] 
 **networkServiceConfig** | **String**| Filter by network_service_config | [optional] 
 **networkFeature** | **String**| Filter by network_feature | [optional] 
 **networkFeatureConfig** | **String**| Filter by network_feature_config | [optional] 
 **version** | **Number**| Filter by version | [optional] 
 **fqdn** | **String**| Filter by fqdn | [optional] 
 **prefixLength** | **Number**| Filter by prefix_length | [optional] 
 **validNotBefore** | **String**| Filter by valid_not_before | [optional] 
 **validNotAfter** | **String**| Filter by valid_not_after | [optional] 

### Return type

[**[IpAddress]**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipsPartialUpdate

> IpAddress ipsPartialUpdate(id, opts)



Update parts of an ip address.   As with the &#x60;PUT&#x60; opertaion, IP addresses, where you don&#39;t have update rights, will yield a &#x60;resource access denied&#x60; error when attempting an update.  If the ip address was allocated for you, you might not be able to change anything but the &#x60;fqdn&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.IpsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'ipAddressUpdatePartial': new IxApi.IpAddressUpdatePartial() // IpAddressUpdatePartial | IP-Address Update
};
apiInstance.ipsPartialUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **ipAddressUpdatePartial** | [**IpAddressUpdatePartial**](IpAddressUpdatePartial.md)| IP-Address Update | [optional] 

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json


## ipsRead

> IpAddress ipsRead(id)



Get a single ip addresses by it&#39;s id.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.IpsApi();
let id = "id_example"; // String | Get by id
apiInstance.ipsRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipsUpdate

> IpAddress ipsUpdate(id, opts)



Update an ip address object.  You can only update IP addresses within your current scope. Not all addresses you can read you can update.  If the ip address was allocated for you, you might not be able to change anything but the &#x60;fqdn&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.IpsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'ipAddressUpdate': new IxApi.IpAddressUpdate() // IpAddressUpdate | IP-Address Update
};
apiInstance.ipsUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **ipAddressUpdate** | [**IpAddressUpdate**](IpAddressUpdate.md)| IP-Address Update | [optional] 

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

