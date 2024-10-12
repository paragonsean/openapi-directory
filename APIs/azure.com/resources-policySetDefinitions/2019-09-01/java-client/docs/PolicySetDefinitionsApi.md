# PolicySetDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policySetDefinitionsCreateOrUpdate**](PolicySetDefinitionsApi.md#policySetDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Creates or updates a policy set definition. |
| [**policySetDefinitionsCreateOrUpdateAtManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsCreateOrUpdateAtManagementGroup) | **PUT** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Creates or updates a policy set definition. |
| [**policySetDefinitionsDelete**](PolicySetDefinitionsApi.md#policySetDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Deletes a policy set definition. |
| [**policySetDefinitionsDeleteAtManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsDeleteAtManagementGroup) | **DELETE** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Deletes a policy set definition. |
| [**policySetDefinitionsGet**](PolicySetDefinitionsApi.md#policySetDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Retrieves a policy set definition. |
| [**policySetDefinitionsGetAtManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsGetAtManagementGroup) | **GET** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Retrieves a policy set definition. |
| [**policySetDefinitionsGetBuiltIn**](PolicySetDefinitionsApi.md#policySetDefinitionsGetBuiltIn) | **GET** /providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | Retrieves a built in policy set definition. |
| [**policySetDefinitionsList**](PolicySetDefinitionsApi.md#policySetDefinitionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions | Retrieves the policy set definitions for a subscription. |
| [**policySetDefinitionsListBuiltIn**](PolicySetDefinitionsApi.md#policySetDefinitionsListBuiltIn) | **GET** /providers/Microsoft.Authorization/policySetDefinitions | Retrieves built-in policy set definitions. |
| [**policySetDefinitionsListByManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsListByManagementGroup) | **GET** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions | Retrieves all policy set definitions in management group. |


<a id="policySetDefinitionsCreateOrUpdate"></a>
# **policySetDefinitionsCreateOrUpdate**
> PolicySetDefinition policySetDefinitionsCreateOrUpdate(policySetDefinitionName, apiVersion, subscriptionId, parameters)

Creates or updates a policy set definition.

This operation creates or updates a policy set definition in the given subscription with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to create.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    PolicySetDefinition parameters = new PolicySetDefinition(); // PolicySetDefinition | The policy set definition properties.
    try {
      PolicySetDefinition result = apiInstance.policySetDefinitionsCreateOrUpdate(policySetDefinitionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsCreateOrUpdate");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to create. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**PolicySetDefinition**](PolicySetDefinition.md)| The policy set definition properties. | |

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy set definition. |  -  |
| **201** | Created - Returns information about the policy set definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsCreateOrUpdateAtManagementGroup"></a>
# **policySetDefinitionsCreateOrUpdateAtManagementGroup**
> PolicySetDefinition policySetDefinitionsCreateOrUpdateAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId, parameters)

Creates or updates a policy set definition.

This operation creates or updates a policy set definition in the given management group with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to create.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
    PolicySetDefinition parameters = new PolicySetDefinition(); // PolicySetDefinition | The policy set definition properties.
    try {
      PolicySetDefinition result = apiInstance.policySetDefinitionsCreateOrUpdateAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsCreateOrUpdateAtManagementGroup");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to create. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **managementGroupId** | **String**| The ID of the management group. | |
| **parameters** | [**PolicySetDefinition**](PolicySetDefinition.md)| The policy set definition properties. | |

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy set definition. |  -  |
| **201** | Created - Returns information about the policy set definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsDelete"></a>
# **policySetDefinitionsDelete**
> policySetDefinitionsDelete(policySetDefinitionName, apiVersion, subscriptionId)

Deletes a policy set definition.

This operation deletes the policy set definition in the given subscription with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.policySetDefinitionsDelete(policySetDefinitionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsDelete");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **200** | OK |  -  |
| **204** | No Content - the policy set definition doesn&#39;t exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsDeleteAtManagementGroup"></a>
# **policySetDefinitionsDeleteAtManagementGroup**
> policySetDefinitionsDeleteAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId)

Deletes a policy set definition.

This operation deletes the policy set definition in the given management group with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
    try {
      apiInstance.policySetDefinitionsDeleteAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsDeleteAtManagementGroup");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **managementGroupId** | **String**| The ID of the management group. | |

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
| **200** | OK |  -  |
| **204** | No Content - the policy set definition doesn&#39;t exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsGet"></a>
# **policySetDefinitionsGet**
> PolicySetDefinition policySetDefinitionsGet(policySetDefinitionName, apiVersion, subscriptionId)

Retrieves a policy set definition.

This operation retrieves the policy set definition in the given subscription with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      PolicySetDefinition result = apiInstance.policySetDefinitionsGet(policySetDefinitionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsGet");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy set definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsGetAtManagementGroup"></a>
# **policySetDefinitionsGetAtManagementGroup**
> PolicySetDefinition policySetDefinitionsGetAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId)

Retrieves a policy set definition.

This operation retrieves the policy set definition in the given management group with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
    try {
      PolicySetDefinition result = apiInstance.policySetDefinitionsGetAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsGetAtManagementGroup");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **managementGroupId** | **String**| The ID of the management group. | |

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy set definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsGetBuiltIn"></a>
# **policySetDefinitionsGetBuiltIn**
> PolicySetDefinition policySetDefinitionsGetBuiltIn(policySetDefinitionName, apiVersion)

Retrieves a built in policy set definition.

This operation retrieves the built-in policy set definition with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      PolicySetDefinition result = apiInstance.policySetDefinitionsGetBuiltIn(policySetDefinitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsGetBuiltIn");
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
| **policySetDefinitionName** | **String**| The name of the policy set definition to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the built in policy set definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsList"></a>
# **policySetDefinitionsList**
> PolicySetDefinitionListResult policySetDefinitionsList(apiVersion, subscriptionId)

Retrieves the policy set definitions for a subscription.

This operation retrieves a list of all the policy set definitions in the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      PolicySetDefinitionListResult result = apiInstance.policySetDefinitionsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsList");
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
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**PolicySetDefinitionListResult**](PolicySetDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy set definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsListBuiltIn"></a>
# **policySetDefinitionsListBuiltIn**
> PolicySetDefinitionListResult policySetDefinitionsListBuiltIn(apiVersion)

Retrieves built-in policy set definitions.

This operation retrieves a list of all the built-in policy set definitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      PolicySetDefinitionListResult result = apiInstance.policySetDefinitionsListBuiltIn(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsListBuiltIn");
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
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicySetDefinitionListResult**](PolicySetDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of built in policy set definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policySetDefinitionsListByManagementGroup"></a>
# **policySetDefinitionsListByManagementGroup**
> PolicySetDefinitionListResult policySetDefinitionsListByManagementGroup(apiVersion, managementGroupId)

Retrieves all policy set definitions in management group.

This operation retrieves a list of all the a policy set definition in the given management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetDefinitionsApi apiInstance = new PolicySetDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
    try {
      PolicySetDefinitionListResult result = apiInstance.policySetDefinitionsListByManagementGroup(apiVersion, managementGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetDefinitionsApi#policySetDefinitionsListByManagementGroup");
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
| **apiVersion** | **String**| The API version to use for the operation. | |
| **managementGroupId** | **String**| The ID of the management group. | |

### Return type

[**PolicySetDefinitionListResult**](PolicySetDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy set definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

