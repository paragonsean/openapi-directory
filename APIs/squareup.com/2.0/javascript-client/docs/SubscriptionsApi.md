# SquareConnectApi.SubscriptionsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelSubscription**](SubscriptionsApi.md#cancelSubscription) | **POST** /v2/subscriptions/{subscription_id}/cancel | CancelSubscription
[**createSubscription**](SubscriptionsApi.md#createSubscription) | **POST** /v2/subscriptions | CreateSubscription
[**listSubscriptionEvents**](SubscriptionsApi.md#listSubscriptionEvents) | **GET** /v2/subscriptions/{subscription_id}/events | ListSubscriptionEvents
[**resumeSubscription**](SubscriptionsApi.md#resumeSubscription) | **POST** /v2/subscriptions/{subscription_id}/resume | ResumeSubscription
[**retrieveSubscription**](SubscriptionsApi.md#retrieveSubscription) | **GET** /v2/subscriptions/{subscription_id} | RetrieveSubscription
[**searchSubscriptions**](SubscriptionsApi.md#searchSubscriptions) | **POST** /v2/subscriptions/search | SearchSubscriptions
[**updateSubscription**](SubscriptionsApi.md#updateSubscription) | **PUT** /v2/subscriptions/{subscription_id} | UpdateSubscription



## cancelSubscription

> CancelSubscriptionResponse cancelSubscription(subscriptionId)

CancelSubscription

Sets the &#x60;canceled_date&#x60; field to the end of the active billing period. After this date, the status changes from ACTIVE to CANCELED.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the subscription to cancel.
apiInstance.cancelSubscription(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the subscription to cancel. | 

### Return type

[**CancelSubscriptionResponse**](CancelSubscriptionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createSubscription

> CreateSubscriptionResponse createSubscription(createSubscriptionRequest)

CreateSubscription

Creates a subscription for a customer to a subscription plan.  If you provide a card on file in the request, Square charges the card for the subscription. Otherwise, Square bills an invoice to the customer&#39;s email address. The subscription starts immediately, unless the request includes the optional &#x60;start_date&#x60;. Each individual subscription is associated with a particular location.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let createSubscriptionRequest = new SquareConnectApi.CreateSubscriptionRequest(); // CreateSubscriptionRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createSubscription(createSubscriptionRequest, (error, data, response) => {
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
 **createSubscriptionRequest** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateSubscriptionResponse**](CreateSubscriptionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSubscriptionEvents

> ListSubscriptionEventsResponse listSubscriptionEvents(subscriptionId, opts)

ListSubscriptionEvents

Lists all events for a specific subscription. In the current implementation, only &#x60;START_SUBSCRIPTION&#x60; and &#x60;STOP_SUBSCRIPTION&#x60; (when the subscription was canceled) events are returned.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the subscription to retrieve the events for.
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
  'limit': 56 // Number | The upper limit on the number of subscription events to return in the response.  Default: `200`
};
apiInstance.listSubscriptionEvents(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the subscription to retrieve the events for. | 
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
 **limit** | **Number**| The upper limit on the number of subscription events to return in the response.  Default: &#x60;200&#x60; | [optional] 

### Return type

[**ListSubscriptionEventsResponse**](ListSubscriptionEventsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resumeSubscription

> ResumeSubscriptionResponse resumeSubscription(subscriptionId)

ResumeSubscription

Resumes a deactivated subscription.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the subscription to resume.
apiInstance.resumeSubscription(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the subscription to resume. | 

### Return type

[**ResumeSubscriptionResponse**](ResumeSubscriptionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveSubscription

> RetrieveSubscriptionResponse retrieveSubscription(subscriptionId)

RetrieveSubscription

Retrieves a subscription.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the subscription to retrieve.
apiInstance.retrieveSubscription(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the subscription to retrieve. | 

### Return type

[**RetrieveSubscriptionResponse**](RetrieveSubscriptionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchSubscriptions

> SearchSubscriptionsResponse searchSubscriptions(searchSubscriptionsRequest)

SearchSubscriptions

Searches for subscriptions. Results are ordered chronologically by subscription creation date. If the request specifies more than one location ID, the endpoint orders the result by location ID, and then by creation date within each location. If no locations are given in the query, all locations are searched.  You can also optionally specify &#x60;customer_ids&#x60; to search by customer. If left unset, all customers associated with the specified locations are returned. If the request specifies customer IDs, the endpoint orders results first by location, within location by customer ID, and within customer by subscription creation date.  For more information, see [Retrieve subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let searchSubscriptionsRequest = new SquareConnectApi.SearchSubscriptionsRequest(); // SearchSubscriptionsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchSubscriptions(searchSubscriptionsRequest, (error, data, response) => {
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
 **searchSubscriptionsRequest** | [**SearchSubscriptionsRequest**](SearchSubscriptionsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchSubscriptionsResponse**](SearchSubscriptionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSubscription

> UpdateSubscriptionResponse updateSubscription(subscriptionId, updateSubscriptionRequest)

UpdateSubscription

Updates a subscription. You can set, modify, and clear the &#x60;subscription&#x60; field values.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID for the subscription to update.
let updateSubscriptionRequest = new SquareConnectApi.UpdateSubscriptionRequest(); // UpdateSubscriptionRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateSubscription(subscriptionId, updateSubscriptionRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID for the subscription to update. | 
 **updateSubscriptionRequest** | [**UpdateSubscriptionRequest**](UpdateSubscriptionRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateSubscriptionResponse**](UpdateSubscriptionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

