# BillsApi.RssApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1RssAllbillsRssGet**](RssApi.md#apiV1RssAllbillsRssGet) | **GET** /api/v1/Rss/allbills.rss | Returns an Rss feed of all Bills.
[**apiV1RssBillsIdRssGet**](RssApi.md#apiV1RssBillsIdRssGet) | **GET** /api/v1/Rss/Bills/{id}.rss | Returns an Rss feed of a certain Bill.
[**apiV1RssPrivatebillsRssGet**](RssApi.md#apiV1RssPrivatebillsRssGet) | **GET** /api/v1/Rss/privatebills.rss | Returns an Rss feed of private Bills.
[**apiV1RssPublicbillsRssGet**](RssApi.md#apiV1RssPublicbillsRssGet) | **GET** /api/v1/Rss/publicbills.rss | Returns an Rss feed of public Bills.



## apiV1RssAllbillsRssGet

> apiV1RssAllbillsRssGet()

Returns an Rss feed of all Bills.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.RssApi();
apiInstance.apiV1RssAllbillsRssGet((error, data, response) => {
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


## apiV1RssBillsIdRssGet

> apiV1RssBillsIdRssGet(id)

Returns an Rss feed of a certain Bill.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.RssApi();
let id = 56; // Number | Id of Bill
apiInstance.apiV1RssBillsIdRssGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Bill | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiV1RssPrivatebillsRssGet

> apiV1RssPrivatebillsRssGet()

Returns an Rss feed of private Bills.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.RssApi();
apiInstance.apiV1RssPrivatebillsRssGet((error, data, response) => {
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


## apiV1RssPublicbillsRssGet

> apiV1RssPublicbillsRssGet()

Returns an Rss feed of public Bills.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.RssApi();
apiInstance.apiV1RssPublicbillsRssGet((error, data, response) => {
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

