# Pims.VenuesApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllVenues**](VenuesApi.md#fetchAllVenues) | **GET** /venues | Find all venues
[**fetchOneVenue**](VenuesApi.md#fetchOneVenue) | **GET** /venues/{venue_id} | Get one venue by ID



## fetchAllVenues

> [VenuesEntity] fetchAllVenues(opts)

Find all venues

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.VenuesApi();
let opts = {
  'label': "label_example", // String | Find only the venues whose label contains this value.
  'city': "city_example", // String | Find only the venues whose city contains this value.
  'countryCode': "countryCode_example", // String | Find only the venues whose country_code is equal to this value.
  'type': "type_example", // String | Find only the venues whose type is equal to this value.
  'sort': "'label'", // String | Sort the venues in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllVenues(opts, (error, data, response) => {
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
 **label** | **String**| Find only the venues whose label contains this value. | [optional] 
 **city** | **String**| Find only the venues whose city contains this value. | [optional] 
 **countryCode** | **String**| Find only the venues whose country_code is equal to this value. | [optional] 
 **type** | **String**| Find only the venues whose type is equal to this value. | [optional] 
 **sort** | **String**| Sort the venues in the corresponding order. | [optional] [default to &#39;label&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[VenuesEntity]**](VenuesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneVenue

> VenuesEntity fetchOneVenue(venueId, opts)

Get one venue by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.VenuesApi();
let venueId = 56; // Number | ID of the targeted venue.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOneVenue(venueId, opts, (error, data, response) => {
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
 **venueId** | **Number**| ID of the targeted venue. | 
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**VenuesEntity**](VenuesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

