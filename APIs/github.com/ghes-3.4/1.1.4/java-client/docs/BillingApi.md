# BillingApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingGetGithubAdvancedSecurityBillingGhe**](BillingApi.md#billingGetGithubAdvancedSecurityBillingGhe) | **GET** /enterprises/{enterprise}/settings/billing/advanced-security | Get GitHub Advanced Security active committers for an enterprise |
| [**billingGetGithubAdvancedSecurityBillingOrg**](BillingApi.md#billingGetGithubAdvancedSecurityBillingOrg) | **GET** /orgs/{org}/settings/billing/advanced-security | Get GitHub Advanced Security active committers for an organization |


<a id="billingGetGithubAdvancedSecurityBillingGhe"></a>
# **billingGetGithubAdvancedSecurityBillingGhe**
> AdvancedSecurityActiveCommitters billingGetGithubAdvancedSecurityBillingGhe(enterprise, perPage, page)

Get GitHub Advanced Security active committers for an enterprise

Gets the GitHub Advanced Security active committers for an enterprise per repository.  Each distinct user login across all repositories is counted as a single Advanced Security seat, so the &#x60;total_advanced_security_committers&#x60; is not the sum of active_users for each repository.  The total number of repositories with committer information is tracked by the &#x60;total_count&#x60; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      AdvancedSecurityActiveCommitters result = apiInstance.billingGetGithubAdvancedSecurityBillingGhe(enterprise, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingGetGithubAdvancedSecurityBillingGhe");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**AdvancedSecurityActiveCommitters**](AdvancedSecurityActiveCommitters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |

<a id="billingGetGithubAdvancedSecurityBillingOrg"></a>
# **billingGetGithubAdvancedSecurityBillingOrg**
> AdvancedSecurityActiveCommitters billingGetGithubAdvancedSecurityBillingOrg(org, perPage, page)

Get GitHub Advanced Security active committers for an organization

Gets the GitHub Advanced Security active committers for an organization per repository.  Each distinct user login across all repositories is counted as a single Advanced Security seat, so the &#x60;total_advanced_security_committers&#x60; is not the sum of advanced_security_committers for each repository.  If this organization defers to an enterprise for billing, the &#x60;total_advanced_security_committers&#x60; returned from the organization API may include some users that are in more than one organization, so they will only consume a single Advanced Security seat at the enterprise level.  The total number of repositories with committer information is tracked by the &#x60;total_count&#x60; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      AdvancedSecurityActiveCommitters result = apiInstance.billingGetGithubAdvancedSecurityBillingOrg(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingGetGithubAdvancedSecurityBillingOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**AdvancedSecurityActiveCommitters**](AdvancedSecurityActiveCommitters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |

