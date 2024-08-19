# NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi

All URIs are relative to *https://api.nowpayments.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRecurringPayment**](RecurringPaymentsAPIEmailSubscriptionsFeatureApi.md#deleteRecurringPayment) | **DELETE** /v1/subscriptions/{sub_id} | Delete recurring payment
[**getManyPlans**](RecurringPaymentsAPIEmailSubscriptionsFeatureApi.md#getManyPlans) | **GET** /v1/subscriptions/plans | Get many plans
[**getManyRecurringPayments**](RecurringPaymentsAPIEmailSubscriptionsFeatureApi.md#getManyRecurringPayments) | **GET** /v1/subscriptions | Get many recurring payments
[**getOnePlan**](RecurringPaymentsAPIEmailSubscriptionsFeatureApi.md#getOnePlan) | **GET** /v1/subscriptions/plans/{plan-id} | Get one plan
[**getOneRecurringPayment**](RecurringPaymentsAPIEmailSubscriptionsFeatureApi.md#getOneRecurringPayment) | **GET** /v1/subscriptions/{sub_id} | Get one recurring payment
[**updatePlan**](RecurringPaymentsAPIEmailSubscriptionsFeatureApi.md#updatePlan) | **PATCH** /v1/subscriptions/plans/{plan-id} | Update plan



## deleteRecurringPayment

> DeleteRecurringPayment200Response deleteRecurringPayment(subId)

Delete recurring payment

Completely removes a particular payment from the recurring payment plan.   You need to specify the payment plan id in the request.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi();
let subId = "subId_example"; // String | 
apiInstance.deleteRecurringPayment(subId, (error, data, response) => {
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
 **subId** | **String**|  | 

### Return type

[**DeleteRecurringPayment200Response**](DeleteRecurringPayment200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## getManyPlans

> GetManyPlans200Response getManyPlans(opts)

Get many plans

This method allows you to obtain information about all the payment plans you’ve created.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi();
let opts = {
  'limit': "10", // String | Number
  'offset': "3", // String | Number
  'xApiKey': "{{your_api_key}}" // String | 
};
apiInstance.getManyPlans(opts, (error, data, response) => {
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
 **limit** | **String**| Number | [optional] 
 **offset** | **String**| Number | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**GetManyPlans200Response**](GetManyPlans200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManyRecurringPayments

> GetManyRecurringPayments200Response getManyRecurringPayments(opts)

Get many recurring payments

The method allows you to view the entire list of recurring payments filtered by payment status and/or payment plan id

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi();
let opts = {
  'status': "PARTIALLY_PAID", // String | \"WAITING_PAY\" / \"PAID\" /  \"PARTIALLY_PAID\" / \"EXPIRED\"
  'subscriptionPlanId': "111394288", // String | 
  'isActive': "false", // String | true / false
  'limit': "10", // String | 
  'offset': "0", // String | 
  'xApiKey': "{{your_api_key}}" // String | 
};
apiInstance.getManyRecurringPayments(opts, (error, data, response) => {
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
 **status** | **String**| \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot; | [optional] 
 **subscriptionPlanId** | **String**|  | [optional] 
 **isActive** | **String**| true / false | [optional] 
 **limit** | **String**|  | [optional] 
 **offset** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**GetManyRecurringPayments200Response**](GetManyRecurringPayments200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## getOnePlan

> GetOnePlan200Response getOnePlan(planId, opts)

Get one plan

This method allows you to obtain information about your payment plan.   (you need to specify your payment plan id in the request).

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi();
let planId = "planId_example"; // String | 
let opts = {
  'xApiKey': "{{your_api_key}}" // String | 
};
apiInstance.getOnePlan(planId, opts, (error, data, response) => {
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
 **planId** | **String**|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**GetOnePlan200Response**](GetOnePlan200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOneRecurringPayment

> GetOneRecurringPayment200Response getOneRecurringPayment(subId, opts)

Get one recurring payment

Get information about a particular recurring payment via its ID.  Here’s the list of available statuses:   \\- WAITING_PAY   \\- PAID   \\- PARTIALLY_PAID   \\- EXPIRED

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi();
let subId = "subId_example"; // String | 
let opts = {
  'xApiKey': "{{your_api_key}}" // String | 
};
apiInstance.getOneRecurringPayment(subId, opts, (error, data, response) => {
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
 **subId** | **String**|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**GetOneRecurringPayment200Response**](GetOneRecurringPayment200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## updatePlan

> updatePlan(planId, opts)

Update plan

This method allows you to add necessary changes to a created plan. They won’t affect users who have already paid; however, the changes will take effect when a new payment is to be made.

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.RecurringPaymentsAPIEmailSubscriptionsFeatureApi();
let planId = "planId_example"; // String | 
let opts = {
  'updatePlanRequest': {"amount":2,"currency":"usd","interval_day":1,"title":"test plan"} // UpdatePlanRequest | 
};
apiInstance.updatePlan(planId, opts, (error, data, response) => {
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
 **planId** | **String**|  | 
 **updatePlanRequest** | [**UpdatePlanRequest**](UpdatePlanRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

