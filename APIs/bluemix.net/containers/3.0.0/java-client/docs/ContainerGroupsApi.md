# ContainerGroupsApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containersGroupsGet**](ContainerGroupsApi.md#containersGroupsGet) | **GET** /containers/groups | List all container groups in a space |
| [**containersGroupsNameOrIdDelete**](ContainerGroupsApi.md#containersGroupsNameOrIdDelete) | **DELETE** /containers/groups/{name_or_id} | Stop and delete all container instances in a container group. |
| [**containersGroupsNameOrIdGet**](ContainerGroupsApi.md#containersGroupsNameOrIdGet) | **GET** /containers/groups/{name_or_id} | Inspect a container group. |
| [**containersGroupsNameOrIdMaproutePost**](ContainerGroupsApi.md#containersGroupsNameOrIdMaproutePost) | **POST** /containers/groups/{name_or_id}/maproute | Map a public route to a container group. |
| [**containersGroupsNameOrIdPatch**](ContainerGroupsApi.md#containersGroupsNameOrIdPatch) | **PATCH** /containers/groups/{name_or_id} | Update a container group. |
| [**containersGroupsNameOrIdUnmaproutePost**](ContainerGroupsApi.md#containersGroupsNameOrIdUnmaproutePost) | **POST** /containers/groups/{name_or_id}/unmaproute | Unmap a public route from a container group |
| [**containersGroupsPost**](ContainerGroupsApi.md#containersGroupsPost) | **POST** /containers/groups | Create and start a container group. |


<a id="containersGroupsGet"></a>
# **containersGroupsGet**
> List&lt;ContainersGroupsGetListItem&gt; containersGroupsGet(xAuthToken, xAuthProjectId)

List all container groups in a space

This endpoint returns a list of all container groups in a space independent of their current state. (corresponding IBM Containers command: &#x60;cf ic group list&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    try {
      List<ContainersGroupsGetListItem> result = apiInstance.containersGroupsGet(xAuthToken, xAuthProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsGet");
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

[**List&lt;ContainersGroupsGetListItem&gt;**](ContainersGroupsGetListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of container groups is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersGroupsNameOrIdDelete"></a>
# **containersGroupsNameOrIdDelete**
> containersGroupsNameOrIdDelete(xAuthToken, xAuthProjectId, nameOrId, force)

Stop and delete all container instances in a container group.

Stops and deletes the container instances that run in a container group (corresponding IBM Containers command: &#x60;cf ic group rm &lt;group_name&gt;&#x60;). When you delete a container group, all floating private IP addresses are released.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The name or unique ID of the container group that you want to delete. Run `cf ic group list` or call the `GET /containers/groups` endpoint to retrieve a list of container groups in your space.
    String force = "force_example"; // String | If you want to force the deletion of a container group that has running container instances, use the force option. This parameter needs to be set to either true or false. If set to `force=true`, `force=True`, or `force=1`, running container instances are deleted. If set to `force=false`, `force=False`, or `force=0`, running container instances are not deleted. If you do not specify this paramater, running container instances are not deleted by default. 
    try {
      apiInstance.containersGroupsNameOrIdDelete(xAuthToken, xAuthProjectId, nameOrId, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsNameOrIdDelete");
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
| **nameOrId** | **String**| The name or unique ID of the container group that you want to delete. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. | |
| **force** | **String**| If you want to force the deletion of a container group that has running container instances, use the force option. This parameter needs to be set to either true or false. If set to &#x60;force&#x3D;true&#x60;, &#x60;force&#x3D;True&#x60;, or &#x60;force&#x3D;1&#x60;, running container instances are deleted. If set to &#x60;force&#x3D;false&#x60;, &#x60;force&#x3D;False&#x60;, or &#x60;force&#x3D;0&#x60;, running container instances are not deleted. If you do not specify this paramater, running container instances are not deleted by default.  | [optional] |

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
| **204** | OK. No content. The deletion of the container group was successfully processed. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **403** | The container group cannot be deleted due to running or failed container instances. Set the force query parameter to &#x60;force&#x3D;true&#x60;, &#x60;force&#x3D;True&#x60;, or &#x60;force&#x3D;1&#x60; and re-run the REST call to force the deletion of your container group. |  -  |
| **404** | Not Found. The name or ID of the container group that you want to delete could not be found. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. Enter the correct name or ID and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersGroupsNameOrIdGet"></a>
# **containersGroupsNameOrIdGet**
> ContainersGroupsNameOrIdGetDetails containersGroupsNameOrIdGet(xAuthToken, xAuthProjectId, nameOrId)

Inspect a container group.

This endpoint retrieves detailed information about a container group with a given name (corresponding IBM Containers command: &#x60;cf ic group inspect GROUP&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The name or unique ID of the container group that you want to inspect. Run `cf ic group list` or call the `GET /containers/groups` endpoint to retrieve a list of container groups in your space.
    try {
      ContainersGroupsNameOrIdGetDetails result = apiInstance.containersGroupsNameOrIdGet(xAuthToken, xAuthProjectId, nameOrId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsNameOrIdGet");
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
| **nameOrId** | **String**| The name or unique ID of the container group that you want to inspect. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. | |

### Return type

[**ContainersGroupsNameOrIdGetDetails**](ContainersGroupsNameOrIdGetDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A detailed list of information about a container group is retrieved. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The specified name or ID of the container group that you want to update could not be found. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. Enter the correct name or ID and re-run the REST call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersGroupsNameOrIdMaproutePost"></a>
# **containersGroupsNameOrIdMaproutePost**
> ContainersGroupsNameOrIdMaproutePostInfo containersGroupsNameOrIdMaproutePost(xAuthToken, xAuthProjectId, nameOrId, route)

Map a public route to a container group.

If you want your container group to be accessible from the Internet, you need to expose a public port and map a public route to it (corresponding IBM Containers command: &#x60;cf ic route map -n &lt;host&gt; -d &lt;domain&gt; &lt;group&gt;&#x60;). Every route consists of the host name and domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The name or unique ID of the container group to which you want to map a public route. Run `cf ic group list` or call the `GET /containers/groups` endpoint to retrieve a list of container groups in your space.
    Route route = new Route(); // Route | The public route that is mapped to the container group. A public route consists of the host name and domain.
    try {
      ContainersGroupsNameOrIdMaproutePostInfo result = apiInstance.containersGroupsNameOrIdMaproutePost(xAuthToken, xAuthProjectId, nameOrId, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsNameOrIdMaproutePost");
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
| **nameOrId** | **String**| The name or unique ID of the container group to which you want to map a public route. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. | |
| **route** | [**Route**](Route.md)| The public route that is mapped to the container group. A public route consists of the host name and domain. | |

### Return type

[**ContainersGroupsNameOrIdMaproutePostInfo**](ContainersGroupsNameOrIdMaproutePostInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK. The route that you specified was successfully mapped to the container group. |  -  |
| **400** | Bad request. The information that you entered in the body request is either incomplete or in the wrong format. To map a route enter the domain and host name in JSON format. Be sure, that you have exposed a public port when you created the container group, otherwise you cannot map a public route to it. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The name or ID of the container group to which you want to map a public route could not be found. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. Enter the correct name or ID and re-run the REST call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersGroupsNameOrIdPatch"></a>
# **containersGroupsNameOrIdPatch**
> containersGroupsNameOrIdPatch(xAuthToken, xAuthProjectId, nameOrId, containersGroupsNameOrIdPatchUpdatedInfo)

Update a container group.

Update the number of container instances that run in a container group (corresponding IBM Containers command: &#x60;cf ic group update &lt;option&gt; &lt;group&gt;&#x60;).   Note: You can run only one update at a time.     The desired number is the number of container instances that you require. It must be within the current limits of Max and Min. To increase the number of desired container instances above the Max value, you must first execute an update on the Max value. Once this update is completed, you can increase the desired number of container instances. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The name or unique ID of the container group that you want to update.
    ContainersGroupsNameOrIdPatchUpdatedInfo containersGroupsNameOrIdPatchUpdatedInfo = new ContainersGroupsNameOrIdPatchUpdatedInfo(); // ContainersGroupsNameOrIdPatchUpdatedInfo | The container group parameter that you want to update.
    try {
      apiInstance.containersGroupsNameOrIdPatch(xAuthToken, xAuthProjectId, nameOrId, containersGroupsNameOrIdPatchUpdatedInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsNameOrIdPatch");
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
| **nameOrId** | **String**| The name or unique ID of the container group that you want to update. | |
| **containersGroupsNameOrIdPatchUpdatedInfo** | [**ContainersGroupsNameOrIdPatchUpdatedInfo**](ContainersGroupsNameOrIdPatchUpdatedInfo.md)| The container group parameter that you want to update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content. The update has successfully been processed. |  -  |
| **400** | Bad request. The information that you entered in the body of your request are either incomplete or in the wrong format. Be sure, to enter the information that you want to update in JSON format and review the description for each parameter to assure your desired update is valid and can be processed. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The name or ID of the container group that you want to update could not be found. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space. Enter the correct name or ID and re-run the REST call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersGroupsNameOrIdUnmaproutePost"></a>
# **containersGroupsNameOrIdUnmaproutePost**
> ContainersGroupsNameOrIdMaproutePostInfo containersGroupsNameOrIdUnmaproutePost(xAuthToken, xAuthProjectId, nameOrId, route)

Unmap a public route from a container group

This endpoint unmaps a public route from a container group (corresponding IBM Containers command: &#x60;cf ic route unmap -n &lt;host&gt; -d &lt;domain&gt; &lt;group&gt;&#x60;). If no other public route is mapped to the container group, then the container group is no longer available from the internet.    When you unmap a route from a container group, the route is not deleted and can be mapped to other container groups. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String nameOrId = "nameOrId_example"; // String | The name or unique ID (UUID) of the container group that you want to inspect.
    Route route = new Route(); // Route | The public route that is unmapped from the container group. A public route consists of the host name and domain.
    try {
      ContainersGroupsNameOrIdMaproutePostInfo result = apiInstance.containersGroupsNameOrIdUnmaproutePost(xAuthToken, xAuthProjectId, nameOrId, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsNameOrIdUnmaproutePost");
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
| **nameOrId** | **String**| The name or unique ID (UUID) of the container group that you want to inspect. | |
| **route** | [**Route**](Route.md)| The public route that is unmapped from the container group. A public route consists of the host name and domain. | |

### Return type

[**ContainersGroupsNameOrIdMaproutePostInfo**](ContainersGroupsNameOrIdMaproutePostInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK. The route that you specified was successfully unmapped from the container group. |  -  |
| **400** | Bad request. The information that you entered in the body of your request is either incomplete or in the wrong format. To unmap a route, enter the domain and host name in JSON format and re-run the REST call. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not Found. The name or ID of the container group from which you want to unmap a public route could not be found. Enter the correct name or ID and re-run the REST call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersGroupsPost"></a>
# **containersGroupsPost**
> ContainersGroupsPostCreatedInfo containersGroupsPost(xAuthToken, xAuthProjectId, containersGroupsPostRequiredAttributes)

Create and start a container group.

This endpoint creates and starts a new container group in your space. A container group consists of two or more single containers that are all created from the same container image and as a consequence are configured in the same way. Container groups offer different options at no cost to make your app highly available, such as in-built load balancing, auto-recovery of unhealthy container instances, and auto-scaling of container instances based on CPU and memory usage.  To create a container group with IBM Containers, you must at least define a container group name and the image that the container group is based on. Required attributes:                 - Name: The container group name must start with a letter and then can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-).  - Image: You must include the full path to the image in your private Bluemix registry in the format:&#x60;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image&gt;&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ContainerGroupsApi apiInstance = new ContainerGroupsApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    ContainersGroupsPostRequiredAttributes containersGroupsPostRequiredAttributes = new ContainersGroupsPostRequiredAttributes(); // ContainersGroupsPostRequiredAttributes | Attributes that are required to create a container group in your space.
    try {
      ContainersGroupsPostCreatedInfo result = apiInstance.containersGroupsPost(xAuthToken, xAuthProjectId, containersGroupsPostRequiredAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerGroupsApi#containersGroupsPost");
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
| **containersGroupsPostRequiredAttributes** | [**ContainersGroupsPostRequiredAttributes**](ContainersGroupsPostRequiredAttributes.md)| Attributes that are required to create a container group in your space. | |

### Return type

[**ContainersGroupsPostCreatedInfo**](ContainersGroupsPostCreatedInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created. Your container group was successfully created. |  -  |
| **400** | Bad request. The information that you entered in the request body are either incomplete or in the wrong format to process your request. Be sure, to specify at least the name and container image for your container group in JSON format and re-run the REST call. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **409** | Conflict. A container group with the same name already exists. Choose a new name for your container group and re-run the REST call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

