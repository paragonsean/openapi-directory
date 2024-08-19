# OrganizationWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organizationDetailsPatchOrganizationDetails**](OrganizationWriteApi.md#organizationDetailsPatchOrganizationDetails) | **PATCH** /v1/organizationdetails | Update (Patch) a organization details or a part of it |


<a id="organizationDetailsPatchOrganizationDetails"></a>
# **organizationDetailsPatchOrganizationDetails**
> OrganizationDetailsOutputModel organizationDetailsPatchOrganizationDetails(patchOperation)

Update (Patch) a organization details or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationWriteApi apiInstance = new OrganizationWriteApi(defaultClient);
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | 
    try {
      OrganizationDetailsOutputModel result = apiInstance.organizationDetailsPatchOrganizationDetails(patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationWriteApi#organizationDetailsPatchOrganizationDetails");
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
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)|  | [optional] |

### Return type

[**OrganizationDetailsOutputModel**](OrganizationDetailsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | organization details |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

