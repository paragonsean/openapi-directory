# AccountsApi

All URIs are relative to *https://api.up.com.au/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsGet**](AccountsApi.md#accountsGet) | **GET** /accounts | List accounts |
| [**accountsIdGet**](AccountsApi.md#accountsIdGet) | **GET** /accounts/{id} | Retrieve account |


<a id="accountsGet"></a>
# **accountsGet**
> ListAccountsResponse accountsGet(pageSize, filterAccountType, filterOwnershipType)

List accounts

Retrieve a paginated list of all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the &#x60;prev&#x60; and &#x60;next&#x60; links where present. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer pageSize = 30; // Integer | The number of records to return in each page. 
    AccountTypeEnum filterAccountType = AccountTypeEnum.fromValue("SAVER"); // AccountTypeEnum | The type of account for which to return records. This can be used to filter Savers from spending accounts. 
    OwnershipTypeEnum filterOwnershipType = OwnershipTypeEnum.fromValue("INDIVIDUAL"); // OwnershipTypeEnum | The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts. 
    try {
      ListAccountsResponse result = apiInstance.accountsGet(pageSize, filterAccountType, filterOwnershipType);
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
| **pageSize** | **Integer**| The number of records to return in each page.  | [optional] |
| **filterAccountType** | [**AccountTypeEnum**](.md)| The type of account for which to return records. This can be used to filter Savers from spending accounts.  | [optional] [enum: SAVER, TRANSACTIONAL] |
| **filterOwnershipType** | [**OwnershipTypeEnum**](.md)| The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts.  | [optional] [enum: INDIVIDUAL, JOINT] |

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="accountsIdGet"></a>
# **accountsIdGet**
> GetAccountResponse accountsIdGet(id)

Retrieve account

Retrieve a specific account by providing its unique identifier. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "92b41408-6b7b-4fca-982b-3fb1fdd77220"; // String | The unique identifier for the account. 
    try {
      GetAccountResponse result = apiInstance.accountsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsIdGet");
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
| **id** | **String**| The unique identifier for the account.  | |

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

