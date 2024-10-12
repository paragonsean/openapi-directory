# FlightCheckInLinks.CheckinLinksApi

All URIs are relative to *https://test.api.amadeus.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCheckinURLs**](CheckinLinksApi.md#getCheckinURLs) | **GET** /reference-data/urls/checkin-links | Lists Check-in URLs.



## getCheckinURLs

> Success getCheckinURLs(airlineCode, opts)

Lists Check-in URLs.

### Example

```javascript
import FlightCheckInLinks from 'flight_check_in_links';

let apiInstance = new FlightCheckInLinks.CheckinLinksApi();
let airlineCode = "BA"; // String | Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)  [ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes) 
let opts = {
  'language': "language_example" // String | Check-in page language with one of the following patterns 'languageCode' (e.g. EN) or 'languageCode-IATAcountryCode' (e.g. en-GB).   Default value is **en-GB** (used when required language is not available or when no value is specified). 
};
apiInstance.getCheckinURLs(airlineCode, opts, (error, data, response) => {
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
 **airlineCode** | **String**| Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)  [ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes)  | 
 **language** | **String**| Check-in page language with one of the following patterns &#39;languageCode&#39; (e.g. EN) or &#39;languageCode-IATAcountryCode&#39; (e.g. en-GB).   Default value is **en-GB** (used when required language is not available or when no value is specified).  | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

