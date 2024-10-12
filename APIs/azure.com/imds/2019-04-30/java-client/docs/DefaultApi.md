# DefaultApi

All URIs are relative to *https://169.254.169.254/metadata*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attestedGetDocument**](DefaultApi.md#attestedGetDocument) | **GET** /attested/document |  |
| [**instancesGetMetadata**](DefaultApi.md#instancesGetMetadata) | **GET** /instance |  |


<a id="attestedGetDocument"></a>
# **attestedGetDocument**
> AttestedData attestedGetDocument(apiVersion, metadata, nonce)



Get Attested Data for the Virtual Machine.

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
    defaultClient.setBasePath("https://169.254.169.254/metadata");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "2018-10-01"; // String | This is the API version to use.
    String metadata = "true"; // String | This must be set to 'true'.
    String nonce = "nonce_example"; // String | This is a string of up to 32 random alphanumeric characters.
    try {
      AttestedData result = apiInstance.attestedGetDocument(apiVersion, metadata, nonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#attestedGetDocument");
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
| **apiVersion** | **String**| This is the API version to use. | [enum: 2018-10-01] |
| **metadata** | **String**| This must be set to &#39;true&#39;. | [enum: true] |
| **nonce** | **String**| This is a string of up to 32 random alphanumeric characters. | [optional] |

### Return type

[**AttestedData**](AttestedData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="instancesGetMetadata"></a>
# **instancesGetMetadata**
> Instance instancesGetMetadata(apiVersion, metadata)



Get Instance Metadata for the Virtual Machine.

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
    defaultClient.setBasePath("https://169.254.169.254/metadata");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "2018-10-01"; // String | This is the API version to use.
    String metadata = "true"; // String | This must be set to 'true'.
    try {
      Instance result = apiInstance.instancesGetMetadata(apiVersion, metadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#instancesGetMetadata");
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
| **apiVersion** | **String**| This is the API version to use. | [enum: 2018-10-01] |
| **metadata** | **String**| This must be set to &#39;true&#39;. | [enum: true] |

### Return type

[**Instance**](Instance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

