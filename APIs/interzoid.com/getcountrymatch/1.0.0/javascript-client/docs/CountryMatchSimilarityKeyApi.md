# InterzoidGetCountryMatchSimilarityKeyApi.CountryMatchSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcountrymatch**](CountryMatchSimilarityKeyApi.md#getcountrymatch) | **GET** /getcountrymatch | Gets a similarity key for matching purposes for country name data



## getcountrymatch

> Getcountrymatch200Response getcountrymatch(license, country)

Gets a similarity key for matching purposes for country name data

Gets a similarity key to use for matching purposes for country name data

### Example

```javascript
import InterzoidGetCountryMatchSimilarityKeyApi from 'interzoid_get_country_match_similarity_key_api';

let apiInstance = new InterzoidGetCountryMatchSimilarityKeyApi.CountryMatchSimilarityKeyApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let country = "country_example"; // String | Country name from which to generate similarity key
apiInstance.getcountrymatch(license, country, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **country** | **String**| Country name from which to generate similarity key | 

### Return type

[**Getcountrymatch200Response**](Getcountrymatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

