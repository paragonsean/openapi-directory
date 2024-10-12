# CouponsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRnbPvtCouponPost**](CouponsApi.md#apiRnbPvtCouponPost) | **POST** /api/rnb/pvt/coupon/ | Create coupon |
| [**apiRnbPvtMultipleCouponsPost**](CouponsApi.md#apiRnbPvtMultipleCouponsPost) | **POST** /api/rnb/pvt/multiple-coupons | Create multiple coupons |
| [**archivebycouponcode**](CouponsApi.md#archivebycouponcode) | **POST** /api/rnb/pvt/archive/coupon/{couponCode} | Archive coupon by coupon code |
| [**getall**](CouponsApi.md#getall) | **GET** /api/rnb/pvt/coupon | Get all coupons |
| [**getarchivedbycouponcode**](CouponsApi.md#getarchivedbycouponcode) | **GET** /api/rnb/pvt/archive/coupon/{couponCode} | Get archived coupon by coupon code |
| [**getbycouponcode**](CouponsApi.md#getbycouponcode) | **GET** /api/rnb/pvt/coupon/{couponCode} | Get coupon by coupon code |
| [**getusage**](CouponsApi.md#getusage) | **GET** /api/rnb/pvt/coupon/usage/{couponCode} | Get coupon usage |
| [**massiveGeneration**](CouponsApi.md#massiveGeneration) | **POST** /api/rnb/pvt/coupons | Coupon Massive Generation |
| [**unarchivebycouponcode**](CouponsApi.md#unarchivebycouponcode) | **POST** /api/rnb/pvt/unarchive/coupon/{couponCode} | Unarchive coupon by coupon code |
| [**update**](CouponsApi.md#update) | **POST** /api/rnb/pvt/coupon | Update coupon |


<a id="apiRnbPvtCouponPost"></a>
# **apiRnbPvtCouponPost**
> Getarchivedbycouponcode200Response apiRnbPvtCouponPost(contentType, accept, apiRnbPvtCouponPostRequest)

Create coupon

Creates a single new coupon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    ApiRnbPvtCouponPostRequest apiRnbPvtCouponPostRequest = new ApiRnbPvtCouponPostRequest(); // ApiRnbPvtCouponPostRequest | 
    try {
      Getarchivedbycouponcode200Response result = apiInstance.apiRnbPvtCouponPost(contentType, accept, apiRnbPvtCouponPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#apiRnbPvtCouponPost");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **apiRnbPvtCouponPostRequest** | [**ApiRnbPvtCouponPostRequest**](ApiRnbPvtCouponPostRequest.md)|  | [optional] |

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="apiRnbPvtMultipleCouponsPost"></a>
# **apiRnbPvtMultipleCouponsPost**
> List&lt;String&gt; apiRnbPvtMultipleCouponsPost(contentType, accept, apiRnbPvtMultipleCouponsPostRequestInner)

Create multiple coupons

Creates multiple coupons with different coupon codes. This endpoint has a throttling of 60 requests per minute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    List<ApiRnbPvtMultipleCouponsPostRequestInner> apiRnbPvtMultipleCouponsPostRequestInner = Arrays.asList(); // List<ApiRnbPvtMultipleCouponsPostRequestInner> | 
    try {
      List<String> result = apiInstance.apiRnbPvtMultipleCouponsPost(contentType, accept, apiRnbPvtMultipleCouponsPostRequestInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#apiRnbPvtMultipleCouponsPost");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **apiRnbPvtMultipleCouponsPostRequestInner** | [**List&lt;ApiRnbPvtMultipleCouponsPostRequestInner&gt;**](ApiRnbPvtMultipleCouponsPostRequestInner.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="archivebycouponcode"></a>
# **archivebycouponcode**
> String archivebycouponcode(contentType, accept, couponCode)

Archive coupon by coupon code

Archives a specifc coupon by its coupon code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String couponCode = "test"; // String | Coupon Code
    try {
      String result = apiInstance.archivebycouponcode(contentType, accept, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#archivebycouponcode");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **couponCode** | **String**| Coupon Code | |

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getall"></a>
# **getall**
> List&lt;Getall200ResponseInner&gt; getall(contentType, accept)

Get all coupons

  &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Promotions and is organized by focusing on the developer&#39;s journey.     Retrieves all coupons from an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | 
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    try {
      List<Getall200ResponseInner> result = apiInstance.getall(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#getall");
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
| **contentType** | **String**|  | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |

### Return type

[**List&lt;Getall200ResponseInner&gt;**](Getall200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getarchivedbycouponcode"></a>
# **getarchivedbycouponcode**
> Getarchivedbycouponcode200Response getarchivedbycouponcode(contentType, accept, couponCode)

Get archived coupon by coupon code

Retrieves a specific archived coupon by its coupon code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String couponCode = "promo10"; // String | Coupon Code
    try {
      Getarchivedbycouponcode200Response result = apiInstance.getarchivedbycouponcode(contentType, accept, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#getarchivedbycouponcode");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **couponCode** | **String**| Coupon Code | |

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getbycouponcode"></a>
# **getbycouponcode**
> Getarchivedbycouponcode200Response getbycouponcode(contentType, accept, couponCode)

Get coupon by coupon code

Retrieves a specific coupon by its coupon code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String couponCode = "promo10"; // String | Coupon Code
    try {
      Getarchivedbycouponcode200Response result = apiInstance.getbycouponcode(contentType, accept, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#getbycouponcode");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **couponCode** | **String**| Coupon Code | |

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getusage"></a>
# **getusage**
> Getusage200Response getusage(contentType, accept, couponCode)

Get coupon usage

Retrieves information about the coupon usage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String couponCode = "test"; // String | Coupon Code
    try {
      Getusage200Response result = apiInstance.getusage(contentType, accept, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#getusage");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **couponCode** | **String**| Coupon Code | |

### Return type

[**Getusage200Response**](Getusage200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="massiveGeneration"></a>
# **massiveGeneration**
> List&lt;String&gt; massiveGeneration(contentType, accept, quantity, massiveGenerationRequest)

Coupon Massive Generation

Generates a massive amount of coupons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    Integer quantity = 10; // Integer | Quantity of coupons to generate
    MassiveGenerationRequest massiveGenerationRequest = new MassiveGenerationRequest(); // MassiveGenerationRequest | 
    try {
      List<String> result = apiInstance.massiveGeneration(contentType, accept, quantity, massiveGenerationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#massiveGeneration");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **quantity** | **Integer**| Quantity of coupons to generate | |
| **massiveGenerationRequest** | [**MassiveGenerationRequest**](MassiveGenerationRequest.md)|  | |

### Return type

**List&lt;String&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="unarchivebycouponcode"></a>
# **unarchivebycouponcode**
> String unarchivebycouponcode(contentType, accept, couponCode)

Unarchive coupon by coupon code

Unarchives a specifc coupon by its coupon code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String couponCode = "test"; // String | Coupon Code
    try {
      String result = apiInstance.unarchivebycouponcode(contentType, accept, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#unarchivebycouponcode");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **couponCode** | **String**| Coupon Code | |

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="update"></a>
# **update**
> Getarchivedbycouponcode200Response update(contentType, accept, updateRequest)

Update coupon

Updates information of a specific coupon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

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

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    UpdateRequest updateRequest = new UpdateRequest(); // UpdateRequest | 
    try {
      Getarchivedbycouponcode200Response result = apiInstance.update(contentType, accept, updateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#update");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **updateRequest** | [**UpdateRequest**](UpdateRequest.md)|  | |

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

