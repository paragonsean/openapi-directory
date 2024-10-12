# MeshSecretsApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshSecretCreateOrUpdate**](MeshSecretsApi.md#meshSecretCreateOrUpdate) | **PUT** /Resources/Secrets/{secretResourceName} | Creates or updates a Secret resource. |
| [**meshSecretDelete**](MeshSecretsApi.md#meshSecretDelete) | **DELETE** /Resources/Secrets/{secretResourceName} | Deletes the Secret resource. |
| [**meshSecretGet**](MeshSecretsApi.md#meshSecretGet) | **GET** /Resources/Secrets/{secretResourceName} | Gets the Secret resource with the given name. |
| [**meshSecretList**](MeshSecretsApi.md#meshSecretList) | **GET** /Resources/Secrets | Lists all the secret resources. |


<a id="meshSecretCreateOrUpdate"></a>
# **meshSecretCreateOrUpdate**
> SecretResourceDescription meshSecretCreateOrUpdate(apiVersion, secretResourceName, secretResourceDescription)

Creates or updates a Secret resource.

Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretsApi apiInstance = new MeshSecretsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    SecretResourceDescription secretResourceDescription = new SecretResourceDescription(); // SecretResourceDescription | Description for creating a secret resource.
    try {
      SecretResourceDescription result = apiInstance.meshSecretCreateOrUpdate(apiVersion, secretResourceName, secretResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretsApi#meshSecretCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **secretResourceName** | **String**| The name of the secret resource. | |
| **secretResourceDescription** | [**SecretResourceDescription**](SecretResourceDescription.md)| Description for creating a secret resource. | |

### Return type

[**SecretResourceDescription**](SecretResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="meshSecretDelete"></a>
# **meshSecretDelete**
> meshSecretDelete(apiVersion, secretResourceName)

Deletes the Secret resource.

Deletes the specified Secret resource and all of its named values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretsApi apiInstance = new MeshSecretsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    try {
      apiInstance.meshSecretDelete(apiVersion, secretResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretsApi#meshSecretDelete");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **secretResourceName** | **String**| The name of the secret resource. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content - the specified secret was not found. |  -  |
| **0** | Error |  -  |

<a id="meshSecretGet"></a>
# **meshSecretGet**
> SecretResourceDescription meshSecretGet(apiVersion, secretResourceName)

Gets the Secret resource with the given name.

Gets the information about the Secret resource with the given name. The information include the description and other properties of the Secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretsApi apiInstance = new MeshSecretsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    try {
      SecretResourceDescription result = apiInstance.meshSecretGet(apiVersion, secretResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretsApi#meshSecretGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **secretResourceName** | **String**| The name of the secret resource. | |

### Return type

[**SecretResourceDescription**](SecretResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="meshSecretList"></a>
# **meshSecretList**
> PagedSecretResourceDescriptionList meshSecretList(apiVersion)

Lists all the secret resources.

Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretsApi apiInstance = new MeshSecretsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    try {
      PagedSecretResourceDescriptionList result = apiInstance.meshSecretList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretsApi#meshSecretList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |

### Return type

[**PagedSecretResourceDescriptionList**](PagedSecretResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

