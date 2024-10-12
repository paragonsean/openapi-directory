# PhantAuth.DomainApi

All URIs are relative to *https://phantauth.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainDomainnameGet**](DomainApi.md#domainDomainnameGet) | **GET** /domain/{domainname} | Get a Domain



## domainDomainnameGet

> DomainDomainnameGet200Response domainDomainnameGet(domainname)

Get a Domain

This endpoint allows you to get the data of a given PhantAuth domain. To use the PhantAuth services, you don&#39;t need this endpoint. It is, therefore, mainly used for debug/diagnostic purposes in tenant customization.  Domainname is the fully qualified DNS name of the domain you get (e.g. *phantauth.net* or *phantauth.cf*).

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.DomainApi();
let domainname = "domainname_example"; // String | The domain ID integrated in the `sub` property.
apiInstance.domainDomainnameGet(domainname, (error, data, response) => {
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
 **domainname** | **String**| The domain ID integrated in the &#x60;sub&#x60; property. | 

### Return type

[**DomainDomainnameGet200Response**](DomainDomainnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

