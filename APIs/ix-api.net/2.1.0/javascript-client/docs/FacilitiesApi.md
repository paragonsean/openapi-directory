# IxApi.FacilitiesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facilitiesList**](FacilitiesApi.md#facilitiesList) | **GET** /facilities | 
[**facilitiesRead**](FacilitiesApi.md#facilitiesRead) | **GET** /facilities/{id} | 



## facilitiesList

> [Facility] facilitiesList(opts)



Get a (filtered) list of &#x60;facilities&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.FacilitiesApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'capabilityMediaType': "capabilityMediaType_example", // String | Filter by capability_media_type
  'capabilitySpeed': 56, // Number | Filter by capability_speed
  'capabilitySpeedLt': 56, // Number | Filter by capability_speed__lt
  'capabilitySpeedLte': 56, // Number | Filter by capability_speed__lte
  'capabilitySpeedGt': 56, // Number | Filter by capability_speed__gt
  'capabilitySpeedGte': 56, // Number | Filter by capability_speed__gte
  'organisationName': "organisationName_example", // String | Filter by organisation_name
  'metroArea': "metroArea_example", // String | Filter by metro_area
  'metroAreaNetwork': "metroAreaNetwork_example", // String | Filter by metro_area_network
  'addressCountry': "addressCountry_example", // String | Filter by address_country
  'addressLocality': "addressLocality_example", // String | Filter by address_locality
  'postalCode': "postalCode_example" // String | Filter by postal_code
};
apiInstance.facilitiesList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **capabilityMediaType** | **String**| Filter by capability_media_type | [optional] 
 **capabilitySpeed** | **Number**| Filter by capability_speed | [optional] 
 **capabilitySpeedLt** | **Number**| Filter by capability_speed__lt | [optional] 
 **capabilitySpeedLte** | **Number**| Filter by capability_speed__lte | [optional] 
 **capabilitySpeedGt** | **Number**| Filter by capability_speed__gt | [optional] 
 **capabilitySpeedGte** | **Number**| Filter by capability_speed__gte | [optional] 
 **organisationName** | **String**| Filter by organisation_name | [optional] 
 **metroArea** | **String**| Filter by metro_area | [optional] 
 **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] 
 **addressCountry** | **String**| Filter by address_country | [optional] 
 **addressLocality** | **String**| Filter by address_locality | [optional] 
 **postalCode** | **String**| Filter by postal_code | [optional] 

### Return type

[**[Facility]**](Facility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## facilitiesRead

> [Facility] facilitiesRead(id)



Retrieve a facility by id

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.FacilitiesApi();
let id = "id_example"; // String | Get by id
apiInstance.facilitiesRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**[Facility]**](Facility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

