# AgcoApi.BrandsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brandsBrands**](BrandsApi.md#brandsBrands) | **GET** /api/v2/Brands | Gets a list of Brands.



## brandsBrands

> [String] brandsBrands()

Gets a list of Brands.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.BrandsApi();
apiInstance.brandsBrands((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

