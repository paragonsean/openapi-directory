# ManagementGroupsDescendantsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managementGroupsGetDescendants**](ManagementGroupsDescendantsApi.md#managementGroupsGetDescendants) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/descendants |  |


<a id="managementGroupsGetDescendants"></a>
# **managementGroupsGetDescendants**
> DescendantListResult managementGroupsGetDescendants(groupId, apiVersion, $skiptoken, $top)



List all entities that descend from a management group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsDescendantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsDescendantsApi apiInstance = new ManagementGroupsDescendantsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    String $skiptoken = "$skiptoken_example"; // String | Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | Number of elements to return when retrieving results. Passing this in will override $skipToken.
    try {
      DescendantListResult result = apiInstance.managementGroupsGetDescendants(groupId, apiVersion, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsDescendantsApi#managementGroupsGetDescendants");
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
| **groupId** | **String**| Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | |
| **$skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| Number of elements to return when retrieving results. Passing this in will override $skipToken. | [optional] |

### Return type

[**DescendantListResult**](DescendantListResult.md)

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

