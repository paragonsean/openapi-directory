# PricingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pricingsGet**](PricingsApi.md#pricingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} |  |
| [**pricingsList**](PricingsApi.md#pricingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings |  |
| [**pricingsUpdate**](PricingsApi.md#pricingsUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} |  |


<a id="pricingsGet"></a>
# **pricingsGet**
> Pricing pricingsGet(apiVersion, subscriptionId, pricingName)



Gets a provided Security Center pricing configuration in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String pricingName = "pricingName_example"; // String | name of the pricing configuration
    try {
      Pricing result = apiInstance.pricingsGet(apiVersion, subscriptionId, pricingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **pricingName** | **String**| name of the pricing configuration | |

### Return type

[**Pricing**](Pricing.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pricingsList"></a>
# **pricingsList**
> PricingList pricingsList(apiVersion, subscriptionId)



Lists Security Center pricing configurations in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      PricingList result = apiInstance.pricingsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**PricingList**](PricingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pricingsUpdate"></a>
# **pricingsUpdate**
> Pricing pricingsUpdate(apiVersion, subscriptionId, pricingName, pricing)



Updates a provided Security Center pricing configuration in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String pricingName = "pricingName_example"; // String | name of the pricing configuration
    Pricing pricing = new Pricing(); // Pricing | Pricing object
    try {
      Pricing result = apiInstance.pricingsUpdate(apiVersion, subscriptionId, pricingName, pricing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsUpdate");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **pricingName** | **String**| name of the pricing configuration | |
| **pricing** | [**Pricing**](Pricing.md)| Pricing object | |

### Return type

[**Pricing**](Pricing.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

