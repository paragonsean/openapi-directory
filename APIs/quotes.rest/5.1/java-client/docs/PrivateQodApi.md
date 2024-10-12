# PrivateQodApi

All URIs are relative to *https://quotes.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**qodGet_0**](PrivateQodApi.md#qodGet_0) | **GET** /qod |  |
| [**qodPatch**](PrivateQodApi.md#qodPatch) | **PATCH** /qod |  |
| [**qodPut**](PrivateQodApi.md#qodPut) | **PUT** /qod |  |


<a id="qodGet_0"></a>
# **qodGet_0**
> QODResponse qodGet_0(category, language, id)



Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQodApi apiInstance = new PrivateQodApi(defaultClient);
    String category = "category_example"; // String | QOD Category (Used in public QOD only)
    String language = "en"; // String | Language of the QOD. The language must be supported in our QOD system.
    String id = "id_example"; // String | QOD defition id (Used in private QOD only)
    try {
      QODResponse result = apiInstance.qodGet_0(category, language, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQodApi#qodGet_0");
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

<a id="qodPatch"></a>
# **qodPatch**
> QuoteResponse qodPatch(title, repeatAfter, authors, _private, language, sfw)



Update an existing private &#x60;Quote of the Day&#x60; definition. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQodApi apiInstance = new PrivateQodApi(defaultClient);
    String title = "title_example"; // String | Title of the Quote of the day category
    Integer repeatAfter = 30; // Integer | How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
    List authors = new List(); // List | Comma seperated author names. Quotes will be chosen from one of these authors.
    Boolean _private = false; // Boolean | Should apply the filters to the private collection. Default is public quotes in the platform.
    String language = "en"; // String | Quotes language.
    Boolean sfw = false; // Boolean | Consider only quotes marked as \"sfw\" (Safe for work).
    try {
      QuoteResponse result = apiInstance.qodPatch(title, repeatAfter, authors, _private, language, sfw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQodApi#qodPatch");
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
| **title** | **String**| Title of the Quote of the day category | |
| **repeatAfter** | **Integer**| How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here. | [optional] [default to 30] |
| **authors** | **List**| Comma seperated author names. Quotes will be chosen from one of these authors. | [optional] |
| **_private** | **Boolean**| Should apply the filters to the private collection. Default is public quotes in the platform. | [optional] [default to false] |
| **language** | **String**| Quotes language. | [optional] [default to en] |
| **sfw** | **Boolean**| Consider only quotes marked as \&quot;sfw\&quot; (Safe for work). | [optional] [default to false] |

### Return type

[**QuoteResponse**](QuoteResponse.md)

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
| **403** | 403  No access response |  -  |

<a id="qodPut"></a>
# **qodPut**
> SuccessResponse qodPut(title, repeatAfter, authors, _private, language, sfw)



Create a private &#x60;Quote of the Day&#x60; service.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQodApi apiInstance = new PrivateQodApi(defaultClient);
    String title = "title_example"; // String | Title of the Quote of the day category
    Integer repeatAfter = 30; // Integer | How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
    List authors = new List(); // List | Comma seperated author names. Quotes will be chosen from one of these authors.
    Boolean _private = false; // Boolean | Should apply the filters to the private collection. Default is public quotes in the platform.
    String language = "en"; // String | Quotes language.
    Boolean sfw = false; // Boolean | Consider only quotes marked as \"sfw\" (Safe for work).
    try {
      SuccessResponse result = apiInstance.qodPut(title, repeatAfter, authors, _private, language, sfw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQodApi#qodPut");
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
| **title** | **String**| Title of the Quote of the day category | |
| **repeatAfter** | **Integer**| How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here. | [optional] [default to 30] |
| **authors** | **List**| Comma seperated author names. Quotes will be chosen from one of these authors. | [optional] |
| **_private** | **Boolean**| Should apply the filters to the private collection. Default is public quotes in the platform. | [optional] [default to false] |
| **language** | **String**| Quotes language. | [optional] [default to en] |
| **sfw** | **Boolean**| Consider only quotes marked as \&quot;sfw\&quot; (Safe for work). | [optional] [default to false] |

### Return type

[**SuccessResponse**](SuccessResponse.md)

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
| **403** | 403  No access response |  -  |

