# PricingApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pricingBundlePricingPost**](PricingApi.md#pricingBundlePricingPost) | **POST** /pricing/bundle-pricing | Bundle pricing |
| [**pricingCompetitivePricingPost**](PricingApi.md#pricingCompetitivePricingPost) | **POST** /pricing/competitive-pricing |  |
| [**pricingCostPlusPricingPost**](PricingApi.md#pricingCostPlusPricingPost) | **POST** /pricing/cost-plus-pricing |  |
| [**pricingDecoyPricingPost**](PricingApi.md#pricingDecoyPricingPost) | **POST** /pricing/decoy-pricing |  |
| [**pricingOddPricingPost**](PricingApi.md#pricingOddPricingPost) | **POST** /pricing/odd-pricing |  |
| [**pricingPenetrationPricingPost**](PricingApi.md#pricingPenetrationPricingPost) | **POST** /pricing/penetration-pricing |  |
| [**pricingPriceElasticityOfDemandPost**](PricingApi.md#pricingPriceElasticityOfDemandPost) | **POST** /pricing/price-elasticity-of-demand |  |


<a id="pricingBundlePricingPost"></a>
# **pricingBundlePricingPost**
> pricingBundlePricingPost(token)

Bundle pricing

Bundle pricing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingBundlePricingPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingBundlePricingPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="pricingCompetitivePricingPost"></a>
# **pricingCompetitivePricingPost**
> pricingCompetitivePricingPost(token)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingCompetitivePricingPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingCompetitivePricingPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="pricingCostPlusPricingPost"></a>
# **pricingCostPlusPricingPost**
> pricingCostPlusPricingPost(token)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingCostPlusPricingPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingCostPlusPricingPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="pricingDecoyPricingPost"></a>
# **pricingDecoyPricingPost**
> pricingDecoyPricingPost(token)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingDecoyPricingPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingDecoyPricingPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="pricingOddPricingPost"></a>
# **pricingOddPricingPost**
> pricingOddPricingPost(token)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingOddPricingPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingOddPricingPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="pricingPenetrationPricingPost"></a>
# **pricingPenetrationPricingPost**
> pricingPenetrationPricingPost(token)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingPenetrationPricingPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingPenetrationPricingPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="pricingPriceElasticityOfDemandPost"></a>
# **pricingPriceElasticityOfDemandPost**
> pricingPriceElasticityOfDemandPost(token)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.pricingPriceElasticityOfDemandPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingPriceElasticityOfDemandPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

