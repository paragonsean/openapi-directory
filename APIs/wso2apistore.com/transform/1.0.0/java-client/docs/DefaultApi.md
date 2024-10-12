# DefaultApi

All URIs are relative to *https://gateway.wso2apistore.com/transform/1.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jsontoxmlPost**](DefaultApi.md#jsontoxmlPost) | **POST** /jsontoxml |  |
| [**xmltojsonPost**](DefaultApi.md#xmltojsonPost) | **POST** /xmltojson |  |


<a id="jsontoxmlPost"></a>
# **jsontoxmlPost**
> jsontoxmlPost(body)



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
    defaultClient.setBasePath("https://gateway.wso2apistore.com/transform/1.0.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String body = "body_example"; // String | JSON payload
    try {
      apiInstance.jsontoxmlPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jsontoxmlPost");
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
| **body** | **String**| JSON payload | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="xmltojsonPost"></a>
# **xmltojsonPost**
> xmltojsonPost(body)



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
    defaultClient.setBasePath("https://gateway.wso2apistore.com/transform/1.0.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String body = "body_example"; // String | XML payload
    try {
      apiInstance.xmltojsonPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#xmltojsonPost");
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
| **body** | **String**| XML payload | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

