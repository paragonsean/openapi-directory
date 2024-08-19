# MtaaApiDocumentation.StreetsInAWardApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**streetsInAWard**](StreetsInAWardApi.md#streetsInAWard) | **GET** /{country}/{region}/{district}/{ward} | Returns all streets in a ward



## streetsInAWard

> streetsInAWard(country, region, district, ward)

Returns all streets in a ward

Returns all streets in a specified ward and ward postcode

### Example

```javascript
import MtaaApiDocumentation from 'mtaa_api_documentation';

let apiInstance = new MtaaApiDocumentation.StreetsInAWardApi();
let country = "country_example"; // String | Country name in lowercase eg( tanzania)
let region = "region_example"; // String | Name of the region eg (Mbeya)
let district = "district_example"; // String | Name of the District eg (Rungwe)
let ward = "ward_example"; // String | Name of the Ward eg (Kiwira)
apiInstance.streetsInAWard(country, region, district, ward, (error, data, response) => {
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
 **country** | **String**| Country name in lowercase eg( tanzania) | 
 **region** | **String**| Name of the region eg (Mbeya) | 
 **district** | **String**| Name of the District eg (Rungwe) | 
 **ward** | **String**| Name of the Ward eg (Kiwira) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

