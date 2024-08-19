# PrivateDockerImagesRegistryApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registryNamespacesGet**](PrivateDockerImagesRegistryApi.md#registryNamespacesGet) | **GET** /registry/namespaces | Retrieve the namespace of an organization. |
| [**registryNamespacesNamespaceGet**](PrivateDockerImagesRegistryApi.md#registryNamespacesNamespaceGet) | **GET** /registry/namespaces/{namespace} | Check the availability of a namespace |
| [**registryNamespacesNamespacePut**](PrivateDockerImagesRegistryApi.md#registryNamespacesNamespacePut) | **PUT** /registry/namespaces/{namespace} | Set a namespace for your private Bluemix registry. |


<a id="registryNamespacesGet"></a>
# **registryNamespacesGet**
> Namespace registryNamespacesGet(xAuthToken, xAuthProjectId)

Retrieve the namespace of an organization.

This endpoint retrieves the namespace that was set for the organization that owns the current space (corresponding IBM Containers command: &#x60;cf ic namespace get&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateDockerImagesRegistryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    PrivateDockerImagesRegistryApi apiInstance = new PrivateDockerImagesRegistryApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    try {
      Namespace result = apiInstance.registryNamespacesGet(xAuthToken, xAuthProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateDockerImagesRegistryApi#registryNamespacesGet");
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
| **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | |
| **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The namespace of the organization is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not found. A namespace could not be found for the organization. Set a namespace by running &#x60;cf ic namespace set &lt;namespace&gt;&#x60;, or calling the &#x60;PUT /registry/namespaces/&lt;namespace&gt;&#x60; endpoint. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="registryNamespacesNamespaceGet"></a>
# **registryNamespacesNamespaceGet**
> Namespace registryNamespacesNamespaceGet(xAuthToken, xAuthProjectId, namespace)

Check the availability of a namespace

This endpoint checks whether a namespace is available in Bluemix and can be used to set up the private Docker images registry for an organization. When a HTTP code &#x60;201 Ok&#x60; is returned, the namespace is already assigned to another organization in Bluemix and cannot be used. When a HTTP code &#x60;404 Not found&#x60; is returned, the namespace can be used for your organization.    Consider the following rules when choosing a namespace for your organization:   - Every organization can have one namespace at a time only  - The namespace must be unique in Bluemix.  - The namespace can be 4-30 characters long.  - The namespace must start with at least one letter or number.  - The namespace can only contain lowercase letters, numbers or underscores (_). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateDockerImagesRegistryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    PrivateDockerImagesRegistryApi apiInstance = new PrivateDockerImagesRegistryApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String namespace = "namespace_example"; // String | The name of the namespace that you would like to use for your organization and for which you would like to check availability in Bluemix.
    try {
      Namespace result = apiInstance.registryNamespacesNamespaceGet(xAuthToken, xAuthProjectId, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateDockerImagesRegistryApi#registryNamespacesNamespaceGet");
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
| **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | |
| **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | |
| **namespace** | **String**| The name of the namespace that you would like to use for your organization and for which you would like to check availability in Bluemix. | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The namespace that you chose is already used in Bluemix. Choose another namespace and re-run the API call. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not found. The namespace that you chose does not exist. You can use it to set it for your organization by running &#x60;cf ic namespace set &lt;namespace&gt;&#x60;, or calling the &#x60;PUT /registry/namespaces/&lt;namespace&gt;&#x60; endpoint. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="registryNamespacesNamespacePut"></a>
# **registryNamespacesNamespacePut**
> Namespace registryNamespacesNamespacePut(xAuthToken, xAuthProjectId, namespace)

Set a namespace for your private Bluemix registry.

Set up your own Docker images registry in Bluemix by defining a namespace for your organization (corresponding IBM Containers command: &#x60;cf ic namespace set &lt;namespace&gt;&#x60;). The namespace is used to generate a unique URL to your private Bluemix registry. In your private registry you store all Docker images that you want to share across your organization. To create a container from an image, you must first push the image to your registry.    The namespace cannot be changed after is has been set. Consider the following rules to choose a namespace for your organization:   - Every organization can have one namespace at a time only  - The namespace must be unique in Bluemix.  - The namespace can be 4-30 characters long.  - The namespace must start with at least one letter or number.  - The namespace can only contain lowercase letters, numbers or underscores (_).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateDockerImagesRegistryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    PrivateDockerImagesRegistryApi apiInstance = new PrivateDockerImagesRegistryApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String namespace = "namespace_example"; // String | The name for your namespace to create your private Docker images registry in Bluemix. You cannot change the name afterward. The namespace can be 4-30 characters long, must start with at least one letter or number, and can only contain lowercase letters, numbers or underscores (_). You can test the availability of your namespace by calling the `GET /registry/namespaces/<namespace>` endpoint. When a HTTP code `404 Not Found` is returned, the namespace is available in Bluemix. 
    try {
      Namespace result = apiInstance.registryNamespacesNamespacePut(xAuthToken, xAuthProjectId, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateDockerImagesRegistryApi#registryNamespacesNamespacePut");
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
| **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | |
| **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | |
| **namespace** | **String**| The name for your namespace to create your private Docker images registry in Bluemix. You cannot change the name afterward. The namespace can be 4-30 characters long, must start with at least one letter or number, and can only contain lowercase letters, numbers or underscores (_). You can test the availability of your namespace by calling the &#x60;GET /registry/namespaces/&lt;namespace&gt;&#x60; endpoint. When a HTTP code &#x60;404 Not Found&#x60; is returned, the namespace is available in Bluemix.  | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK. The namespace is successfully set for your organization. |  -  |
| **400** | Bad request. The specified namespace does not meet the Bluemix namespace requirements. The namespace can be 4-30 characters long, must start with at least one letter or number, and can only contain lowercase letters, numbers or underscores (_). Verify your namespace and re-run the API request. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **409** | Conflict. The namespace that you chose either already exists in Bluemix, or a namespace is already been set for your organization. Run &#x60;cf ic namespace get&#x60; or call the &#x60;GET /registry/namespaces&#x60; endpoint to retrieve your namespace information. If a namespace is not yet set for your organization, choose another name. You can test the namespace by calling the &#x60;GET /registry/namespaces/&lt;namespace&gt;&#x60; endpoint. Re-run the API call with the updated namespace. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

