# AccountBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1BlocklistStatusGet**](AccountBlocksApi.md#apiV1BlocklistStatusGet) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts |
| [**apiV1ServerBlocklistAccountsAccountNameDelete**](AccountBlocksApi.md#apiV1ServerBlocklistAccountsAccountNameDelete) | **DELETE** /api/v1/server/blocklist/accounts/{accountName} | Unblock an account by its handle |
| [**apiV1ServerBlocklistAccountsGet**](AccountBlocksApi.md#apiV1ServerBlocklistAccountsGet) | **GET** /api/v1/server/blocklist/accounts | List account blocks |
| [**apiV1ServerBlocklistAccountsPost**](AccountBlocksApi.md#apiV1ServerBlocklistAccountsPost) | **POST** /api/v1/server/blocklist/accounts | Block an account |


<a id="apiV1BlocklistStatusGet"></a>
# **apiV1BlocklistStatusGet**
> BlockStatus apiV1BlocklistStatusGet(accounts, hosts)

Get block status of accounts/hosts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    AccountBlocksApi apiInstance = new AccountBlocksApi(defaultClient);
    List<String> accounts = Arrays.asList(); // List<String> | Check if these accounts are blocked
    List<String> hosts = Arrays.asList(); // List<String> | Check if these hosts are blocked
    try {
      BlockStatus result = apiInstance.apiV1BlocklistStatusGet(accounts, hosts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountBlocksApi#apiV1BlocklistStatusGet");
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
| **accounts** | [**List&lt;String&gt;**](String.md)| Check if these accounts are blocked | [optional] |
| **hosts** | [**List&lt;String&gt;**](String.md)| Check if these hosts are blocked | [optional] |

### Return type

[**BlockStatus**](BlockStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1ServerBlocklistAccountsAccountNameDelete"></a>
# **apiV1ServerBlocklistAccountsAccountNameDelete**
> apiV1ServerBlocklistAccountsAccountNameDelete(accountName)

Unblock an account by its handle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountBlocksApi apiInstance = new AccountBlocksApi(defaultClient);
    String accountName = "accountName_example"; // String | account to unblock, in the form `username@domain`
    try {
      apiInstance.apiV1ServerBlocklistAccountsAccountNameDelete(accountName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountBlocksApi#apiV1ServerBlocklistAccountsAccountNameDelete");
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
| **accountName** | **String**| account to unblock, in the form &#x60;username@domain&#x60; | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **404** | account or account block does not exist |  -  |

<a id="apiV1ServerBlocklistAccountsGet"></a>
# **apiV1ServerBlocklistAccountsGet**
> apiV1ServerBlocklistAccountsGet(start, count, sort)

List account blocks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountBlocksApi apiInstance = new AccountBlocksApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      apiInstance.apiV1ServerBlocklistAccountsGet(start, count, sort);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountBlocksApi#apiV1ServerBlocklistAccountsGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1ServerBlocklistAccountsPost"></a>
# **apiV1ServerBlocklistAccountsPost**
> apiV1ServerBlocklistAccountsPost(apiV1ServerBlocklistAccountsPostRequest)

Block an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountBlocksApi apiInstance = new AccountBlocksApi(defaultClient);
    ApiV1ServerBlocklistAccountsPostRequest apiV1ServerBlocklistAccountsPostRequest = new ApiV1ServerBlocklistAccountsPostRequest(); // ApiV1ServerBlocklistAccountsPostRequest | 
    try {
      apiInstance.apiV1ServerBlocklistAccountsPost(apiV1ServerBlocklistAccountsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountBlocksApi#apiV1ServerBlocklistAccountsPost");
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
| **apiV1ServerBlocklistAccountsPostRequest** | [**ApiV1ServerBlocklistAccountsPostRequest**](ApiV1ServerBlocklistAccountsPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **409** | self-blocking forbidden |  -  |

