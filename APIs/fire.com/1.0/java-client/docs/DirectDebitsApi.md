# DirectDebitsApi

All URIs are relative to *https://api.fire.com/business*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateMandate**](DirectDebitsApi.md#activateMandate) | **POST** /v1/mandates/{mandateUuid}/activate | Activate a direct debit mandate |
| [**cancelMandateByUuid**](DirectDebitsApi.md#cancelMandateByUuid) | **POST** /v1/mandates/{mandateUuid}/cancel | Cancel a direct debit mandate |
| [**getDirectDebitByUuid**](DirectDebitsApi.md#getDirectDebitByUuid) | **GET** /v1/directdebits/{directDebitUuid} | Get the details of a direct debit |
| [**getDirectDebitMandates**](DirectDebitsApi.md#getDirectDebitMandates) | **GET** /v1/mandates | List all direct debit mandates |
| [**getDirectDebitsForMandateUuid**](DirectDebitsApi.md#getDirectDebitsForMandateUuid) | **GET** /v1/directdebits | Get all DD payments associated with a direct debit mandate |
| [**getMandate**](DirectDebitsApi.md#getMandate) | **GET** /v1/mandates/{mandateUuid} | Get direct debit mandate details |
| [**rejectDirectDebit**](DirectDebitsApi.md#rejectDirectDebit) | **POST** /v1/directdebits/{directDebitUuid}/reject | Reject a direct debit payment |
| [**updateMandateAlias**](DirectDebitsApi.md#updateMandateAlias) | **POST** /v1/mandates/{mandateUuid} | Update a direct debit mandate alias |


<a id="activateMandate"></a>
# **activateMandate**
> activateMandate(mandateUuid)

Activate a direct debit mandate

This endpoint can only be used to activate a direct debit mandate when it is in the status REJECT_REQUESTED (even if the account has direct debits disabled). This action will also enable the account for direct debits if it was previously set to be disabled. The permision needed to access this endpoint is PERM_BUSINESS_POST_MANDATE_ACTIVATE 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.activateMandate(mandateUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#activateMandate");
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
| **mandateUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | 204 no content |  -  |

<a id="cancelMandateByUuid"></a>
# **cancelMandateByUuid**
> cancelMandateByUuid(mandateUuid)

Cancel a direct debit mandate

This endpoint allows you to cancel a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_POST_MANDATE_CANCEL 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.cancelMandateByUuid(mandateUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#cancelMandateByUuid");
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
| **mandateUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | 204 no content |  -  |

<a id="getDirectDebitByUuid"></a>
# **getDirectDebitByUuid**
> DirectDebit getDirectDebitByUuid(directDebitUuid)

Get the details of a direct debit

Retrieve all details of a single direct debit collection/payment, whether successful or not. The permision needed to access this endpoint is **PERM_BUSINESS_GET_DIRECT_DEBIT** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String directDebitUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      DirectDebit result = apiInstance.getDirectDebitByUuid(directDebitUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#getDirectDebitByUuid");
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
| **directDebitUuid** | **String**|  | |

### Return type

[**DirectDebit**](DirectDebit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve all details of a single direct debit collection/payment |  -  |

<a id="getDirectDebitMandates"></a>
# **getDirectDebitMandates**
> Mandates getDirectDebitMandates()

List all direct debit mandates

The permision needed to access this endpoint is PERM_BUSINESS_GET_MANDATES 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    try {
      Mandates result = apiInstance.getDirectDebitMandates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#getDirectDebitMandates");
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

[**Mandates**](Mandates.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all direct debit mandates. |  -  |

<a id="getDirectDebitsForMandateUuid"></a>
# **getDirectDebitsForMandateUuid**
> DirectDebits getDirectDebitsForMandateUuid(mandateUuid)

Get all DD payments associated with a direct debit mandate

Retrieve all direct debit payments associated with a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_GET_DIRECT_DEBITS 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String mandateUuid = "1A07774B-1461-4595-BC4B-423B739712AF"; // String | The mandate UUID to retrieve
    try {
      DirectDebits result = apiInstance.getDirectDebitsForMandateUuid(mandateUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#getDirectDebitsForMandateUuid");
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
| **mandateUuid** | **String**| The mandate UUID to retrieve | |

### Return type

[**DirectDebits**](DirectDebits.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve all direct debit payments associated with a direct debit mandate. |  -  |

<a id="getMandate"></a>
# **getMandate**
> Mandate getMandate(mandateUuid)

Get direct debit mandate details

Retrieve all details for a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_GET_MANDATE 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      Mandate result = apiInstance.getMandate(mandateUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#getMandate");
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
| **mandateUuid** | **String**|  | |

### Return type

[**Mandate**](Mandate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve all details for a direct debit mandate. |  -  |

<a id="rejectDirectDebit"></a>
# **rejectDirectDebit**
> rejectDirectDebit(directDebitUuid)

Reject a direct debit payment

This endpoint allows you to reject a direct debit payment where the status is still set to RECEIVED. Permission name PERM_BUSINESS_POST_DIRECT_DEBIT_REJECT 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String directDebitUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.rejectDirectDebit(directDebitUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#rejectDirectDebit");
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
| **directDebitUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | 204 no content |  -  |

<a id="updateMandateAlias"></a>
# **updateMandateAlias**
> updateMandateAlias(mandateUuid)

Update a direct debit mandate alias

Update Direct Debit Mandate Alias The permision needed to access this endpoint is PERM_BUSINESS_PUT_MANDATE 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDebitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DirectDebitsApi apiInstance = new DirectDebitsApi(defaultClient);
    String mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.updateMandateAlias(mandateUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDebitsApi#updateMandateAlias");
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
| **mandateUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | 204 no content |  -  |

