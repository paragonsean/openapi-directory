# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logProfilesUpdate**](DefaultApi.md#logProfilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} |  |


<a id="logProfilesUpdate"></a>
# **logProfilesUpdate**
> LogProfileResource logProfilesUpdate(subscriptionId, logProfileName, apiVersion, logProfilesResource)



Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String logProfileName = "logProfileName_example"; // String | The name of the log profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    LogProfileResourcePatch logProfilesResource = new LogProfileResourcePatch(); // LogProfileResourcePatch | Parameters supplied to the operation.
    try {
      LogProfileResource result = apiInstance.logProfilesUpdate(subscriptionId, logProfileName, apiVersion, logProfilesResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#logProfilesUpdate");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **logProfileName** | **String**| The name of the log profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **logProfilesResource** | [**LogProfileResourcePatch**](LogProfileResourcePatch.md)| Parameters supplied to the operation. | |

### Return type

[**LogProfileResource**](LogProfileResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing log profile was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

