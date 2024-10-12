# AirlineCodeLookupApi.AirlinesApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getairlines**](AirlinesApi.md#getairlines) | **GET** /reference-data/airlines | Return airlines information.



## getairlines

> SuccessThings getairlines(opts)

Return airlines information.

### Example

```javascript
import AirlineCodeLookupApi from 'airline_code_lookup_api';

let apiInstance = new AirlineCodeLookupApi.AirlinesApi();
let opts = {
  'airlineCodes': "BA" // String | Code of the airline following IATA standard([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)) or ICAO standard ([ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes))  Several airlines can be selected at once by sending a list separated by a coma (i.e. AF, SWA) 
};
apiInstance.getairlines(opts, (error, data, response) => {
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
 **airlineCodes** | **String**| Code of the airline following IATA standard([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)) or ICAO standard ([ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes))  Several airlines can be selected at once by sending a list separated by a coma (i.e. AF, SWA)  | [optional] 

### Return type

[**SuccessThings**](SuccessThings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

