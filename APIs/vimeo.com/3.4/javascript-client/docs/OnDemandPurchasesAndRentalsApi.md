# Vimeo.OnDemandPurchasesAndRentalsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkIfVodWasPurchased**](OnDemandPurchasesAndRentalsApi.md#checkIfVodWasPurchased) | **GET** /users/{user_id}/ondemand/purchases | Check if a user has made a purchase or rental from an On Demand page
[**checkIfVodWasPurchasedAlt1**](OnDemandPurchasesAndRentalsApi.md#checkIfVodWasPurchasedAlt1) | **GET** /me/ondemand/purchases/{ondemand_id} | Check if a user has made a purchase or rental from an On Demand page
[**getVodPurchases**](OnDemandPurchasesAndRentalsApi.md#getVodPurchases) | **GET** /me/ondemand/purchases | Get all the On Demand purchases and rentals that a user has made



## checkIfVodWasPurchased

> OnDemandPage checkIfVodWasPurchased(userId)

Check if a user has made a purchase or rental from an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPurchasesAndRentalsApi();
let userId = 152184; // Number | The ID of the user.
apiInstance.checkIfVodWasPurchased(userId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## checkIfVodWasPurchasedAlt1

> OnDemandPage checkIfVodWasPurchasedAlt1(ondemandId)

Check if a user has made a purchase or rental from an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPurchasesAndRentalsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.checkIfVodWasPurchasedAlt1(ondemandId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## getVodPurchases

> [OnDemandPage] getVodPurchases(opts)

Get all the On Demand purchases and rentals that a user has made

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPurchasesAndRentalsApi();
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The type of On Demand videos to show.  Option descriptions:  * `important` - Will show all pages which are about to expire. 
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getVodPurchases(opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The type of On Demand videos to show.  Option descriptions:  * &#x60;important&#x60; - Will show all pages which are about to expire.  | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[OnDemandPage]**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json

