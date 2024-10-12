# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignmentsWhoIsBlueprint**](DefaultApi.md#assignmentsWhoIsBlueprint) | **POST** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName}/WhoIsBlueprint |  |


<a id="assignmentsWhoIsBlueprint"></a>
# **assignmentsWhoIsBlueprint**
> WhoIsBlueprintContract assignmentsWhoIsBlueprint(apiVersion, scope, assignmentName)



Get Blueprints service SPN objectId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
    try {
      WhoIsBlueprintContract result = apiInstance.assignmentsWhoIsBlueprint(apiVersion, scope, assignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assignmentsWhoIsBlueprint");
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **assignmentName** | **String**| Name of the blueprint assignment. | |

### Return type

[**WhoIsBlueprintContract**](WhoIsBlueprintContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blueprints service SPN objectId |  -  |

