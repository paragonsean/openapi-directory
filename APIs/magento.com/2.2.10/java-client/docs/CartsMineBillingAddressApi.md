# CartsMineBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteBillingAddressManagementV1AssignPost**](CartsMineBillingAddressApi.md#quoteBillingAddressManagementV1AssignPost) | **POST** /V1/carts/mine/billing-address | carts/mine/billing-address |
| [**quoteBillingAddressManagementV1GetGet**](CartsMineBillingAddressApi.md#quoteBillingAddressManagementV1GetGet) | **GET** /V1/carts/mine/billing-address | carts/mine/billing-address |


<a id="quoteBillingAddressManagementV1AssignPost"></a>
# **quoteBillingAddressManagementV1AssignPost**
> Integer quoteBillingAddressManagementV1AssignPost(quoteBillingAddressManagementV1AssignPostRequest)

carts/mine/billing-address

Assigns a specified billing address to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineBillingAddressApi apiInstance = new CartsMineBillingAddressApi(defaultClient);
    QuoteBillingAddressManagementV1AssignPostRequest quoteBillingAddressManagementV1AssignPostRequest = new QuoteBillingAddressManagementV1AssignPostRequest(); // QuoteBillingAddressManagementV1AssignPostRequest | 
    try {
      Integer result = apiInstance.quoteBillingAddressManagementV1AssignPost(quoteBillingAddressManagementV1AssignPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineBillingAddressApi#quoteBillingAddressManagementV1AssignPost");
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
| **quoteBillingAddressManagementV1AssignPostRequest** | [**QuoteBillingAddressManagementV1AssignPostRequest**](QuoteBillingAddressManagementV1AssignPostRequest.md)|  | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="quoteBillingAddressManagementV1GetGet"></a>
# **quoteBillingAddressManagementV1GetGet**
> QuoteDataAddressInterface quoteBillingAddressManagementV1GetGet()

carts/mine/billing-address

Returns the billing address for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineBillingAddressApi apiInstance = new CartsMineBillingAddressApi(defaultClient);
    try {
      QuoteDataAddressInterface result = apiInstance.quoteBillingAddressManagementV1GetGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineBillingAddressApi#quoteBillingAddressManagementV1GetGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

