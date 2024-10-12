# LhPartnerApi.OrdersApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders**](OrdersApi.md#orders) | **GET** /orders/orders/{orderID}/{name} | Orders



## orders

> String orders(orderID, accept, name)

Orders

Retrieve order by ID and optionally name. This service is only accessible for LH privileged partners

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OrdersApi();
let orderID = "orderID_example"; // String | Unique order identifier
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let name = "name_example"; // String | Surname of traveller
apiInstance.orders(orderID, accept, name, (error, data, response) => {
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
 **orderID** | **String**| Unique order identifier | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **name** | **String**| Surname of traveller | 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

