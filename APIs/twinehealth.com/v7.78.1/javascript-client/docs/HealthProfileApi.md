# FitbitPlusApi.HealthProfileApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchHealthProfile**](HealthProfileApi.md#fetchHealthProfile) | **GET** /health_profile/{id} | Get a health profile
[**fetchHealthProfiles**](HealthProfileApi.md#fetchHealthProfiles) | **GET** /health_profile | List health profiles



## fetchHealthProfile

> FetchHealthProfileResponse fetchHealthProfile(id, opts)

Get a health profile

Get a health profile by id

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthProfileApi();
let id = "id_example"; // String | Health profile identifier
let opts = {
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchHealthProfile(id, opts, (error, data, response) => {
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
 **id** | **String**| Health profile identifier | 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchHealthProfileResponse**](FetchHealthProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchHealthProfiles

> FetchHealthProfilesResponse fetchHealthProfiles(opts)

List health profiles

Get a list of health profiles

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthProfileApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Patient id to fetch health profile. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'filterOrganization': "filterOrganization_example", // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
  'pageNumber': 1, // Number | Page number
  'pageSize': 10, // Number | Page size
  'pageLimit': 50, // Number | Page limit
  'pageCursor': "pageCursor_example", // String | Page cursor
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchHealthProfiles(opts, (error, data, response) => {
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
 **filterPatient** | **String**| Patient id to fetch health profile. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] 
 **pageNumber** | **Number**| Page number | [optional] [default to 1]
 **pageSize** | **Number**| Page size | [optional] [default to 10]
 **pageLimit** | **Number**| Page limit | [optional] [default to 50]
 **pageCursor** | **String**| Page cursor | [optional] 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchHealthProfilesResponse**](FetchHealthProfilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

