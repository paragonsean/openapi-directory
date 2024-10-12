# MtaaApiDocumentation.WardsInADistrictApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wardsInADistrict**](WardsInADistrictApi.md#wardsInADistrict) | **GET** /{country}/{region}/{district} | Returns all wards in a district



## wardsInADistrict

> wardsInADistrict(country, region, district)

Returns all wards in a district

Returns all wards in a  specified district and district postcode

### Example

```javascript
import MtaaApiDocumentation from 'mtaa_api_documentation';

let apiInstance = new MtaaApiDocumentation.WardsInADistrictApi();
let country = "country_example"; // String | Country name in lowercase eg( tanzania)
let region = "region_example"; // String | Name of the region eg (Mbeya)
let district = "district_example"; // String | Name of the District eg (Rungwe)
apiInstance.wardsInADistrict(country, region, district, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

