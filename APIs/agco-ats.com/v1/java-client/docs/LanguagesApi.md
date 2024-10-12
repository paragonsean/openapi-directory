# LanguagesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**languagesCreateLanguage**](LanguagesApi.md#languagesCreateLanguage) | **POST** /api/v2/Languages | Add a Language to support for translations. Accepts a Language object. Returns the Id of the created object. |
| [**languagesDeleteLanguage**](LanguagesApi.md#languagesDeleteLanguage) | **DELETE** /api/v2/Languages/{LocaleID} | Remove a Language from those supported for translations. Marks language as deleted. |
| [**languagesGetLanguage**](LanguagesApi.md#languagesGetLanguage) | **GET** /api/v2/Languages/{LocaleID} | Get a language by its id. Returns a Language object |
| [**languagesGetLanguages**](LanguagesApi.md#languagesGetLanguages) | **GET** /api/v2/Languages | Get a list of the languages for which translations are supported. Returns a PagedResponse of Language objects. |
| [**languagesUpdateLanguage**](LanguagesApi.md#languagesUpdateLanguage) | **PUT** /api/v2/Languages/{LocaleID} | Update a language’s description. Accepts a Language object. |


<a id="languagesCreateLanguage"></a>
# **languagesCreateLanguage**
> Integer languagesCreateLanguage(globalResourcesSharedModelsLanguage)

Add a Language to support for translations. Accepts a Language object. Returns the Id of the created object.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    GlobalResourcesSharedModelsLanguage globalResourcesSharedModelsLanguage = new GlobalResourcesSharedModelsLanguage(); // GlobalResourcesSharedModelsLanguage | 
    try {
      Integer result = apiInstance.languagesCreateLanguage(globalResourcesSharedModelsLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#languagesCreateLanguage");
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
| **globalResourcesSharedModelsLanguage** | [**GlobalResourcesSharedModelsLanguage**](GlobalResourcesSharedModelsLanguage.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="languagesDeleteLanguage"></a>
# **languagesDeleteLanguage**
> languagesDeleteLanguage(localeID)

Remove a Language from those supported for translations. Marks language as deleted.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    Integer localeID = 56; // Integer | 
    try {
      apiInstance.languagesDeleteLanguage(localeID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#languagesDeleteLanguage");
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
| **localeID** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="languagesGetLanguage"></a>
# **languagesGetLanguage**
> GlobalResourcesSharedModelsLanguage languagesGetLanguage(localeID)

Get a language by its id. Returns a Language object

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    Integer localeID = 56; // Integer | 
    try {
      GlobalResourcesSharedModelsLanguage result = apiInstance.languagesGetLanguage(localeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#languagesGetLanguage");
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
| **localeID** | **Integer**|  | |

### Return type

[**GlobalResourcesSharedModelsLanguage**](GlobalResourcesSharedModelsLanguage.md)

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

<a id="languagesGetLanguages"></a>
# **languagesGetLanguages**
> APIIPagedResponseGlobalResourcesSharedModelsLanguage languagesGetLanguages(limit, offset, includeDeleted)

Get a list of the languages for which translations are supported. Returns a PagedResponse of Language objects.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    Integer limit = 56; // Integer | limit the number of Language objects returned. Optional (defaults to 10).
    Integer offset = 56; // Integer | the number of Language objects to skip. Optional (defaults to 0).
    Boolean includeDeleted = true; // Boolean | whether to include languages marked as deleted. Defaults to false
    try {
      APIIPagedResponseGlobalResourcesSharedModelsLanguage result = apiInstance.languagesGetLanguages(limit, offset, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#languagesGetLanguages");
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
| **limit** | **Integer**| limit the number of Language objects returned. Optional (defaults to 10). | [optional] |
| **offset** | **Integer**| the number of Language objects to skip. Optional (defaults to 0). | [optional] |
| **includeDeleted** | **Boolean**| whether to include languages marked as deleted. Defaults to false | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsLanguage**](APIIPagedResponseGlobalResourcesSharedModelsLanguage.md)

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

<a id="languagesUpdateLanguage"></a>
# **languagesUpdateLanguage**
> languagesUpdateLanguage(localeID, globalResourcesSharedModelsLanguage)

Update a language’s description. Accepts a Language object.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    Integer localeID = 56; // Integer | 
    GlobalResourcesSharedModelsLanguage globalResourcesSharedModelsLanguage = new GlobalResourcesSharedModelsLanguage(); // GlobalResourcesSharedModelsLanguage | 
    try {
      apiInstance.languagesUpdateLanguage(localeID, globalResourcesSharedModelsLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#languagesUpdateLanguage");
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
| **localeID** | **Integer**|  | |
| **globalResourcesSharedModelsLanguage** | [**GlobalResourcesSharedModelsLanguage**](GlobalResourcesSharedModelsLanguage.md)|  | |

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

