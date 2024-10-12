# KlarnaPaymentsApiV1.SessionsApi

All URIs are relative to *https://api.klarna.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCreditSession**](SessionsApi.md#createCreditSession) | **POST** /payments/v1/sessions | Create a new payment session
[**readCreditSession**](SessionsApi.md#readCreditSession) | **GET** /payments/v1/sessions/{session_id} | Read an existing payment session
[**updateCreditSession**](SessionsApi.md#updateCreditSession) | **POST** /payments/v1/sessions/{session_id} | Update an existing payment session



## createCreditSession

> MerchantSession createCreditSession(sessionCreate)

Create a new payment session

Use this API call to create a Klarna Payments session.&lt;br/&gt;When a session is created you will receive the available &#x60;payment_method_categories&#x60; for the session, a &#x60;session_id&#x60; and a &#x60;client_token&#x60;. The &#x60;session_id&#x60; can be used to read or update the session using the REST API. The &#x60;client_token&#x60; should be passed to the browser. Read more on **[Create a new payment session](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/)**.

### Example

```javascript
import KlarnaPaymentsApiV1 from 'klarna_payments_api_v1';

let apiInstance = new KlarnaPaymentsApiV1.SessionsApi();
let sessionCreate = new KlarnaPaymentsApiV1.SessionCreate(); // SessionCreate | session_request
apiInstance.createCreditSession(sessionCreate, (error, data, response) => {
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
 **sessionCreate** | [**SessionCreate**](SessionCreate.md)| session_request | 

### Return type

[**MerchantSession**](MerchantSession.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## readCreditSession

> SessionRead readCreditSession(sessionId)

Read an existing payment session

Use this API call to read a Klarna Payments session. You can read the Klarna Payments session at any time after it has been created, to get information about it. This will return all data that has been collected during the session. Read more on **[Read an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/check-the-details-of-a-payment-session/)**.

### Example

```javascript
import KlarnaPaymentsApiV1 from 'klarna_payments_api_v1';

let apiInstance = new KlarnaPaymentsApiV1.SessionsApi();
let sessionId = "sessionId_example"; // String | session_id
apiInstance.readCreditSession(sessionId, (error, data, response) => {
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
 **sessionId** | **String**| session_id | 

### Return type

[**SessionRead**](SessionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCreditSession

> updateCreditSession(sessionId, session)

Update an existing payment session

Use this API call to update a Klarna Payments session with new details, in case something in the order has changed and the checkout has been reloaded. Including if the consumer adds a new item to the cart or if consumer details are updated. Read more on **[Update an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/update-the-cart/)**.

### Example

```javascript
import KlarnaPaymentsApiV1 from 'klarna_payments_api_v1';

let apiInstance = new KlarnaPaymentsApiV1.SessionsApi();
let sessionId = "sessionId_example"; // String | session_id
let session = new KlarnaPaymentsApiV1.Session(); // Session | session_request
apiInstance.updateCreditSession(sessionId, session, (error, data, response) => {
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
 **sessionId** | **String**| session_id | 
 **session** | [**Session**](Session.md)| session_request | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

