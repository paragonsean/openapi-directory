# MtaaApiDocumentation.DistrictsInRegionApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**districtsInARegion**](DistrictsInRegionApi.md#districtsInARegion) | **GET** /{country}/{region} | Returns all districts in region



## districtsInARegion

> districtsInARegion(country, region)

Returns all districts in region

Returns a post code and all districts in a specified region

### Example

```javascript
import MtaaApiDocumentation from 'mtaa_api_documentation';

let apiInstance = new MtaaApiDocumentation.DistrictsInRegionApi();
let country = "country_example"; // String | Country name in lowercase eg( tanzania)
let region = "region_example"; // String | Name of the region eg (Mbeya)
apiInstance.districtsInARegion(country, region, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

