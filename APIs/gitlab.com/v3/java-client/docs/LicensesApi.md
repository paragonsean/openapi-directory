# LicensesApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getV3Licenses**](LicensesApi.md#getV3Licenses) | **GET** /v3/licenses | Get the list of the available license template |
| [**getV3LicensesName**](LicensesApi.md#getV3LicensesName) | **GET** /v3/licenses/{name} | Get the text for a specific license |


<a id="getV3Licenses"></a>
# **getV3Licenses**
> RepoLicense getV3Licenses(popular)

Get the list of the available license template

This feature was introduced in GitLab 8.7. This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    Boolean popular = true; // Boolean | If passed, returns only popular licenses
    try {
      RepoLicense result = apiInstance.getV3Licenses(popular);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getV3Licenses");
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
| **popular** | **Boolean**| If passed, returns only popular licenses | [optional] |

### Return type

[**RepoLicense**](RepoLicense.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the list of the available license template |  -  |

<a id="getV3LicensesName"></a>
# **getV3LicensesName**
> RepoLicense getV3LicensesName(name)

Get the text for a specific license

This feature was introduced in GitLab 8.7. This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String name = "name_example"; // String | The name of the template
    try {
      RepoLicense result = apiInstance.getV3LicensesName(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getV3LicensesName");
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
| **name** | **String**| The name of the template | |

### Return type

[**RepoLicense**](RepoLicense.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the text for a specific license |  -  |

