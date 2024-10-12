# DefaultApi

All URIs are relative to *https://api.openfigi.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mappingPost**](DefaultApi.md#mappingPost) | **POST** /mapping |  |
| [**mappingValuesKeyGet**](DefaultApi.md#mappingValuesKeyGet) | **GET** /mapping/values/{key} |  |


<a id="mappingPost"></a>
# **mappingPost**
> List&lt;MappingJobResult&gt; mappingPost(mappingJob)



Allows mapping from third-party identifiers to FIGIs.

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
    defaultClient.setBasePath("https://api.openfigi.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<MappingJob> mappingJob = Arrays.asList(); // List<MappingJob> | A list of third-party identifiers and extra filters.
    try {
      List<MappingJobResult> result = apiInstance.mappingPost(mappingJob);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mappingPost");
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
| **mappingJob** | [**List&lt;MappingJob&gt;**](MappingJob.md)| A list of third-party identifiers and extra filters. | [optional] |

### Return type

[**List&lt;MappingJobResult&gt;**](MappingJobResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of FIGIs and their metadata. |  -  |
| **400** | Invalid request (body). |  -  |
| **401** | API Key is invalid. |  -  |
| **406** | Unsupported &#39;Accept&#39; type. |  -  |
| **413** | Too many mapping jobs in request. |  -  |
| **500** | Internal server error. |  -  |

<a id="mappingValuesKeyGet"></a>
# **mappingValuesKeyGet**
> MappingValuesKeyGet200Response mappingValuesKeyGet(key)



Get values for enum-like fields.

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
    defaultClient.setBasePath("https://api.openfigi.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "idType"; // String | Key of MappingJob for which to get possible values.
    try {
      MappingValuesKeyGet200Response result = apiInstance.mappingValuesKeyGet(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mappingValuesKeyGet");
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
| **key** | **String**| Key of MappingJob for which to get possible values. | [enum: idType, exchCode, micCode, currency, marketSecDes, securityType, securityType2] |

### Return type

[**MappingValuesKeyGet200Response**](MappingValuesKeyGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values. |  -  |
| **400** | Invalid request (key). |  -  |
| **500** | Internal server error. |  -  |

