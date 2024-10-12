# ExternalAmbassadorApiApi

All URIs are relative to *http://seldon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**predict**](ExternalAmbassadorApiApi.md#predict) | **POST** /seldon/{namespace}/{deployment}/api/v1.0/predictions |  |
| [**sendFeedback**](ExternalAmbassadorApiApi.md#sendFeedback) | **POST** /seldon/{namespace}/{deployment}/api/v1.0/feedback |  |


<a id="predict"></a>
# **predict**
> SeldonMessage predict(namespace, deployment, seldonMessage)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalAmbassadorApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ExternalAmbassadorApiApi apiInstance = new ExternalAmbassadorApiApi(defaultClient);
    String namespace = "namespace_example"; // String | 
    String deployment = "deployment_example"; // String | 
    SeldonMessage seldonMessage = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.predict(namespace, deployment, seldonMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalAmbassadorApiApi#predict");
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
| **namespace** | **String**|  | |
| **deployment** | **String**|  | |
| **seldonMessage** | [**SeldonMessage**](SeldonMessage.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, text/*
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="sendFeedback"></a>
# **sendFeedback**
> SeldonMessage sendFeedback(namespace, deployment, feedback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalAmbassadorApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ExternalAmbassadorApiApi apiInstance = new ExternalAmbassadorApiApi(defaultClient);
    String namespace = "namespace_example"; // String | 
    String deployment = "deployment_example"; // String | 
    Feedback feedback = new Feedback(); // Feedback | 
    try {
      SeldonMessage result = apiInstance.sendFeedback(namespace, deployment, feedback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalAmbassadorApiApi#sendFeedback");
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
| **namespace** | **String**|  | |
| **deployment** | **String**|  | |
| **feedback** | [**Feedback**](Feedback.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

