# NameApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiNameBrandNamePost**](NameApi.md#apiNameBrandNamePost) | **POST** /api/Name/BrandName | Generate brand name suggestions |
| [**apiNameBusinessNamePost**](NameApi.md#apiNameBusinessNamePost) | **POST** /api/Name/BusinessName | Get business names for a specific culture |
| [**apiNameCulturesGet**](NameApi.md#apiNameCulturesGet) | **GET** /api/Name/Cultures | Get available cultures |
| [**apiNameGet**](NameApi.md#apiNameGet) | **GET** /api/Name | Get name |
| [**apiNameSuggestionsGet**](NameApi.md#apiNameSuggestionsGet) | **GET** /api/Name/Suggestions | Get business name suggestions |


<a id="apiNameBrandNamePost"></a>
# **apiNameBrandNamePost**
> apiNameBrandNamePost(startingWords, xApiKey)

Generate brand name suggestions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NameApi apiInstance = new NameApi(defaultClient);
    String startingWords = "startingWords_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiNameBrandNamePost(startingWords, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameApi#apiNameBrandNamePost");
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
| **startingWords** | **String**|  | |
| **xApiKey** | **String**| Enter your key | [optional] |

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

<a id="apiNameBusinessNamePost"></a>
# **apiNameBusinessNamePost**
> apiNameBusinessNamePost(number, cultureCode, xApiKey)

Get business names for a specific culture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NameApi apiInstance = new NameApi(defaultClient);
    Integer number = 56; // Integer | 
    String cultureCode = "en_US"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiNameBusinessNamePost(number, cultureCode, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameApi#apiNameBusinessNamePost");
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
| **number** | **Integer**|  | |
| **cultureCode** | **String**|  | [optional] [default to en_US] |
| **xApiKey** | **String**| Enter your key | [optional] |

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

<a id="apiNameCulturesGet"></a>
# **apiNameCulturesGet**
> apiNameCulturesGet(xApiKey)

Get available cultures

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NameApi apiInstance = new NameApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiNameCulturesGet(xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameApi#apiNameCulturesGet");
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
| **xApiKey** | **String**| Enter your key | [optional] |

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

<a id="apiNameGet"></a>
# **apiNameGet**
> apiNameGet(nameType, quantity, xApiKey)

Get name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NameApi apiInstance = new NameApi(defaultClient);
    NameType nameType = NameType.fromValue("firstname"); // NameType | 
    Integer quantity = 56; // Integer | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiNameGet(nameType, quantity, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameApi#apiNameGet");
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
| **nameType** | [**NameType**](.md)|  | [enum: firstname, surname, fullname] |
| **quantity** | **Integer**|  | |
| **xApiKey** | **String**| Enter your key | [optional] |

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

<a id="apiNameSuggestionsGet"></a>
# **apiNameSuggestionsGet**
> apiNameSuggestionsGet(startingWords, xApiKey)

Get business name suggestions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NameApi apiInstance = new NameApi(defaultClient);
    String startingWords = "startingWords_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiNameSuggestionsGet(startingWords, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameApi#apiNameSuggestionsGet");
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
| **startingWords** | **String**|  | |
| **xApiKey** | **String**| Enter your key | [optional] |

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

