# InformationRetrievalApi

All URIs are relative to *http://api.datumbox.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keywordExtraction**](InformationRetrievalApi.md#keywordExtraction) | **POST** /1.0/KeywordExtraction.json | Extracts the Keywords of the Document |
| [**textExtraction**](InformationRetrievalApi.md#textExtraction) | **POST** /1.0/TextExtraction.json | Extracts the clear text from Webpage |


<a id="keywordExtraction"></a>
# **keywordExtraction**
> keywordExtraction(apiKey, n, text)

Extracts the Keywords of the Document

The Keyword Extraction function enables you to extract from an arbitrary document all the keywords and word-combinations along with their occurrences in the text.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InformationRetrievalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    InformationRetrievalApi apiInstance = new InformationRetrievalApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    Integer n = 56; // Integer | The number of keyword combinations (n-grams) that you wish to extract.
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.keywordExtraction(apiKey, n, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling InformationRetrievalApi#keywordExtraction");
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
| **apiKey** | **String**| Your API Key | |
| **n** | **Integer**| The number of keyword combinations (n-grams) that you wish to extract. | [optional] |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="textExtraction"></a>
# **textExtraction**
> textExtraction(apiKey, text)

Extracts the clear text from Webpage

The Text Extraction function enables you to extract the important information from a given webpage. Extracting the clear text of the documents is an important step before any other analysis.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InformationRetrievalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    InformationRetrievalApi apiInstance = new InformationRetrievalApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The HTML source of the webpage.
    try {
      apiInstance.textExtraction(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling InformationRetrievalApi#textExtraction");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The HTML source of the webpage. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

