# SolarVps.DnsApi

All URIs are relative to *http://api.ss.solarvps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsDomainAddPost**](DnsApi.md#dnsDomainAddPost) | **POST** /dns/{domain}/add | Add dns record for given domain
[**dnsDomainDeletePost**](DnsApi.md#dnsDomainDeletePost) | **POST** /dns/{domain}/delete | Delete dns record for a given domain
[**dnsDomainGet**](DnsApi.md#dnsDomainGet) | **GET** /dns/{domain} | View all your records for a given domain
[**dnsDomainUpdatePost**](DnsApi.md#dnsDomainUpdatePost) | **POST** /dns/{domain}/update | Update dns record for a given domain



## dnsDomainAddPost

> dnsDomainAddPost(domain, name, type, content, ttl, prio)

Add dns record for given domain

You can try example.com below. Types allowed are: A CNAME NS TXT MX SRV SPF

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DnsApi();
let domain = "domain_example"; // String | Domain you want to add records for
let name = "name_example"; // String | Fully qualified DNS name
let type = "type_example"; // String | Type of DNS record
let content = "content_example"; // String | Content for DNS record
let ttl = "ttl_example"; // String | Time To Live for DNS record
let prio = "prio_example"; // String | Priority of DNS record
apiInstance.dnsDomainAddPost(domain, name, type, content, ttl, prio, (error, data, response) => {
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
 **domain** | **String**| Domain you want to add records for | 
 **name** | **String**| Fully qualified DNS name | 
 **type** | **String**| Type of DNS record | 
 **content** | **String**| Content for DNS record | 
 **ttl** | **String**| Time To Live for DNS record | 
 **prio** | **String**| Priority of DNS record | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dnsDomainDeletePost

> dnsDomainDeletePost(domain, id)

Delete dns record for a given domain

Shows all your records for a specific domain. You can try example.com below.

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DnsApi();
let domain = "domain_example"; // String | Domain name you want to get records for
let id = "id_example"; // String | Id of the DNS Record
apiInstance.dnsDomainDeletePost(domain, id, (error, data, response) => {
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
 **domain** | **String**| Domain name you want to get records for | 
 **id** | **String**| Id of the DNS Record | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dnsDomainGet

> dnsDomainGet(domain)

View all your records for a given domain

Shows all your records for a specific domain. You can try example.com below.

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DnsApi();
let domain = "domain_example"; // String | Domain name you want to get records for
apiInstance.dnsDomainGet(domain, (error, data, response) => {
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
 **domain** | **String**| Domain name you want to get records for | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dnsDomainUpdatePost

> dnsDomainUpdatePost(domain, id, opts)

Update dns record for a given domain

You can try example.com below.

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DnsApi();
let domain = "domain_example"; // String | Domain name to add record under
let id = "id_example"; // String | Id of DNS record
let opts = {
  'name': "name_example", // String | Fully qualified name for the DNS record
  'type': "type_example", // String | Type for DNS record
  'content': "content_example", // String | Content for the DNS Record
  'ttl': "ttl_example", // String | Time To Live for DNS record
  'prio': "prio_example" // String | Priority of the DNS record
};
apiInstance.dnsDomainUpdatePost(domain, id, opts, (error, data, response) => {
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
 **domain** | **String**| Domain name to add record under | 
 **id** | **String**| Id of DNS record | 
 **name** | **String**| Fully qualified name for the DNS record | [optional] 
 **type** | **String**| Type for DNS record | [optional] 
 **content** | **String**| Content for the DNS Record | [optional] 
 **ttl** | **String**| Time To Live for DNS record | [optional] 
 **prio** | **String**| Priority of the DNS record | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

