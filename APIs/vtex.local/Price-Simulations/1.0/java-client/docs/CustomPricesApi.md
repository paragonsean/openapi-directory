# CustomPricesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vCustomPricesSessionSchemaGet**](CustomPricesApi.md#vCustomPricesSessionSchemaGet) | **GET** /_v/custom-prices/session/schema | Get custom prices schema |
| [**vCustomPricesSessionSchemaPost**](CustomPricesApi.md#vCustomPricesSessionSchemaPost) | **POST** /_v/custom-prices/session/schema | Create or Update custom prices schema |


<a id="vCustomPricesSessionSchemaGet"></a>
# **vCustomPricesSessionSchemaGet**
> RequestBody1 vCustomPricesSessionSchemaGet(contentType, accept)

Get custom prices schema

Retrieves all custom price for all shopping scenarios

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CustomPricesApi apiInstance = new CustomPricesApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    try {
      RequestBody1 result = apiInstance.vCustomPricesSessionSchemaGet(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPricesApi#vCustomPricesSessionSchemaGet");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |

### Return type

[**RequestBody1**](RequestBody1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vCustomPricesSessionSchemaPost"></a>
# **vCustomPricesSessionSchemaPost**
> RequestBody1 vCustomPricesSessionSchemaPost(contentType, accept, requestBody1)

Create or Update custom prices schema

Creates a new custom price for a shopping scenario or updates an existing one

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CustomPricesApi apiInstance = new CustomPricesApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    RequestBody1 requestBody1 = new RequestBody1(); // RequestBody1 | 
    try {
      RequestBody1 result = apiInstance.vCustomPricesSessionSchemaPost(contentType, accept, requestBody1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPricesApi#vCustomPricesSessionSchemaPost");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |
| **requestBody1** | [**RequestBody1**](RequestBody1.md)|  | [optional] |

### Return type

[**RequestBody1**](RequestBody1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

