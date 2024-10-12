# TransactionApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTransaction**](TransactionApi.md#createTransaction) | **POST** /transaction | Create Transaction |
| [**getTransaction**](TransactionApi.md#getTransaction) | **GET** /transaction/{transactionNumber} | Get Transaction  |
| [**listTransactions**](TransactionApi.md#listTransactions) | **GET** /transaction | List Transactions |
| [**updateTransaction**](TransactionApi.md#updateTransaction) | **POST** /transaction/{transactionNumber} | Update Transaction |


<a id="createTransaction"></a>
# **createTransaction**
> Netlicensing createTransaction(active, source, status, dateClosed, dateCreated, licenseeNumber, number, paymentMethod)

Create Transaction

Creates a new Transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    Boolean active = true; // Boolean | Always 'true' for Transactions
    String source = "SHOP"; // String | AUTO Transaction for internal use only
    String status = "CANCELLED"; // String | 
    OffsetDateTime dateClosed = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | 
    String licenseeNumber = "licenseeNumber_example"; // String | 
    String number = "number_example"; // String | Unique number (across all Products of a Vendor) that identifies the Transaction
    String paymentMethod = "paymentMethod_example"; // String | 
    try {
      Netlicensing result = apiInstance.createTransaction(active, source, status, dateClosed, dateCreated, licenseeNumber, number, paymentMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#createTransaction");
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
| **active** | **Boolean**| Always &#39;true&#39; for Transactions | |
| **source** | **String**| AUTO Transaction for internal use only | [enum: SHOP] |
| **status** | **String**|  | [enum: CANCELLED, CLOSED, PENDING] |
| **dateClosed** | **OffsetDateTime**|  | [optional] |
| **dateCreated** | **OffsetDateTime**|  | [optional] |
| **licenseeNumber** | **String**|  | [optional] |
| **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | [optional] |
| **paymentMethod** | **String**|  | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="getTransaction"></a>
# **getTransaction**
> Netlicensing getTransaction(transactionNumber)

Get Transaction 

Return a Transaction by &#39;transactionNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String transactionNumber = "transactionNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Transaction
    try {
      Netlicensing result = apiInstance.getTransaction(transactionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#getTransaction");
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
| **transactionNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="listTransactions"></a>
# **listTransactions**
> List&lt;Netlicensing&gt; listTransactions()

List Transactions

Return a list of all Transactions for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listTransactions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#listTransactions");
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

[**List&lt;Netlicensing&gt;**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="updateTransaction"></a>
# **updateTransaction**
> Netlicensing updateTransaction(transactionNumber, active, dateClosed, dateCreated, number, paymentMethod, source, status)

Update Transaction

Sets the provided properties to a Transaction. Return an updated Transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String transactionNumber = "transactionNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Transaction
    Boolean active = true; // Boolean | Always 'true' for Transactions
    OffsetDateTime dateClosed = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | 
    String number = "number_example"; // String | Unique number (across all Products of a Vendor) that identifies the Transaction
    String paymentMethod = "paymentMethod_example"; // String | 
    String source = "SHOP"; // String | AUTO Transaction for internal use only
    String status = "CANCELLED"; // String | 
    try {
      Netlicensing result = apiInstance.updateTransaction(transactionNumber, active, dateClosed, dateCreated, number, paymentMethod, source, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#updateTransaction");
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
| **transactionNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | |
| **active** | **Boolean**| Always &#39;true&#39; for Transactions | [optional] |
| **dateClosed** | **OffsetDateTime**|  | [optional] |
| **dateCreated** | **OffsetDateTime**|  | [optional] |
| **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | [optional] |
| **paymentMethod** | **String**|  | [optional] |
| **source** | **String**| AUTO Transaction for internal use only | [optional] [enum: SHOP] |
| **status** | **String**|  | [optional] [enum: CANCELLED, CLOSED, PENDING] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

