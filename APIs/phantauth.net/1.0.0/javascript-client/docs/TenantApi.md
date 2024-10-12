# PhantAuth.TenantApi

All URIs are relative to *https://phantauth.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantTenantnameGet**](TenantApi.md#tenantTenantnameGet) | **GET** /tenant/{tenantname} | Get a Tenant



## tenantTenantnameGet

> TenantTenantnameGet200Response tenantTenantnameGet(tenantname)

Get a Tenant

This endpoint allows you to get the data of a given PhantAuth tenant. To use the PhantAuth services, you don&#39;t need this endpoint. It is, therefore, mainly used for debug/diagnostic purposes in tenant customization.  Tenantname is the name of the full DNS domain of the tenant you get. In the case of an official and shared tenant (phantauth.net and phantauth.cf DNS domains), the DNS domain can be omitted (e.g. *default* or *faker*).

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.TenantApi();
let tenantname = "tenantname_example"; // String | The tenant ID integrated in the `sub` property.
apiInstance.tenantTenantnameGet(tenantname, (error, data, response) => {
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
 **tenantname** | **String**| The tenant ID integrated in the &#x60;sub&#x60; property. | 

### Return type

[**TenantTenantnameGet200Response**](TenantTenantnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

