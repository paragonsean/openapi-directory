# ApiApi

All URIs are relative to *https://api.fire.com/business*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiApplication**](ApiApi.md#createApiApplication) | **POST** /v1/apps | Create a new API Application |


<a id="createApiApplication"></a>
# **createApiApplication**
> ApiApplication createApiApplication(newApiApplication)

Create a new API Application

Create a new API Application with specified permissions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ApiApi apiInstance = new ApiApi(defaultClient);
    NewApiApplication newApiApplication = new NewApiApplication(); // NewApiApplication | Details of the new API Application
    try {
      ApiApplication result = apiInstance.createApiApplication(newApiApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#createApiApplication");
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
| **newApiApplication** | [**NewApiApplication**](NewApiApplication.md)| Details of the new API Application | |

### Return type

[**ApiApplication**](ApiApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Application created successfully |  -  |

