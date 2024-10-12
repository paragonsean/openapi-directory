# RegistrationDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registrationDefinitionsCreateOrUpdate**](RegistrationDefinitionsApi.md#registrationDefinitionsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registrationDefinitionId} |  |
| [**registrationDefinitionsDelete**](RegistrationDefinitionsApi.md#registrationDefinitionsDelete) | **DELETE** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registrationDefinitionId} |  |
| [**registrationDefinitionsGet**](RegistrationDefinitionsApi.md#registrationDefinitionsGet) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registrationDefinitionId} |  |
| [**registrationDefinitionsList**](RegistrationDefinitionsApi.md#registrationDefinitionsList) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions |  |


<a id="registrationDefinitionsCreateOrUpdate"></a>
# **registrationDefinitionsCreateOrUpdate**
> RegistrationDefinition registrationDefinitionsCreateOrUpdate(registrationDefinitionId, apiVersion, scope, requestBody)



Creates or updates a registration definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationDefinitionsApi apiInstance = new RegistrationDefinitionsApi(defaultClient);
    String registrationDefinitionId = "registrationDefinitionId_example"; // String | Guid of the registration definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scope = "scope_example"; // String | Scope of the resource.
    RegistrationDefinition requestBody = new RegistrationDefinition(); // RegistrationDefinition | The parameters required to create new registration definition.
    try {
      RegistrationDefinition result = apiInstance.registrationDefinitionsCreateOrUpdate(registrationDefinitionId, apiVersion, scope, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationDefinitionsApi#registrationDefinitionsCreateOrUpdate");
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
| **registrationDefinitionId** | **String**| Guid of the registration definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scope** | **String**| Scope of the resource. | |
| **requestBody** | [**RegistrationDefinition**](RegistrationDefinition.md)| The parameters required to create new registration definition. | |

### Return type

[**RegistrationDefinition**](RegistrationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok - Returns information about the updated registration definition. |  -  |
| **201** | Created - Returns information about the created registration definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationDefinitionsDelete"></a>
# **registrationDefinitionsDelete**
> registrationDefinitionsDelete(registrationDefinitionId, apiVersion, scope)



Deletes the registration definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationDefinitionsApi apiInstance = new RegistrationDefinitionsApi(defaultClient);
    String registrationDefinitionId = "registrationDefinitionId_example"; // String | Guid of the registration definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scope = "scope_example"; // String | Scope of the resource.
    try {
      apiInstance.registrationDefinitionsDelete(registrationDefinitionId, apiVersion, scope);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationDefinitionsApi#registrationDefinitionsDelete");
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
| **registrationDefinitionId** | **String**| Guid of the registration definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scope** | **String**| Scope of the resource. | |

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
| **200** | OK - The registration definition is deleted. |  -  |
| **204** | No Content- The registration definition does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationDefinitionsGet"></a>
# **registrationDefinitionsGet**
> RegistrationDefinition registrationDefinitionsGet(scope, registrationDefinitionId, apiVersion)



Gets the registration definition details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationDefinitionsApi apiInstance = new RegistrationDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String registrationDefinitionId = "registrationDefinitionId_example"; // String | Guid of the registration definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RegistrationDefinition result = apiInstance.registrationDefinitionsGet(scope, registrationDefinitionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationDefinitionsApi#registrationDefinitionsGet");
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
| **scope** | **String**| Scope of the resource. | |
| **registrationDefinitionId** | **String**| Guid of the registration definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RegistrationDefinition**](RegistrationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the complete registration definition with plan details. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationDefinitionsList"></a>
# **registrationDefinitionsList**
> RegistrationDefinitionList registrationDefinitionsList(scope, apiVersion)



Gets a list of the registration definitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationDefinitionsApi apiInstance = new RegistrationDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RegistrationDefinitionList result = apiInstance.registrationDefinitionsList(scope, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationDefinitionsApi#registrationDefinitionsList");
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
| **scope** | **String**| Scope of the resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RegistrationDefinitionList**](RegistrationDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns a list of the registration definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

