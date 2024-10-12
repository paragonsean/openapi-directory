# NlpAnnotateApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnnotate**](NlpAnnotateApi.md#getAnnotate) | **GET** /nlp/annotate/ | Annotate a given text using SciGraph annotator |
| [**getAnnotateEntities**](NlpAnnotateApi.md#getAnnotateEntities) | **GET** /nlp/annotate/entities | Annotate a given content using SciGraph annotator and get all entities from content |
| [**postAnnotate**](NlpAnnotateApi.md#postAnnotate) | **POST** /nlp/annotate/ | Annotate a given text using SciGraph annotator |
| [**postAnnotateEntities**](NlpAnnotateApi.md#postAnnotateEntities) | **POST** /nlp/annotate/entities | Annotate a given content using SciGraph annotator and get all entities from content |


<a id="getAnnotate"></a>
# **getAnnotate**
> getAnnotate(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers)

Annotate a given text using SciGraph annotator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NlpAnnotateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    NlpAnnotateApi apiInstance = new NlpAnnotateApi(defaultClient);
    String content = "content_example"; // String | The text content to annotate
    List<String> includeCategory = Arrays.asList(); // List<String> | Categories to include for annotation
    List<String> excludeCategory = Arrays.asList(); // List<String> | Categories to exclude for annotation
    String minLength = "4"; // String | The minimum number of characters in the annotated entity
    Boolean longestOnly = false; // Boolean | Should only the longest entity be returned for an overlapping group
    Boolean includeAbbreviation = false; // Boolean | Should abbreviations be included
    Boolean includeAcronym = false; // Boolean | Should acronyms be included
    Boolean includeNumbers = false; // Boolean | Should numbers be included
    try {
      apiInstance.getAnnotate(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers);
    } catch (ApiException e) {
      System.err.println("Exception when calling NlpAnnotateApi#getAnnotate");
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
| **content** | **String**| The text content to annotate | [optional] |
| **includeCategory** | [**List&lt;String&gt;**](String.md)| Categories to include for annotation | [optional] |
| **excludeCategory** | [**List&lt;String&gt;**](String.md)| Categories to exclude for annotation | [optional] |
| **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to 4] |
| **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false] |
| **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false] |
| **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false] |
| **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false] |

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

<a id="getAnnotateEntities"></a>
# **getAnnotateEntities**
> EntityAnnotationResult getAnnotateEntities(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers)

Annotate a given content using SciGraph annotator and get all entities from content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NlpAnnotateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    NlpAnnotateApi apiInstance = new NlpAnnotateApi(defaultClient);
    String content = "content_example"; // String | The text content to annotate
    List<String> includeCategory = Arrays.asList(); // List<String> | Categories to include for annotation
    List<String> excludeCategory = Arrays.asList(); // List<String> | Categories to exclude for annotation
    String minLength = "4"; // String | The minimum number of characters in the annotated entity
    Boolean longestOnly = false; // Boolean | Should only the longest entity be returned for an overlapping group
    Boolean includeAbbreviation = false; // Boolean | Should abbreviations be included
    Boolean includeAcronym = false; // Boolean | Should acronyms be included
    Boolean includeNumbers = false; // Boolean | Should numbers be included
    try {
      EntityAnnotationResult result = apiInstance.getAnnotateEntities(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NlpAnnotateApi#getAnnotateEntities");
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
| **content** | **String**| The text content to annotate | [optional] |
| **includeCategory** | [**List&lt;String&gt;**](String.md)| Categories to include for annotation | [optional] |
| **excludeCategory** | [**List&lt;String&gt;**](String.md)| Categories to exclude for annotation | [optional] |
| **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to 4] |
| **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false] |
| **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false] |
| **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false] |
| **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false] |

### Return type

[**EntityAnnotationResult**](EntityAnnotationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="postAnnotate"></a>
# **postAnnotate**
> postAnnotate(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers)

Annotate a given text using SciGraph annotator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NlpAnnotateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    NlpAnnotateApi apiInstance = new NlpAnnotateApi(defaultClient);
    String content = "content_example"; // String | The text content to annotate
    List<String> includeCategory = Arrays.asList(); // List<String> | Categories to include for annotation
    List<String> excludeCategory = Arrays.asList(); // List<String> | Categories to exclude for annotation
    String minLength = "4"; // String | The minimum number of characters in the annotated entity
    Boolean longestOnly = false; // Boolean | Should only the longest entity be returned for an overlapping group
    Boolean includeAbbreviation = false; // Boolean | Should abbreviations be included
    Boolean includeAcronym = false; // Boolean | Should acronyms be included
    Boolean includeNumbers = false; // Boolean | Should numbers be included
    try {
      apiInstance.postAnnotate(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers);
    } catch (ApiException e) {
      System.err.println("Exception when calling NlpAnnotateApi#postAnnotate");
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
| **content** | **String**| The text content to annotate | [optional] |
| **includeCategory** | [**List&lt;String&gt;**](String.md)| Categories to include for annotation | [optional] |
| **excludeCategory** | [**List&lt;String&gt;**](String.md)| Categories to exclude for annotation | [optional] |
| **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to 4] |
| **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false] |
| **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false] |
| **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false] |
| **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false] |

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

<a id="postAnnotateEntities"></a>
# **postAnnotateEntities**
> EntityAnnotationResult postAnnotateEntities(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers)

Annotate a given content using SciGraph annotator and get all entities from content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NlpAnnotateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    NlpAnnotateApi apiInstance = new NlpAnnotateApi(defaultClient);
    String content = "content_example"; // String | The text content to annotate
    List<String> includeCategory = Arrays.asList(); // List<String> | Categories to include for annotation
    List<String> excludeCategory = Arrays.asList(); // List<String> | Categories to exclude for annotation
    String minLength = "4"; // String | The minimum number of characters in the annotated entity
    Boolean longestOnly = false; // Boolean | Should only the longest entity be returned for an overlapping group
    Boolean includeAbbreviation = false; // Boolean | Should abbreviations be included
    Boolean includeAcronym = false; // Boolean | Should acronyms be included
    Boolean includeNumbers = false; // Boolean | Should numbers be included
    try {
      EntityAnnotationResult result = apiInstance.postAnnotateEntities(content, includeCategory, excludeCategory, minLength, longestOnly, includeAbbreviation, includeAcronym, includeNumbers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NlpAnnotateApi#postAnnotateEntities");
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
| **content** | **String**| The text content to annotate | [optional] |
| **includeCategory** | [**List&lt;String&gt;**](String.md)| Categories to include for annotation | [optional] |
| **excludeCategory** | [**List&lt;String&gt;**](String.md)| Categories to exclude for annotation | [optional] |
| **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to 4] |
| **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false] |
| **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false] |
| **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false] |
| **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false] |

### Return type

[**EntityAnnotationResult**](EntityAnnotationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

