# UpdateLocationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateLocationsGet**](UpdateLocationsApi.md#updateLocationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation} |  |
| [**updateLocationsList**](UpdateLocationsApi.md#updateLocationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/ |  |


<a id="updateLocationsGet"></a>
# **updateLocationsGet**
> UpdateLocation updateLocationsGet(subscriptionId, resourceGroupName, updateLocation, apiVersion)



Get an update location based on name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateLocationsApi apiInstance = new UpdateLocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String updateLocation = "updateLocation_example"; // String | The name of the update location.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      UpdateLocation result = apiInstance.updateLocationsGet(subscriptionId, resourceGroupName, updateLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateLocationsApi#updateLocationsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **updateLocation** | **String**| The name of the update location. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**UpdateLocation**](UpdateLocation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateLocationsList"></a>
# **updateLocationsList**
> UpdateLocationList updateLocationsList(subscriptionId, resourceGroupName, apiVersion)



Get the list of update locations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateLocationsApi apiInstance = new UpdateLocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      UpdateLocationList result = apiInstance.updateLocationsList(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateLocationsApi#updateLocationsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**UpdateLocationList**](UpdateLocationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

