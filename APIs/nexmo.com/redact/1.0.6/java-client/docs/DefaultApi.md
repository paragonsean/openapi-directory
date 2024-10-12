# DefaultApi

All URIs are relative to *https://api.nexmo.com/v1/redact*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**redactMessage**](DefaultApi.md#redactMessage) | **POST** /transaction | Redact a specific message |


<a id="redactMessage"></a>
# **redactMessage**
> redactMessage(redactTransaction)

Redact a specific message



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/redact");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RedactTransaction redactTransaction = new RedactTransaction(); // RedactTransaction | 
    try {
      apiInstance.redactMessage(redactTransaction);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#redactMessage");
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
| **redactTransaction** | [**RedactTransaction**](RedactTransaction.md)|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** | Authentication failure |  -  |
| **403** | Authorisation denied |  -  |
| **404** | No such record |  -  |
| **422** | Invalid JSON body |  -  |
| **429** | Rate Limited |  -  |

