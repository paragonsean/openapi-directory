# TranslateApi

All URIs are relative to *http://libretranslate.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**detectPost**](TranslateApi.md#detectPost) | **POST** /detect | Detect the language of a single text |
| [**languagesGet**](TranslateApi.md#languagesGet) | **GET** /languages | Retrieve list of supported languages |
| [**translateFilePost**](TranslateApi.md#translateFilePost) | **POST** /translate_file | Translate file from a language to another |
| [**translatePost**](TranslateApi.md#translatePost) | **POST** /translate | Translate text from a language to another |


<a id="detectPost"></a>
# **detectPost**
> List&lt;DetectionsInner&gt; detectPost()

Detect the language of a single text



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://libretranslate.local");

    TranslateApi apiInstance = new TranslateApi(defaultClient);
    try {
      List<DetectionsInner> result = apiInstance.detectPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslateApi#detectPost");
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

[**List&lt;DetectionsInner&gt;**](DetectionsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detections |  -  |
| **400** | Invalid request |  -  |
| **403** | Banned |  -  |
| **429** | Slow down |  -  |
| **500** | Detection error |  -  |

<a id="languagesGet"></a>
# **languagesGet**
> List&lt;LanguagesInner&gt; languagesGet()

Retrieve list of supported languages



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://libretranslate.local");

    TranslateApi apiInstance = new TranslateApi(defaultClient);
    try {
      List<LanguagesInner> result = apiInstance.languagesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslateApi#languagesGet");
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

[**List&lt;LanguagesInner&gt;**](LanguagesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of languages |  -  |

<a id="translateFilePost"></a>
# **translateFilePost**
> TranslateFile translateFilePost()

Translate file from a language to another



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://libretranslate.local");

    TranslateApi apiInstance = new TranslateApi(defaultClient);
    try {
      TranslateFile result = apiInstance.translateFilePost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslateApi#translateFilePost");
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

[**TranslateFile**](TranslateFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Translated file |  -  |
| **400** | Invalid request |  -  |
| **403** | Banned |  -  |
| **429** | Slow down |  -  |
| **500** | Translation error |  -  |

<a id="translatePost"></a>
# **translatePost**
> Translate translatePost()

Translate text from a language to another



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://libretranslate.local");

    TranslateApi apiInstance = new TranslateApi(defaultClient);
    try {
      Translate result = apiInstance.translatePost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslateApi#translatePost");
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

[**Translate**](Translate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Translated text |  -  |
| **400** | Invalid request |  -  |
| **403** | Banned |  -  |
| **429** | Slow down |  -  |
| **500** | Translation error |  -  |

