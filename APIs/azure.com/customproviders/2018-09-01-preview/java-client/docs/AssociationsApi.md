# AssociationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associationsCreateOrUpdate**](AssociationsApi.md#associationsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.CustomProviders/associations/{associationName} |  |
| [**associationsDelete**](AssociationsApi.md#associationsDelete) | **DELETE** /{scope}/providers/Microsoft.CustomProviders/associations/{associationName} |  |
| [**associationsGet**](AssociationsApi.md#associationsGet) | **GET** /{scope}/providers/Microsoft.CustomProviders/associations/{associationName} |  |
| [**associationsListAll**](AssociationsApi.md#associationsListAll) | **GET** /{scope}/providers/Microsoft.CustomProviders/associations |  |


<a id="associationsCreateOrUpdate"></a>
# **associationsCreateOrUpdate**
> Association associationsCreateOrUpdate(scope, associationName, apiVersion, association)



Create or update an association.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssociationsApi apiInstance = new AssociationsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.
    String associationName = "associationName_example"; // String | The name of the association.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    Association association = new Association(); // Association | The parameters required to create or update an association.
    try {
      Association result = apiInstance.associationsCreateOrUpdate(scope, associationName, apiVersion, association);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationsApi#associationsCreateOrUpdate");
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
| **scope** | **String**| The scope of the association. The scope can be any valid REST resource instance. For example, use &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}&#39; for a virtual machine resource. | |
| **associationName** | **String**| The name of the association. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **association** | [**Association**](Association.md)| The parameters required to create or update an association. | |

### Return type

[**Association**](Association.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Association already exists and the changes have been accepted. |  -  |
| **201** | Created. Association has been created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="associationsDelete"></a>
# **associationsDelete**
> associationsDelete(scope, associationName, apiVersion)



Delete an association.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssociationsApi apiInstance = new AssociationsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the association.
    String associationName = "associationName_example"; // String | The name of the association.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      apiInstance.associationsDelete(scope, associationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationsApi#associationsDelete");
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
| **scope** | **String**| The scope of the association. | |
| **associationName** | **String**| The name of the association. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

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
| **200** | OK. Association deleted. |  -  |
| **202** | Accepted. Association delete has been accepted. |  -  |
| **204** | No Content. Association was not found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="associationsGet"></a>
# **associationsGet**
> Association associationsGet(scope, associationName, apiVersion)



Get an association.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssociationsApi apiInstance = new AssociationsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the association.
    String associationName = "associationName_example"; // String | The name of the association.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      Association result = apiInstance.associationsGet(scope, associationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationsApi#associationsGet");
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
| **scope** | **String**| The scope of the association. | |
| **associationName** | **String**| The name of the association. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**Association**](Association.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns association. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="associationsListAll"></a>
# **associationsListAll**
> AssociationsList associationsListAll(scope, apiVersion)



Gets all association for the given scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssociationsApi apiInstance = new AssociationsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the association.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      AssociationsList result = apiInstance.associationsListAll(scope, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationsApi#associationsListAll");
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
| **scope** | **String**| The scope of the association. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**AssociationsList**](AssociationsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns all associations for the given scope. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

