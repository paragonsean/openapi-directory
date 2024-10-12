# MeshSecretValuesApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshSecretValueAddValue**](MeshSecretValuesApi.md#meshSecretValueAddValue) | **PUT** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName} | Adds the specified value as a new version of the specified secret resource. |
| [**meshSecretValueDelete**](MeshSecretValuesApi.md#meshSecretValueDelete) | **DELETE** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName} | Deletes the specified  value of the named secret resource. |
| [**meshSecretValueGet**](MeshSecretValuesApi.md#meshSecretValueGet) | **GET** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName} | Gets the specified secret value resource. |
| [**meshSecretValueList**](MeshSecretValuesApi.md#meshSecretValueList) | **GET** /Resources/Secrets/{secretResourceName}/values | List names of all values of the specified secret resource. |
| [**meshSecretValueShow**](MeshSecretValuesApi.md#meshSecretValueShow) | **POST** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName}/list_value | Lists the specified value of the secret resource. |


<a id="meshSecretValueAddValue"></a>
# **meshSecretValueAddValue**
> SecretValueResourceDescription meshSecretValueAddValue(apiVersion, secretResourceName, secretValueResourceName, secretValueResourceDescription)

Adds the specified value as a new version of the specified secret resource.

Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretValuesApi apiInstance = new MeshSecretValuesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    SecretValueResourceDescription secretValueResourceDescription = new SecretValueResourceDescription(); // SecretValueResourceDescription | Description for creating a value of a secret resource.
    try {
      SecretValueResourceDescription result = apiInstance.meshSecretValueAddValue(apiVersion, secretResourceName, secretValueResourceName, secretValueResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretValuesApi#meshSecretValueAddValue");
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
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |
| **secretValueResourceDescription** | [**SecretValueResourceDescription**](SecretValueResourceDescription.md)| Description for creating a value of a secret resource. | |

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

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

<a id="meshSecretValueDelete"></a>
# **meshSecretValueDelete**
> meshSecretValueDelete(apiVersion, secretResourceName, secretValueResourceName)

Deletes the specified  value of the named secret resource.

Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretValuesApi apiInstance = new MeshSecretValuesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    try {
      apiInstance.meshSecretValueDelete(apiVersion, secretResourceName, secretValueResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretValuesApi#meshSecretValueDelete");
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
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |

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
| **204** | No Content - the specified secret value was not found. |  -  |
| **0** | Error |  -  |

<a id="meshSecretValueGet"></a>
# **meshSecretValueGet**
> SecretValueResourceDescription meshSecretValueGet(apiVersion, secretResourceName, secretValueResourceName)

Gets the specified secret value resource.

Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretValuesApi apiInstance = new MeshSecretValuesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    try {
      SecretValueResourceDescription result = apiInstance.meshSecretValueGet(apiVersion, secretResourceName, secretValueResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretValuesApi#meshSecretValueGet");
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
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

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

<a id="meshSecretValueList"></a>
# **meshSecretValueList**
> PagedSecretValueResourceDescriptionList meshSecretValueList(apiVersion, secretResourceName)

List names of all values of the specified secret resource.

Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretValuesApi apiInstance = new MeshSecretValuesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    try {
      PagedSecretValueResourceDescriptionList result = apiInstance.meshSecretValueList(apiVersion, secretResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretValuesApi#meshSecretValueList");
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

[**PagedSecretValueResourceDescriptionList**](PagedSecretValueResourceDescriptionList.md)

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

<a id="meshSecretValueShow"></a>
# **meshSecretValueShow**
> SecretValue meshSecretValueShow(apiVersion, secretResourceName, secretValueResourceName)

Lists the specified value of the secret resource.

Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshSecretValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshSecretValuesApi apiInstance = new MeshSecretValuesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
    String secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
    try {
      SecretValue result = apiInstance.meshSecretValueShow(apiVersion, secretResourceName, secretValueResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshSecretValuesApi#meshSecretValueShow");
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
| **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | |

### Return type

[**SecretValue**](SecretValue.md)

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

