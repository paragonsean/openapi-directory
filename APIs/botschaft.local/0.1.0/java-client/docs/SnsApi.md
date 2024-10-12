# SnsApi

All URIs are relative to *http://botschaft.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**snsGetSnsGet**](SnsApi.md#snsGetSnsGet) | **GET** /sns | Sns Get |
| [**snsPostSnsPost**](SnsApi.md#snsPostSnsPost) | **POST** /sns | Sns Post |


<a id="snsGetSnsGet"></a>
# **snsGetSnsGet**
> Object snsGetSnsGet(message, base64Message, authorization)

Sns Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    SnsApi apiInstance = new SnsApi(defaultClient);
    String message = "message_example"; // String | 
    String base64Message = "base64Message_example"; // String | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.snsGetSnsGet(message, base64Message, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnsApi#snsGetSnsGet");
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
| **message** | **String**|  | [optional] |
| **base64Message** | **String**|  | [optional] |
| **authorization** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="snsPostSnsPost"></a>
# **snsPostSnsPost**
> Object snsPostSnsPost(snsMessageRequest, authorization)

Sns Post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    SnsApi apiInstance = new SnsApi(defaultClient);
    SnsMessageRequest snsMessageRequest = new SnsMessageRequest(); // SnsMessageRequest | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.snsPostSnsPost(snsMessageRequest, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnsApi#snsPostSnsPost");
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
| **snsMessageRequest** | [**SnsMessageRequest**](SnsMessageRequest.md)|  | |
| **authorization** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

