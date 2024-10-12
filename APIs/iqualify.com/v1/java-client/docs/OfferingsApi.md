# OfferingsApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsCurrentGet**](OfferingsApi.md#offeringsCurrentGet) | **GET** /offerings/current | Find active offerings |
| [**offeringsFutureGet**](OfferingsApi.md#offeringsFutureGet) | **GET** /offerings/future | Find scheduled offerings |
| [**offeringsGet**](OfferingsApi.md#offeringsGet) | **GET** /offerings | Find current, past and future offerings |
| [**offeringsInfoTextPatternGet**](OfferingsApi.md#offeringsInfoTextPatternGet) | **GET** /offerings/info/{textPattern} | Find offerings where info field matches the specified textPattern |
| [**offeringsOfferingIdGet**](OfferingsApi.md#offeringsOfferingIdGet) | **GET** /offerings/{offeringId} | Find offering by ID |
| [**offeringsOfferingIdPatch**](OfferingsApi.md#offeringsOfferingIdPatch) | **PATCH** /offerings/{offeringId} | Update offering |
| [**offeringsPastGet**](OfferingsApi.md#offeringsPastGet) | **GET** /offerings/past | Find past offerings |
| [**offeringsPost**](OfferingsApi.md#offeringsPost) | **POST** /offerings | Create offering |
| [**offeringsSummaryGet**](OfferingsApi.md#offeringsSummaryGet) | **GET** /offerings/summary | Offerings summary |


<a id="offeringsCurrentGet"></a>
# **offeringsCurrentGet**
> List&lt;OfferingMetadataResponse&gt; offeringsCurrentGet()

Find active offerings

Responds with active offerings for your organisation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    try {
      List<OfferingMetadataResponse> result = apiInstance.offeringsCurrentGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsCurrentGet");
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

[**List&lt;OfferingMetadataResponse&gt;**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | current offerings |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="offeringsFutureGet"></a>
# **offeringsFutureGet**
> List&lt;OfferingMetadataResponse&gt; offeringsFutureGet()

Find scheduled offerings

Responds with scheduled offerings for your organisation. Scheduled offerings have a start date after today&#39;s date (inclusive).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    try {
      List<OfferingMetadataResponse> result = apiInstance.offeringsFutureGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsFutureGet");
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

[**List&lt;OfferingMetadataResponse&gt;**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | future offerings |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="offeringsGet"></a>
# **offeringsGet**
> List&lt;OfferingMetadataResponse&gt; offeringsGet()

Find current, past and future offerings

Responds with all offerings for your organisation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    try {
      List<OfferingMetadataResponse> result = apiInstance.offeringsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsGet");
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

[**List&lt;OfferingMetadataResponse&gt;**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | all offerings (current, past and future ones) |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="offeringsInfoTextPatternGet"></a>
# **offeringsInfoTextPatternGet**
> List&lt;PortfolioActivations&gt; offeringsInfoTextPatternGet(textPattern)

Find offerings where info field matches the specified textPattern

Find offerings where info field matches the specified text pattern.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    String textPattern = "textPattern_example"; // String | Text pattern to search for (minimum of 3 characters length).
    try {
      List<PortfolioActivations> result = apiInstance.offeringsInfoTextPatternGet(textPattern);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsInfoTextPatternGet");
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
| **textPattern** | **String**| Text pattern to search for (minimum of 3 characters length). | |

### Return type

[**List&lt;PortfolioActivations&gt;**](PortfolioActivations.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offerings |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdGet"></a>
# **offeringsOfferingIdGet**
> OfferingMetadataResponse offeringsOfferingIdGet(offeringId)

Find offering by ID

Responds with an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      OfferingMetadataResponse result = apiInstance.offeringsOfferingIdGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsOfferingIdGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdPatch"></a>
# **offeringsOfferingIdPatch**
> OfferingMetadataResponse offeringsOfferingIdPatch(offeringId, offering)

Update offering

Updates the offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    Offering offering = new Offering(); // Offering | 
    try {
      OfferingMetadataResponse result = apiInstance.offeringsOfferingIdPatch(offeringId, offering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsOfferingIdPatch");
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
| **offeringId** | **String**| offering&#39;s id | |
| **offering** | [**Offering**](Offering.md)|  | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsPastGet"></a>
# **offeringsPastGet**
> List&lt;OfferingMetadataResponse&gt; offeringsPastGet()

Find past offerings

Responds with past offerings for your organisation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    try {
      List<OfferingMetadataResponse> result = apiInstance.offeringsPastGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsPastGet");
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

[**List&lt;OfferingMetadataResponse&gt;**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | past offerings |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="offeringsPost"></a>
# **offeringsPost**
> OfferingMetadataResponse offeringsPost(offeringRequired)

Create offering

Creates a new offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    OfferingRequired offeringRequired = new OfferingRequired(); // OfferingRequired | 
    try {
      OfferingMetadataResponse result = apiInstance.offeringsPost(offeringRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsPost");
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
| **offeringRequired** | [**OfferingRequired**](OfferingRequired.md)|  | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | offering created |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsSummaryGet"></a>
# **offeringsSummaryGet**
> List&lt;PortfolioActivations&gt; offeringsSummaryGet($top, $orderby, $filter)

Offerings summary

Responds with a summary of all offerings for your organisation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingsApi apiInstance = new OfferingsApi(defaultClient);
    String $top = "50"; // String | Returns only the first n results.
    String $orderby = "$orderby_example"; // String | Sorts the results.
    String $filter = "$filter_example"; // String | Filters the results, based on a Boolean condition.
    try {
      List<PortfolioActivations> result = apiInstance.offeringsSummaryGet($top, $orderby, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingsApi#offeringsSummaryGet");
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
| **$top** | **String**| Returns only the first n results. | [optional] [default to 50] |
| **$orderby** | **String**| Sorts the results. | [optional] |
| **$filter** | **String**| Filters the results, based on a Boolean condition. | [optional] |

### Return type

[**List&lt;PortfolioActivations&gt;**](PortfolioActivations.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | all offerings. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

