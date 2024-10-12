# SecretValuesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**secretValueCreate**](SecretValuesApi.md#secretValueCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName} | Adds the specified value as a new version of the specified secret resource. |
| [**secretValueDelete**](SecretValuesApi.md#secretValueDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName} | Deletes the specified  value of the named secret resource. |
| [**secretValueGet**](SecretValuesApi.md#secretValueGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName} | Gets the specified secret value resource. |
| [**secretValueList**](SecretValuesApi.md#secretValueList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values | List names of all values of the specified secret resource. |
| [**secretValueListValue**](SecretValuesApi.md#secretValueListValue) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName}/list_value | Lists the specified value of the secret resource. |


<a id="secretValueCreate"></a>
# **secretValueCreate**
> SecretValueResourceDescription secretValueCreate(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, secretValueResourceDescription)

Adds the specified value as a new version of the specified secret resource.

Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretValuesApi apiInstance = new SecretValuesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    SecretValueResourceDescription secretValueResourceDescription = new SecretValueResourceDescription(); // SecretValueResourceDescription | Description for creating a value of a secret resource.
    try {
      SecretValueResourceDescription result = apiInstance.secretValueCreate(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, secretValueResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretValuesApi#secretValueCreate");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **secretResourceName** | **String**| The name of the secret resource. | |
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |
| **secretValueResourceDescription** | [**SecretValueResourceDescription**](SecretValueResourceDescription.md)| Description for creating a value of a secret resource. | |

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

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
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="secretValueDelete"></a>
# **secretValueDelete**
> secretValueDelete(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName)

Deletes the specified  value of the named secret resource.

Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretValuesApi apiInstance = new SecretValuesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    try {
      apiInstance.secretValueDelete(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretValuesApi#secretValueDelete");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **secretResourceName** | **String**| The name of the secret resource. | |
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |

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
| **202** | Accepted |  -  |
| **204** | No Content - the specified named secret value was not found. |  -  |
| **0** | Error |  -  |

<a id="secretValueGet"></a>
# **secretValueGet**
> SecretValueResourceDescription secretValueGet(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName)

Gets the specified secret value resource.

Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretValuesApi apiInstance = new SecretValuesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    try {
      SecretValueResourceDescription result = apiInstance.secretValueGet(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretValuesApi#secretValueGet");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **secretResourceName** | **String**| The name of the secret resource. | |
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="secretValueList"></a>
# **secretValueList**
> SecretValueResourceDescriptionList secretValueList(subscriptionId, apiVersion, resourceGroupName, secretResourceName)

List names of all values of the specified secret resource.

Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretValuesApi apiInstance = new SecretValuesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    try {
      SecretValueResourceDescriptionList result = apiInstance.secretValueList(subscriptionId, apiVersion, resourceGroupName, secretResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretValuesApi#secretValueList");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **secretResourceName** | **String**| The name of the secret resource. | |

### Return type

[**SecretValueResourceDescriptionList**](SecretValueResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="secretValueListValue"></a>
# **secretValueListValue**
> SecretValue secretValueListValue(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName)

Lists the specified value of the secret resource.

Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SecretValuesApi apiInstance = new SecretValuesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    try {
      SecretValue result = apiInstance.secretValueListValue(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretValuesApi#secretValueListValue");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **secretResourceName** | **String**| The name of the secret resource. | |
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

