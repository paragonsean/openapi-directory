# CustomersApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customersDelete**](CustomersApi.md#customersDelete) | **DELETE** /v1/customers/{id} | Removes an existing Customer. |
| [**customersGet**](CustomersApi.md#customersGet) | **GET** /v1/customers | Returns a list of company&#39;s Customers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields. |
| [**customersGetAccountTrans**](CustomersApi.md#customersGetAccountTrans) | **GET** /v1/customers/{itemId}/accountTrans | Returns a list of Customer&#39;s account transactions. |
| [**customersGetOpeningBalance**](CustomersApi.md#customersGetOpeningBalance) | **GET** /v1/customers/{itemId}/openingBalance | Returns a Customer&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old. |
| [**customersGetOpeningBalanceList**](CustomersApi.md#customersGetOpeningBalanceList) | **GET** /v1/customers/{itemId}/openingBalanceList | Returns a list of Customer&#39;s opening balance transactions. |
| [**customersGetQuotes**](CustomersApi.md#customersGetQuotes) | **GET** /v1/customers/{itemId}/quotes | Returns a list of Customer&#39;s quotes. |
| [**customersPost**](CustomersApi.md#customersPost) | **POST** /v1/customers | Creates a new Customer. |
| [**customersProcessBatch**](CustomersApi.md#customersProcessBatch) | **PUT** /v1/customers/batch | Processes a batch of Customers. |
| [**customersPut**](CustomersApi.md#customersPut) | **PUT** /v1/customers/{id} | Updates an existing Customer. |
| [**v1CustomersIdGet**](CustomersApi.md#v1CustomersIdGet) | **GET** /v1/customers/{id} | Returns information about a single Customer. You may specify that Customer&#39;s ledger balance should be calculated. |


<a id="customersDelete"></a>
# **customersDelete**
> Object customersDelete(id, timestamp)

Removes an existing Customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | Id of Customer to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Customer to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.customersDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersDelete");
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
| **id** | **Long**| Id of Customer to remove. | |
| **timestamp** | **String**| Timestamp of Customer to remove. Should be encoded in Base64. | |

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

<a id="customersGet"></a>
# **customersGet**
> PageResultCustomerQueryDto customersGet()

Returns a list of company&#39;s Customers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    try {
      PageResultCustomerQueryDto result = apiInstance.customersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGet");
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

[**PageResultCustomerQueryDto**](PageResultCustomerQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customersGetAccountTrans"></a>
# **customersGetAccountTrans**
> List&lt;AccountTranDto&gt; customersGetAccountTrans(itemId)

Returns a list of Customer&#39;s account transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Customer to return account transaction.
    try {
      List<AccountTranDto> result = apiInstance.customersGetAccountTrans(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGetAccountTrans");
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
| **itemId** | **Long**| Id of Customer to return account transaction. | |

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

<a id="customersGetOpeningBalance"></a>
# **customersGetOpeningBalance**
> OwnerOpeningBalanceInPeriodsDto customersGetOpeningBalance(itemId)

Returns a Customer&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Customer to return opening balances.
    try {
      OwnerOpeningBalanceInPeriodsDto result = apiInstance.customersGetOpeningBalance(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGetOpeningBalance");
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
| **itemId** | **Long**| Id of Customer to return opening balances. | |

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

<a id="customersGetOpeningBalanceList"></a>
# **customersGetOpeningBalanceList**
> List&lt;OwnerOpeningBalanceDto&gt; customersGetOpeningBalanceList(itemId)

Returns a list of Customer&#39;s opening balance transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Customer to return opening balances transaction.
    try {
      List<OwnerOpeningBalanceDto> result = apiInstance.customersGetOpeningBalanceList(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGetOpeningBalanceList");
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
| **itemId** | **Long**| Id of Customer to return opening balances transaction. | |

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

<a id="customersGetQuotes"></a>
# **customersGetQuotes**
> List&lt;QuoteDto&gt; customersGetQuotes(itemId)

Returns a list of Customer&#39;s quotes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long itemId = 56L; // Long | Id of Customer to return quotes.
    try {
      List<QuoteDto> result = apiInstance.customersGetQuotes(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGetQuotes");
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
| **itemId** | **Long**| Id of Customer to return quotes. | |

### Return type

[**List&lt;QuoteDto&gt;**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customersPost"></a>
# **customersPost**
> Object customersPost(customerDto)

Creates a new Customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    CustomerDto customerDto = new CustomerDto(); // CustomerDto | Information of Customer to create.
    try {
      Object result = apiInstance.customersPost(customerDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersPost");
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
| **customerDto** | [**CustomerDto**](CustomerDto.md)| Information of Customer to create. | |

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

<a id="customersProcessBatch"></a>
# **customersProcessBatch**
> Object customersProcessBatch(batchItemCustomerDto)

Processes a batch of Customers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    List<BatchItemCustomerDto> batchItemCustomerDto = Arrays.asList(); // List<BatchItemCustomerDto> | Batch of Customers to process.
    try {
      Object result = apiInstance.customersProcessBatch(batchItemCustomerDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersProcessBatch");
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
| **batchItemCustomerDto** | [**List&lt;BatchItemCustomerDto&gt;**](BatchItemCustomerDto.md)| Batch of Customers to process. | |

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

<a id="customersPut"></a>
# **customersPut**
> Object customersPut(id, customerDto)

Updates an existing Customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | Id of Customer to update.
    CustomerDto customerDto = new CustomerDto(); // CustomerDto | Information of Customer to update.
    try {
      Object result = apiInstance.customersPut(id, customerDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersPut");
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
| **id** | **Long**| Id of Customer to update. | |
| **customerDto** | [**CustomerDto**](CustomerDto.md)| Information of Customer to update. | |

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

<a id="v1CustomersIdGet"></a>
# **v1CustomersIdGet**
> CustomerDto v1CustomersIdGet(id, needBalance)

Returns information about a single Customer. You may specify that Customer&#39;s ledger balance should be calculated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | Id of Customer to return.
    Boolean needBalance = true; // Boolean | If \"true\" then Customer's ledger balance will be calculated; otherwise balance will be returned as 0.
    try {
      CustomerDto result = apiInstance.v1CustomersIdGet(id, needBalance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#v1CustomersIdGet");
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
| **id** | **Long**| Id of Customer to return. | |
| **needBalance** | **Boolean**| If \&quot;true\&quot; then Customer&#39;s ledger balance will be calculated; otherwise balance will be returned as 0. | [optional] |

### Return type

[**CustomerDto**](CustomerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

