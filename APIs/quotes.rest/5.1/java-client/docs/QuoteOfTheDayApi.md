# QuoteOfTheDayApi

All URIs are relative to *https://quotes.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**qodCategoriesGet**](QuoteOfTheDayApi.md#qodCategoriesGet) | **GET** /qod/categories |  |
| [**qodGet**](QuoteOfTheDayApi.md#qodGet) | **GET** /qod |  |
| [**qodLanguagesGet**](QuoteOfTheDayApi.md#qodLanguagesGet) | **GET** /qod/languages |  |


<a id="qodCategoriesGet"></a>
# **qodCategoriesGet**
> qodCategoriesGet(language, detailed)



Gets a list of &#x60;Quote of the Day&#x60; Categories. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteOfTheDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteOfTheDayApi apiInstance = new QuoteOfTheDayApi(defaultClient);
    String language = "en"; // String | Language of the QOD category. The language must be supported in our QOD system.
    Boolean detailed = false; // Boolean | Return detailed information of the categories. Note the data format changes between the two values of this switch.
    try {
      apiInstance.qodCategoriesGet(language, detailed);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteOfTheDayApi#qodCategoriesGet");
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
| **language** | **String**| Language of the QOD category. The language must be supported in our QOD system. | [optional] [default to en] |
| **detailed** | **Boolean**| Return detailed information of the categories. Note the data format changes between the two values of this switch. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **400** | 400  response |  -  |

<a id="qodGet"></a>
# **qodGet**
> QODResponse qodGet(category, language, id)



Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteOfTheDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteOfTheDayApi apiInstance = new QuoteOfTheDayApi(defaultClient);
    String category = "category_example"; // String | QOD Category (Used in public QOD only)
    String language = "en"; // String | Language of the QOD. The language must be supported in our QOD system.
    String id = "id_example"; // String | QOD defition id (Used in private QOD only)
    try {
      QODResponse result = apiInstance.qodGet(category, language, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteOfTheDayApi#qodGet");
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
| **category** | **String**| QOD Category (Used in public QOD only) | [optional] |
| **language** | **String**| Language of the QOD. The language must be supported in our QOD system. | [optional] [default to en] |
| **id** | **String**| QOD defition id (Used in private QOD only) | [optional] |

### Return type

[**QODResponse**](QODResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **400** | 400  response |  -  |

<a id="qodLanguagesGet"></a>
# **qodLanguagesGet**
> qodLanguagesGet()



Gets a list of supported languages for &#x60;Quote of the Day&#x60;.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteOfTheDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteOfTheDayApi apiInstance = new QuoteOfTheDayApi(defaultClient);
    try {
      apiInstance.qodLanguagesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteOfTheDayApi#qodLanguagesGet");
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

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |

