# EarningsApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrUpdateAnEmployeeEarning**](EarningsApi.md#addOrUpdateAnEmployeeEarning) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/earnings | Add/Update Earning |
| [**deleteEarningByEarningCodeAndStartDate**](EarningsApi.md#deleteEarningByEarningCodeAndStartDate) | **DELETE** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate} | Delete Earning by Earning Code and Start Date |
| [**getAllEarnings**](EarningsApi.md#getAllEarnings) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings | Get All Earnings |
| [**getEarningByEarningCodeAndStartDate**](EarningsApi.md#getEarningByEarningCodeAndStartDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate} | Get Earning by Earning Code and Start Date |
| [**getEarningsByEarningCode**](EarningsApi.md#getEarningsByEarningCode) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode} | Get Earnings by Earning Code |


<a id="addOrUpdateAnEmployeeEarning"></a>
# **addOrUpdateAnEmployeeEarning**
> addOrUpdateAnEmployeeEarning(companyId, employeeId, earning)

Add/Update Earning

Add/Update Earning API sends new or updated employee earnings information directly to Web Pay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarningsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EarningsApi apiInstance = new EarningsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    Earning earning = new Earning(); // Earning | Earning Model
    try {
      apiInstance.addOrUpdateAnEmployeeEarning(companyId, employeeId, earning);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarningsApi#addOrUpdateAnEmployeeEarning");
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
| **earning** | [**Earning**](Earning.md)| Earning Model | |

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
| **200** | Successfully added or updated |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="deleteEarningByEarningCodeAndStartDate"></a>
# **deleteEarningByEarningCodeAndStartDate**
> deleteEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate)

Delete Earning by Earning Code and Start Date

Delete Earning by Earning Code and Start Date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarningsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EarningsApi apiInstance = new EarningsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String earningCode = "earningCode_example"; // String | Earning Code
    String startDate = "startDate_example"; // String | Start Date
    try {
      apiInstance.deleteEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarningsApi#deleteEarningByEarningCodeAndStartDate");
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
| **earningCode** | **String**| Earning Code | |
| **startDate** | **String**| Start Date | |

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
| **404** | The employee does not exist, or the specified earningCode-startDate combination does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAllEarnings"></a>
# **getAllEarnings**
> List&lt;Earning&gt; getAllEarnings(companyId, employeeId)

Get All Earnings

Get All Earnings returns all earnings for the selected employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarningsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EarningsApi apiInstance = new EarningsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    try {
      List<Earning> result = apiInstance.getAllEarnings(companyId, employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarningsApi#getAllEarnings");
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

[**List&lt;Earning&gt;**](Earning.md)

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

<a id="getEarningByEarningCodeAndStartDate"></a>
# **getEarningByEarningCodeAndStartDate**
> Earning getEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate)

Get Earning by Earning Code and Start Date

Get Earnings returns the single earning with the provided earning code and start date for the selected employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarningsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EarningsApi apiInstance = new EarningsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String earningCode = "earningCode_example"; // String | Earning Code
    String startDate = "startDate_example"; // String | Start Date
    try {
      Earning result = apiInstance.getEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarningsApi#getEarningByEarningCodeAndStartDate");
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
| **earningCode** | **String**| Earning Code | |
| **startDate** | **String**| Start Date | |

### Return type

[**Earning**](Earning.md)

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
| **404** | The employee does not exist, or the specified earningCode-startDate combination does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getEarningsByEarningCode"></a>
# **getEarningsByEarningCode**
> List&lt;Earning&gt; getEarningsByEarningCode(companyId, employeeId, earningCode)

Get Earnings by Earning Code

Get Earnings returns all earnings with the provided earning code for the selected employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarningsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EarningsApi apiInstance = new EarningsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String earningCode = "earningCode_example"; // String | Earning Code
    try {
      List<Earning> result = apiInstance.getEarningsByEarningCode(companyId, employeeId, earningCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarningsApi#getEarningsByEarningCode");
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
| **earningCode** | **String**| Earning Code | |

### Return type

[**List&lt;Earning&gt;**](Earning.md)

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

