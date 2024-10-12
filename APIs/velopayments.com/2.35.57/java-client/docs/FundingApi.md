# FundingApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFundingRequestV2**](FundingApi.md#createFundingRequestV2) | **POST** /v2/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request |
| [**createFundingRequestV3**](FundingApi.md#createFundingRequestV3) | **POST** /v3/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request |
| [**getFundingAccountV2**](FundingApi.md#getFundingAccountV2) | **GET** /v2/fundingAccounts/{fundingAccountId} | Get Funding Account |
| [**getFundingAccountsV2**](FundingApi.md#getFundingAccountsV2) | **GET** /v2/fundingAccounts | Get Funding Accounts |
| [**getFundingByIdV1**](FundingApi.md#getFundingByIdV1) | **GET** /v1/fundings/{fundingId} | Get Funding |
| [**listFundingAuditDeltas**](FundingApi.md#listFundingAuditDeltas) | **GET** /v1/deltas/fundings | Get Funding Audit Delta |


<a id="createFundingRequestV2"></a>
# **createFundingRequestV2**
> createFundingRequestV2(sourceAccountId, fundingRequestV2)

Create Funding Request

Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo  (202 - accepted, 400 - invalid request body, 404 - source account not found).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingApi apiInstance = new FundingApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    FundingRequestV2 fundingRequestV2 = new FundingRequestV2(); // FundingRequestV2 | Body to included amount to be funded
    try {
      apiInstance.createFundingRequestV2(sourceAccountId, fundingRequestV2);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#createFundingRequestV2");
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
| **fundingRequestV2** | [**FundingRequestV2**](FundingRequestV2.md)| Body to included amount to be funded | |

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
| **202** | Request Accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="createFundingRequestV3"></a>
# **createFundingRequestV3**
> createFundingRequestV3(sourceAccountId, fundingRequestV3)

Create Funding Request

&lt;p&gt;Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingApi apiInstance = new FundingApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    FundingRequestV3 fundingRequestV3 = new FundingRequestV3(); // FundingRequestV3 | Body to included amount to be funded
    try {
      apiInstance.createFundingRequestV3(sourceAccountId, fundingRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#createFundingRequestV3");
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
| **fundingRequestV3** | [**FundingRequestV3**](FundingRequestV3.md)| Body to included amount to be funded | |

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
| **202** | Request Accepted |  * Location - Reference to created Funding Request <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getFundingAccountV2"></a>
# **getFundingAccountV2**
> FundingAccountResponseV2 getFundingAccountV2(fundingAccountId, sensitive)

Get Funding Account

Get Funding Account by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingApi apiInstance = new FundingApi(defaultClient);
    UUID fundingAccountId = UUID.randomUUID(); // UUID | 
    Boolean sensitive = false; // Boolean | 
    try {
      FundingAccountResponseV2 result = apiInstance.getFundingAccountV2(fundingAccountId, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#getFundingAccountV2");
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
| **fundingAccountId** | **UUID**|  | |
| **sensitive** | **Boolean**|  | [optional] [default to false] |

### Return type

[**FundingAccountResponseV2**](FundingAccountResponseV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Funding Account Response |  -  |
| **400** | Bad Request |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getFundingAccountsV2"></a>
# **getFundingAccountsV2**
> ListFundingAccountsResponseV2 getFundingAccountsV2(payorId, name, country, currency, type, page, pageSize, sort, sensitive)

Get Funding Accounts

Get the funding accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingApi apiInstance = new FundingApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | 
    String name = "name_example"; // String | The descriptive funding account name
    String country = "US"; // String | The 2 letter ISO 3166-1 country code (upper case)
    String currency = "USD"; // String | The ISO 4217 currency code
    String type = "type_example"; // String | The type of funding account.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "accountName:asc"; // String | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name.
    Boolean sensitive = false; // Boolean | 
    try {
      ListFundingAccountsResponseV2 result = apiInstance.getFundingAccountsV2(payorId, name, country, currency, type, page, pageSize, sort, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#getFundingAccountsV2");
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
| **payorId** | **UUID**|  | [optional] |
| **name** | **String**| The descriptive funding account name | [optional] |
| **country** | **String**| The 2 letter ISO 3166-1 country code (upper case) | [optional] |
| **currency** | **String**| The ISO 4217 currency code | [optional] |
| **type** | **String**| The type of funding account. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. | [optional] [default to accountName:asc] |
| **sensitive** | **Boolean**|  | [optional] [default to false] |

### Return type

[**ListFundingAccountsResponseV2**](ListFundingAccountsResponseV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Funding Accounts Response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="getFundingByIdV1"></a>
# **getFundingByIdV1**
> FundingResponse getFundingByIdV1(fundingId)

Get Funding

Get Funding by Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingApi apiInstance = new FundingApi(defaultClient);
    UUID fundingId = UUID.randomUUID(); // UUID | 
    try {
      FundingResponse result = apiInstance.getFundingByIdV1(fundingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#getFundingByIdV1");
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
| **fundingId** | **UUID**|  | |

### Return type

[**FundingResponse**](FundingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Funding response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="listFundingAuditDeltas"></a>
# **listFundingAuditDeltas**
> PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse listFundingAuditDeltas(payorId, updatedSince, page, pageSize)

Get Funding Audit Delta

Get funding audit deltas for a payor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FundingApi apiInstance = new FundingApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | 
    OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | 
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    try {
      PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse result = apiInstance.listFundingAuditDeltas(payorId, updatedSince, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#listFundingAuditDeltas");
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
| **payorId** | **UUID**|  | |
| **updatedSince** | **OffsetDateTime**|  | |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |

### Return type

[**PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse**](PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Funding Account Deltas |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

