# FetchAccountInfoApi

All URIs are relative to *https://api.remove.bg/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountGet**](FetchAccountInfoApi.md#accountGet) | **GET** /account | Fetch credit balance and free API calls. |


<a id="accountGet"></a>
# **accountGet**
> AccountGet200Response accountGet()

Fetch credit balance and free API calls.

Get the current credit balance and number of free API calls.  Notes:  * Balance changes may be delayed by several seconds. To locally keep track of your credit balance, you should therefore only call this endpoint initially (or e.g. when the user manually triggers a refresh), then use the &#x60;X-Credits-Charged&#x60; response header returned with each image processing response to adjust the local balance.  * The \&quot;*sizes*\&quot; field is always \&quot;all\&quot;, is deprecated and will soon be removed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FetchAccountInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.remove.bg/v1.0");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    FetchAccountInfoApi apiInstance = new FetchAccountInfoApi(defaultClient);
    try {
      AccountGet200Response result = apiInstance.accountGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FetchAccountInfoApi#accountGet");
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

[**AccountGet200Response**](AccountGet200Response.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | Error: Authentication failed |  -  |
| **429** | Error: Rate limit exceeded |  -  |

