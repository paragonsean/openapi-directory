# TravelRecommendationsApi.RecommendedLocationsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecommendedLocation**](RecommendedLocationsApi.md#getRecommendedLocation) | **GET** /reference-data/recommended-locations | GET recommended destinations



## getRecommendedLocation

> GetRecommendedLocation200Response getRecommendedLocation(cityCodes, opts)

GET recommended destinations



### Example

```javascript
import TravelRecommendationsApi from 'travel_recommendations_api';

let apiInstance = new TravelRecommendationsApi.RecommendedLocationsApi();
let cityCodes = "PAR"; // String | City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx)
let opts = {
  'travelerCountryCode': "FR", // String | Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US)
  'destinationCountryCodes': "destinationCountryCodes_example" // String | List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US)
};
apiInstance.getRecommendedLocation(cityCodes, opts, (error, data, response) => {
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
 **cityCodes** | **String**| City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx) | 
 **travelerCountryCode** | **String**| Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) | [optional] [default to &#39;FR&#39;]
 **destinationCountryCodes** | **String**| List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) | [optional] 

### Return type

[**GetRecommendedLocation200Response**](GetRecommendedLocation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

