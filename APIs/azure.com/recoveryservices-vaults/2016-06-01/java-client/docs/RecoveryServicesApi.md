# RecoveryServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recoveryServicesCheckNameAvailability**](RecoveryServicesApi.md#recoveryServicesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/locations/{location}/checkNameAvailability | API to check for resource name availability.  A name is available if no other resource exists that has the same SubscriptionId, Resource Name and Type  or if one or more such resources exist, each of these must be GC&#39;d and their time of deletion be more than 24 Hours Ago |


<a id="recoveryServicesCheckNameAvailability"></a>
# **recoveryServicesCheckNameAvailability**
> CheckNameAvailabilityResultResource recoveryServicesCheckNameAvailability(subscriptionId, resourceGroupName, apiVersion, location, input)

API to check for resource name availability.  A name is available if no other resource exists that has the same SubscriptionId, Resource Name and Type  or if one or more such resources exist, each of these must be GC&#39;d and their time of deletion be more than 24 Hours Ago

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecoveryServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecoveryServicesApi apiInstance = new RecoveryServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String location = "location_example"; // String | Location of the resource
    CheckNameAvailabilityParameters input = new CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Contains information about Resource type and Resource name
    try {
      CheckNameAvailabilityResultResource result = apiInstance.recoveryServicesCheckNameAvailability(subscriptionId, resourceGroupName, apiVersion, location, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecoveryServicesApi#recoveryServicesCheckNameAvailability");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **apiVersion** | **String**| Client Api Version. | |
| **location** | **String**| Location of the resource | |
| **input** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Contains information about Resource type and Resource name | |

### Return type

[**CheckNameAvailabilityResultResource**](CheckNameAvailabilityResultResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

