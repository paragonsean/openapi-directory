# DracoonApi.InternalApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internalRequestSubscriptionPlan**](InternalApi.md#internalRequestSubscriptionPlan) | **GET** /v4/internal/tenant/subscription_plan | Request subscription plan
[**internalSetSubscriptionPlan**](InternalApi.md#internalSetSubscriptionPlan) | **PUT** /v4/internal/tenant/subscription_plan | Set subscription plan



## internalRequestSubscriptionPlan

> SubscriptionPlanResponse internalRequestSubscriptionPlan(xSdsServiceToken)

Request subscription plan

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.InternalApi();
let xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
apiInstance.internalRequestSubscriptionPlan(xSdsServiceToken, (error, data, response) => {
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
 **xSdsServiceToken** | **String**| Service Authentication token | 

### Return type

[**SubscriptionPlanResponse**](SubscriptionPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## internalSetSubscriptionPlan

> SubscriptionPlanResponse internalSetSubscriptionPlan(xSdsServiceToken, subscriptionPlanRequest)

Set subscription plan

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.InternalApi();
let xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
let subscriptionPlanRequest = new DracoonApi.SubscriptionPlanRequest(); // SubscriptionPlanRequest | 
apiInstance.internalSetSubscriptionPlan(xSdsServiceToken, subscriptionPlanRequest, (error, data, response) => {
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
 **xSdsServiceToken** | **String**| Service Authentication token | 
 **subscriptionPlanRequest** | [**SubscriptionPlanRequest**](SubscriptionPlanRequest.md)|  | 

### Return type

[**SubscriptionPlanResponse**](SubscriptionPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

