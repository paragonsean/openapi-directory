# SuppliersApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**suppliersDelete**](SuppliersApi.md#suppliersDelete) | **DELETE** /v1/suppliers/{id} | Removes an existing Supplier. |
| [**suppliersGet**](SuppliersApi.md#suppliersGet) | **GET** /v1/suppliers | Returns a list of company&#39;s Suppliers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields. |
| [**suppliersGetAccountTrans**](SuppliersApi.md#suppliersGetAccountTrans) | **GET** /v1/suppliers/{itemId}/accountTrans | Returns a list of Supplier&#39;s account transactions. |
| [**suppliersGetOpeningBalance**](SuppliersApi.md#suppliersGetOpeningBalance) | **GET** /v1/suppliers/{itemId}/openingBalance | Returns a Supplier&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old. |
| [**suppliersGetOpeningBalanceList**](SuppliersApi.md#suppliersGetOpeningBalanceList) | **GET** /v1/suppliers/{itemId}/openingBalanceList | Returns a list of Supplier&#39;s opening balance transactions. |
| [**suppliersPost**](SuppliersApi.md#suppliersPost) | **POST** /v1/suppliers | Creates a new Supplier. |
| [**suppliersProcessBatch**](SuppliersApi.md#suppliersProcessBatch) | **PUT** /v1/suppliers/batch | Processes a batch of Suppliers. |
| [**suppliersPut**](SuppliersApi.md#suppliersPut) | **PUT** /v1/suppliers/{id} | Updates an existing Supplier. |
| [**v1SuppliersIdGet**](SuppliersApi.md#v1SuppliersIdGet) | **GET** /v1/suppliers/{id} | Returns information about a single Supplier. You may specify that Supplier&#39;s ledger balance should be calculated. |


<a id="suppliersDelete"></a>
# **suppliersDelete**
> Object suppliersDelete(id, timestamp)

Removes an existing Supplier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    Long id = 56L; // Long | Id of Supplier to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Supplier to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.suppliersDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersDelete");
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
| **id** | **Long**| Id of Supplier to remove. | |
| **timestamp** | **String**| Timestamp of Supplier to remove. Should be encoded in Base64. | |

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

<a id="suppliersGet"></a>
# **suppliersGet**
> PageResultSupplierQueryDto suppliersGet()

Returns a list of company&#39;s Suppliers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    try {
      PageResultSupplierQueryDto result = apiInstance.suppliersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersGet");
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

[**PageResultSupplierQueryDto**](PageResultSupplierQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="suppliersGetAccountTrans"></a>
# **suppliersGetAccountTrans**
> List&lt;AccountTranDto&gt; suppliersGetAccountTrans(itemId)

Returns a list of Supplier&#39;s account transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Supplier to return account transaction.
    try {
      List<AccountTranDto> result = apiInstance.suppliersGetAccountTrans(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersGetAccountTrans");
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
| **itemId** | **Long**| Id of Supplier to return account transaction. | |

### Return type

[**List&lt;AccountTranDto&gt;**](AccountTranDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="suppliersGetOpeningBalance"></a>
# **suppliersGetOpeningBalance**
> OwnerOpeningBalanceInPeriodsDto suppliersGetOpeningBalance(itemId)

Returns a Supplier&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Supplier to return opening balances.
    try {
      OwnerOpeningBalanceInPeriodsDto result = apiInstance.suppliersGetOpeningBalance(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersGetOpeningBalance");
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
| **itemId** | **Long**| Id of Supplier to return opening balances. | |

### Return type

[**OwnerOpeningBalanceInPeriodsDto**](OwnerOpeningBalanceInPeriodsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="suppliersGetOpeningBalanceList"></a>
# **suppliersGetOpeningBalanceList**
> List&lt;OwnerOpeningBalanceDto&gt; suppliersGetOpeningBalanceList(itemId)

Returns a list of Supplier&#39;s opening balance transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Supplier to return opening balances transaction.
    try {
      List<OwnerOpeningBalanceDto> result = apiInstance.suppliersGetOpeningBalanceList(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersGetOpeningBalanceList");
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
| **itemId** | **Long**| Id of Supplier to return opening balances transaction. | |

### Return type

[**List&lt;OwnerOpeningBalanceDto&gt;**](OwnerOpeningBalanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="suppliersPost"></a>
# **suppliersPost**
> Object suppliersPost(supplierDto)

Creates a new Supplier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    SupplierDto supplierDto = new SupplierDto(); // SupplierDto | Information of Supplier to create.
    try {
      Object result = apiInstance.suppliersPost(supplierDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersPost");
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
| **supplierDto** | [**SupplierDto**](SupplierDto.md)| Information of Supplier to create. | |

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

<a id="suppliersProcessBatch"></a>
# **suppliersProcessBatch**
> Object suppliersProcessBatch(batchItemSupplierDto)

Processes a batch of Suppliers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    List<BatchItemSupplierDto> batchItemSupplierDto = Arrays.asList(); // List<BatchItemSupplierDto> | Batch of Suppliers to process.
    try {
      Object result = apiInstance.suppliersProcessBatch(batchItemSupplierDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersProcessBatch");
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
| **batchItemSupplierDto** | [**List&lt;BatchItemSupplierDto&gt;**](BatchItemSupplierDto.md)| Batch of Suppliers to process. | |

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

<a id="suppliersPut"></a>
# **suppliersPut**
> Object suppliersPut(id, supplierDto)

Updates an existing Supplier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    Long id = 56L; // Long | Id of Supplier to update.
    SupplierDto supplierDto = new SupplierDto(); // SupplierDto | Information of Supplier to update.
    try {
      Object result = apiInstance.suppliersPut(id, supplierDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#suppliersPut");
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
| **id** | **Long**| Id of Supplier to update. | |
| **supplierDto** | [**SupplierDto**](SupplierDto.md)| Information of Supplier to update. | |

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

<a id="v1SuppliersIdGet"></a>
# **v1SuppliersIdGet**
> SupplierDto v1SuppliersIdGet(id, needBalance)

Returns information about a single Supplier. You may specify that Supplier&#39;s ledger balance should be calculated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppliersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SuppliersApi apiInstance = new SuppliersApi(defaultClient);
    Long id = 56L; // Long | Id of Supplier to return.
    Boolean needBalance = true; // Boolean | If \"true\" then Supplier's ledger balance will be calculated; otherwise balance will be returned as 0.
    try {
      SupplierDto result = apiInstance.v1SuppliersIdGet(id, needBalance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppliersApi#v1SuppliersIdGet");
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
| **id** | **Long**| Id of Supplier to return. | |
| **needBalance** | **Boolean**| If \&quot;true\&quot; then Supplier&#39;s ledger balance will be calculated; otherwise balance will be returned as 0. | [optional] |

### Return type

[**SupplierDto**](SupplierDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

