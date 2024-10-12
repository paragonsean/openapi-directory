# UpdateRunsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateRunsGet**](UpdateRunsApi.md#updateRunsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updates/{updateName}/updateRuns/{runName} |  |
| [**updateRunsGetTopLevel**](UpdateRunsApi.md#updateRunsGetTopLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updateRuns/{runName} |  |
| [**updateRunsList**](UpdateRunsApi.md#updateRunsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updates/{updateName}/updateRuns |  |
| [**updateRunsListTopLevel**](UpdateRunsApi.md#updateRunsListTopLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updateRuns |  |
| [**updateRunsRerun**](UpdateRunsApi.md#updateRunsRerun) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updates/{updateName}/updateRuns/{runName}/rerun |  |


<a id="updateRunsGet"></a>
# **updateRunsGet**
> UpdateRun updateRunsGet(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion)



Get an instance of update run using the ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateRunsApi apiInstance = new UpdateRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String updateLocation = "updateLocation_example"; // String | The name of the update location.
    String updateName = "updateName_example"; // String | Name of the update.
    String runName = "runName_example"; // String | Update run identifier.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      UpdateRun result = apiInstance.updateRunsGet(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateRunsApi#updateRunsGet");
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
| **updateName** | **String**| Name of the update. | |
| **runName** | **String**| Update run identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**UpdateRun**](UpdateRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRunsGetTopLevel"></a>
# **updateRunsGetTopLevel**
> UpdateRun updateRunsGetTopLevel(subscriptionId, resourceGroupName, updateLocation, runName, apiVersion)



Get an instance of update run using the ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateRunsApi apiInstance = new UpdateRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String updateLocation = "updateLocation_example"; // String | The name of the update location.
    String runName = "runName_example"; // String | Update run identifier.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      UpdateRun result = apiInstance.updateRunsGetTopLevel(subscriptionId, resourceGroupName, updateLocation, runName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateRunsApi#updateRunsGetTopLevel");
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
| **runName** | **String**| Update run identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**UpdateRun**](UpdateRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRunsList"></a>
# **updateRunsList**
> UpdateRunList updateRunsList(subscriptionId, resourceGroupName, updateLocation, updateName, apiVersion)



Get the list of update runs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateRunsApi apiInstance = new UpdateRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String updateLocation = "updateLocation_example"; // String | The name of the update location.
    String updateName = "updateName_example"; // String | Name of the update.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      UpdateRunList result = apiInstance.updateRunsList(subscriptionId, resourceGroupName, updateLocation, updateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateRunsApi#updateRunsList");
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
| **updateName** | **String**| Name of the update. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**UpdateRunList**](UpdateRunList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRunsListTopLevel"></a>
# **updateRunsListTopLevel**
> UpdateRunList updateRunsListTopLevel(subscriptionId, resourceGroupName, updateLocation, apiVersion)



Get the list of update runs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateRunsApi apiInstance = new UpdateRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String updateLocation = "updateLocation_example"; // String | The name of the update location.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      UpdateRunList result = apiInstance.updateRunsListTopLevel(subscriptionId, resourceGroupName, updateLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateRunsApi#updateRunsListTopLevel");
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

[**UpdateRunList**](UpdateRunList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRunsRerun"></a>
# **updateRunsRerun**
> updateRunsRerun(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion)



Resume a failed update.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UpdateRunsApi apiInstance = new UpdateRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String updateLocation = "updateLocation_example"; // String | The name of the update location.
    String updateName = "updateName_example"; // String | Name of the update.
    String runName = "runName_example"; // String | Update run identifier.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.updateRunsRerun(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateRunsApi#updateRunsRerun");
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
| **updateName** | **String**| Name of the update. | |
| **runName** | **String**| Update run identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

