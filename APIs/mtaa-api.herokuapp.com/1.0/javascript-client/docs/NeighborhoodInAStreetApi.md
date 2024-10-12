# MtaaApiDocumentation.NeighborhoodInAStreetApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**neighborhoodInAStreet**](NeighborhoodInAStreetApi.md#neighborhoodInAStreet) | **GET** /{country}/{region}/{district}/{ward}/{street} | Returns all neighborhood in a street



## neighborhoodInAStreet

> neighborhoodInAStreet(country, region, district, ward, street)

Returns all neighborhood in a street

Returns all neighborhood in a specified street

### Example

```javascript
import MtaaApiDocumentation from 'mtaa_api_documentation';

let apiInstance = new MtaaApiDocumentation.NeighborhoodInAStreetApi();
let country = "country_example"; // String | Country name in lowercase eg( tanzania)
let region = "region_example"; // String | Name of the region eg (Mbeya)
let district = "district_example"; // String | Name of the District eg (Rungwe)
let ward = "ward_example"; // String | Name of the Ward eg (Kiwira)
let street = "street_example"; // String | Name of the Street eg (Ilundo)
apiInstance.neighborhoodInAStreet(country, region, district, ward, street, (error, data, response) => {
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
 **street** | **String**| Name of the Street eg (Ilundo) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

