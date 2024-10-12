# InterzoidGetFullNameMatchSimilarityKeyApi.FullNameMatchSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getfullnamematch**](FullNameMatchSimilarityKeyApi.md#getfullnamematch) | **GET** /getfullnamematch | Gets a similarity key for matching purposes for full name data



## getfullnamematch

> Getfullnamematch200Response getfullnamematch(license, fullname)

Gets a similarity key for matching purposes for full name data

Gets a similarity key for matching purposes for full name data, where first and last name are part of the same field.

### Example

```javascript
import InterzoidGetFullNameMatchSimilarityKeyApi from 'interzoid_get_full_name_match_similarity_key_api';

let apiInstance = new InterzoidGetFullNameMatchSimilarityKeyApi.FullNameMatchSimilarityKeyApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let fullname = "fullname_example"; // String | Full name from which to generate similarity key
apiInstance.getfullnamematch(license, fullname, (error, data, response) => {
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
 **fullname** | **String**| Full name from which to generate similarity key | 

### Return type

[**Getfullnamematch200Response**](Getfullnamematch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

