# AgcoApi.DealerByCountryApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dealerByCountryGetCountries**](DealerByCountryApi.md#dealerByCountryGetCountries) | **GET** /api/v2/DealerByCountry | Get a total count of dealers per country



## dealerByCountryGetCountries

> APIPagedResponseDealerDBModelsDealersPerCountry dealerByCountryGetCountries(opts)

Get a total count of dealers per country

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.DealerByCountryApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.dealerByCountryGetCountries(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseDealerDBModelsDealersPerCountry**](APIPagedResponseDealerDBModelsDealersPerCountry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

