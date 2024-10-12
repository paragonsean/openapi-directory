# CompanyRoleRoleIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyRoleRepositoryV1DeleteDelete**](CompanyRoleRoleIdApi.md#companyRoleRepositoryV1DeleteDelete) | **DELETE** /V1/company/role/{roleId} | company/role/{roleId} |
| [**companyRoleRepositoryV1GetGet**](CompanyRoleRoleIdApi.md#companyRoleRepositoryV1GetGet) | **GET** /V1/company/role/{roleId} | company/role/{roleId} |


<a id="companyRoleRepositoryV1DeleteDelete"></a>
# **companyRoleRepositoryV1DeleteDelete**
> Boolean companyRoleRepositoryV1DeleteDelete(roleId)

company/role/{roleId}

Delete a role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyRoleRoleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyRoleRoleIdApi apiInstance = new CompanyRoleRoleIdApi(defaultClient);
    Integer roleId = 56; // Integer | 
    try {
      Boolean result = apiInstance.companyRoleRepositoryV1DeleteDelete(roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyRoleRoleIdApi#companyRoleRepositoryV1DeleteDelete");
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
| **roleId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="companyRoleRepositoryV1GetGet"></a>
# **companyRoleRepositoryV1GetGet**
> CompanyDataRoleInterface companyRoleRepositoryV1GetGet(roleId)

company/role/{roleId}

Returns the list of permissions for a specified role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyRoleRoleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyRoleRoleIdApi apiInstance = new CompanyRoleRoleIdApi(defaultClient);
    Integer roleId = 56; // Integer | 
    try {
      CompanyDataRoleInterface result = apiInstance.companyRoleRepositoryV1GetGet(roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyRoleRoleIdApi#companyRoleRepositoryV1GetGet");
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
| **roleId** | **Integer**|  | |

### Return type

[**CompanyDataRoleInterface**](CompanyDataRoleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

