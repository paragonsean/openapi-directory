# EDrvApi.TransactionsApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTransaction**](TransactionsApi.md#getTransaction) | **GET** /v1/transactions/{id} | 
[**getTransactionCost**](TransactionsApi.md#getTransactionCost) | **GET** /v1/transactions/{id}/cost | 
[**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /v1/transactions | 



## getTransaction

> getTransaction(id, opts)



Get a specific transaction

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.TransactionsApi();
let id = "id_example"; // String | The transaction id that needs to be fetched
let opts = {
  'includeChargestation': true, // Boolean | Populate chargestation
  'includeEvse': true, // Boolean | Populate evse
  'includeConnector': true, // Boolean | Populate connector
  'includeDriver': true, // Boolean | Populate driver
  'includeToken': true, // Boolean | Populate token
  'includeReservation': true, // Boolean | Populate reservation
  'includeOrganization': true, // Boolean | Populate organization
  'includeRate': true // Boolean | Populate rate
};
apiInstance.getTransaction(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The transaction id that needs to be fetched | 
 **includeChargestation** | **Boolean**| Populate chargestation | [optional] 
 **includeEvse** | **Boolean**| Populate evse | [optional] 
 **includeConnector** | **Boolean**| Populate connector | [optional] 
 **includeDriver** | **Boolean**| Populate driver | [optional] 
 **includeToken** | **Boolean**| Populate token | [optional] 
 **includeReservation** | **Boolean**| Populate reservation | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 
 **includeRate** | **Boolean**| Populate rate | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTransactionCost

> getTransactionCost(id)



Get a specific transaction&#39;s cost

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.TransactionsApi();
let id = "id_example"; // String | The transaction id that needs to be fetched
apiInstance.getTransactionCost(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The transaction id that needs to be fetched | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTransactions

> GetTransactions200Response getTransactions(opts)



Get a list of transactions

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.TransactionsApi();
let opts = {
  'status': "status_example", // String | Started to get only active transactions
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeChargestation': true, // Boolean | Populate chargestation
  'includeEvse': true, // Boolean | Populate evse
  'includeConnector': true, // Boolean | Populate connector
  'includeDriver': true, // Boolean | Populate driver
  'includeToken': true, // Boolean | Populate token
  'includeReservation': true, // Boolean | Populate reservation
  'includeOrganization': true, // Boolean | Populate organization
  'includeRate': true // Boolean | Populate rate
};
apiInstance.getTransactions(opts, (error, data, response) => {
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
 **status** | **String**| Started to get only active transactions | [optional] 
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeChargestation** | **Boolean**| Populate chargestation | [optional] 
 **includeEvse** | **Boolean**| Populate evse | [optional] 
 **includeConnector** | **Boolean**| Populate connector | [optional] 
 **includeDriver** | **Boolean**| Populate driver | [optional] 
 **includeToken** | **Boolean**| Populate token | [optional] 
 **includeReservation** | **Boolean**| Populate reservation | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 
 **includeRate** | **Boolean**| Populate rate | [optional] 

### Return type

[**GetTransactions200Response**](GetTransactions200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

