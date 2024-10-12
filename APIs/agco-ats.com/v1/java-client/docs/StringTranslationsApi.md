# StringTranslationsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stringTranslationsGetTranslation**](StringTranslationsApi.md#stringTranslationsGetTranslation) | **GET** /api/v2/StringTranslations/{stringId}/{languageId} | Get a single translation based upon stringId and languageId |
| [**stringTranslationsGetTranslations**](StringTranslationsApi.md#stringTranslationsGetTranslations) | **GET** /api/v2/StringTranslations | Get a paged response of Global String Translations. |
| [**stringTranslationsUpdateTranslation**](StringTranslationsApi.md#stringTranslationsUpdateTranslation) | **PUT** /api/v2/StringTranslations/{stringId}/{languageId} | Update a string value or a state for a string translation. |
| [**stringTranslationsUpdateTranslations**](StringTranslationsApi.md#stringTranslationsUpdateTranslations) | **PUT** /api/v2/StringTranslations/Batch | Update corrections to string translations |


<a id="stringTranslationsGetTranslation"></a>
# **stringTranslationsGetTranslation**
> GlobalResourcesSharedModelsStringTranslation stringTranslationsGetTranslation(stringId, languageId)

Get a single translation based upon stringId and languageId

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringTranslationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringTranslationsApi apiInstance = new StringTranslationsApi(defaultClient);
    String stringId = "stringId_example"; // String | 
    Integer languageId = 56; // Integer | 
    try {
      GlobalResourcesSharedModelsStringTranslation result = apiInstance.stringTranslationsGetTranslation(stringId, languageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringTranslationsApi#stringTranslationsGetTranslation");
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
| **stringId** | **String**|  | |
| **languageId** | **Integer**|  | |

### Return type

[**GlobalResourcesSharedModelsStringTranslation**](GlobalResourcesSharedModelsStringTranslation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="stringTranslationsGetTranslations"></a>
# **stringTranslationsGetTranslations**
> APIIPagedResponseGlobalResourcesSharedModelsStringTranslation stringTranslationsGetTranslations(limit, modifiedAfterTimestamp)

Get a paged response of Global String Translations.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringTranslationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringTranslationsApi apiInstance = new StringTranslationsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    String modifiedAfterTimestamp = "modifiedAfterTimestamp_example"; // String | Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
    try {
      APIIPagedResponseGlobalResourcesSharedModelsStringTranslation result = apiInstance.stringTranslationsGetTranslations(limit, modifiedAfterTimestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringTranslationsApi#stringTranslationsGetTranslations");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **modifiedAfterTimestamp** | **String**| Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array. | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsStringTranslation**](APIIPagedResponseGlobalResourcesSharedModelsStringTranslation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="stringTranslationsUpdateTranslation"></a>
# **stringTranslationsUpdateTranslation**
> stringTranslationsUpdateTranslation(stringId, languageId, globalResourcesSharedModelsStringTranslation)

Update a string value or a state for a string translation.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringTranslationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringTranslationsApi apiInstance = new StringTranslationsApi(defaultClient);
    String stringId = "stringId_example"; // String | 
    Integer languageId = 56; // Integer | 
    GlobalResourcesSharedModelsStringTranslation globalResourcesSharedModelsStringTranslation = new GlobalResourcesSharedModelsStringTranslation(); // GlobalResourcesSharedModelsStringTranslation | 
    try {
      apiInstance.stringTranslationsUpdateTranslation(stringId, languageId, globalResourcesSharedModelsStringTranslation);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringTranslationsApi#stringTranslationsUpdateTranslation");
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
| **stringId** | **String**|  | |
| **languageId** | **Integer**|  | |
| **globalResourcesSharedModelsStringTranslation** | [**GlobalResourcesSharedModelsStringTranslation**](GlobalResourcesSharedModelsStringTranslation.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="stringTranslationsUpdateTranslations"></a>
# **stringTranslationsUpdateTranslations**
> stringTranslationsUpdateTranslations(globalResourcesSharedModelsStringTranslation)

Update corrections to string translations

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringTranslationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringTranslationsApi apiInstance = new StringTranslationsApi(defaultClient);
    List<GlobalResourcesSharedModelsStringTranslation> globalResourcesSharedModelsStringTranslation = Arrays.asList(); // List<GlobalResourcesSharedModelsStringTranslation> | 
    try {
      apiInstance.stringTranslationsUpdateTranslations(globalResourcesSharedModelsStringTranslation);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringTranslationsApi#stringTranslationsUpdateTranslations");
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
| **globalResourcesSharedModelsStringTranslation** | [**List&lt;GlobalResourcesSharedModelsStringTranslation&gt;**](GlobalResourcesSharedModelsStringTranslation.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

