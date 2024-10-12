# AlterationsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alterationsGet**](AlterationsApi.md#alterationsGet) | **GET** /alterations | Download alterations from runtime. |
| [**alterationsReplace**](AlterationsApi.md#alterationsReplace) | **PUT** /alterations | Replace alterations data. |


<a id="alterationsGet"></a>
# **alterationsGet**
> WordAlterationsDTO alterationsGet()

Download alterations from runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlterationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    AlterationsApi apiInstance = new AlterationsApi(defaultClient);
    try {
      WordAlterationsDTO result = apiInstance.alterationsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlterationsApi#alterationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WordAlterationsDTO**](WordAlterationsDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alterations data. |  -  |
| **0** | Error response. |  -  |

<a id="alterationsReplace"></a>
# **alterationsReplace**
> alterationsReplace(wordAlterations)

Replace alterations data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlterationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    AlterationsApi apiInstance = new AlterationsApi(defaultClient);
    WordAlterationsDTO wordAlterations = new WordAlterationsDTO(); // WordAlterationsDTO | New alterations data.
    try {
      apiInstance.alterationsReplace(wordAlterations);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlterationsApi#alterationsReplace");
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
| **wordAlterations** | [**WordAlterationsDTO**](WordAlterationsDTO.md)| New alterations data. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | HTTP 204 No Content. |  -  |
| **0** | Error response. |  -  |

