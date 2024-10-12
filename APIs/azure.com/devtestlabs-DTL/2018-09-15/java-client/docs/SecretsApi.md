# SecretsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**secretsCreateOrUpdate**](SecretsApi.md#secretsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} |  |
| [**secretsDelete**](SecretsApi.md#secretsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} |  |
| [**secretsGet**](SecretsApi.md#secretsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} |  |
| [**secretsList**](SecretsApi.md#secretsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets |  |
| [**secretsUpdate**](SecretsApi.md#secretsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name} |  |


<a id="secretsCreateOrUpdate"></a>
# **secretsCreateOrUpdate**
> Secret secretsCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret)



Create or replace an existing secret. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the secret.
    String apiVersion = "2018-09-15"; // String | Client API version.
    Secret secret = new Secret(); // Secret | A secret.
    try {
      Secret result = apiInstance.secretsCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **secret** | [**Secret**](Secret.md)| A secret. | |

### Return type

[**Secret**](Secret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="secretsDelete"></a>
# **secretsDelete**
> secretsDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Delete secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the secret.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.secretsDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="secretsGet"></a>
# **secretsGet**
> Secret secretsGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, $expand)



Get secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the secret.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=value)'
    try {
      Secret result = apiInstance.secretsGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;value)&#39; | [optional] |

### Return type

[**Secret**](Secret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="secretsList"></a>
# **secretsList**
> SecretList secretsList(subscriptionId, resourceGroupName, labName, userName, apiVersion, $expand, $filter, $top, $orderby)



List secrets in a given user profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=value)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation. Example: '$top=10'
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    try {
      SecretList result = apiInstance.secretsList(subscriptionId, resourceGroupName, labName, userName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;value)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] |

### Return type

[**SecretList**](SecretList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="secretsUpdate"></a>
# **secretsUpdate**
> Secret secretsUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret)



Allows modifying tags of secrets. All other properties will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the secret.
    String apiVersion = "2018-09-15"; // String | Client API version.
    SecretFragment secret = new SecretFragment(); // SecretFragment | A secret.
    try {
      Secret result = apiInstance.secretsUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **secret** | [**SecretFragment**](SecretFragment.md)| A secret. | |

### Return type

[**Secret**](Secret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

