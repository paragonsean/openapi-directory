# BankAccountsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bankAccountsDelete**](BankAccountsApi.md#bankAccountsDelete) | **DELETE** /v1/bankAccounts/{id} | Removes an existing Bank Account. |
| [**bankAccountsGet**](BankAccountsApi.md#bankAccountsGet) | **GET** /v1/bankAccounts | Returns a list of company&#39;s Bank Account. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;acCode\&quot; fields. |
| [**bankAccountsPost**](BankAccountsApi.md#bankAccountsPost) | **POST** /v1/bankAccounts | Creates a new Bank Account. |
| [**bankAccountsProcessBatch**](BankAccountsApi.md#bankAccountsProcessBatch) | **PUT** /v1/bankAccounts/batch | Processes a batch of Bank Accounts. |
| [**bankAccountsPut**](BankAccountsApi.md#bankAccountsPut) | **PUT** /v1/bankAccounts/{id} | Updates an existing Bank Account. |
| [**v1BankAccountsIdGet**](BankAccountsApi.md#v1BankAccountsIdGet) | **GET** /v1/bankAccounts/{id} | Returns information about a single Bank Account. |


<a id="bankAccountsDelete"></a>
# **bankAccountsDelete**
> Object bankAccountsDelete(id, timestamp)

Removes an existing Bank Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    Long id = 56L; // Long | Id of Bank Account to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Bank Account to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.bankAccountsDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#bankAccountsDelete");
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
| **id** | **Long**| Id of Bank Account to remove. | |
| **timestamp** | **String**| Timestamp of Bank Account to remove. Should be encoded in Base64. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bankAccountsGet"></a>
# **bankAccountsGet**
> PageResultBankAccountQueryDto bankAccountsGet()

Returns a list of company&#39;s Bank Account. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;acCode\&quot; fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    try {
      PageResultBankAccountQueryDto result = apiInstance.bankAccountsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#bankAccountsGet");
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

[**PageResultBankAccountQueryDto**](PageResultBankAccountQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bankAccountsPost"></a>
# **bankAccountsPost**
> Object bankAccountsPost(bankAccountDto)

Creates a new Bank Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    BankAccountDto bankAccountDto = new BankAccountDto(); // BankAccountDto | Information of Bank Account to create.
    try {
      Object result = apiInstance.bankAccountsPost(bankAccountDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#bankAccountsPost");
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
| **bankAccountDto** | [**BankAccountDto**](BankAccountDto.md)| Information of Bank Account to create. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bankAccountsProcessBatch"></a>
# **bankAccountsProcessBatch**
> Object bankAccountsProcessBatch(batchItemBankAccountDto)

Processes a batch of Bank Accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    List<BatchItemBankAccountDto> batchItemBankAccountDto = Arrays.asList(); // List<BatchItemBankAccountDto> | Batch of Bank Accounts to process.
    try {
      Object result = apiInstance.bankAccountsProcessBatch(batchItemBankAccountDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#bankAccountsProcessBatch");
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
| **batchItemBankAccountDto** | [**List&lt;BatchItemBankAccountDto&gt;**](BatchItemBankAccountDto.md)| Batch of Bank Accounts to process. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bankAccountsPut"></a>
# **bankAccountsPut**
> Object bankAccountsPut(id, bankAccountDto)

Updates an existing Bank Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    Long id = 56L; // Long | Id of Bank Account to update.
    BankAccountDto bankAccountDto = new BankAccountDto(); // BankAccountDto | Information of Bank Account to update.
    try {
      Object result = apiInstance.bankAccountsPut(id, bankAccountDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#bankAccountsPut");
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
| **id** | **Long**| Id of Bank Account to update. | |
| **bankAccountDto** | [**BankAccountDto**](BankAccountDto.md)| Information of Bank Account to update. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v1BankAccountsIdGet"></a>
# **v1BankAccountsIdGet**
> BankAccountDto v1BankAccountsIdGet(id)

Returns information about a single Bank Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    Long id = 56L; // Long | Id of Bank Account to return.
    try {
      BankAccountDto result = apiInstance.v1BankAccountsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#v1BankAccountsIdGet");
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
| **id** | **Long**| Id of Bank Account to return. | |

### Return type

[**BankAccountDto**](BankAccountDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

