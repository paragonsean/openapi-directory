# InternalApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**internalRequestSubscriptionPlan**](InternalApi.md#internalRequestSubscriptionPlan) | **GET** /v4/internal/tenant/subscription_plan | Request subscription plan |
| [**internalSetSubscriptionPlan**](InternalApi.md#internalSetSubscriptionPlan) | **PUT** /v4/internal/tenant/subscription_plan | Set subscription plan |


<a id="internalRequestSubscriptionPlan"></a>
# **internalRequestSubscriptionPlan**
> SubscriptionPlanResponse internalRequestSubscriptionPlan(xSdsServiceToken)

Request subscription plan

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    InternalApi apiInstance = new InternalApi(defaultClient);
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      SubscriptionPlanResponse result = apiInstance.internalRequestSubscriptionPlan(xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#internalRequestSubscriptionPlan");
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
| **xSdsServiceToken** | **String**| Service Authentication token | |

### Return type

[**SubscriptionPlanResponse**](SubscriptionPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="internalSetSubscriptionPlan"></a>
# **internalSetSubscriptionPlan**
> SubscriptionPlanResponse internalSetSubscriptionPlan(xSdsServiceToken, subscriptionPlanRequest)

Set subscription plan

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    InternalApi apiInstance = new InternalApi(defaultClient);
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    SubscriptionPlanRequest subscriptionPlanRequest = new SubscriptionPlanRequest(); // SubscriptionPlanRequest | 
    try {
      SubscriptionPlanResponse result = apiInstance.internalSetSubscriptionPlan(xSdsServiceToken, subscriptionPlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#internalSetSubscriptionPlan");
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
| **xSdsServiceToken** | **String**| Service Authentication token | |
| **subscriptionPlanRequest** | [**SubscriptionPlanRequest**](SubscriptionPlanRequest.md)|  | |

### Return type

[**SubscriptionPlanResponse**](SubscriptionPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

