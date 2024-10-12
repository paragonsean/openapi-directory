# ShopsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shopsIdStorefrontsGet**](ShopsApi.md#shopsIdStorefrontsGet) | **GET** /shops/{id}/storefronts | Get storefront details on a shop. |
| [**shopsShopIdShippingProfilesGet**](ShopsApi.md#shopsShopIdShippingProfilesGet) | **GET** /shops/{shop_id}/shipping_profiles | List of shipping profiles for your shop |
| [**shopsSlugFeedbackBuyerGet**](ShopsApi.md#shopsSlugFeedbackBuyerGet) | **GET** /shops/{slug}/feedback/buyer | Get seller&#39;s feedback as a buyer |
| [**shopsSlugFeedbackGet**](ShopsApi.md#shopsSlugFeedbackGet) | **GET** /shops/{slug}/feedback | Get seller&#39;s feedback |
| [**shopsSlugFeedbackSellerGet**](ShopsApi.md#shopsSlugFeedbackSellerGet) | **GET** /shops/{slug}/feedback/seller | Get seller&#39;s feedback as a seller |
| [**shopsSlugGet**](ShopsApi.md#shopsSlugGet) | **GET** /shops/{slug} | Get details on a shop. |


<a id="shopsIdStorefrontsGet"></a>
# **shopsIdStorefrontsGet**
> shopsIdStorefrontsGet(id)

Get storefront details on a shop.

Get storefront details on a shop.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShopsApi apiInstance = new ShopsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.shopsIdStorefrontsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShopsApi#shopsIdStorefrontsGet");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="shopsShopIdShippingProfilesGet"></a>
# **shopsShopIdShippingProfilesGet**
> shopsShopIdShippingProfilesGet(shopId)

List of shipping profiles for your shop

List of shipping profiles for your shop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ShopsApi apiInstance = new ShopsApi(defaultClient);
    String shopId = "shopId_example"; // String | 
    try {
      apiInstance.shopsShopIdShippingProfilesGet(shopId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShopsApi#shopsShopIdShippingProfilesGet");
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
| **shopId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="shopsSlugFeedbackBuyerGet"></a>
# **shopsSlugFeedbackBuyerGet**
> shopsSlugFeedbackBuyerGet(slug)

Get seller&#39;s feedback as a buyer

Get seller&#39;s feedback as a buyer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShopsApi apiInstance = new ShopsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.shopsSlugFeedbackBuyerGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShopsApi#shopsSlugFeedbackBuyerGet");
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
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="shopsSlugFeedbackGet"></a>
# **shopsSlugFeedbackGet**
> shopsSlugFeedbackGet(slug)

Get seller&#39;s feedback

Get seller&#39;s feedback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShopsApi apiInstance = new ShopsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.shopsSlugFeedbackGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShopsApi#shopsSlugFeedbackGet");
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
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="shopsSlugFeedbackSellerGet"></a>
# **shopsSlugFeedbackSellerGet**
> shopsSlugFeedbackSellerGet(slug)

Get seller&#39;s feedback as a seller

Get seller&#39;s feedback as a seller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShopsApi apiInstance = new ShopsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.shopsSlugFeedbackSellerGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShopsApi#shopsSlugFeedbackSellerGet");
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
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="shopsSlugGet"></a>
# **shopsSlugGet**
> shopsSlugGet(slug, includeListingCount)

Get details on a shop.

Get details on a shop.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShopsApi apiInstance = new ShopsApi(defaultClient);
    String slug = "slug_example"; // String | 
    Boolean includeListingCount = true; // Boolean | Include the live listing count in the response.
    try {
      apiInstance.shopsSlugGet(slug, includeListingCount);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShopsApi#shopsSlugGet");
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
| **slug** | **String**|  | |
| **includeListingCount** | **Boolean**| Include the live listing count in the response. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

