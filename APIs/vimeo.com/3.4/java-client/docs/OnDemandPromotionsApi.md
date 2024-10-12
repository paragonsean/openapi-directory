# OnDemandPromotionsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVodPromotion**](OnDemandPromotionsApi.md#createVodPromotion) | **POST** /ondemand/pages/{ondemand_id}/promotions | Add a promotion to an On Demand page |
| [**deleteVodPromotion**](OnDemandPromotionsApi.md#deleteVodPromotion) | **DELETE** /ondemand/pages/{ondemand_id}/promotions/{promotion_id} | Remove a promotion from an On Demand page |
| [**getVodPromotion**](OnDemandPromotionsApi.md#getVodPromotion) | **GET** /ondemand/pages/{ondemand_id}/promotions/{promotion_id} | Get a specific promotion on an On Demand page |
| [**getVodPromotionCodes**](OnDemandPromotionsApi.md#getVodPromotionCodes) | **GET** /ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes | Get all the codes of a promotion on an On Demand page |
| [**getVodPromotions**](OnDemandPromotionsApi.md#getVodPromotions) | **GET** /ondemand/pages/{ondemand_id}/promotions | Get all the promotions on an On Demand page |


<a id="createVodPromotion"></a>
# **createVodPromotion**
> OnDemandPromotion createVodPromotion(ondemandId, createVodPromotionRequest)

Add a promotion to an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPromotionsApi apiInstance = new OnDemandPromotionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    CreateVodPromotionRequest createVodPromotionRequest = new CreateVodPromotionRequest(); // CreateVodPromotionRequest | 
    try {
      OnDemandPromotion result = apiInstance.createVodPromotion(ondemandId, createVodPromotionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPromotionsApi#createVodPromotion");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **createVodPromotionRequest** | [**CreateVodPromotionRequest**](CreateVodPromotionRequest.md)|  | |

### Return type

[**OnDemandPromotion**](OnDemandPromotion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.ondemand.promotion+json
 - **Accept**: application/vnd.vimeo.ondemand.promotion+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The promotion was added. |  -  |
| **400** | * There are errors in the request. * The promo code already exists. |  -  |
| **403** | You can&#39;t create promotions for an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page exists. |  -  |

<a id="deleteVodPromotion"></a>
# **deleteVodPromotion**
> deleteVodPromotion(ondemandId, promotionId)

Remove a promotion from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPromotionsApi apiInstance = new OnDemandPromotionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal promotionId = new BigDecimal("12345"); // BigDecimal | The ID of the promotion.
    try {
      apiInstance.deleteVodPromotion(ondemandId, promotionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPromotionsApi#deleteVodPromotion");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **promotionId** | **BigDecimal**| The ID of the promotion. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The promotion was deleted. |  -  |
| **403** | You can&#39;t delete a promotion for an On Demand page that you not own. |  -  |
| **404** | No such On Demand page or promotion exists. |  -  |

<a id="getVodPromotion"></a>
# **getVodPromotion**
> OnDemandPromotion getVodPromotion(ondemandId, promotionId)

Get a specific promotion on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPromotionsApi apiInstance = new OnDemandPromotionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal promotionId = new BigDecimal("12345"); // BigDecimal | The ID of the promotion.
    try {
      OnDemandPromotion result = apiInstance.getVodPromotion(ondemandId, promotionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPromotionsApi#getVodPromotion");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **promotionId** | **BigDecimal**| The ID of the promotion. | |

### Return type

[**OnDemandPromotion**](OnDemandPromotion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.promotion+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The promotion was returned. |  -  |
| **403** | You can&#39;t view a promotion for an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or promotion exists. |  -  |

<a id="getVodPromotionCodes"></a>
# **getVodPromotionCodes**
> OnDemandPromotionCode getVodPromotionCodes(ondemandId, promotionId, page, perPage)

Get all the codes of a promotion on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPromotionsApi apiInstance = new OnDemandPromotionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal promotionId = new BigDecimal("12345"); // BigDecimal | The ID of the promotion.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      OnDemandPromotionCode result = apiInstance.getVodPromotionCodes(ondemandId, promotionId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPromotionsApi#getVodPromotionCodes");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **promotionId** | **BigDecimal**| The ID of the promotion. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**OnDemandPromotionCode**](OnDemandPromotionCode.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.promocode+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The codes were returned. |  -  |
| **403** | You can&#39;t create promotions for an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page exists. |  -  |

<a id="getVodPromotions"></a>
# **getVodPromotions**
> OnDemandPromotion getVodPromotions(ondemandId, filter, page, perPage)

Get all the promotions on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPromotionsApi apiInstance = new OnDemandPromotionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    String filter = "batch"; // String | The filter to apply to the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      OnDemandPromotion result = apiInstance.getVodPromotions(ondemandId, filter, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPromotionsApi#getVodPromotions");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **filter** | **String**| The filter to apply to the results. | [enum: batch, default, single, vip] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**OnDemandPromotion**](OnDemandPromotion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.promotion+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The promotions were returned. |  -  |
| **400** | The filter is invalid. |  -  |
| **403** | You can&#39;t view promotions for an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page exists. |  -  |

