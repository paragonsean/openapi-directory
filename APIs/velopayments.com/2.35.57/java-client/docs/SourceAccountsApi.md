# SourceAccountsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSourceAccountV2**](SourceAccountsApi.md#getSourceAccountV2) | **GET** /v2/sourceAccounts/{sourceAccountId} | Get Source Account |
| [**getSourceAccountV3**](SourceAccountsApi.md#getSourceAccountV3) | **GET** /v3/sourceAccounts/{sourceAccountId} | Get details about given source account. |
| [**getSourceAccountsV2**](SourceAccountsApi.md#getSourceAccountsV2) | **GET** /v2/sourceAccounts | Get list of source accounts |
| [**getSourceAccountsV3**](SourceAccountsApi.md#getSourceAccountsV3) | **GET** /v3/sourceAccounts | Get list of source accounts |
| [**setNotificationsRequest**](SourceAccountsApi.md#setNotificationsRequest) | **POST** /v1/sourceAccounts/{sourceAccountId}/notifications | Set notifications |
| [**setNotificationsRequestV3**](SourceAccountsApi.md#setNotificationsRequestV3) | **POST** /v3/sourceAccounts/{sourceAccountId}/notifications | Set notifications |
| [**transferFundsV2**](SourceAccountsApi.md#transferFundsV2) | **POST** /v2/sourceAccounts/{sourceAccountId}/transfers | Transfer Funds between source accounts |
| [**transferFundsV3**](SourceAccountsApi.md#transferFundsV3) | **POST** /v3/sourceAccounts/{sourceAccountId}/transfers | Transfer Funds between source accounts |


<a id="getSourceAccountV2"></a>
# **getSourceAccountV2**
> SourceAccountResponseV2 getSourceAccountV2(sourceAccountId)

Get Source Account

Get details about given source account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    try {
      SourceAccountResponseV2 result = apiInstance.getSourceAccountV2(sourceAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#getSourceAccountV2");
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

[**SourceAccountResponseV2**](SourceAccountResponseV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Source account response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getSourceAccountV3"></a>
# **getSourceAccountV3**
> SourceAccountResponseV3 getSourceAccountV3(sourceAccountId)

Get details about given source account.

Get details about given source account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    try {
      SourceAccountResponseV3 result = apiInstance.getSourceAccountV3(sourceAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#getSourceAccountV3");
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

[**SourceAccountResponseV3**](SourceAccountResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Source account response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getSourceAccountsV2"></a>
# **getSourceAccountsV2**
> ListSourceAccountResponseV2 getSourceAccountsV2(physicalAccountName, physicalAccountId, payorId, fundingAccountId, page, pageSize, sort)

Get list of source accounts

List source accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    String physicalAccountName = "physicalAccountName_example"; // String | Physical Account Name
    UUID physicalAccountId = UUID.randomUUID(); // UUID | The physical account ID
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    UUID fundingAccountId = UUID.randomUUID(); // UUID | The funding account ID
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "fundingRef:asc"; // String | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance 
    try {
      ListSourceAccountResponseV2 result = apiInstance.getSourceAccountsV2(physicalAccountName, physicalAccountId, payorId, fundingAccountId, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#getSourceAccountsV2");
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
| **physicalAccountName** | **String**| Physical Account Name | [optional] |
| **physicalAccountId** | **UUID**| The physical account ID | [optional] |
| **payorId** | **UUID**| The account owner Payor ID | [optional] |
| **fundingAccountId** | **UUID**| The funding account ID | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  | [optional] [default to fundingRef:asc] |

### Return type

[**ListSourceAccountResponseV2**](ListSourceAccountResponseV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List Source Account response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getSourceAccountsV3"></a>
# **getSourceAccountsV3**
> ListSourceAccountResponseV3 getSourceAccountsV3(physicalAccountName, physicalAccountId, payorId, fundingAccountId, includeUserDeleted, type, page, pageSize, sort)

Get list of source accounts

List source accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    String physicalAccountName = "physicalAccountName_example"; // String | Physical Account Name
    UUID physicalAccountId = UUID.randomUUID(); // UUID | The physical account ID
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    UUID fundingAccountId = UUID.randomUUID(); // UUID | The funding account ID
    Boolean includeUserDeleted = true; // Boolean | A filter for retrieving both active accounts and user deleted ones
    String type = "type_example"; // String | The type of source account.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "fundingRef:asc"; // String | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance 
    try {
      ListSourceAccountResponseV3 result = apiInstance.getSourceAccountsV3(physicalAccountName, physicalAccountId, payorId, fundingAccountId, includeUserDeleted, type, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#getSourceAccountsV3");
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
| **physicalAccountName** | **String**| Physical Account Name | [optional] |
| **physicalAccountId** | **UUID**| The physical account ID | [optional] |
| **payorId** | **UUID**| The account owner Payor ID | [optional] |
| **fundingAccountId** | **UUID**| The funding account ID | [optional] |
| **includeUserDeleted** | **Boolean**| A filter for retrieving both active accounts and user deleted ones | [optional] |
| **type** | **String**| The type of source account. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  | [optional] [default to fundingRef:asc] |

### Return type

[**ListSourceAccountResponseV3**](ListSourceAccountResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List Source Account response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="setNotificationsRequest"></a>
# **setNotificationsRequest**
> setNotificationsRequest(sourceAccountId, setNotificationsRequest)

Set notifications

&lt;p&gt;Set notifications for a given source account&lt;/p&gt; &lt;p&gt;deprecated since 2.34 (use v3 version)&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    SetNotificationsRequest setNotificationsRequest = new SetNotificationsRequest(); // SetNotificationsRequest | Body to included minimum balance to set
    try {
      apiInstance.setNotificationsRequest(sourceAccountId, setNotificationsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#setNotificationsRequest");
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
| **setNotificationsRequest** | [**SetNotificationsRequest**](SetNotificationsRequest.md)| Body to included minimum balance to set | |

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
| **204** | Request Fulfilled |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="setNotificationsRequestV3"></a>
# **setNotificationsRequestV3**
> setNotificationsRequestV3(sourceAccountId, setNotificationsRequest2)

Set notifications

&lt;p&gt;Set notifications for a given source account&lt;/p&gt; &lt;p&gt;If the balance falls below the amount set in the request an email notification will be sent to the email address registered in the payor profile&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | Source account id
    SetNotificationsRequest2 setNotificationsRequest2 = new SetNotificationsRequest2(); // SetNotificationsRequest2 | Body to included minimum balance to set
    try {
      apiInstance.setNotificationsRequestV3(sourceAccountId, setNotificationsRequest2);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#setNotificationsRequestV3");
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
| **setNotificationsRequest2** | [**SetNotificationsRequest2**](SetNotificationsRequest2.md)| Body to included minimum balance to set | |

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
| **204** | Request Fulfilled |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="transferFundsV2"></a>
# **transferFundsV2**
> transferFundsV2(sourceAccountId, transferRequestV2)

Transfer Funds between source accounts

Transfer funds between source accounts for a Payor. The &#39;from&#39; source account is identified in the URL, and is the account which will be debited. The &#39;to&#39; (destination) source account is in the body, and is the account which will be credited. Both source accounts must belong to the same Payor. There must be sufficient balance in the &#39;from&#39; source account, otherwise the transfer attempt will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | The 'from' source account id, which will be debited
    TransferRequestV2 transferRequestV2 = new TransferRequestV2(); // TransferRequestV2 | Body
    try {
      apiInstance.transferFundsV2(sourceAccountId, transferRequestV2);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#transferFundsV2");
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
| **sourceAccountId** | **UUID**| The &#39;from&#39; source account id, which will be debited | |
| **transferRequestV2** | [**TransferRequestV2**](TransferRequestV2.md)| Body | |

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
| **204** | Request Processed |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="transferFundsV3"></a>
# **transferFundsV3**
> transferFundsV3(sourceAccountId, transferRequestV3)

Transfer Funds between source accounts

Transfer funds between source accounts for a Payor. The &#39;from&#39; source account is identified in the URL, and is the account which will be debited. The &#39;to&#39; (destination) source account is in the body, and is the account which will be credited. Both source accounts must belong to the same Payor. There must be sufficient balance in the &#39;from&#39; source account, otherwise the transfer attempt will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SourceAccountsApi apiInstance = new SourceAccountsApi(defaultClient);
    UUID sourceAccountId = UUID.randomUUID(); // UUID | The 'from' source account id, which will be debited
    TransferRequestV3 transferRequestV3 = new TransferRequestV3(); // TransferRequestV3 | Body
    try {
      apiInstance.transferFundsV3(sourceAccountId, transferRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceAccountsApi#transferFundsV3");
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
| **sourceAccountId** | **UUID**| The &#39;from&#39; source account id, which will be debited | |
| **transferRequestV3** | [**TransferRequestV3**](TransferRequestV3.md)| Body | |

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
| **204** | Request Processed |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

