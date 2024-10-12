# NowPaymentsApi.BillingSubPartnerAPIApi

All URIs are relative to *https://api.nowpayments.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllTransfers**](BillingSubPartnerAPIApi.md#getAllTransfers) | **GET** /v1/sub-partner/transfers | Get all transfers
[**getSubPartnerBalance**](BillingSubPartnerAPIApi.md#getSubPartnerBalance) | **GET** /v1/sub-partner/balance/{id} | Get sub-partner balance
[**getSubPartners**](BillingSubPartnerAPIApi.md#getSubPartners) | **GET** /v1/sub-partner | Get sub-partners
[**getTransfer**](BillingSubPartnerAPIApi.md#getTransfer) | **GET** /v1/sub-partner/transfer/{id} | Get transfer



## getAllTransfers

> GetAllTransfers200Response getAllTransfers(opts)

Get all transfers

Returns the entire list of transfers created by your sub-partners.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.BillingSubPartnerAPIApi();
let opts = {
  'id': "111", // String | int or array of int (optional)
  'status': "CREATED", // String | string or array of string  \"WAITING\"/\"CREATED\"/\"FINISHED\"/\"REJECTED\" (optional)
  'limit': "10", // String | (optional) default 10
  'offset': "0", // String | (optional) default 0
  'order': "ASC" // String | ASC / DESC (optional) default ASC
};
apiInstance.getAllTransfers(opts, (error, data, response) => {
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
 **id** | **String**| int or array of int (optional) | [optional] 
 **status** | **String**| string or array of string  \&quot;WAITING\&quot;/\&quot;CREATED\&quot;/\&quot;FINISHED\&quot;/\&quot;REJECTED\&quot; (optional) | [optional] 
 **limit** | **String**| (optional) default 10 | [optional] 
 **offset** | **String**| (optional) default 0 | [optional] 
 **order** | **String**| ASC / DESC (optional) default ASC | [optional] 

### Return type

[**GetAllTransfers200Response**](GetAllTransfers200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubPartnerBalance

> GetSubPartnerBalance200Response getSubPartnerBalance(id, opts)

Get sub-partner balance

This request can be made only from a whitelisted IP.   If IP whitelisting is disabled, this request can be made by any user that has an API key.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.BillingSubPartnerAPIApi();
let id = "id_example"; // String | 
let opts = {
  'xApiKey': "{{your_api_key}}" // String | 
};
apiInstance.getSubPartnerBalance(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**GetSubPartnerBalance200Response**](GetSubPartnerBalance200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubPartners

> getSubPartners(opts)

Get sub-partners

This method returns the entire list of your sub-partners.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.BillingSubPartnerAPIApi();
let opts = {
  'id': "111", // String | int or array of int (optional)
  'offset': "0", // String | (optional) default 0
  'limit': "10", // String | (optional) default 10
  'order': "DESC" // String | ASC / DESC (optional) default ASC
};
apiInstance.getSubPartners(opts, (error, data, response) => {
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
 **id** | **String**| int or array of int (optional) | [optional] 
 **offset** | **String**| (optional) default 0 | [optional] 
 **limit** | **String**| (optional) default 10 | [optional] 
 **order** | **String**| ASC / DESC (optional) default ASC | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTransfer

> GetTransfer200Response getTransfer(id)

Get transfer

Get the actual information about the transfer. You need to provide the transfer ID in the request.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.BillingSubPartnerAPIApi();
let id = "id_example"; // String | 
apiInstance.getTransfer(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**GetTransfer200Response**](GetTransfer200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

