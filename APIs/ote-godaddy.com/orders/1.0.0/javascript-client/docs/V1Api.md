# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](V1Api.md#get) | **GET** /v1/orders/{orderId} | Retrieve details for specified order
[**list**](V1Api.md#list) | **GET** /v1/orders | Retrieve a list of orders for the authenticated shopper. Only one filter may be used at a time



## get

> Order get(orderId, opts)

Retrieve details for specified order

&lt;strong&gt;API Resellers&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;This endpoint does not support subaccounts and therefore API Resellers should not supply an X-Shopper-Id header&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let orderId = "orderId_example"; // String | Order id whose details are to be retrieved
let opts = {
  'xShopperId': "xShopperId_example", // String | Shopper ID to be operated on, if different from JWT<br/><b>Reseller subaccounts are not supported</b>
  'xMarketId': "'en-US'" // String | Unique identifier of the Market in which the request is happening
};
apiInstance.get(orderId, opts, (error, data, response) => {
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
 **orderId** | **String**| Order id whose details are to be retrieved | 
 **xShopperId** | **String**| Shopper ID to be operated on, if different from JWT&lt;br/&gt;&lt;b&gt;Reseller subaccounts are not supported&lt;/b&gt; | [optional] 
 **xMarketId** | **String**| Unique identifier of the Market in which the request is happening | [optional] [default to &#39;en-US&#39;]

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## list

> OrderList list(opts)

Retrieve a list of orders for the authenticated shopper. Only one filter may be used at a time

&lt;strong&gt;API Resellers&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;This endpoint does not support subaccounts and therefore API Resellers should not supply an X-Shopper-Id header&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let opts = {
  'periodStart': "periodStart_example", // String | Start of range indicating what time-frame should be returned. Inclusive
  'periodEnd': "periodEnd_example", // String | End of range indicating what time-frame should be returned. Inclusive
  'domain': "domain_example", // String | Domain name to use as the filter of results
  'productGroupId': 56, // Number | Product group id to use as the filter of results
  'paymentProfileId': 56, // Number | Payment profile id to use as the filter of results
  'parentOrderId': "parentOrderId_example", // String | Parent order id to use as the filter of results
  'offset': 0, // Number | Number of results to skip for pagination
  'limit': 25, // Number | Maximum number of items to return
  'sort': "'-createdAt'", // String | Property name that will be used to sort results. '-' indicates descending
  'xShopperId': "xShopperId_example", // String | Shopper ID to be operated on, if different from JWT<br/><b>Reseller subaccounts are not supported</b>
  'xMarketId': "'en-US'" // String | Unique identifier of the Market in which the request is happening
};
apiInstance.list(opts, (error, data, response) => {
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
 **periodStart** | **String**| Start of range indicating what time-frame should be returned. Inclusive | [optional] 
 **periodEnd** | **String**| End of range indicating what time-frame should be returned. Inclusive | [optional] 
 **domain** | **String**| Domain name to use as the filter of results | [optional] 
 **productGroupId** | **Number**| Product group id to use as the filter of results | [optional] 
 **paymentProfileId** | **Number**| Payment profile id to use as the filter of results | [optional] 
 **parentOrderId** | **String**| Parent order id to use as the filter of results | [optional] 
 **offset** | **Number**| Number of results to skip for pagination | [optional] [default to 0]
 **limit** | **Number**| Maximum number of items to return | [optional] [default to 25]
 **sort** | **String**| Property name that will be used to sort results. &#39;-&#39; indicates descending | [optional] [default to &#39;-createdAt&#39;]
 **xShopperId** | **String**| Shopper ID to be operated on, if different from JWT&lt;br/&gt;&lt;b&gt;Reseller subaccounts are not supported&lt;/b&gt; | [optional] 
 **xMarketId** | **String**| Unique identifier of the Market in which the request is happening | [optional] [default to &#39;en-US&#39;]

### Return type

[**OrderList**](OrderList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

