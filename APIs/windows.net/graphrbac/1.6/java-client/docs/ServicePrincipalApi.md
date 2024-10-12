# ServicePrincipalApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicePrincipalsCreate**](ServicePrincipalApi.md#servicePrincipalsCreate) | **POST** /{tenantID}/servicePrincipals |  |
| [**servicePrincipalsDelete**](ServicePrincipalApi.md#servicePrincipalsDelete) | **DELETE** /{tenantID}/servicePrincipals/{objectId} |  |
| [**servicePrincipalsGet**](ServicePrincipalApi.md#servicePrincipalsGet) | **GET** /{tenantID}/servicePrincipals/{objectId} |  |
| [**servicePrincipalsList**](ServicePrincipalApi.md#servicePrincipalsList) | **GET** /{tenantID}/servicePrincipals |  |
| [**servicePrincipalsUpdate**](ServicePrincipalApi.md#servicePrincipalsUpdate) | **PATCH** /{tenantID}/servicePrincipals/{objectId} |  |


<a id="servicePrincipalsCreate"></a>
# **servicePrincipalsCreate**
> ServicePrincipal servicePrincipalsCreate(apiVersion, tenantID, servicePrincipalCreateParameters)



Creates a service principal in the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalApi apiInstance = new ServicePrincipalApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    ServicePrincipalCreateParameters servicePrincipalCreateParameters = new ServicePrincipalCreateParameters(); // ServicePrincipalCreateParameters | Parameters to create a service principal.
    try {
      ServicePrincipal result = apiInstance.servicePrincipalsCreate(apiVersion, tenantID, servicePrincipalCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalApi#servicePrincipalsCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **servicePrincipalCreateParameters** | [**ServicePrincipalCreateParameters**](ServicePrincipalCreateParameters.md)| Parameters to create a service principal. | |

### Return type

[**ServicePrincipal**](ServicePrincipal.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The service principal was created successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="servicePrincipalsDelete"></a>
# **servicePrincipalsDelete**
> servicePrincipalsDelete(objectId, apiVersion, tenantID)



Deletes a service principal from the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalApi apiInstance = new ServicePrincipalApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal to delete.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.servicePrincipalsDelete(objectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalApi#servicePrincipalsDelete");
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
| **objectId** | **String**| The object ID of the service principal to delete. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="servicePrincipalsGet"></a>
# **servicePrincipalsGet**
> ServicePrincipal servicePrincipalsGet(objectId, apiVersion, tenantID)



Gets service principal information from the directory. Query by objectId or pass a filter to query by appId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalApi apiInstance = new ServicePrincipalApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal to get.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      ServicePrincipal result = apiInstance.servicePrincipalsGet(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalApi#servicePrincipalsGet");
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
| **objectId** | **String**| The object ID of the service principal to get. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**ServicePrincipal**](ServicePrincipal.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="servicePrincipalsList"></a>
# **servicePrincipalsList**
> ServicePrincipalListResult servicePrincipalsList(apiVersion, tenantID, $filter)



Gets a list of service principals from the current tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalApi apiInstance = new ServicePrincipalApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    try {
      ServicePrincipalListResult result = apiInstance.servicePrincipalsList(apiVersion, tenantID, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalApi#servicePrincipalsList");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |

### Return type

[**ServicePrincipalListResult**](ServicePrincipalListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="servicePrincipalsUpdate"></a>
# **servicePrincipalsUpdate**
> servicePrincipalsUpdate(objectId, apiVersion, tenantID, servicePrincipalUpdateParameters)



Updates a service principal in the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalApi apiInstance = new ServicePrincipalApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal to delete.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    ServicePrincipalUpdateParameters servicePrincipalUpdateParameters = new ServicePrincipalUpdateParameters(); // ServicePrincipalUpdateParameters | Parameters to update a service principal.
    try {
      apiInstance.servicePrincipalsUpdate(objectId, apiVersion, tenantID, servicePrincipalUpdateParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalApi#servicePrincipalsUpdate");
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
| **objectId** | **String**| The object ID of the service principal to delete. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **servicePrincipalUpdateParameters** | [**ServicePrincipalUpdateParameters**](ServicePrincipalUpdateParameters.md)| Parameters to update a service principal. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

