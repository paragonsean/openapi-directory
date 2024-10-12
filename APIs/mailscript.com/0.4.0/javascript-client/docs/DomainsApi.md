# Mailscript.DomainsApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDomain**](DomainsApi.md#addDomain) | **POST** /domains | Claim a new Domain
[**checkDomainVerify**](DomainsApi.md#checkDomainVerify) | **POST** /domains/verify/{domain} | Check a new Domain
[**getAllDomains**](DomainsApi.md#getAllDomains) | **GET** /domains | Get all domains you have access to
[**getDomainVerify**](DomainsApi.md#getDomainVerify) | **GET** /domains/verify/{domain} | Get domain verification
[**removeDomainVerify**](DomainsApi.md#removeDomainVerify) | **DELETE** /domains/{domain} | Remove a domain



## addDomain

> DomainResponse addDomain(addDomainRequest)

Claim a new Domain



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.DomainsApi();
let addDomainRequest = new Mailscript.AddDomainRequest(); // AddDomainRequest | Domain body
apiInstance.addDomain(addDomainRequest, (error, data, response) => {
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
 **addDomainRequest** | [**AddDomainRequest**](AddDomainRequest.md)| Domain body | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkDomainVerify

> CheckDomainVerify checkDomainVerify(domain)

Check a new Domain



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.DomainsApi();
let domain = "domain_example"; // String | Full Top-level domain name
apiInstance.checkDomainVerify(domain, (error, data, response) => {
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
 **domain** | **String**| Full Top-level domain name | 

### Return type

[**CheckDomainVerify**](CheckDomainVerify.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllDomains

> GetAllDomainsResponse getAllDomains()

Get all domains you have access to



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.DomainsApi();
apiInstance.getAllDomains((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllDomainsResponse**](GetAllDomainsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainVerify

> DomainResponse getDomainVerify(domain)

Get domain verification



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.DomainsApi();
let domain = "domain_example"; // String | Full Top-level domain name
apiInstance.getDomainVerify(domain, (error, data, response) => {
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
 **domain** | **String**| Full Top-level domain name | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeDomainVerify

> removeDomainVerify(domain)

Remove a domain



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.DomainsApi();
let domain = "domain_example"; // String | Full Top-level domain name
apiInstance.removeDomainVerify(domain, (error, data, response) => {
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
 **domain** | **String**| Full Top-level domain name | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

