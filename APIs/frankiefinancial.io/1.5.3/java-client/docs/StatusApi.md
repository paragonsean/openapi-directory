# StatusApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statusCheck**](StatusApi.md#statusCheck) | **GET** /ruok | Service Status |


<a id="statusCheck"></a>
# **statusCheck**
> PuppyObject statusCheck(askingNicely)

Service Status

Simple check to see if the service is running smoothly.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");

    StatusApi apiInstance = new StatusApi(defaultClient);
    Boolean askingNicely = true; // Boolean | If set to true, the request is being made politely. 
    try {
      PuppyObject result = apiInstance.statusCheck(askingNicely);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#statusCheck");
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
| **askingNicely** | **Boolean**| If set to true, the request is being made politely.  | [optional] |

### Return type

[**PuppyObject**](PuppyObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The system is fine. No issues, and everyone gets a puppy. But only if a Customer ID is supplied, otherwise, no puppy for you. Also, try asking nicely. |  -  |
| **500** | The system is presently unavailable, or running in a severely degraded state. Check the error message for details |  -  |

