# DeployedBranchApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSiteDeployedBranches**](DeployedBranchApi.md#listSiteDeployedBranches) | **GET** /sites/{site_id}/deployed-branches |  |


<a id="listSiteDeployedBranches"></a>
# **listSiteDeployedBranches**
> List&lt;DeployedBranch&gt; listSiteDeployedBranches(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployedBranchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployedBranchApi apiInstance = new DeployedBranchApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<DeployedBranch> result = apiInstance.listSiteDeployedBranches(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployedBranchApi#listSiteDeployedBranches");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;DeployedBranch&gt;**](DeployedBranch.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

