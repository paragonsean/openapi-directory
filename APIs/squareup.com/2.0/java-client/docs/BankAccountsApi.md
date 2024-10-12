# BankAccountsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBankAccount**](BankAccountsApi.md#getBankAccount) | **GET** /v2/bank-accounts/{bank_account_id} | GetBankAccount |
| [**getBankAccountByV1Id**](BankAccountsApi.md#getBankAccountByV1Id) | **GET** /v2/bank-accounts/by-v1-id/{v1_bank_account_id} | GetBankAccountByV1Id |
| [**listBankAccounts**](BankAccountsApi.md#listBankAccounts) | **GET** /v2/bank-accounts | ListBankAccounts |


<a id="getBankAccount"></a>
# **getBankAccount**
> GetBankAccountResponse getBankAccount(bankAccountId)

GetBankAccount

Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) linked to a Square account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String bankAccountId = "bankAccountId_example"; // String | Square-issued ID of the desired `BankAccount`.
    try {
      GetBankAccountResponse result = apiInstance.getBankAccount(bankAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#getBankAccount");
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
| **bankAccountId** | **String**| Square-issued ID of the desired &#x60;BankAccount&#x60;. | |

### Return type

[**GetBankAccountResponse**](GetBankAccountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getBankAccountByV1Id"></a>
# **getBankAccountByV1Id**
> GetBankAccountByV1IdResponse getBankAccountByV1Id(v1BankAccountId)

GetBankAccountByV1Id

Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String v1BankAccountId = "v1BankAccountId_example"; // String | Connect V1 ID of the desired `BankAccount`. For more information, see  [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).
    try {
      GetBankAccountByV1IdResponse result = apiInstance.getBankAccountByV1Id(v1BankAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#getBankAccountByV1Id");
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
| **v1BankAccountId** | **String**| Connect V1 ID of the desired &#x60;BankAccount&#x60;. For more information, see  [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api). | |

### Return type

[**GetBankAccountByV1IdResponse**](GetBankAccountByV1IdResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listBankAccounts"></a>
# **listBankAccounts**
> ListBankAccountsResponse listBankAccounts(cursor, limit, locationId)

ListBankAccounts

Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String cursor = "cursor_example"; // String | The pagination cursor returned by a previous call to this endpoint. Use it in the next `ListBankAccounts` request to retrieve the next set  of results.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    Integer limit = 56; // Integer | Upper limit on the number of bank accounts to return in the response.  Currently, 1000 is the largest supported limit. You can specify a limit  of up to 1000 bank accounts. This is also the default limit.
    String locationId = "locationId_example"; // String | Location ID. You can specify this optional filter  to retrieve only the linked bank accounts belonging to a specific location.
    try {
      ListBankAccountsResponse result = apiInstance.listBankAccounts(cursor, limit, locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#listBankAccounts");
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
| **cursor** | **String**| The pagination cursor returned by a previous call to this endpoint. Use it in the next &#x60;ListBankAccounts&#x60; request to retrieve the next set  of results.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. | [optional] |
| **limit** | **Integer**| Upper limit on the number of bank accounts to return in the response.  Currently, 1000 is the largest supported limit. You can specify a limit  of up to 1000 bank accounts. This is also the default limit. | [optional] |
| **locationId** | **String**| Location ID. You can specify this optional filter  to retrieve only the linked bank accounts belonging to a specific location. | [optional] |

### Return type

[**ListBankAccountsResponse**](ListBankAccountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

