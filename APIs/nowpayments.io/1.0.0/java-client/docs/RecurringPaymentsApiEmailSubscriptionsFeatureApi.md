# RecurringPaymentsApiEmailSubscriptionsFeatureApi

All URIs are relative to *https://api.nowpayments.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRecurringPayment**](RecurringPaymentsApiEmailSubscriptionsFeatureApi.md#deleteRecurringPayment) | **DELETE** /v1/subscriptions/{sub_id} | Delete recurring payment |
| [**getManyPlans**](RecurringPaymentsApiEmailSubscriptionsFeatureApi.md#getManyPlans) | **GET** /v1/subscriptions/plans | Get many plans |
| [**getManyRecurringPayments**](RecurringPaymentsApiEmailSubscriptionsFeatureApi.md#getManyRecurringPayments) | **GET** /v1/subscriptions | Get many recurring payments |
| [**getOnePlan**](RecurringPaymentsApiEmailSubscriptionsFeatureApi.md#getOnePlan) | **GET** /v1/subscriptions/plans/{plan-id} | Get one plan |
| [**getOneRecurringPayment**](RecurringPaymentsApiEmailSubscriptionsFeatureApi.md#getOneRecurringPayment) | **GET** /v1/subscriptions/{sub_id} | Get one recurring payment |
| [**updatePlan**](RecurringPaymentsApiEmailSubscriptionsFeatureApi.md#updatePlan) | **PATCH** /v1/subscriptions/plans/{plan-id} | Update plan |


<a id="deleteRecurringPayment"></a>
# **deleteRecurringPayment**
> DeleteRecurringPayment200Response deleteRecurringPayment(subId)

Delete recurring payment

Completely removes a particular payment from the recurring payment plan.   You need to specify the payment plan id in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringPaymentsApiEmailSubscriptionsFeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    RecurringPaymentsApiEmailSubscriptionsFeatureApi apiInstance = new RecurringPaymentsApiEmailSubscriptionsFeatureApi(defaultClient);
    String subId = "subId_example"; // String | 
    try {
      DeleteRecurringPayment200Response result = apiInstance.deleteRecurringPayment(subId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringPaymentsApiEmailSubscriptionsFeatureApi#deleteRecurringPayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subId** | **String**|  | |

### Return type

[**DeleteRecurringPayment200Response**](DeleteRecurringPayment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |
| **404** | 404 |  -  |

<a id="getManyPlans"></a>
# **getManyPlans**
> GetManyPlans200Response getManyPlans(limit, offset, xApiKey)

Get many plans

This method allows you to obtain information about all the payment plans you’ve created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringPaymentsApiEmailSubscriptionsFeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    RecurringPaymentsApiEmailSubscriptionsFeatureApi apiInstance = new RecurringPaymentsApiEmailSubscriptionsFeatureApi(defaultClient);
    String limit = "10"; // String | Number
    String offset = "3"; // String | Number
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetManyPlans200Response result = apiInstance.getManyPlans(limit, offset, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringPaymentsApiEmailSubscriptionsFeatureApi#getManyPlans");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **String**| Number | [optional] |
| **offset** | **String**| Number | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetManyPlans200Response**](GetManyPlans200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="getManyRecurringPayments"></a>
# **getManyRecurringPayments**
> GetManyRecurringPayments200Response getManyRecurringPayments(status, subscriptionPlanId, isActive, limit, offset, xApiKey)

Get many recurring payments

The method allows you to view the entire list of recurring payments filtered by payment status and/or payment plan id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringPaymentsApiEmailSubscriptionsFeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    RecurringPaymentsApiEmailSubscriptionsFeatureApi apiInstance = new RecurringPaymentsApiEmailSubscriptionsFeatureApi(defaultClient);
    String status = "PARTIALLY_PAID"; // String | \"WAITING_PAY\" / \"PAID\" /  \"PARTIALLY_PAID\" / \"EXPIRED\"
    String subscriptionPlanId = "111394288"; // String | 
    String isActive = "false"; // String | true / false
    String limit = "10"; // String | 
    String offset = "0"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetManyRecurringPayments200Response result = apiInstance.getManyRecurringPayments(status, subscriptionPlanId, isActive, limit, offset, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringPaymentsApiEmailSubscriptionsFeatureApi#getManyRecurringPayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **status** | **String**| \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot; | [optional] |
| **subscriptionPlanId** | **String**|  | [optional] |
| **isActive** | **String**| true / false | [optional] |
| **limit** | **String**|  | [optional] |
| **offset** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetManyRecurringPayments200Response**](GetManyRecurringPayments200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="getOnePlan"></a>
# **getOnePlan**
> GetOnePlan200Response getOnePlan(planId, xApiKey)

Get one plan

This method allows you to obtain information about your payment plan.   (you need to specify your payment plan id in the request).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringPaymentsApiEmailSubscriptionsFeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    RecurringPaymentsApiEmailSubscriptionsFeatureApi apiInstance = new RecurringPaymentsApiEmailSubscriptionsFeatureApi(defaultClient);
    String planId = "planId_example"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetOnePlan200Response result = apiInstance.getOnePlan(planId, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringPaymentsApiEmailSubscriptionsFeatureApi#getOnePlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **planId** | **String**|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetOnePlan200Response**](GetOnePlan200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |
| **404** | 404 |  -  |

<a id="getOneRecurringPayment"></a>
# **getOneRecurringPayment**
> GetOneRecurringPayment200Response getOneRecurringPayment(subId, xApiKey)

Get one recurring payment

Get information about a particular recurring payment via its ID.  Here’s the list of available statuses:   \\- WAITING_PAY   \\- PAID   \\- PARTIALLY_PAID   \\- EXPIRED

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringPaymentsApiEmailSubscriptionsFeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    RecurringPaymentsApiEmailSubscriptionsFeatureApi apiInstance = new RecurringPaymentsApiEmailSubscriptionsFeatureApi(defaultClient);
    String subId = "subId_example"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetOneRecurringPayment200Response result = apiInstance.getOneRecurringPayment(subId, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringPaymentsApiEmailSubscriptionsFeatureApi#getOneRecurringPayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subId** | **String**|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetOneRecurringPayment200Response**](GetOneRecurringPayment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |
| **404** | 404 |  -  |

<a id="updatePlan"></a>
# **updatePlan**
> updatePlan(planId, updatePlanRequest)

Update plan

This method allows you to add necessary changes to a created plan. They won’t affect users who have already paid; however, the changes will take effect when a new payment is to be made.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringPaymentsApiEmailSubscriptionsFeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    RecurringPaymentsApiEmailSubscriptionsFeatureApi apiInstance = new RecurringPaymentsApiEmailSubscriptionsFeatureApi(defaultClient);
    String planId = "planId_example"; // String | 
    UpdatePlanRequest updatePlanRequest = new UpdatePlanRequest(); // UpdatePlanRequest | 
    try {
      apiInstance.updatePlan(planId, updatePlanRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringPaymentsApiEmailSubscriptionsFeatureApi#updatePlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **planId** | **String**|  | |
| **updatePlanRequest** | [**UpdatePlanRequest**](UpdatePlanRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

