# UuidGenerationApi

All URIs are relative to *https://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uuidGet**](UuidGenerationApi.md#uuidGet) | **GET** /uuid |  |
| [**uuidVersionVersionGet**](UuidGenerationApi.md#uuidVersionVersionGet) | **GET** /uuid/version/{version} |  |


<a id="uuidGet"></a>
# **uuidGet**
> uuidGet(count)



Generate a random UUID (v4).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UuidGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    UuidGenerationApi apiInstance = new UuidGenerationApi(defaultClient);
    Integer count = 56; // Integer | Number of UUID's to generate (defaults to 1)
    try {
      apiInstance.uuidGet(count);
    } catch (ApiException e) {
      System.err.println("Exception when calling UuidGenerationApi#uuidGet");
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
| **count** | **Integer**| Number of UUID&#39;s to generate (defaults to 1) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="uuidVersionVersionGet"></a>
# **uuidVersionVersionGet**
> uuidVersionVersionGet(version, count, type, text)



Generate a random UUID (v4).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UuidGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    UuidGenerationApi apiInstance = new UuidGenerationApi(defaultClient);
    Integer version = 56; // Integer | Version of the UUID spec to use. (0-5), Use '0' for nil (00000000-0000-0000-0000-000000000000) UUID.
    Integer count = 56; // Integer | Number of UUID's to generate (defaults to 1)
    String type = "type_example"; // String | For v3 and v5 of UUID Spec you can supply the type (dns/url/oid/x500/nil).
    String text = "text_example"; // String | For v3 and v5 of UUID Spec supply the text value for the type specified dns/url/oid/x500/nil. For example specify a dns/domain string if the type is \"dns\"
    try {
      apiInstance.uuidVersionVersionGet(version, count, type, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling UuidGenerationApi#uuidVersionVersionGet");
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
| **version** | **Integer**| Version of the UUID spec to use. (0-5), Use &#39;0&#39; for nil (00000000-0000-0000-0000-000000000000) UUID. | |
| **count** | **Integer**| Number of UUID&#39;s to generate (defaults to 1) | [optional] |
| **type** | **String**| For v3 and v5 of UUID Spec you can supply the type (dns/url/oid/x500/nil). | [optional] |
| **text** | **String**| For v3 and v5 of UUID Spec supply the text value for the type specified dns/url/oid/x500/nil. For example specify a dns/domain string if the type is \&quot;dns\&quot; | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

