# GuestDiagnosticsSettingsAssociationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**guestDiagnosticsSettingsAssociationCreateOrUpdate**](GuestDiagnosticsSettingsAssociationApi.md#guestDiagnosticsSettingsAssociationCreateOrUpdate) | **PUT** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} |  |
| [**guestDiagnosticsSettingsAssociationDelete**](GuestDiagnosticsSettingsAssociationApi.md#guestDiagnosticsSettingsAssociationDelete) | **DELETE** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} |  |
| [**guestDiagnosticsSettingsAssociationGet**](GuestDiagnosticsSettingsAssociationApi.md#guestDiagnosticsSettingsAssociationGet) | **GET** /{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName} |  |


<a id="guestDiagnosticsSettingsAssociationCreateOrUpdate"></a>
# **guestDiagnosticsSettingsAssociationCreateOrUpdate**
> GuestDiagnosticSettingsAssociationResource guestDiagnosticsSettingsAssociationCreateOrUpdate(resourceUri, associationName, apiVersion, diagnosticSettingsAssociation)



Creates or updates guest diagnostics settings association.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestDiagnosticsSettingsAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GuestDiagnosticsSettingsAssociationApi apiInstance = new GuestDiagnosticsSettingsAssociationApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
    String associationName = "associationName_example"; // String | The name of the diagnostic settings association.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GuestDiagnosticSettingsAssociationResource diagnosticSettingsAssociation = new GuestDiagnosticSettingsAssociationResource(); // GuestDiagnosticSettingsAssociationResource | The diagnostic settings association to create or update.
    try {
      GuestDiagnosticSettingsAssociationResource result = apiInstance.guestDiagnosticsSettingsAssociationCreateOrUpdate(resourceUri, associationName, apiVersion, diagnosticSettingsAssociation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestDiagnosticsSettingsAssociationApi#guestDiagnosticsSettingsAssociationCreateOrUpdate");
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
| **associationName** | **String**| The name of the diagnostic settings association. | |
| **apiVersion** | **String**| Client Api Version. | |
| **diagnosticSettingsAssociation** | [**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)| The diagnostic settings association to create or update. | |

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
| **200** | An existing guest diagnostic settings association was successfully updated. |  -  |
| **201** | A new guest diagnostic settings association was successfully created. |  -  |
| **0** | An error occurred and the guest diagnostic settings association could not be created or updated. |  -  |

<a id="guestDiagnosticsSettingsAssociationDelete"></a>
# **guestDiagnosticsSettingsAssociationDelete**
> guestDiagnosticsSettingsAssociationDelete(resourceUri, associationName, apiVersion)



Delete guest diagnostics association settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestDiagnosticsSettingsAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GuestDiagnosticsSettingsAssociationApi apiInstance = new GuestDiagnosticsSettingsAssociationApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
    String associationName = "associationName_example"; // String | The name of the diagnostic settings association.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.guestDiagnosticsSettingsAssociationDelete(resourceUri, associationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestDiagnosticsSettingsAssociationApi#guestDiagnosticsSettingsAssociationDelete");
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
| **associationName** | **String**| The name of the diagnostic settings association. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The diagnostic settings association was successfully deleted. |  -  |
| **204** | The diagnostic settings association does not exist. It may have already been deleted. |  -  |
| **0** | An error occurred and the diagnostic settings association could not be deleted. |  -  |

<a id="guestDiagnosticsSettingsAssociationGet"></a>
# **guestDiagnosticsSettingsAssociationGet**
> GuestDiagnosticSettingsAssociationResource guestDiagnosticsSettingsAssociationGet(resourceUri, associationName, apiVersion)



Gets guest diagnostics association settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestDiagnosticsSettingsAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GuestDiagnosticsSettingsAssociationApi apiInstance = new GuestDiagnosticsSettingsAssociationApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type.
    String associationName = "associationName_example"; // String | The name of the diagnostic settings association.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GuestDiagnosticSettingsAssociationResource result = apiInstance.guestDiagnosticsSettingsAssociationGet(resourceUri, associationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestDiagnosticsSettingsAssociationApi#guestDiagnosticsSettingsAssociationGet");
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
| **associationName** | **String**| The name of the diagnostic settings association. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GuestDiagnosticSettingsAssociationResource**](GuestDiagnosticSettingsAssociationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the diagnostic settings association could not be retrieved. |  -  |

