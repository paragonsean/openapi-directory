# TransactionsApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTransaction**](TransactionsApi.md#getTransaction) | **GET** /v1/transactions/{id} |  |
| [**getTransactionCost**](TransactionsApi.md#getTransactionCost) | **GET** /v1/transactions/{id}/cost |  |
| [**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /v1/transactions |  |


<a id="getTransaction"></a>
# **getTransaction**
> getTransaction(id, includeChargestation, includeEvse, includeConnector, includeDriver, includeToken, includeReservation, includeOrganization, includeRate)



Get a specific transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The transaction id that needs to be fetched
    Boolean includeChargestation = true; // Boolean | Populate chargestation
    Boolean includeEvse = true; // Boolean | Populate evse
    Boolean includeConnector = true; // Boolean | Populate connector
    Boolean includeDriver = true; // Boolean | Populate driver
    Boolean includeToken = true; // Boolean | Populate token
    Boolean includeReservation = true; // Boolean | Populate reservation
    Boolean includeOrganization = true; // Boolean | Populate organization
    Boolean includeRate = true; // Boolean | Populate rate
    try {
      apiInstance.getTransaction(id, includeChargestation, includeEvse, includeConnector, includeDriver, includeToken, includeReservation, includeOrganization, includeRate);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransaction");
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
| **id** | **String**| The transaction id that needs to be fetched | |
| **includeChargestation** | **Boolean**| Populate chargestation | [optional] |
| **includeEvse** | **Boolean**| Populate evse | [optional] |
| **includeConnector** | **Boolean**| Populate connector | [optional] |
| **includeDriver** | **Boolean**| Populate driver | [optional] |
| **includeToken** | **Boolean**| Populate token | [optional] |
| **includeReservation** | **Boolean**| Populate reservation | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |
| **includeRate** | **Boolean**| Populate rate | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a transaction object |  -  |
| **401** | Not Found |  -  |

<a id="getTransactionCost"></a>
# **getTransactionCost**
> getTransactionCost(id)



Get a specific transaction&#39;s cost

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The transaction id that needs to be fetched
    try {
      apiInstance.getTransactionCost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionCost");
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
| **id** | **String**| The transaction id that needs to be fetched | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a transaction&#39;s cost object |  -  |
| **401** | Not Found |  -  |

<a id="getTransactions"></a>
# **getTransactions**
> GetTransactions200Response getTransactions(status, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeChargestation, includeEvse, includeConnector, includeDriver, includeToken, includeReservation, includeOrganization, includeRate)



Get a list of transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String status = "Started"; // String | Started to get only active transactions
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeChargestation = true; // Boolean | Populate chargestation
    Boolean includeEvse = true; // Boolean | Populate evse
    Boolean includeConnector = true; // Boolean | Populate connector
    Boolean includeDriver = true; // Boolean | Populate driver
    Boolean includeToken = true; // Boolean | Populate token
    Boolean includeReservation = true; // Boolean | Populate reservation
    Boolean includeOrganization = true; // Boolean | Populate organization
    Boolean includeRate = true; // Boolean | Populate rate
    try {
      GetTransactions200Response result = apiInstance.getTransactions(status, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeChargestation, includeEvse, includeConnector, includeDriver, includeToken, includeReservation, includeOrganization, includeRate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactions");
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
| **status** | **String**| Started to get only active transactions | [optional] [enum: Started, Ended] |
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeChargestation** | **Boolean**| Populate chargestation | [optional] |
| **includeEvse** | **Boolean**| Populate evse | [optional] |
| **includeConnector** | **Boolean**| Populate connector | [optional] |
| **includeDriver** | **Boolean**| Populate driver | [optional] |
| **includeToken** | **Boolean**| Populate token | [optional] |
| **includeReservation** | **Boolean**| Populate reservation | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |
| **includeRate** | **Boolean**| Populate rate | [optional] |

### Return type

[**GetTransactions200Response**](GetTransactions200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of transaction objects |  -  |
| **400** | Not Found |  -  |

