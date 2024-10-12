# InputsApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllInputs**](InputsApi.md#getAllInputs) | **GET** /inputs | Get all inputs you have access to |


<a id="getAllInputs"></a>
# **getAllInputs**
> GetAllInputsResponse getAllInputs(name)

Get all inputs you have access to



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InputsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    InputsApi apiInstance = new InputsApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      GetAllInputsResponse result = apiInstance.getAllInputs(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InputsApi#getAllInputs");
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
| **name** | **String**|  | [optional] |

### Return type

[**GetAllInputsResponse**](GetAllInputsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid input |  -  |
| **403** | Bad credentials |  -  |

