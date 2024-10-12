# ShippingPoliciesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiLogisticsPvtShippingPoliciesGet**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesGet) | **GET** /api/logistics/pvt/shipping-policies | List shipping policies |
| [**apiLogisticsPvtShippingPoliciesIdDelete**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesIdDelete) | **DELETE** /api/logistics/pvt/shipping-policies/{id} | Delete shipping policies by ID |
| [**apiLogisticsPvtShippingPoliciesIdGet**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesIdGet) | **GET** /api/logistics/pvt/shipping-policies/{id} | Retrieve shipping policy by ID |
| [**apiLogisticsPvtShippingPoliciesIdPut**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesIdPut) | **PUT** /api/logistics/pvt/shipping-policies/{id} | Update shipping policy |
| [**apiLogisticsPvtShippingPoliciesPost**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesPost) | **POST** /api/logistics/pvt/shipping-policies | Create shipping policy |


<a id="apiLogisticsPvtShippingPoliciesGet"></a>
# **apiLogisticsPvtShippingPoliciesGet**
> apiLogisticsPvtShippingPoliciesGet(accept, contentType, page, perPage)

List shipping policies

This endpoint lists existing shipping policies from carriers in your store.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ShippingPoliciesApi apiInstance = new ShippingPoliciesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Type of the content being sent
    String page = "page"; // String | Desired number of pages to retrieve information from your Shipping Policies.
    String perPage = "perPage"; // String | Desired number of items per page, to retrieve information from your Shipping Policies.
    try {
      apiInstance.apiLogisticsPvtShippingPoliciesGet(accept, contentType, page, perPage);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingPoliciesApi#apiLogisticsPvtShippingPoliciesGet");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **page** | **String**| Desired number of pages to retrieve information from your Shipping Policies. | |
| **perPage** | **String**| Desired number of items per page, to retrieve information from your Shipping Policies. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiLogisticsPvtShippingPoliciesIdDelete"></a>
# **apiLogisticsPvtShippingPoliciesIdDelete**
> apiLogisticsPvtShippingPoliciesIdDelete(accept, contentType, id)

Delete shipping policies by ID

This endpoint deletes existing shipping policies from carriers in your store, searching by their IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ShippingPoliciesApi apiInstance = new ShippingPoliciesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Type of the content being sent
    String id = "id"; // String | ID of the shipping policy.
    try {
      apiInstance.apiLogisticsPvtShippingPoliciesIdDelete(accept, contentType, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingPoliciesApi#apiLogisticsPvtShippingPoliciesIdDelete");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **id** | **String**| ID of the shipping policy. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiLogisticsPvtShippingPoliciesIdGet"></a>
# **apiLogisticsPvtShippingPoliciesIdGet**
> apiLogisticsPvtShippingPoliciesIdGet(accept, contentType, id)

Retrieve shipping policy by ID

This endpoint lists existing [shipping policies](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) from carriers in your store, searching by their IDs.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ShippingPoliciesApi apiInstance = new ShippingPoliciesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Type of the content being sent
    String id = "id"; // String | ID of the shipping policy.
    try {
      apiInstance.apiLogisticsPvtShippingPoliciesIdGet(accept, contentType, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingPoliciesApi#apiLogisticsPvtShippingPoliciesIdGet");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **id** | **String**| ID of the shipping policy. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiLogisticsPvtShippingPoliciesIdPut"></a>
# **apiLogisticsPvtShippingPoliciesIdPut**
> apiLogisticsPvtShippingPoliciesIdPut(accept, contentType, id, requestBody1)

Update shipping policy

This endpoint updates information on existing Shipping Policies from carriers.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ShippingPoliciesApi apiInstance = new ShippingPoliciesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Type of the content being sent
    String id = "shippingpolicyid1"; // String | Shipping policy's ID
    RequestBody1 requestBody1 = new RequestBody1(); // RequestBody1 | 
    try {
      apiInstance.apiLogisticsPvtShippingPoliciesIdPut(accept, contentType, id, requestBody1);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingPoliciesApi#apiLogisticsPvtShippingPoliciesIdPut");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **id** | **String**| Shipping policy&#39;s ID | |
| **requestBody1** | [**RequestBody1**](RequestBody1.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiLogisticsPvtShippingPoliciesPost"></a>
# **apiLogisticsPvtShippingPoliciesPost**
> apiLogisticsPvtShippingPoliciesPost(accept, contentType, requestBody)

Create shipping policy

This endpoint creates new shipping policies from carriers in your store.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ShippingPoliciesApi apiInstance = new ShippingPoliciesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Type of the content being sent
    RequestBody requestBody = new RequestBody(); // RequestBody | 
    try {
      apiInstance.apiLogisticsPvtShippingPoliciesPost(accept, contentType, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingPoliciesApi#apiLogisticsPvtShippingPoliciesPost");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

