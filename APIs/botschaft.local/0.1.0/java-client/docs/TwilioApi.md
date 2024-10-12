# TwilioApi

All URIs are relative to *http://botschaft.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**twilioMessageGetTwilioGet**](TwilioApi.md#twilioMessageGetTwilioGet) | **GET** /twilio | Twilio Message Get |
| [**twilioMessagePostTwilioPost**](TwilioApi.md#twilioMessagePostTwilioPost) | **POST** /twilio | Twilio Message Post |


<a id="twilioMessageGetTwilioGet"></a>
# **twilioMessageGetTwilioGet**
> Object twilioMessageGetTwilioGet(to, message, base64Message, authorization)

Twilio Message Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    TwilioApi apiInstance = new TwilioApi(defaultClient);
    String to = "to_example"; // String | 
    String message = "message_example"; // String | 
    String base64Message = "base64Message_example"; // String | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.twilioMessageGetTwilioGet(to, message, base64Message, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TwilioApi#twilioMessageGetTwilioGet");
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
| **to** | **String**|  | |
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

<a id="twilioMessagePostTwilioPost"></a>
# **twilioMessagePostTwilioPost**
> Object twilioMessagePostTwilioPost(twilioMessageRequest, authorization)

Twilio Message Post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    TwilioApi apiInstance = new TwilioApi(defaultClient);
    TwilioMessageRequest twilioMessageRequest = new TwilioMessageRequest(); // TwilioMessageRequest | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.twilioMessagePostTwilioPost(twilioMessageRequest, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TwilioApi#twilioMessagePostTwilioPost");
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
| **twilioMessageRequest** | [**TwilioMessageRequest**](TwilioMessageRequest.md)|  | |
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

