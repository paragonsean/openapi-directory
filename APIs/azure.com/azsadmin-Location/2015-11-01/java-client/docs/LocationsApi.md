# LocationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsCreateOrUpdate**](LocationsApi.md#locationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations/{location} |  |
| [**locationsGet**](LocationsApi.md#locationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations/{location} |  |
| [**locationsGetOperationsStatus**](LocationsApi.md#locationsGetOperationsStatus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations/{location}/operationsStatus/{operationsStatusName} |  |
| [**locationsList**](LocationsApi.md#locationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations |  |


<a id="locationsCreateOrUpdate"></a>
# **locationsCreateOrUpdate**
> Location locationsCreateOrUpdate(subscriptionId, location, apiVersion, newLocation)



Updates the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The AzureStack location.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    Location newLocation = new Location(); // Location | The new location
    try {
      Location result = apiInstance.locationsCreateOrUpdate(subscriptionId, location, apiVersion, newLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| The AzureStack location. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |
| **newLocation** | [**Location**](Location.md)| The new location | |

### Return type

[**Location**](Location.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="locationsGet"></a>
# **locationsGet**
> Location locationsGet(subscriptionId, location, apiVersion)



Get the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The AzureStack location.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      Location result = apiInstance.locationsGet(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| The AzureStack location. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**Location**](Location.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="locationsGetOperationsStatus"></a>
# **locationsGetOperationsStatus**
> OperationsStatus locationsGetOperationsStatus(subscriptionId, location, operationsStatusName, apiVersion)



Get the operation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The AzureStack location.
    String operationsStatusName = "operationsStatusName_example"; // String | The operation status name.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      OperationsStatus result = apiInstance.locationsGetOperationsStatus(subscriptionId, location, operationsStatusName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsGetOperationsStatus");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| The AzureStack location. | |
| **operationsStatusName** | **String**| The operation status name. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**OperationsStatus**](OperationsStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | Not Content |  -  |
| **404** | Not Found |  -  |

<a id="locationsList"></a>
# **locationsList**
> LocationList locationsList(subscriptionId, apiVersion)



Get a list of all AzureStack location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      LocationList result = apiInstance.locationsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**LocationList**](LocationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

