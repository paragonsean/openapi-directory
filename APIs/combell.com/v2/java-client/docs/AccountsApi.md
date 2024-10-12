# AccountsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAccount**](AccountsApi.md#createAccount) | **POST** /accounts | Create a new account |
| [**getAccount**](AccountsApi.md#getAccount) | **GET** /accounts/{accountId} | Get a specific account |
| [**getAccounts**](AccountsApi.md#getAccounts) | **GET** /accounts | Overview of accounts |


<a id="createAccount"></a>
# **createAccount**
> createAccount(createAccount)

Create a new account

The creation of an account requires some background processing. There is no instant feedback of the creation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    CreateAccount createAccount = new CreateAccount(); // CreateAccount | 
    try {
      apiInstance.createAccount(createAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#createAccount");
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
| **createAccount** | [**CreateAccount**](CreateAccount.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="getAccount"></a>
# **getAccount**
> AccountDetail getAccount(accountId, accountId2)

Get a specific account



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The id of the account.
    String accountId2 = "accountId_example"; // String | Automatically added
    try {
      AccountDetail result = apiInstance.getAccount(accountId, accountId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#getAccount");
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
| **accountId** | **Integer**| The id of the account. | |
| **accountId2** | **String**| Automatically added | |

### Return type

[**AccountDetail**](AccountDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getAccounts"></a>
# **getAccounts**
> List&lt;Account&gt; getAccounts(skip, take, assetType, identifier)

Overview of accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    AssetType assetType = AssetType.fromValue("domain"); // AssetType | Filters the list, returning only accounts containing the specified asset type.
    String identifier = "identifier_example"; // String | Return only accounts, matching the specified identifier.
    try {
      List<Account> result = apiInstance.getAccounts(skip, take, assetType, identifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#getAccounts");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |
| **assetType** | [**AssetType**](.md)| Filters the list, returning only accounts containing the specified asset type. | [optional] [enum: domain, linux_hosting, mysql, dns, mailbox, windows_hosting] |
| **identifier** | **String**| Return only accounts, matching the specified identifier. | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

