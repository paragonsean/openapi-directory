# Wikimedia.FeedContentAvailabilityApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedAvailabilityGet**](FeedContentAvailabilityApi.md#feedAvailabilityGet) | **GET** /feed/availability | Gets availability of featured feed content for the apps by wiki domain.



## feedAvailabilityGet

> Availability feedAvailabilityGet()

Gets availability of featured feed content for the apps by wiki domain.

Gets availability of featured feed content for the apps by wiki domain.  Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.FeedContentAvailabilityApi();
apiInstance.feedAvailabilityGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Availability**](Availability.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8; profile=https://www.mediawiki.org/wiki/Specs/Availability/1.0.1, application/problem+json

