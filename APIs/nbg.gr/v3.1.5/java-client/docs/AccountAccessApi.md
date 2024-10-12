# AccountAccessApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountAccessConsentsConsentIdDelete**](AccountAccessApi.md#accountAccessConsentsConsentIdDelete) | **DELETE** /account-access-consents/{consentId} | Delete Account Access Consents |
| [**accountAccessConsentsConsentIdGet**](AccountAccessApi.md#accountAccessConsentsConsentIdGet) | **GET** /account-access-consents/{consentId} | Get Account Access Consents |
| [**accountAccessConsentsPost**](AccountAccessApi.md#accountAccessConsentsPost) | **POST** /account-access-consents | Create Account Access Consents |


<a id="accountAccessConsentsConsentIdDelete"></a>
# **accountAccessConsentsConsentIdDelete**
> accountAccessConsentsConsentIdDelete(consentId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Delete Account Access Consents

Delete Account Access Consents by Consent ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Client-Credentials-Token
    OAuth Client-Credentials-Token = (OAuth) defaultClient.getAuthentication("Client-Credentials-Token");
    Client-Credentials-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    AccountAccessApi apiInstance = new AccountAccessApi(defaultClient);
    String consentId = "consentId_example"; // String | ConsentId
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      apiInstance.accountAccessConsentsConsentIdDelete(consentId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountAccessApi#accountAccessConsentsConsentIdDelete");
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
| **consentId** | **String**| ConsentId | |
| **sandboxId** | **String**| The unique id of the sandbox to be used | |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

null (empty response body)

### Authorization

[Client-Credentials-Token](../README.md#Client-Credentials-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Account Access Consents Deleted |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="accountAccessConsentsConsentIdGet"></a>
# **accountAccessConsentsConsentIdGet**
> OBReadConsentResponse1 accountAccessConsentsConsentIdGet(consentId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent)

Get Account Access Consents

Get Account Access Consents by Consent ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Client-Credentials-Token
    OAuth Client-Credentials-Token = (OAuth) defaultClient.getAuthentication("Client-Credentials-Token");
    Client-Credentials-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    AccountAccessApi apiInstance = new AccountAccessApi(defaultClient);
    String consentId = "consentId_example"; // String | ConsentId
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    try {
      OBReadConsentResponse1 result = apiInstance.accountAccessConsentsConsentIdGet(consentId, sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountAccessApi#accountAccessConsentsConsentIdGet");
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
| **consentId** | **String**| ConsentId | |
| **sandboxId** | **String**| The unique id of the sandbox to be used | |
| **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] |
| **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] |
| **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] |
| **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] |

### Return type

[**OBReadConsentResponse1**](OBReadConsentResponse1.md)

### Authorization

[Client-Credentials-Token](../README.md#Client-Credentials-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Access Consents Read |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="accountAccessConsentsPost"></a>
# **accountAccessConsentsPost**
> OBReadConsentResponse1 accountAccessConsentsPost(sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent, obReadConsent1)

Create Account Access Consents

Create Account Access Consents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Client-Credentials-Token
    OAuth Client-Credentials-Token = (OAuth) defaultClient.getAuthentication("Client-Credentials-Token");
    Client-Credentials-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    AccountAccessApi apiInstance = new AccountAccessApi(defaultClient);
    String sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
    String xFapiAuthDate = "xFapiAuthDate_example"; // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    String xFapiCustomerIpAddress = "xFapiCustomerIpAddress_example"; // String | The PSU's IP address if the PSU is currently logged in with the TPP.
    String xFapiInteractionId = "xFapiInteractionId_example"; // String | An RFC4122 UID used as a correlation id.
    String xCustomerUserAgent = "xCustomerUserAgent_example"; // String | Indicates the user-agent that the PSU is using.
    OBReadConsent1 obReadConsent1 = new OBReadConsent1(); // OBReadConsent1 | Default
    try {
      OBReadConsentResponse1 result = apiInstance.accountAccessConsentsPost(sandboxId, xFapiAuthDate, xFapiCustomerIpAddress, xFapiInteractionId, xCustomerUserAgent, obReadConsent1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountAccessApi#accountAccessConsentsPost");
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
| **obReadConsent1** | [**OBReadConsent1**](OBReadConsent1.md)| Default | [optional] |

### Return type

[**OBReadConsentResponse1**](OBReadConsentResponse1.md)

### Authorization

[Client-Credentials-Token](../README.md#Client-Credentials-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: application/json, application/json; charset=utf-8
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Account Access Consents Created |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **415** | Unsupported Media Type |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

