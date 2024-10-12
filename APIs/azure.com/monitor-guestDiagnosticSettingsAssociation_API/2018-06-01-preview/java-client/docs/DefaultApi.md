# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**guestDiagnosticsSettingsAssociationList**](DefaultApi.md#guestDiagnosticsSettingsAssociationList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/guestDiagnosticSettingsAssociations |  |
| [**guestDiagnosticsSettingsAssociationListByResourceGroup**](DefaultApi.md#guestDiagnosticsSettingsAssociationListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/guestDiagnosticSettingsAssociations |  |
| [**guestDiagnosticsSettingsAssociationUpdate**](DefaultApi.md#guestDiagnosticsSettingsAssociationUpdate) | **PATCH** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} |  |


<a id="guestDiagnosticsSettingsAssociationList"></a>
# **guestDiagnosticsSettingsAssociationList**
> GuestDiagnosticSettingsAssociationList guestDiagnosticsSettingsAssociationList(subscriptionId, apiVersion)



Get a list of all guest diagnostic settings association in a subscription.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GuestDiagnosticSettingsAssociationList result = apiInstance.guestDiagnosticsSettingsAssociationList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#guestDiagnosticsSettingsAssociationList");
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GuestDiagnosticSettingsAssociationList**](GuestDiagnosticSettingsAssociationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the list of guest diagnostic settings association could not be retrieved. |  -  |

<a id="guestDiagnosticsSettingsAssociationListByResourceGroup"></a>
# **guestDiagnosticsSettingsAssociationListByResourceGroup**
> GuestDiagnosticSettingsAssociationList guestDiagnosticsSettingsAssociationListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Get a list of all guest diagnostic settings association in a resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GuestDiagnosticSettingsAssociationList result = apiInstance.guestDiagnosticsSettingsAssociationListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#guestDiagnosticsSettingsAssociationListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GuestDiagnosticSettingsAssociationList**](GuestDiagnosticSettingsAssociationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the list of guest diagnostic settings association could not be retrieved. |  -  |

<a id="guestDiagnosticsSettingsAssociationUpdate"></a>
# **guestDiagnosticsSettingsAssociationUpdate**
> GuestDiagnosticSettingsAssociationResource guestDiagnosticsSettingsAssociationUpdate(resourceUri, apiVersion, associationName, parameters)



Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use the CreateOrUpdate method

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
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String associationName = "associationName_example"; // String | The name of the diagnostic settings association.
    GuestDiagnosticSettingsAssociationResourcePatch parameters = new GuestDiagnosticSettingsAssociationResourcePatch(); // GuestDiagnosticSettingsAssociationResourcePatch | Parameters supplied to the operation.
    try {
      GuestDiagnosticSettingsAssociationResource result = apiInstance.guestDiagnosticsSettingsAssociationUpdate(resourceUri, apiVersion, associationName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#guestDiagnosticsSettingsAssociationUpdate");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. | |
| **apiVersion** | **String**| Client Api Version. | |
| **associationName** | **String**| The name of the diagnostic settings association. | |
| **parameters** | [**GuestDiagnosticSettingsAssociationResourcePatch**](GuestDiagnosticSettingsAssociationResourcePatch.md)| Parameters supplied to the operation. | |

### Return type

[**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing guest diagnostics setting resource was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

