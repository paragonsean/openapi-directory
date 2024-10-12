# EnrollmentAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enrollmentAccountsGet**](EnrollmentAccountsApi.md#enrollmentAccountsGet) | **GET** /providers/Microsoft.Billing/enrollmentAccounts/{name} |  |
| [**enrollmentAccountsList**](EnrollmentAccountsApi.md#enrollmentAccountsList) | **GET** /providers/Microsoft.Billing/enrollmentAccounts |  |


<a id="enrollmentAccountsGet"></a>
# **enrollmentAccountsGet**
> EnrollmentAccount enrollmentAccountsGet(name, apiVersion)



Gets a enrollment account by name.

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
    String name = "name_example"; // String | Enrollment Account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    try {
      EnrollmentAccount result = apiInstance.enrollmentAccountsGet(name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnrollmentAccountsApi#enrollmentAccountsGet");
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
| **name** | **String**| Enrollment Account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-01-preview. | |

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

<a id="enrollmentAccountsList"></a>
# **enrollmentAccountsList**
> EnrollmentAccountListResult enrollmentAccountsList(apiVersion)



Lists the enrollment accounts the caller has access to.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    try {
      EnrollmentAccountListResult result = apiInstance.enrollmentAccountsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnrollmentAccountsApi#enrollmentAccountsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-01-preview. | |

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

