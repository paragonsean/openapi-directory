# AccountsApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountIdGet**](AccountsApi.md#accountsAccountIdGet) | **GET** /accounts/{accountId} | Get Accounts |
| [**accountsGet**](AccountsApi.md#accountsGet) | **GET** /accounts | Get Accounts |


<a id="accountsAccountIdGet"></a>
# **accountsAccountIdGet**
> OBReadAccount5 accountsAccountIdGet(accountId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Get Accounts

Get Accounts by Account ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Authorization-Code-Token
    OAuth Authorization-Code-Token = (OAuth) defaultClient.getAuthentication("Authorization-Code-Token");
    Authorization-Code-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | AccountId
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      OBReadAccount5 result = apiInstance.accountsAccountIdGet(accountId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsAccountIdGet");
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
| **accountId** | **String**| AccountId | |
| **sandboxId** | **String**| The unique id of the sandbox to be used | |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

[**OBReadAccount5**](OBReadAccount5.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounts Read |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="accountsGet"></a>
# **accountsGet**
> OBReadAccount5 accountsGet(sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Get Accounts

Get Accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Authorization-Code-Token
    OAuth Authorization-Code-Token = (OAuth) defaultClient.getAuthentication("Authorization-Code-Token");
    Authorization-Code-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      OBReadAccount5 result = apiInstance.accountsGet(sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGet");
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
| **sandboxId** | **String**| The unique id of the sandbox to be used | |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

[**OBReadAccount5**](OBReadAccount5.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounts Read |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

