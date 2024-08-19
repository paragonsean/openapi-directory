# SingleContainersApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containersCreatePost**](SingleContainersApi.md#containersCreatePost) | **POST** /containers/create | Create and start a single container |
| [**containersIdStatusGet**](SingleContainersApi.md#containersIdStatusGet) | **GET** /containers/{id}/status | List the current state of a container. |
| [**containersJsonGet**](SingleContainersApi.md#containersJsonGet) | **GET** /containers/json | List single containers in a space. |
| [**containersNameOrIdDelete**](SingleContainersApi.md#containersNameOrIdDelete) | **DELETE** /containers/{name_or_id} | Remove a single container |
| [**containersNameOrIdJsonGet**](SingleContainersApi.md#containersNameOrIdJsonGet) | **GET** /containers/{name_or_id}/json | Inspect a single container |
| [**containersNameOrIdPausePost**](SingleContainersApi.md#containersNameOrIdPausePost) | **POST** /containers/{name_or_id}/pause | Pause a single container |
| [**containersNameOrIdRenamePost**](SingleContainersApi.md#containersNameOrIdRenamePost) | **POST** /containers/{name_or_id}/rename | Rename a single container |
| [**containersNameOrIdRestartPost**](SingleContainersApi.md#containersNameOrIdRestartPost) | **POST** /containers/{name_or_id}/restart | Restart a single container |
| [**containersNameOrIdStartPost**](SingleContainersApi.md#containersNameOrIdStartPost) | **POST** /containers/{name_or_id}/start | Start a single container |
| [**containersNameOrIdStopPost**](SingleContainersApi.md#containersNameOrIdStopPost) | **POST** /containers/{name_or_id}/stop | Stop a single container |
| [**containersNameOrIdUnpausePost**](SingleContainersApi.md#containersNameOrIdUnpausePost) | **POST** /containers/{name_or_id}/unpause | Unpause a single container |


<a id="containersCreatePost"></a>
# **containersCreatePost**
> ContainerId containersCreatePost(xAuthToken, xAuthProjectId, createContainer, name)

Create and start a single container

This endpoint creates and starts a single container in your space based on the Docker image that is specified in the Image field of the request json. A single container in IBM Containers is similar to a container that you create in your local Docker environment. Single containers are a good way to start with IBM Containers and to learn about how containers work in the IBM Cloud and the features that IBM Containers provides. They are also recommended when you want to run simple app tests or during the development process of an app.    In the Docker API there are two separate APIs to create and start a container. However in IBM Containers a container is created and started in a single API call. Therefore, this API merges parameters from the Docker API to create and start container.    To create a container with IBM Containers, you must at least define the image that the container is based on.  - Image: You must include the full path to the image in your private Bluemix registry in the format: &#x60;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image&gt;&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    CreateContainer createContainer = new CreateContainer(); // CreateContainer | Summary of input parameter to create a container in IBM Containers.
    String name = "name_example"; // String | Choose a name for your container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter.
    try {
      ContainerId result = apiInstance.containersCreatePost(xAuthToken, xAuthProjectId, createContainer, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersCreatePost");
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
| **createContainer** | [**CreateContainer**](CreateContainer.md)| Summary of input parameter to create a container in IBM Containers. | |
| **name** | **String**| Choose a name for your container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter. | [optional] |

### Return type

[**ContainerId**](ContainerId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK. The creation of a single container with the specified attributes has been initiated. |  -  |
| **400** | Bad request. The data that you entered in the request body are either incomplete or in the wrong format. Be sure to include at least the Docker image that you want to use in JSON format and re-run the API request. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **409** |  Conflict. A container with the same name already exists. Choose another name for your container and re-run the API request. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="containersIdStatusGet"></a>
# **containersIdStatusGet**
> GetContainerStatus containersIdStatusGet(xAuthToken, xAuthProjectId, id)

List the current state of a container.

This endpoint returns the current state of a container. This state can either be a transient state, such as BUILDING and NETWORKING, or a non-transient state, such as RUNNING, SHUTDOWN, CRASHED, or SUSPENDED.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String id = "id_example"; // String | The unique identifier that represents the container. Run `cf ic ps`, or call the `GET /containers/json` endpoint to retrieve the ID of the container.
    try {
      GetContainerStatus result = apiInstance.containersIdStatusGet(xAuthToken, xAuthProjectId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersIdStatusGet");
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
| **id** | **String**| The unique identifier that represents the container. Run &#x60;cf ic ps&#x60;, or call the &#x60;GET /containers/json&#x60; endpoint to retrieve the ID of the container. | |

### Return type

[**GetContainerStatus**](GetContainerStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK. The current status of a container is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container could not be found. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the ID of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="containersJsonGet"></a>
# **containersJsonGet**
> List&lt;Container&gt; containersJsonGet(xAuthToken, xAuthProjectId, all, filters)

List single containers in a space.

This endpoint returns a list of all single containers in a space that are currently in a running state (corresponding IBM Containers command: &#x60;cf ic ps&#x60;). To list all single containers independent of their current state, set the &#x60;all&#x60; query parameter to true.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String all = "all_example"; // String | By default, the `GET /containers/json` endpoint returns a list of all single containers in a space that are in a running state. To request a list of all containers independent of their current state, set the `all` query parameter to true. Allowed values are: `all=true`, `all=True`, and `all=1`. 
    String filters = "filters_example"; // String | You can filter your containers by any environment variable key or value that is listed in the `Env` section of your CLI/ API response when you run the `cf ic inspect <container>` command, or call the `GET /containers/{id}/json` endpoint. Your search criteria does not need to be an exact match. It can also be a part of the key or value you are looking for. For example, to filter all containers with an environment variable that contains `id` in one of their environment variables, use `filter=id`.
    try {
      List<Container> result = apiInstance.containersJsonGet(xAuthToken, xAuthProjectId, all, filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersJsonGet");
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
| **all** | **String**| By default, the &#x60;GET /containers/json&#x60; endpoint returns a list of all single containers in a space that are in a running state. To request a list of all containers independent of their current state, set the &#x60;all&#x60; query parameter to true. Allowed values are: &#x60;all&#x3D;true&#x60;, &#x60;all&#x3D;True&#x60;, and &#x60;all&#x3D;1&#x60;.  | [optional] |
| **filters** | **String**| You can filter your containers by any environment variable key or value that is listed in the &#x60;Env&#x60; section of your CLI/ API response when you run the &#x60;cf ic inspect &lt;container&gt;&#x60; command, or call the &#x60;GET /containers/{id}/json&#x60; endpoint. Your search criteria does not need to be an exact match. It can also be a part of the key or value you are looking for. For example, to filter all containers with an environment variable that contains &#x60;id&#x60; in one of their environment variables, use &#x60;filter&#x3D;id&#x60;. | [optional] |

### Return type

[**List&lt;Container&gt;**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of single containers that match the search criteria is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="containersNameOrIdDelete"></a>
# **containersNameOrIdDelete**
> containersNameOrIdDelete(xAuthToken, xAuthProjectId, nameOrId, force)

Remove a single container

Remove a single container that is identified by container ID or name from a space (corresponding IBM Containers command: &#x60;cf ic delete &lt;container&gt;&#x60;). The container must be stopped before it can be deleted, unless the &#x60;force&#x60; query parameter is set to true.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to delete. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review all containers in your space.
    Boolean force = true; // Boolean | Use the `force` query parameter if you want to delete the container independent of their current state. The container does not need to be stopped first. To force the deletion of a container, enter `force=true`, `force=True`, or `force=1`. If you want to delete containers that are in a non-running state only, do either not set this query parameter, or enter `force=false`, `force=False`, or `force=0`.
    try {
      apiInstance.containersNameOrIdDelete(xAuthToken, xAuthProjectId, nameOrId, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdDelete");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to delete. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space. | |
| **force** | **Boolean**| Use the &#x60;force&#x60; query parameter if you want to delete the container independent of their current state. The container does not need to be stopped first. To force the deletion of a container, enter &#x60;force&#x3D;true&#x60;, &#x60;force&#x3D;True&#x60;, or &#x60;force&#x3D;1&#x60;. If you want to delete containers that are in a non-running state only, do either not set this query parameter, or enter &#x60;force&#x3D;false&#x60;, &#x60;force&#x3D;False&#x60;, or &#x60;force&#x3D;0&#x60;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The deletion of your container has been initiated. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the ID and name of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdJsonGet"></a>
# **containersNameOrIdJsonGet**
> ContainerInfo containersNameOrIdJsonGet(xAuthToken, xAuthProjectId, nameOrId)

Inspect a single container

This endpoint retrieves detailed information about a single container (corresponding IBM Containers command: &#x60;cf ic inspect &lt;container&gt;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The name or ID of the container that you want to inspect. Run the `cf ic ps` command or call the `GET /containers/json` endpoint to retrieve a list of containers in your space.
    try {
      ContainerInfo result = apiInstance.containersNameOrIdJsonGet(xAuthToken, xAuthProjectId, nameOrId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdJsonGet");
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
| **nameOrId** | **String**| The name or ID of the container that you want to inspect. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space. | |

### Return type

[**ContainerInfo**](ContainerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list with detailed information about the container is returned.  |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container name or ID that you entered, could not be found. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; to review the name or ID of the container that you want to inspect. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdPausePost"></a>
# **containersNameOrIdPausePost**
> containersNameOrIdPausePost(xAuthToken, xAuthProjectId, nameOrId)

Pause a single container

Pause all processes in a running single container with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic pause &lt;container&gt;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to pause. Run `cf ic ps` or call the `GET /containers/json` endpoint to review all containers in your space that are currently in a running state.
    try {
      apiInstance.containersNameOrIdPausePost(xAuthToken, xAuthProjectId, nameOrId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdPausePost");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to pause. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review all containers in your space that are currently in a running state. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The pausing of all processes inside the container has been initiated. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the ID and name of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdRenamePost"></a>
# **containersNameOrIdRenamePost**
> containersNameOrIdRenamePost(xAuthToken, xAuthProjectId, nameOrId, name)

Rename a single container

Change the current name of an existing single container that is identified by the container ID or name (corresponding IBM Containers command: &#x60;cf ic rename &lt;old_name&gt; &lt;new_name&gt;&#x60;). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to rename. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review all containers in your space.
    String name = "name_example"; // String | The new name for the container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter.
    try {
      apiInstance.containersNameOrIdRenamePost(xAuthToken, xAuthProjectId, nameOrId, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdRenamePost");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to rename. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space. | |
| **name** | **String**| The new name for the container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The request to rename the container has been initiated. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the ID and name of your container. |  -  |
| **409** | Conflict. A container with the same name already exists. Choose another name for your container and re-run the API call.  |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdRestartPost"></a>
# **containersNameOrIdRestartPost**
> containersNameOrIdRestartPost(xAuthToken, xAuthProjectId, nameOrId, t)

Restart a single container

Restart a container with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic restart &lt;container&gt;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to restart. Run `cf ic ps` or call the `GET /containers/json` endpoint to review all containers in your space.
    Integer t = 56; // Integer | The number of seconds to wait before the container is restarted. For example, if you want a container to restart after 10 seconds, enter `t=10`.
    try {
      apiInstance.containersNameOrIdRestartPost(xAuthToken, xAuthProjectId, nameOrId, t);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdRestartPost");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to restart. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review all containers in your space. | |
| **t** | **Integer**| The number of seconds to wait before the container is restarted. For example, if you want a container to restart after 10 seconds, enter &#x60;t&#x3D;10&#x60;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The restart of the container has been initiated. |  -  |
| **304** | Not Modified. A request to restart the container with the specified name or ID has already been initiated. To review the current state of your container, run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the ID and name of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdStartPost"></a>
# **containersNameOrIdStartPost**
> containersNameOrIdStartPost(xAuthToken, xAuthProjectId, nameOrId)

Start a single container

Start a single container with a given container name or ID (corresponding IBM Containers command: &#x60;cf ic start &lt;container&gt;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to start. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review the containers in your space that are currently not in a running state.
    try {
      apiInstance.containersNameOrIdStartPost(xAuthToken, xAuthProjectId, nameOrId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdStartPost");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to start. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the containers in your space that are currently not in a running state. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The start of the container has been initiated. |  -  |
| **304** | Not Modified. A request to start the container with the specified name or ID has already been initiated. To review the current state of your container, run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the ID and name of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdStopPost"></a>
# **containersNameOrIdStopPost**
> containersNameOrIdStopPost(xAuthToken, xAuthProjectId, nameOrId, t)

Stop a single container

Stop a single container with a given container name or ID (corresponding IBM Containers command: &#x60;cf ic stop &lt;container&gt;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to stop. Run `cf ic ps` or call the `GET /containers/json` endpoint to review the containers in your space that are currently in a running state.
    Integer t = 56; // Integer | The number of seconds to wait before the container is stopped. For example, if you want a container to stop after 10 seconds, enter `t=10`.
    try {
      apiInstance.containersNameOrIdStopPost(xAuthToken, xAuthProjectId, nameOrId, t);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdStopPost");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to stop. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the containers in your space that are currently in a running state. | |
| **t** | **Integer**| The number of seconds to wait before the container is stopped. For example, if you want a container to stop after 10 seconds, enter &#x60;t&#x3D;10&#x60;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The stop of the container has been initiated. |  -  |
| **304** | Not Modified. A request to stop the container with the specified name or ID has already been initiated. To review the current state of your container, run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the ID and name of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersNameOrIdUnpausePost"></a>
# **containersNameOrIdUnpausePost**
> containersNameOrIdUnpausePost(xAuthToken, xAuthProjectId, nameOrId)

Unpause a single container

Unpause all processes that are currently stopped inside a single containers with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic unpause &lt;container&gt;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    SingleContainersApi apiInstance = new SingleContainersApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to unpause. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review all containers in your space.
    try {
      apiInstance.containersNameOrIdUnpausePost(xAuthToken, xAuthProjectId, nameOrId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleContainersApi#containersNameOrIdUnpausePost");
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
| **nameOrId** | **String**| The unique identifier or name of the container that you want to unpause. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The unpausing of all processes inside the container has been initiated. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The container with the specified name or ID could not be found. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the ID and name of your container. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

