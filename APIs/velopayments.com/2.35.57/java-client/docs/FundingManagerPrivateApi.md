# FundingManagerPrivateApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFundingAccountV2**](FundingManagerPrivateApi.md#createFundingAccountV2) | **POST** /v2/fundingAccounts | Create Funding Account |
| [**deleteSourceAccountV3**](FundingManagerPrivateApi.md#deleteSourceAccountV3) | **DELETE** /v3/sourceAccounts/{sourceAccountId} | Delete a source account by ID |


<a id="createFundingAccountV2"></a>
# **createFundingAccountV2**
> createFundingAccountV2(createFundingAccountRequestV2)

Create Funding Account

Create Funding Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingManagerPrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingManagerPrivateApi apiInstance = new FundingManagerPrivateApi(defaultClient);
    CreateFundingAccountRequestV2 createFundingAccountRequestV2 = new CreateFundingAccountRequestV2(); // CreateFundingAccountRequestV2 | 
    try {
      apiInstance.createFundingAccountV2(createFundingAccountRequestV2);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingManagerPrivateApi#createFundingAccountV2");
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
| **createFundingAccountRequestV2** | [**CreateFundingAccountRequestV2**](CreateFundingAccountRequestV2.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Funding Account Creation Request Accepted |  * Location - Reference to created payout <br>  * Retry-After - How long the user agent should wait before making a follow-up request (seconds) <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="deleteSourceAccountV3"></a>
# **deleteSourceAccountV3**
> deleteSourceAccountV3(sourceAccountId)

Delete a source account by ID

Mark a source account as deleted by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingManagerPrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingManagerPrivateApi apiInstance = new FundingManagerPrivateApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    try {
      apiInstance.deleteSourceAccountV3(sourceAccountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingManagerPrivateApi#deleteSourceAccountV3");
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
| **sourceAccountId** | **UUID**| Source account id | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - Source account is deleted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

