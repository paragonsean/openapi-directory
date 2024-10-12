# FitbitPlusApi.CoachApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchCoach**](CoachApi.md#fetchCoach) | **GET** /coach/{id} | Get a coach
[**fetchCoaches**](CoachApi.md#fetchCoaches) | **GET** /coach | List coaches



## fetchCoach

> FetchCoachResponse fetchCoach(id)

Get a coach

Get a coach record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.CoachApi();
let id = "id_example"; // String | Coach identifier
apiInstance.fetchCoach(id, (error, data, response) => {
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
 **id** | **String**| Coach identifier | 

### Return type

[**FetchCoachResponse**](FetchCoachResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchCoaches

> FetchCoachesResponse fetchCoaches(opts)

List coaches

Get a list of coaches matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.CoachApi();
let opts = {
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
  'filterOrganization': "filterOrganization_example" // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
};
apiInstance.fetchCoaches(opts, (error, data, response) => {
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
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 

### Return type

[**FetchCoachesResponse**](FetchCoachesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

