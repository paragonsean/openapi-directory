# OrganizationsApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugOrganizationsGet**](OrganizationsApi.md#workspaceSlugOrganizationsGet) | **GET** /{workspace_slug}/organizations | List organizations in a workspace |
| [**workspaceSlugOrganizationsOrganizationIdGet**](OrganizationsApi.md#workspaceSlugOrganizationsOrganizationIdGet) | **GET** /{workspace_slug}/organizations/{organization_id} | Get an organization |
| [**workspaceSlugOrganizationsOrganizationIdPut**](OrganizationsApi.md#workspaceSlugOrganizationsOrganizationIdPut) | **PUT** /{workspace_slug}/organizations/{organization_id} | Update an organization |


<a id="workspaceSlugOrganizationsGet"></a>
# **workspaceSlugOrganizationsGet**
> workspaceSlugOrganizationsGet(workspaceSlug, query, page, direction, items, sort)

List organizations in a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String query = "query_example"; // String | 
    String page = "page_example"; // String | 
    String direction = "ASC"; // String | 
    String items = "10"; // String | 
    String sort = "name"; // String | 
    try {
      apiInstance.workspaceSlugOrganizationsGet(workspaceSlug, query, page, direction, items, sort);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#workspaceSlugOrganizationsGet");
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
| **workspaceSlug** | **String**|  | |
| **query** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] [enum: ASC, DESC] |
| **items** | **String**|  | [optional] [enum: 10, 50, 100] |
| **sort** | **String**|  | [optional] [enum: name, website, members_count, employees_count] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugOrganizationsOrganizationIdGet"></a>
# **workspaceSlugOrganizationsOrganizationIdGet**
> workspaceSlugOrganizationsOrganizationIdGet(workspaceSlug, organizationId)

Get an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String organizationId = "organizationId_example"; // String | 
    try {
      apiInstance.workspaceSlugOrganizationsOrganizationIdGet(workspaceSlug, organizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#workspaceSlugOrganizationsOrganizationIdGet");
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
| **workspaceSlug** | **String**|  | |
| **organizationId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugOrganizationsOrganizationIdPut"></a>
# **workspaceSlugOrganizationsOrganizationIdPut**
> workspaceSlugOrganizationsOrganizationIdPut(workspaceSlug, organizationId, organization)

Update an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String organizationId = "organizationId_example"; // String | 
    Organization organization = new Organization(); // Organization | 
    try {
      apiInstance.workspaceSlugOrganizationsOrganizationIdPut(workspaceSlug, organizationId, organization);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#workspaceSlugOrganizationsOrganizationIdPut");
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
| **workspaceSlug** | **String**|  | |
| **organizationId** | **String**|  | |
| **organization** | [**Organization**](Organization.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | organization updated |  -  |
| **403** | forbidden |  -  |
| **422** | deal_closed_date is invalid |  -  |

