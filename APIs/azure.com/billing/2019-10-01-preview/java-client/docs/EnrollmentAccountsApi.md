# EnrollmentAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enrollmentAccountsGetByEnrollmentAccountId**](EnrollmentAccountsApi.md#enrollmentAccountsGetByEnrollmentAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/enrollmentAccounts/{enrollmentAccountName} |  |
| [**enrollmentAccountsListByBillingAccountName**](EnrollmentAccountsApi.md#enrollmentAccountsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/enrollmentAccounts |  |


<a id="enrollmentAccountsGetByEnrollmentAccountId"></a>
# **enrollmentAccountsGetByEnrollmentAccountId**
> EnrollmentAccount enrollmentAccountsGetByEnrollmentAccountId(apiVersion, billingAccountName, enrollmentAccountName, $expand, $filter)



Get the enrollment account by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnrollmentAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnrollmentAccountsApi apiInstance = new EnrollmentAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String enrollmentAccountName = "enrollmentAccountName_example"; // String | Enrollment Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the Department.
    String $filter = "$filter_example"; // String | The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      EnrollmentAccount result = apiInstance.enrollmentAccountsGetByEnrollmentAccountId(apiVersion, billingAccountName, enrollmentAccountName, $expand, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnrollmentAccountsApi#enrollmentAccountsGetByEnrollmentAccountId");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **enrollmentAccountName** | **String**| Enrollment Account Id. | |
| **$expand** | **String**| May be used to expand the Department. | [optional] |
| **$filter** | **String**| The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**EnrollmentAccount**](EnrollmentAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="enrollmentAccountsListByBillingAccountName"></a>
# **enrollmentAccountsListByBillingAccountName**
> EnrollmentAccountListResult enrollmentAccountsListByBillingAccountName(apiVersion, billingAccountName, $expand, $filter)



Lists all Enrollment Accounts for a user which he has access to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnrollmentAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnrollmentAccountsApi apiInstance = new EnrollmentAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the department.
    String $filter = "$filter_example"; // String | The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      EnrollmentAccountListResult result = apiInstance.enrollmentAccountsListByBillingAccountName(apiVersion, billingAccountName, $expand, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnrollmentAccountsApi#enrollmentAccountsListByBillingAccountName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **$expand** | **String**| May be used to expand the department. | [optional] |
| **$filter** | **String**| The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**EnrollmentAccountListResult**](EnrollmentAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

