# ExtractApi

All URIs are relative to *http://api.text2data.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extractGet**](ExtractApi.md#extractGet) | **GET** /v3/Extract | Test api response without api key |
| [**extractPost**](ExtractApi.md#extractPost) | **POST** /v3/Extract | Document extraction service |


<a id="extractGet"></a>
# **extractGet**
> DocumentResult extractGet()

Test api response without api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtractApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.text2data.org");

    ExtractApi apiInstance = new ExtractApi(defaultClient);
    try {
      DocumentResult result = apiInstance.extractGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtractApi#extractGet");
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

<a id="extractPost"></a>
# **extractPost**
> DocumentResult extractPost(requestDoc)

Document extraction service

Sample request:                    POST /Extract      {         \&quot;DocumentText\&quot;: \&quot;Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.\&quot;,         \&quot;PrivateKey\&quot;: \&quot;your_api_key\&quot;,         \&quot;UserCategoryModelName\&quot;: \&quot;your_model_name\&quot;,         \&quot;Secret\&quot;: \&quot;\&quot;      }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtractApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.text2data.org");

    ExtractApi apiInstance = new ExtractApi(defaultClient);
    Document requestDoc = new Document(); // Document | 
    try {
      DocumentResult result = apiInstance.extractPost(requestDoc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtractApi#extractPost");
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

