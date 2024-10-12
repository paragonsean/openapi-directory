# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](V1Api.md#cancel) | **DELETE** /v1/subscriptions/{subscriptionId} | Cancel the specified Subscription
[**get**](V1Api.md#get) | **GET** /v1/subscriptions/{subscriptionId} | Retrieve details for the specified Subscription
[**list**](V1Api.md#list) | **GET** /v1/subscriptions | Retrieve a list of Subscriptions for the specified Shopper
[**productGroups**](V1Api.md#productGroups) | **GET** /v1/subscriptions/productGroups | Retrieve a list of ProductGroups for the specified Shopper
[**update**](V1Api.md#update) | **PATCH** /v1/subscriptions/{subscriptionId} | Update details for the specified Subscription



## cancel

> cancel(subscriptionId, opts)

Cancel the specified Subscription

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Subscription to cancel
let opts = {
  'xShopperId': "xShopperId_example" // String | Shopper ID to cancel subscriptions for when not using JWT
};
apiInstance.cancel(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Subscription to cancel | 
 **xShopperId** | **String**| Shopper ID to cancel subscriptions for when not using JWT | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## get

> Subscription get(subscriptionId, opts)

Retrieve details for the specified Subscription

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Subscription to retrieve
let opts = {
  'xShopperId': "xShopperId_example", // String | Shopper ID to be operated on, if different from JWT
  'xMarketId': "'en-US'" // String | Unique identifier of the Market in which the request is happening
};
apiInstance.get(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Subscription to retrieve | 
 **xShopperId** | **String**| Shopper ID to be operated on, if different from JWT | [optional] 
 **xMarketId** | **String**| Unique identifier of the Market in which the request is happening | [optional] [default to &#39;en-US&#39;]

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## list

> SubscriptionList list(opts)

Retrieve a list of Subscriptions for the specified Shopper

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let opts = {
  'xShopperId': "xShopperId_example", // String | Shopper ID to return subscriptions for when not using JWT
  'xMarketId': "'en-US'", // String | The market that the response should be formatted for
  'productGroupKeys': ["null"], // [String] | Only return Subscriptions with the specified product groups
  'includes': ["null"], // [String] | Optional details to be included in the response
  'offset': 0, // Number | Number of Subscriptions to skip before starting to return paged results (must be a multiple of the limit)
  'limit': 25, // Number | Number of Subscriptions to retrieve in this page, starting after offset
  'sort': "'-expiresAt'" // String | Property name that will be used to sort results. \"-\" indicates descending
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
 **xShopperId** | **String**| Shopper ID to return subscriptions for when not using JWT | [optional] 
 **xMarketId** | **String**| The market that the response should be formatted for | [optional] [default to &#39;en-US&#39;]
 **productGroupKeys** | [**[String]**](String.md)| Only return Subscriptions with the specified product groups | [optional] 
 **includes** | [**[String]**](String.md)| Optional details to be included in the response | [optional] 
 **offset** | **Number**| Number of Subscriptions to skip before starting to return paged results (must be a multiple of the limit) | [optional] [default to 0]
 **limit** | **Number**| Number of Subscriptions to retrieve in this page, starting after offset | [optional] [default to 25]
 **sort** | **String**| Property name that will be used to sort results. \&quot;-\&quot; indicates descending | [optional] [default to &#39;-expiresAt&#39;]

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## productGroups

> [ProductGroup] productGroups(opts)

Retrieve a list of ProductGroups for the specified Shopper

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let opts = {
  'xShopperId': "xShopperId_example", // String | Shopper ID to return data for when not using JWT
  'xMarketId': "'en-US'" // String | The market that the response should be formatted for
};
apiInstance.productGroups(opts, (error, data, response) => {
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
 **xShopperId** | **String**| Shopper ID to return data for when not using JWT | [optional] 
 **xMarketId** | **String**| The market that the response should be formatted for | [optional] [default to &#39;en-US&#39;]

### Return type

[**[ProductGroup]**](ProductGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## update

> update(subscriptionId, subscriptionUpdate)

Update details for the specified Subscription

Only Subscription properties that can be changed without immediate financial impact can be modified via PATCH, whereas some properties can be changed by purchasing a renewal&lt;br/&gt;&lt;strong&gt;This endpoint only supports JWT authentication&lt;/strong&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Subscription to update
let subscriptionUpdate = new OpenapiJsClient.SubscriptionUpdate(); // SubscriptionUpdate | Details of the Subscription to change
apiInstance.update(subscriptionId, subscriptionUpdate, (error, data, response) => {
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
 **subscriptionId** | **String**| Unique identifier of the Subscription to update | 
 **subscriptionUpdate** | [**SubscriptionUpdate**](SubscriptionUpdate.md)| Details of the Subscription to change | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml

