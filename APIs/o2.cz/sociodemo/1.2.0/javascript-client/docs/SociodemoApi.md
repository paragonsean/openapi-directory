# SocioDemoApi.SociodemoApi

All URIs are relative to *https://developer.o2.cz/sociodemo/sandbox/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**age**](SociodemoApi.md#age) | **GET** /age/{location} | Presence in a location aggregated by age
[**gender**](SociodemoApi.md#gender) | **GET** /gender/{location} | Presence in a location aggregated by gender



## age

> CountResult age(location, ageGroup, occurenceType, hour)

Presence in a location aggregated by age

Get count of people in a given location and an hour, aggregated by age.

### Example

```javascript
import SocioDemoApi from 'socio_demo_api';

let apiInstance = new SocioDemoApi.SociodemoApi();
let location = "127752"; // String | basic residential unit
let ageGroup = "2"; // String | age-group specification (1: 8-18, 2: 19-25, 3: 26-35, 4: 36-55, 5: 56+)
let occurenceType = "1"; // String | occurence type in the basic residential unit (1 - transit, 2 - visit)
let hour = "10"; // String | time interval for the count aggregation (from 0 to 23)
apiInstance.age(location, ageGroup, occurenceType, hour, (error, data, response) => {
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
 **location** | **String**| basic residential unit | 
 **ageGroup** | **String**| age-group specification (1: 8-18, 2: 19-25, 3: 26-35, 4: 36-55, 5: 56+) | 
 **occurenceType** | **String**| occurence type in the basic residential unit (1 - transit, 2 - visit) | 
 **hour** | **String**| time interval for the count aggregation (from 0 to 23) | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gender

> CountResult gender(location, g, occurenceType, hour)

Presence in a location aggregated by gender

Get count of people in a given location and an hour, aggregated by gender.

### Example

```javascript
import SocioDemoApi from 'socio_demo_api';

let apiInstance = new SocioDemoApi.SociodemoApi();
let location = "127752"; // String | basic residential unit
let g = "1"; // String | gender specification (1 - male, 2 - female)
let occurenceType = "1"; // String | occurence type in the basic residential unit (1 - transit, 2 - visit)
let hour = "10"; // String | time interval for the count aggregation (from 0 to 23)
apiInstance.gender(location, g, occurenceType, hour, (error, data, response) => {
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
 **location** | **String**| basic residential unit | 
 **g** | **String**| gender specification (1 - male, 2 - female) | 
 **occurenceType** | **String**| occurence type in the basic residential unit (1 - transit, 2 - visit) | 
 **hour** | **String**| time interval for the count aggregation (from 0 to 23) | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

