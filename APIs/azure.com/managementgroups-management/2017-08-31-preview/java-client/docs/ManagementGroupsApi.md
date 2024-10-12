# ManagementGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managementGroupsGet**](ManagementGroupsApi.md#managementGroupsGet) | **GET** /providers/Microsoft.Management/managementGroups/{groupId} |  |
| [**managementGroupsList**](ManagementGroupsApi.md#managementGroupsList) | **GET** /providers/Microsoft.Management/managementGroups |  |


<a id="managementGroupsGet"></a>
# **managementGroupsGet**
> ManagementGroupWithHierarchy managementGroupsGet(groupId, apiVersion, $expand, $recurse)



Get the details of the management group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    UUID groupId = UUID.randomUUID(); // UUID | Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-08-31-preview.
    String $expand = "children"; // String | The $expand=children query string parameter allows clients to request inclusion of children in the response payload.
    Boolean $recurse = true; // Boolean | The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload.
    try {
      ManagementGroupWithHierarchy result = apiInstance.managementGroupsGet(groupId, apiVersion, $expand, $recurse);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsGet");
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
| **groupId** | **UUID**| Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-08-31-preview. | |
| **$expand** | **String**| The $expand&#x3D;children query string parameter allows clients to request inclusion of children in the response payload. | [optional] [enum: children] |
| **$recurse** | **Boolean**| The $recurse&#x3D;true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. | [optional] |

### Return type

[**ManagementGroupWithHierarchy**](ManagementGroupWithHierarchy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="managementGroupsList"></a>
# **managementGroupsList**
> ManagementGroupListResult managementGroupsList(apiVersion, $skiptoken)



List management groups for the authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-08-31-preview.
    String $skiptoken = "$skiptoken_example"; // String | Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
    try {
      ManagementGroupListResult result = apiInstance.managementGroupsList(apiVersion, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-08-31-preview. | |
| **$skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.  | [optional] |

### Return type

[**ManagementGroupListResult**](ManagementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

