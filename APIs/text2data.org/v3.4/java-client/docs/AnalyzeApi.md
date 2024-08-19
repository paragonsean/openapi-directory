# AnalyzeApi

All URIs are relative to *http://api.text2data.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyzeGet**](AnalyzeApi.md#analyzeGet) | **GET** /v3/Analyze | Test api response without api key |
| [**analyzePost**](AnalyzeApi.md#analyzePost) | **POST** /v3/Analyze | Sentiment analysis service |


<a id="analyzeGet"></a>
# **analyzeGet**
> DocumentResult analyzeGet()

Test api response without api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyzeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.text2data.org");

    AnalyzeApi apiInstance = new AnalyzeApi(defaultClient);
    try {
      DocumentResult result = apiInstance.analyzeGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyzeApi#analyzeGet");
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

[**DocumentResult**](DocumentResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="analyzePost"></a>
# **analyzePost**
> DocumentResult analyzePost(requestDoc)

Sentiment analysis service

Sample request:                    POST /Analyze      {         \&quot;DocumentText\&quot;: \&quot;Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.\&quot;,         \&quot;PrivateKey\&quot;: \&quot;your_api_key\&quot;,         \&quot;Secret\&quot;: \&quot;\&quot;      }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyzeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.text2data.org");

    AnalyzeApi apiInstance = new AnalyzeApi(defaultClient);
    Document requestDoc = new Document(); // Document | 
    try {
      DocumentResult result = apiInstance.analyzePost(requestDoc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyzeApi#analyzePost");
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
| **requestDoc** | [**Document**](Document.md)|  | |

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

