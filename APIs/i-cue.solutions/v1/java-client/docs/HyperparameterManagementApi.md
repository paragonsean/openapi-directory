# HyperparameterManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hyperparameterGet**](HyperparameterManagementApi.md#hyperparameterGet) | **GET** /hyperparameter | Get hyperparameters |
| [**hyperparameterPost**](HyperparameterManagementApi.md#hyperparameterPost) | **POST** /hyperparameter | Set hyperparameters |


<a id="hyperparameterGet"></a>
# **hyperparameterGet**
> HyperparameterModel hyperparameterGet(token)

Get hyperparameters

Get entity global hyperparameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HyperparameterManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HyperparameterManagementApi apiInstance = new HyperparameterManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      HyperparameterModel result = apiInstance.hyperparameterGet(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HyperparameterManagementApi#hyperparameterGet");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

[**HyperparameterModel**](HyperparameterModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="hyperparameterPost"></a>
# **hyperparameterPost**
> hyperparameterPost(token, hyperparameterModel)

Set hyperparameters

Set entity global hyperparameters. Hyperparameters can be overwritten by user and planning level (add to JSON body).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HyperparameterManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HyperparameterManagementApi apiInstance = new HyperparameterManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    HyperparameterModel hyperparameterModel = new HyperparameterModel(); // HyperparameterModel | 
    try {
      apiInstance.hyperparameterPost(token, hyperparameterModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling HyperparameterManagementApi#hyperparameterPost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **hyperparameterModel** | [**HyperparameterModel**](HyperparameterModel.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

