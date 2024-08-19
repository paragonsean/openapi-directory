# EntitlementsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnOrganizationsEntitlementValue**](EntitlementsApi.md#getAnOrganizationsEntitlementValue) | **GET** /org/{orgId}/entitlement/{entitlementKey} | Get an organization&#39;s entitlement value |
| [**listAllEntitlements**](EntitlementsApi.md#listAllEntitlements) | **GET** /org/{orgId}/entitlements | List all entitlements |


<a id="getAnOrganizationsEntitlementValue"></a>
# **getAnOrganizationsEntitlementValue**
> getAnOrganizationsEntitlementValue(orgId, entitlementKey)

Get an organization&#39;s entitlement value



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitlementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    EntitlementsApi apiInstance = new EntitlementsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to query the entitlement for. The `API_KEY` must have access to this organization.
    String entitlementKey = "licenses"; // String | The entitlement to query.
    try {
      apiInstance.getAnOrganizationsEntitlementValue(orgId, entitlementKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitlementsApi#getAnOrganizationsEntitlementValue");
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
| **orgId** | **String**| The organization ID to query the entitlement for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **entitlementKey** | **String**| The entitlement to query. | [enum: licenses, reports, fullVulnDB] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllEntitlements"></a>
# **listAllEntitlements**
> listAllEntitlements(orgId)

List all entitlements



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitlementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    EntitlementsApi apiInstance = new EntitlementsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list entitlements for. The `API_KEY` must have access to this organization.
    try {
      apiInstance.listAllEntitlements(orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitlementsApi#listAllEntitlements");
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
| **orgId** | **String**| The organization ID to list entitlements for. The &#x60;API_KEY&#x60; must have access to this organization. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

