# LocalTaxesApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addLocalTax**](LocalTaxesApi.md#addLocalTax) | **POST** /v2/companies/{companyId}/employees/{employeeId}/localTaxes | Add new local tax |
| [**deleteLocalTaxByTaxCode**](LocalTaxesApi.md#deleteLocalTaxByTaxCode) | **DELETE** /v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode} | Delete local tax by tax code |
| [**getAllLocalTaxes**](LocalTaxesApi.md#getAllLocalTaxes) | **GET** /v2/companies/{companyId}/employees/{employeeId}/localTaxes | Get all local taxes |
| [**getLocalTaxByTaxCode**](LocalTaxesApi.md#getLocalTaxByTaxCode) | **GET** /v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode} | Get local taxes by tax code |


<a id="addLocalTax"></a>
# **addLocalTax**
> addLocalTax(companyId, employeeId, localTax)

Add new local tax

Sends new employee local tax information directly to Web Pay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalTaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalTaxesApi apiInstance = new LocalTaxesApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    LocalTax localTax = new LocalTax(); // LocalTax | LocalTax Model
    try {
      apiInstance.addLocalTax(companyId, employeeId, localTax);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalTaxesApi#addLocalTax");
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
| **companyId** | **String**| Company Id | |
| **employeeId** | **String**| Employee Id | |
| **localTax** | [**LocalTax**](LocalTax.md)| LocalTax Model | |

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully added |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="deleteLocalTaxByTaxCode"></a>
# **deleteLocalTaxByTaxCode**
> deleteLocalTaxByTaxCode(companyId, employeeId, taxCode)

Delete local tax by tax code

Delete local tax by tax code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalTaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalTaxesApi apiInstance = new LocalTaxesApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String taxCode = "taxCode_example"; // String | Tax Code
    try {
      apiInstance.deleteLocalTaxByTaxCode(companyId, employeeId, taxCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalTaxesApi#deleteLocalTaxByTaxCode");
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
| **companyId** | **String**| Company Id | |
| **employeeId** | **String**| Employee Id | |
| **taxCode** | **String**| Tax Code | |

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee does not exist, or the specified tax code does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAllLocalTaxes"></a>
# **getAllLocalTaxes**
> List&lt;LocalTax&gt; getAllLocalTaxes(companyId, employeeId)

Get all local taxes

Returns all local taxes for the selected employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalTaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalTaxesApi apiInstance = new LocalTaxesApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    try {
      List<LocalTax> result = apiInstance.getAllLocalTaxes(companyId, employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalTaxesApi#getAllLocalTaxes");
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
| **companyId** | **String**| Company Id | |
| **employeeId** | **String**| Employee Id | |

### Return type

[**List&lt;LocalTax&gt;**](LocalTax.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getLocalTaxByTaxCode"></a>
# **getLocalTaxByTaxCode**
> List&lt;LocalTax&gt; getLocalTaxByTaxCode(companyId, employeeId, taxCode)

Get local taxes by tax code

Returns all local taxes with the provided tax code for the selected employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalTaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalTaxesApi apiInstance = new LocalTaxesApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String taxCode = "taxCode_example"; // String | Tax Code
    try {
      List<LocalTax> result = apiInstance.getLocalTaxByTaxCode(companyId, employeeId, taxCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalTaxesApi#getLocalTaxByTaxCode");
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
| **companyId** | **String**| Company Id | |
| **employeeId** | **String**| Employee Id | |
| **taxCode** | **String**| Tax Code | |

### Return type

[**List&lt;LocalTax&gt;**](LocalTax.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee does not exist, or the specified tax code does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

