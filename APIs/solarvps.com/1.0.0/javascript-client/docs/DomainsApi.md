# SolarVps.DomainsApi

All URIs are relative to *http://api.ss.solarvps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsAddPost**](DomainsApi.md#domainsAddPost) | **POST** /domains/add | Add domain to be managed by SolarVPS Distributed DNS
[**domainsDeletePost**](DomainsApi.md#domainsDeletePost) | **POST** /domains/delete | Delete domain from SolarVPS Distributed DNS
[**domainsGet**](DomainsApi.md#domainsGet) | **GET** /domains | View all your domains managed by SolarVPS Distributed DNS



## domainsAddPost

> domainsAddPost(domain)

Add domain to be managed by SolarVPS Distributed DNS

Adds domain to SolarVPS Distributed DNS

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DomainsApi();
let domain = "domain_example"; // String | Domain to add to SolarVPS Distributed DNS
apiInstance.domainsAddPost(domain, (error, data, response) => {
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
 **domain** | **String**| Domain to add to SolarVPS Distributed DNS | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainsDeletePost

> domainsDeletePost(domain)

Delete domain from SolarVPS Distributed DNS

Deletes domain from SolarVPS Distributed DNS

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DomainsApi();
let domain = "domain_example"; // String | Domain to delete from SolarVPS Distributed DNS
apiInstance.domainsDeletePost(domain, (error, data, response) => {
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
 **domain** | **String**| Domain to delete from SolarVPS Distributed DNS | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainsGet

> domainsGet()

View all your domains managed by SolarVPS Distributed DNS

Shows all your domains

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.DomainsApi();
apiInstance.domainsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

