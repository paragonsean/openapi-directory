# Reverb.ListingConditionsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listingConditionsGet**](ListingConditionsApi.md#listingConditionsGet) | **GET** /listing_conditions | List of supported product conditions



## listingConditionsGet

> listingConditionsGet()

List of supported product conditions

List of supported product conditions

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingConditionsApi();
apiInstance.listingConditionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

