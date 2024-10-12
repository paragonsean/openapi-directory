# CompaniesVendorsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCompaniesVendor**](CompaniesVendorsApi.md#addCompaniesVendor) | **POST** /companies_vendors | Add a new companies vendor |
| [**bulkCompaniesVendors**](CompaniesVendorsApi.md#bulkCompaniesVendors) | **DELETE** /companies_vendors/bulkDelete | Bulk delete companies vendors |
| [**companiesVendorsCompaniesVendorIdDelete**](CompaniesVendorsApi.md#companiesVendorsCompaniesVendorIdDelete) | **DELETE** /companies_vendors/{companies_vendor_id} | Delete a companies vendor |
| [**editCompaniesVendor**](CompaniesVendorsApi.md#editCompaniesVendor) | **PUT** /companies_vendors/{companies_vendor_id} | Edit a companies vendor |
| [**getCompaiesVendorsList**](CompaniesVendorsApi.md#getCompaiesVendorsList) | **GET** /companies_vendors | Get a list of companies vendors |
| [**getCompaniesVendor**](CompaniesVendorsApi.md#getCompaniesVendor) | **GET** /companies_vendors/{companies_vendor_id} | Get a companies vendor |
| [**getCompaniesVendorsExpenseStatistics**](CompaniesVendorsApi.md#getCompaniesVendorsExpenseStatistics) | **GET** /companies_vendors/{companies_vendor_id}/expense_statistics | Get companies vendor expense statistics |


<a id="addCompaniesVendor"></a>
# **addCompaniesVendor**
> ClockingRecordsPost201Response addCompaniesVendor(addCompaniesVendorRequest)

Add a new companies vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    AddCompaniesVendorRequest addCompaniesVendorRequest = new AddCompaniesVendorRequest(); // AddCompaniesVendorRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.addCompaniesVendor(addCompaniesVendorRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#addCompaniesVendor");
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
| **addCompaniesVendorRequest** | [**AddCompaniesVendorRequest**](AddCompaniesVendorRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully added companies vendor |  -  |
| **422** | Validation error |  -  |

<a id="bulkCompaniesVendors"></a>
# **bulkCompaniesVendors**
> EmptySuccessResponse bulkCompaniesVendors(bulkActionRequestBody)

Bulk delete companies vendors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Companies vendors ids
    try {
      EmptySuccessResponse result = apiInstance.bulkCompaniesVendors(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#bulkCompaniesVendors");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Companies vendors ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |

<a id="companiesVendorsCompaniesVendorIdDelete"></a>
# **companiesVendorsCompaniesVendorIdDelete**
> ClockingRecordsClockingRecordIdDelete200Response companiesVendorsCompaniesVendorIdDelete(companiesVendorId)

Delete a companies vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    String companiesVendorId = "companiesVendorId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdDelete200Response result = apiInstance.companiesVendorsCompaniesVendorIdDelete(companiesVendorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#companiesVendorsCompaniesVendorIdDelete");
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
| **companiesVendorId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="editCompaniesVendor"></a>
# **editCompaniesVendor**
> ClockingRecordsClockingRecordIdPut200Response editCompaniesVendor(companiesVendorId, addCompaniesVendorRequest)

Edit a companies vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    UUID companiesVendorId = UUID.randomUUID(); // UUID | 
    AddCompaniesVendorRequest addCompaniesVendorRequest = new AddCompaniesVendorRequest(); // AddCompaniesVendorRequest | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.editCompaniesVendor(companiesVendorId, addCompaniesVendorRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#editCompaniesVendor");
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
| **companiesVendorId** | **UUID**|  | |
| **addCompaniesVendorRequest** | [**AddCompaniesVendorRequest**](AddCompaniesVendorRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCompaiesVendorsList"></a>
# **getCompaiesVendorsList**
> GetCompaiesVendorsList200Response getCompaiesVendorsList()

Get a list of companies vendors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    try {
      GetCompaiesVendorsList200Response result = apiInstance.getCompaiesVendorsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#getCompaiesVendorsList");
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

[**GetCompaiesVendorsList200Response**](GetCompaiesVendorsList200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCompaniesVendor"></a>
# **getCompaniesVendor**
> GetCompaniesVendor200Response getCompaniesVendor(companiesVendorId)

Get a companies vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    String companiesVendorId = "companiesVendorId_example"; // String | 
    try {
      GetCompaniesVendor200Response result = apiInstance.getCompaniesVendor(companiesVendorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#getCompaniesVendor");
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
| **companiesVendorId** | **String**|  | |

### Return type

[**GetCompaniesVendor200Response**](GetCompaniesVendor200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="getCompaniesVendorsExpenseStatistics"></a>
# **getCompaniesVendorsExpenseStatistics**
> GetCompaniesVendorsExpenseStatistics200Response getCompaniesVendorsExpenseStatistics(companiesVendorId)

Get companies vendor expense statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesVendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesVendorsApi apiInstance = new CompaniesVendorsApi(defaultClient);
    UUID companiesVendorId = UUID.randomUUID(); // UUID | 
    try {
      GetCompaniesVendorsExpenseStatistics200Response result = apiInstance.getCompaniesVendorsExpenseStatistics(companiesVendorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesVendorsApi#getCompaniesVendorsExpenseStatistics");
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
| **companiesVendorId** | **UUID**|  | |

### Return type

[**GetCompaniesVendorsExpenseStatistics200Response**](GetCompaniesVendorsExpenseStatistics200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

