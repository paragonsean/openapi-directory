# HotelNameAutocomplete.SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gethotels**](SearchApi.md#gethotels) | **GET** /reference-data/locations/hotel | Returns a list of hotels matching a given keyword.



## gethotels

> Success gethotels(keyword, subType, opts)

Returns a list of hotels matching a given keyword.

### Example

```javascript
import HotelNameAutocomplete from 'hotel_name_autocomplete';

let apiInstance = new HotelNameAutocomplete.SearchApi();
let keyword = "PARI"; // String | Location query keyword
let subType = ["null"]; // [String] | Category of search - To enter several values, repeat the query parameter   Use HOTEL_LEISURE to target aggregators or HOTEL_GDS to target directly the chains
let opts = {
  'countryCode': "FR", // String | The country in which you search the subType. Country Code in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format
  'lang': "'EN'", // String | The language in which you want the results in following [ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1).   If the language entered is not available then the results will be shown in the default language, English.
  'max': 20 // Number | The number of results requested from 1 to 20
};
apiInstance.gethotels(keyword, subType, opts, (error, data, response) => {
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
 **keyword** | **String**| Location query keyword | 
 **subType** | [**[String]**](String.md)| Category of search - To enter several values, repeat the query parameter   Use HOTEL_LEISURE to target aggregators or HOTEL_GDS to target directly the chains | 
 **countryCode** | **String**| The country in which you search the subType. Country Code in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format | [optional] 
 **lang** | **String**| The language in which you want the results in following [ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1).   If the language entered is not available then the results will be shown in the default language, English. | [optional] [default to &#39;EN&#39;]
 **max** | **Number**| The number of results requested from 1 to 20 | [optional] [default to 20]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

