# StatementsApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountIdStatementsGet**](StatementsApi.md#accountsAccountIdStatementsGet) | **GET** /accounts/{accountId}/statements | Get Statements |
| [**accountsAccountIdStatementsStatementIdFileGet**](StatementsApi.md#accountsAccountIdStatementsStatementIdFileGet) | **GET** /accounts/{accountId}/statements/{statementId}/file | Get Statements |
| [**accountsAccountIdStatementsStatementIdGet**](StatementsApi.md#accountsAccountIdStatementsStatementIdGet) | **GET** /accounts/{accountId}/statements/{statementId} | Get Statements |


<a id="accountsAccountIdStatementsGet"></a>
# **accountsAccountIdStatementsGet**
> OBReadStatement2 accountsAccountIdStatementsGet(accountId, sandboxId, fromStatementDateTime, toStatementDateTime, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Get Statements

Get Statements by Account ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatementsApi;

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

    StatementsApi apiInstance = new StatementsApi(defaultClient);
    String accountId = "accountId_example"; // String | AccountId
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    OffsetDateTime fromStatementDateTime = OffsetDateTime.now(); // OffsetDateTime | The UTC ISO 8601 Date Time to filter statements FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    OffsetDateTime toStatementDateTime = OffsetDateTime.now(); // OffsetDateTime | The UTC ISO 8601 Date Time to filter statements TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      OBReadStatement2 result = apiInstance.accountsAccountIdStatementsGet(accountId, sandboxId, fromStatementDateTime, toStatementDateTime, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatementsApi#accountsAccountIdStatementsGet");
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
| **fromStatementDateTime** | **OffsetDateTime**| The UTC ISO 8601 Date Time to filter statements FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component. | [optional] |
| **toStatementDateTime** | **OffsetDateTime**| The UTC ISO 8601 Date Time to filter statements TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component. | [optional] |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

[**OBReadStatement2**](OBReadStatement2.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Statements Read |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="accountsAccountIdStatementsStatementIdFileGet"></a>
# **accountsAccountIdStatementsStatementIdFileGet**
> File accountsAccountIdStatementsStatementIdFileGet(accountId, statementId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Get Statements

Get Statement PDF File by Account ID and Statement ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatementsApi;

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

    StatementsApi apiInstance = new StatementsApi(defaultClient);
    String accountId = "accountId_example"; // String | AccountId
    String statementId = "statementId_example"; // String | StatementId
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      File result = apiInstance.accountsAccountIdStatementsStatementIdFileGet(accountId, statementId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatementsApi#accountsAccountIdStatementsStatementIdFileGet");
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
| **statementId** | **String**| StatementId | |
| **sandboxId** | **String**| The unique id of the sandbox to be used | |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Statements Read |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="accountsAccountIdStatementsStatementIdGet"></a>
# **accountsAccountIdStatementsStatementIdGet**
> OBReadStatement2 accountsAccountIdStatementsStatementIdGet(accountId, statementId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Get Statements

Get Statements by Account ID and Statement ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatementsApi;

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

    StatementsApi apiInstance = new StatementsApi(defaultClient);
    String accountId = "accountId_example"; // String | AccountId
    String statementId = "statementId_example"; // String | StatementId
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      OBReadStatement2 result = apiInstance.accountsAccountIdStatementsStatementIdGet(accountId, statementId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatementsApi#accountsAccountIdStatementsStatementIdGet");
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
| **statementId** | **String**| StatementId | |
| **sandboxId** | **String**| The unique id of the sandbox to be used | |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

[**OBReadStatement2**](OBReadStatement2.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Statements Read |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

