# PaymentsApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPayment**](PaymentsApi.md#createPayment) | **POST** /api/v2/payments/ |  |
| [**deletePeriodicPayment**](PaymentsApi.md#deletePeriodicPayment) | **DELETE** /api/v2/payments/{id}/ |  |
| [**listMinimumRequiredFieldsForInstitution**](PaymentsApi.md#listMinimumRequiredFieldsForInstitution) | **GET** /api/v2/payments/fields/{institution_id}/ |  |
| [**listPayments**](PaymentsApi.md#listPayments) | **GET** /api/v2/payments/ |  |
| [**paymentsCreditorsCreate**](PaymentsApi.md#paymentsCreditorsCreate) | **POST** /api/v2/payments/creditors/ |  |
| [**paymentsCreditorsDestroy**](PaymentsApi.md#paymentsCreditorsDestroy) | **DELETE** /api/v2/payments/creditors/{id}/ |  |
| [**paymentsCreditorsList**](PaymentsApi.md#paymentsCreditorsList) | **GET** /api/v2/payments/creditors/ |  |
| [**paymentsCreditorsRetrieve**](PaymentsApi.md#paymentsCreditorsRetrieve) | **GET** /api/v2/payments/creditors/{id}/ |  |
| [**paymentsSubmitCreate**](PaymentsApi.md#paymentsSubmitCreate) | **POST** /api/v2/payments/{id}/submit/ |  |
| [**retrieveAllPaymentCreditorAccounts**](PaymentsApi.md#retrieveAllPaymentCreditorAccounts) | **GET** /api/v2/payments/account/ |  |
| [**retrievePayment**](PaymentsApi.md#retrievePayment) | **GET** /api/v2/payments/{id}/ |  |


<a id="createPayment"></a>
# **createPayment**
> PaymentWrite createPayment(paymentWriteRequest)



Create payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    PaymentWriteRequest paymentWriteRequest = new PaymentWriteRequest(); // PaymentWriteRequest | 
    try {
      PaymentWrite result = apiInstance.createPayment(paymentWriteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#createPayment");
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
| **paymentWriteRequest** | [**PaymentWriteRequest**](PaymentWriteRequest.md)|  | |

### Return type

[**PaymentWrite**](PaymentWrite.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create payment |  -  |
| **400** | Unknown Fields |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |

<a id="deletePeriodicPayment"></a>
# **deletePeriodicPayment**
> Map&lt;String, Object&gt; deletePeriodicPayment(id)



Delete periodic payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      Map<String, Object> result = apiInstance.deletePeriodicPayment(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#deletePeriodicPayment");
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
| **id** | **UUID**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment deleted |  -  |
| **400** | Invalid ID |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **409** | Payment delete error |  -  |

<a id="listMinimumRequiredFieldsForInstitution"></a>
# **listMinimumRequiredFieldsForInstitution**
> Map&lt;String, Object&gt; listMinimumRequiredFieldsForInstitution(institutionId)



List minimum required fields for institution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String institutionId = "institutionId_example"; // String | 
    try {
      Map<String, Object> result = apiInstance.listMinimumRequiredFieldsForInstitution(institutionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#listMinimumRequiredFieldsForInstitution");
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
| **institutionId** | **String**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Minimum required fields |  -  |
| **400** | Unknown Fields |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |

<a id="listPayments"></a>
# **listPayments**
> PaginatedPaymentReadList listPayments(limit, offset)



Retrieve all payments belonging to the company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Integer limit = 100; // Integer | Number of results to return per page.
    Integer offset = 1; // Integer | The initial index from which to return the results.
    try {
      PaginatedPaymentReadList result = apiInstance.listPayments(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#listPayments");
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
| **limit** | **Integer**| Number of results to return per page. | [optional] [default to 100] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] [default to 1] |

### Return type

[**PaginatedPaymentReadList**](PaginatedPaymentReadList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List payments |  -  |
| **400** | Unknown Fields |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |

<a id="paymentsCreditorsCreate"></a>
# **paymentsCreditorsCreate**
> CreditorAccountWrite paymentsCreditorsCreate(creditorAccountWriteRequest)



API endpoints related to creditor accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    CreditorAccountWriteRequest creditorAccountWriteRequest = new CreditorAccountWriteRequest(); // CreditorAccountWriteRequest | 
    try {
      CreditorAccountWrite result = apiInstance.paymentsCreditorsCreate(creditorAccountWriteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsCreditorsCreate");
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
| **creditorAccountWriteRequest** | [**CreditorAccountWriteRequest**](CreditorAccountWriteRequest.md)|  | |

### Return type

[**CreditorAccountWrite**](CreditorAccountWrite.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="paymentsCreditorsDestroy"></a>
# **paymentsCreditorsDestroy**
> paymentsCreditorsDestroy(id)



API endpoints related to creditor accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.paymentsCreditorsDestroy(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsCreditorsDestroy");
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
| **id** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No response body |  -  |

<a id="paymentsCreditorsList"></a>
# **paymentsCreditorsList**
> PaginatedCreditorAccountList paymentsCreditorsList(account, addressCountry, agent, currency, limit, name, offset, type)



API endpoints related to creditor accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String account = "account_example"; // String | 
    String addressCountry = "addressCountry_example"; // String | 
    String agent = "agent_example"; // String | 
    String currency = "currency_example"; // String | 
    Integer limit = 100; // Integer | Number of results to return per page.
    String name = "name_example"; // String | 
    Integer offset = 1; // Integer | The initial index from which to return the results.
    String type = "type_example"; // String | 
    try {
      PaginatedCreditorAccountList result = apiInstance.paymentsCreditorsList(account, addressCountry, agent, currency, limit, name, offset, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsCreditorsList");
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
| **account** | **String**|  | [optional] |
| **addressCountry** | **String**|  | [optional] |
| **agent** | **String**|  | [optional] |
| **currency** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] [default to 100] |
| **name** | **String**|  | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] [default to 1] |
| **type** | **String**|  | [optional] |

### Return type

[**PaginatedCreditorAccountList**](PaginatedCreditorAccountList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="paymentsCreditorsRetrieve"></a>
# **paymentsCreditorsRetrieve**
> CreditorAccount paymentsCreditorsRetrieve(id)



API endpoints related to creditor accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      CreditorAccount result = apiInstance.paymentsCreditorsRetrieve(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsCreditorsRetrieve");
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
| **id** | **UUID**|  | |

### Return type

[**CreditorAccount**](CreditorAccount.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="paymentsSubmitCreate"></a>
# **paymentsSubmitCreate**
> PaymentRead paymentsSubmitCreate(id, paymentReadRequest)



Initiate the payment on bank&#39;s side.  Complete the payment and return payment details as a response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    PaymentReadRequest paymentReadRequest = new PaymentReadRequest(); // PaymentReadRequest | 
    try {
      PaymentRead result = apiInstance.paymentsSubmitCreate(id, paymentReadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsSubmitCreate");
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
| **id** | **UUID**|  | |
| **paymentReadRequest** | [**PaymentReadRequest**](PaymentReadRequest.md)|  | |

### Return type

[**PaymentRead**](PaymentRead.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="retrieveAllPaymentCreditorAccounts"></a>
# **retrieveAllPaymentCreditorAccounts**
> List&lt;CreditorAccount&gt; retrieveAllPaymentCreditorAccounts()



Retrieve all payment creditor accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      List<CreditorAccount> result = apiInstance.retrieveAllPaymentCreditorAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#retrieveAllPaymentCreditorAccounts");
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

[**List&lt;CreditorAccount&gt;**](CreditorAccount.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve all payment creditor accounts |  -  |
| **400** | Unknown Fields |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |

<a id="retrievePayment"></a>
# **retrievePayment**
> PaymentRead retrievePayment(id)



Retrieve payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      PaymentRead result = apiInstance.retrievePayment(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#retrievePayment");
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
| **id** | **UUID**|  | |

### Return type

[**PaymentRead**](PaymentRead.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve payment information |  -  |
| **400** | Invalid ID |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |

