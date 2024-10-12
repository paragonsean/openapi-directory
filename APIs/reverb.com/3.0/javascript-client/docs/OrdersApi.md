# Reverb.OrdersApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ordersOrderIdFeedbackBuyerGet**](OrdersApi.md#ordersOrderIdFeedbackBuyerGet) | **GET** /orders/{order_id}/feedback/buyer | Feedback details for an order&#39;s buyer
[**ordersOrderIdFeedbackBuyerPost**](OrdersApi.md#ordersOrderIdFeedbackBuyerPost) | **POST** /orders/{order_id}/feedback/buyer | Add feedback about an order&#39;s buyer
[**ordersOrderIdFeedbackSellerGet**](OrdersApi.md#ordersOrderIdFeedbackSellerGet) | **GET** /orders/{order_id}/feedback/seller | Feedback details for an order&#39;s seller
[**ordersOrderIdFeedbackSellerPost**](OrdersApi.md#ordersOrderIdFeedbackSellerPost) | **POST** /orders/{order_id}/feedback/seller | Add feedback about an order&#39;s seller



## ordersOrderIdFeedbackBuyerGet

> ordersOrderIdFeedbackBuyerGet(orderId)

Feedback details for an order&#39;s buyer

Feedback details for an order&#39;s buyer

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.OrdersApi();
let orderId = "orderId_example"; // String | 
apiInstance.ordersOrderIdFeedbackBuyerGet(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ordersOrderIdFeedbackBuyerPost

> ordersOrderIdFeedbackBuyerPost(orderId)

Add feedback about an order&#39;s buyer

Add feedback about an order&#39;s buyer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.OrdersApi();
let orderId = "orderId_example"; // String | 
apiInstance.ordersOrderIdFeedbackBuyerPost(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ordersOrderIdFeedbackSellerGet

> ordersOrderIdFeedbackSellerGet(orderId)

Feedback details for an order&#39;s seller

Feedback details for an order&#39;s seller

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.OrdersApi();
let orderId = "orderId_example"; // String | 
apiInstance.ordersOrderIdFeedbackSellerGet(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ordersOrderIdFeedbackSellerPost

> ordersOrderIdFeedbackSellerPost(orderId)

Add feedback about an order&#39;s seller

Add feedback about an order&#39;s seller

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.OrdersApi();
let orderId = "orderId_example"; // String | 
apiInstance.ordersOrderIdFeedbackSellerPost(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

