# PolicyAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyAssignmentsCreate**](PolicyAssignmentsApi.md#policyAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} |  |
| [**policyAssignmentsCreateById**](PolicyAssignmentsApi.md#policyAssignmentsCreateById) | **PUT** /{policyAssignmentId} |  |
| [**policyAssignmentsDelete**](PolicyAssignmentsApi.md#policyAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} |  |
| [**policyAssignmentsDeleteById**](PolicyAssignmentsApi.md#policyAssignmentsDeleteById) | **DELETE** /{policyAssignmentId} |  |
| [**policyAssignmentsGet**](PolicyAssignmentsApi.md#policyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} |  |
| [**policyAssignmentsGetById**](PolicyAssignmentsApi.md#policyAssignmentsGetById) | **GET** /{policyAssignmentId} |  |
| [**policyAssignmentsList**](PolicyAssignmentsApi.md#policyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments |  |
| [**policyAssignmentsListForResource**](PolicyAssignmentsApi.md#policyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}providers/Microsoft.Authorization/policyAssignments |  |
| [**policyAssignmentsListForResourceGroup**](PolicyAssignmentsApi.md#policyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments |  |
| [**policyAssignmentsListForScope**](PolicyAssignmentsApi.md#policyAssignmentsListForScope) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments |  |


<a id="policyAssignmentsCreate"></a>
# **policyAssignmentsCreate**
> PolicyAssignment policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters)



Create policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    PolicyAssignment parameters = new PolicyAssignment(); // PolicyAssignment | Policy assignment.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsCreate");
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
| **scope** | **String**| Scope. | |
| **policyAssignmentName** | **String**| Policy assignment name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Policy assignment. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="policyAssignmentsCreateById"></a>
# **policyAssignmentsCreateById**
> PolicyAssignment policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters)



Create policy assignment by Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String policyAssignmentId = "policyAssignmentId_example"; // String | Policy assignment Id
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    PolicyAssignment parameters = new PolicyAssignment(); // PolicyAssignment | Policy assignment.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsCreateById");
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
| **policyAssignmentId** | **String**| Policy assignment Id | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Policy assignment. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="policyAssignmentsDelete"></a>
# **policyAssignmentsDelete**
> PolicyAssignment policyAssignmentsDelete(scope, policyAssignmentName)



Delete policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsDelete(scope, policyAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsDelete");
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
| **scope** | **String**| Scope. | |
| **policyAssignmentName** | **String**| Policy assignment name. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsDeleteById"></a>
# **policyAssignmentsDeleteById**
> PolicyAssignment policyAssignmentsDeleteById(policyAssignmentId, apiVersion)



Delete policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String policyAssignmentId = "policyAssignmentId_example"; // String | Policy assignment Id
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsDeleteById(policyAssignmentId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsDeleteById");
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
| **policyAssignmentId** | **String**| Policy assignment Id | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsGet"></a>
# **policyAssignmentsGet**
> PolicyAssignment policyAssignmentsGet(scope, policyAssignmentName, apiVersion)



Get single policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsGet(scope, policyAssignmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsGet");
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
| **scope** | **String**| Scope. | |
| **policyAssignmentName** | **String**| Policy assignment name. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsGetById"></a>
# **policyAssignmentsGetById**
> PolicyAssignment policyAssignmentsGetById(policyAssignmentId, apiVersion)



Get single policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String policyAssignmentId = "policyAssignmentId_example"; // String | Policy assignment Id
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsGetById(policyAssignmentId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsGetById");
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
| **policyAssignmentId** | **String**| Policy assignment Id | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsList"></a>
# **policyAssignmentsList**
> PolicyAssignmentListResult policyAssignmentsList(apiVersion, subscriptionId, $filter)



Gets policy assignments of the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsList(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsListForResource"></a>
# **policyAssignmentsListForResource**
> PolicyAssignmentListResult policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter)



Gets policy assignments of the resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The name of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource path.
    String resourceType = "resourceType_example"; // String | The resource type.
    String resourceName = "resourceName_example"; // String | The resource name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsListForResource");
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
| **resourceProviderNamespace** | **String**| The name of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource path. | |
| **resourceType** | **String**| The resource type. | |
| **resourceName** | **String**| The resource name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsListForResourceGroup"></a>
# **policyAssignmentsListForResourceGroup**
> PolicyAssignmentListResult policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter)



Gets policy assignments of the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsListForResourceGroup");
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
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyAssignmentsListForScope"></a>
# **policyAssignmentsListForScope**
> PolicyAssignmentListResult policyAssignmentsListForScope(scope, apiVersion, $filter)



Gets policy assignments of the scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsListForScope(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsListForScope");
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
| **scope** | **String**| Scope. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

