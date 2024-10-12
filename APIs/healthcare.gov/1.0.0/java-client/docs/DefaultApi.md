# DefaultApi

All URIs are relative to *https://www.healthcare.gov*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiArticlesmediaTypeExtensionGet**](DefaultApi.md#apiArticlesmediaTypeExtensionGet) | **GET** /api/articles{mediaTypeExtension} |  |
| [**apiBlogmediaTypeExtensionGet**](DefaultApi.md#apiBlogmediaTypeExtensionGet) | **GET** /api/blog{mediaTypeExtension} |  |
| [**apiGlossarymediaTypeExtensionGet**](DefaultApi.md#apiGlossarymediaTypeExtensionGet) | **GET** /api/glossary{mediaTypeExtension} |  |
| [**apiQuestionsmediaTypeExtensionGet**](DefaultApi.md#apiQuestionsmediaTypeExtensionGet) | **GET** /api/questions{mediaTypeExtension} |  |
| [**apiStatesmediaTypeExtensionGet**](DefaultApi.md#apiStatesmediaTypeExtensionGet) | **GET** /api/states{mediaTypeExtension} |  |
| [**apiTopicsmediaTypeExtensionGet**](DefaultApi.md#apiTopicsmediaTypeExtensionGet) | **GET** /api/topics{mediaTypeExtension} |  |
| [**blogPageNamemediaTypeExtensionGet**](DefaultApi.md#blogPageNamemediaTypeExtensionGet) | **GET** /blog/{pageName}{mediaTypeExtension} |  |
| [**esBlogPageNamemediaTypeExtensionGet**](DefaultApi.md#esBlogPageNamemediaTypeExtensionGet) | **GET** /es/blog/{pageName}{mediaTypeExtension} |  |
| [**esGlossaryPageNamemediaTypeExtensionGet**](DefaultApi.md#esGlossaryPageNamemediaTypeExtensionGet) | **GET** /es/glossary/{pageName}{mediaTypeExtension} |  |
| [**esPageNamemediaTypeExtensionGet**](DefaultApi.md#esPageNamemediaTypeExtensionGet) | **GET** /es/{pageName}{mediaTypeExtension} |  |
| [**esQuestionPageNamemediaTypeExtensionGet**](DefaultApi.md#esQuestionPageNamemediaTypeExtensionGet) | **GET** /es/question/{pageName}{mediaTypeExtension} |  |
| [**esStateNamemediaTypeExtensionGet**](DefaultApi.md#esStateNamemediaTypeExtensionGet) | **GET** /es/{stateName}{mediaTypeExtension} |  |
| [**glossaryPageNamemediaTypeExtensionGet**](DefaultApi.md#glossaryPageNamemediaTypeExtensionGet) | **GET** /glossary/{pageName}{mediaTypeExtension} |  |
| [**pageNamemediaTypeExtensionGet**](DefaultApi.md#pageNamemediaTypeExtensionGet) | **GET** /{pageName}{mediaTypeExtension} |  |
| [**questionPageNamemediaTypeExtensionGet**](DefaultApi.md#questionPageNamemediaTypeExtensionGet) | **GET** /question/{pageName}{mediaTypeExtension} |  |
| [**stateNamemediaTypeExtensionGet**](DefaultApi.md#stateNamemediaTypeExtensionGet) | **GET** /{stateName}{mediaTypeExtension} |  |


<a id="apiArticlesmediaTypeExtensionGet"></a>
# **apiArticlesmediaTypeExtensionGet**
> ArticlesList apiArticlesmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    try {
      ArticlesList result = apiInstance.apiArticlesmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiArticlesmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |

### Return type

[**ArticlesList**](ArticlesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="apiBlogmediaTypeExtensionGet"></a>
# **apiBlogmediaTypeExtensionGet**
> BlogList apiBlogmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    try {
      BlogList result = apiInstance.apiBlogmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiBlogmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |

### Return type

[**BlogList**](BlogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="apiGlossarymediaTypeExtensionGet"></a>
# **apiGlossarymediaTypeExtensionGet**
> GlossaryList apiGlossarymediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    try {
      GlossaryList result = apiInstance.apiGlossarymediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiGlossarymediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |

### Return type

[**GlossaryList**](GlossaryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="apiQuestionsmediaTypeExtensionGet"></a>
# **apiQuestionsmediaTypeExtensionGet**
> QuestionsList apiQuestionsmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    try {
      QuestionsList result = apiInstance.apiQuestionsmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiQuestionsmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |

### Return type

[**QuestionsList**](QuestionsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="apiStatesmediaTypeExtensionGet"></a>
# **apiStatesmediaTypeExtensionGet**
> StatesList apiStatesmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    try {
      StatesList result = apiInstance.apiStatesmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiStatesmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |

### Return type

[**StatesList**](StatesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="apiTopicsmediaTypeExtensionGet"></a>
# **apiTopicsmediaTypeExtensionGet**
> TopicsList apiTopicsmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    try {
      TopicsList result = apiInstance.apiTopicsmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiTopicsmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |

### Return type

[**TopicsList**](TopicsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="blogPageNamemediaTypeExtensionGet"></a>
# **blogPageNamemediaTypeExtensionGet**
> BlogPage blogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      BlogPage result = apiInstance.blogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#blogPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**BlogPage**](BlogPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="esBlogPageNamemediaTypeExtensionGet"></a>
# **esBlogPageNamemediaTypeExtensionGet**
> BlogPage esBlogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      BlogPage result = apiInstance.esBlogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#esBlogPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**BlogPage**](BlogPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="esGlossaryPageNamemediaTypeExtensionGet"></a>
# **esGlossaryPageNamemediaTypeExtensionGet**
> GlossaryPage esGlossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      GlossaryPage result = apiInstance.esGlossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#esGlossaryPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**GlossaryPage**](GlossaryPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="esPageNamemediaTypeExtensionGet"></a>
# **esPageNamemediaTypeExtensionGet**
> Page esPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      Page result = apiInstance.esPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#esPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="esQuestionPageNamemediaTypeExtensionGet"></a>
# **esQuestionPageNamemediaTypeExtensionGet**
> QuestionPage esQuestionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      QuestionPage result = apiInstance.esQuestionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#esQuestionPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**QuestionPage**](QuestionPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="esStateNamemediaTypeExtensionGet"></a>
# **esStateNamemediaTypeExtensionGet**
> StatePage esStateNamemediaTypeExtensionGet(mediaTypeExtension, stateName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String stateName = "stateName_example"; // String | 
    try {
      StatePage result = apiInstance.esStateNamemediaTypeExtensionGet(mediaTypeExtension, stateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#esStateNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **stateName** | **String**|  | |

### Return type

[**StatePage**](StatePage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="glossaryPageNamemediaTypeExtensionGet"></a>
# **glossaryPageNamemediaTypeExtensionGet**
> GlossaryPage glossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      GlossaryPage result = apiInstance.glossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#glossaryPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**GlossaryPage**](GlossaryPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="pageNamemediaTypeExtensionGet"></a>
# **pageNamemediaTypeExtensionGet**
> Page pageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      Page result = apiInstance.pageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="questionPageNamemediaTypeExtensionGet"></a>
# **questionPageNamemediaTypeExtensionGet**
> QuestionPage questionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String pageName = "pageName_example"; // String | 
    try {
      QuestionPage result = apiInstance.questionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#questionPageNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **pageName** | **String**|  | |

### Return type

[**QuestionPage**](QuestionPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

<a id="stateNamemediaTypeExtensionGet"></a>
# **stateNamemediaTypeExtensionGet**
> StatePage stateNamemediaTypeExtensionGet(mediaTypeExtension, stateName)



Returns pages content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.healthcare.gov");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | Omiting the param causes html to be returned.
    String stateName = "stateName_example"; // String | 
    try {
      StatePage result = apiInstance.stateNamemediaTypeExtensionGet(mediaTypeExtension, stateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stateNamemediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | [enum: .json] |
| **stateName** | **String**|  | |

### Return type

[**StatePage**](StatePage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Resource not found. |  -  |

