# MtaaApiDocumentation.TanzaniaRegionsApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tanzaniaRegions**](TanzaniaRegionsApi.md#tanzaniaRegions) | **GET** /{country} | Returns all regions present in Tanzania



## tanzaniaRegions

> tanzaniaRegions(country)

Returns all regions present in Tanzania

Fetches all regions present in Tanzania and then return a response as json

### Example

```javascript
import MtaaApiDocumentation from 'mtaa_api_documentation';

let apiInstance = new MtaaApiDocumentation.TanzaniaRegionsApi();
let country = "country_example"; // String | Country name in lowercase eg (Tanzania)
apiInstance.tanzaniaRegions(country, (error, data, response) => {
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
 **country** | **String**| Country name in lowercase eg (Tanzania) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

