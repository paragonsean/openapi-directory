# VolumesApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesCreatePost**](VolumesApi.md#volumesCreatePost) | **POST** /volumes/create | Create a volume in a space |
| [**volumesJsonGet**](VolumesApi.md#volumesJsonGet) | **GET** /volumes/json | List all volumes for a space |
| [**volumesNameDelete**](VolumesApi.md#volumesNameDelete) | **DELETE** /volumes/{name} | Delete a volume |
| [**volumesNameJsonGet**](VolumesApi.md#volumesNameJsonGet) | **GET** /volumes/{name}/json | Retrieve detailed information about a volume.  |
| [**volumesNamePost**](VolumesApi.md#volumesNamePost) | **POST** /volumes/{name} | Share a volume with another space |


<a id="volumesCreatePost"></a>
# **volumesCreatePost**
> Volume volumesCreatePost(xAuthToken, xAuthProjectId, name, fsName)

Create a volume in a space

This endpoints creates a new volume in your space (corresponding IBM Containers command: &#x60;cf ic volume create VOLNAME&#x60;). A volume is used to persist and access app data between container restarts. Volumes are hosted on file shares that define the available actual storage in Bluemix and the number of input and output transactions per second (IOPS).    After you have created a volume, you must mount it to a container by using the &#x60;--volume&#x60; option in the &#x60;cf ic run&#x60; (single containers) or &#x60;cf ic group create&#x60; (container groups) command. You can also define the volume as part of the HTTP body and send a request to the &#x60;POST /containers/create&#x60; (single containers) or &#x60;POST /containers/groups&#x60; (container groups) endpoints.    Note: If you mount multiple containers in a space to the same volume, they share the data in the volume and can access them anytime. When a container is deleted, the associated volume is not removed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String name = "name_example"; // String | The name of the volume. The name must be unique for a space and can contain uppercase letters, lowercase letters, numbers, underscores (_), and hyphens (-).
    String fsName = "fsName_example"; // String | The name of the file share that the volume is hosted on. File shares can have different storage sizes and IOPS based on the required workload. If this field is left blank, the volume is hosted on the default file share.
    try {
      Volume result = apiInstance.volumesCreatePost(xAuthToken, xAuthProjectId, name, fsName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesCreatePost");
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
| **name** | **String**| The name of the volume. The name must be unique for a space and can contain uppercase letters, lowercase letters, numbers, underscores (_), and hyphens (-). | |
| **fsName** | **String**| The name of the file share that the volume is hosted on. File shares can have different storage sizes and IOPS based on the required workload. If this field is left blank, the volume is hosted on the default file share. | [optional] |

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created. Your volume was successfully created in your space. |  -  |
| **400** | Bad request. Your request could not be processed due to missing parameter. Make sure to enter a name for your volume as part of your query and re-run the request |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **409** | Conflict. A volume with the same name already exists. Choose a new name for your volume and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesJsonGet"></a>
# **volumesJsonGet**
> List&lt;Volume&gt; volumesJsonGet(xAuthToken, xAuthProjectId)

List all volumes for a space

This endpoint returns a list of all volumes that are available in the given space (corresponding IBM Containers command: &#x60;cf ic volume list&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    try {
      List<Volume> result = apiInstance.volumesJsonGet(xAuthToken, xAuthProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesJsonGet");
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

[**List&lt;Volume&gt;**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list containing all volumes of a given space is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesNameDelete"></a>
# **volumesNameDelete**
> volumesNameDelete(xAuthToken, xAuthProjectId, name)

Delete a volume

Delete a volume with a given name from a space (corresponding IBM Containers command: &#x60;cf ic volume rm VOLNAME&#x60;). To delete a volume, all mounted containers must be unmounted first. After the volume is deleted, the data that are stored in the volume are lost. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String name = "name_example"; // String | The name of the volume that you want to delete. Run `cf ic volume list` or call the `GET /volumes/json` endpoint to retrieve a list of all volumes that are available in your space.
    try {
      apiInstance.volumesNameDelete(xAuthToken, xAuthProjectId, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesNameDelete");
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
| **name** | **String**| The name of the volume that you want to delete. Run &#x60;cf ic volume list&#x60; or call the &#x60;GET /volumes/json&#x60; endpoint to retrieve a list of all volumes that are available in your space. | |

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
| **204** | No Content. Your request to delete the volume has successfully been processed.  |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not found. The volume could not be found. Verify that the name is correct by running the &#x60;cf ic volume list&#x60; command or by calling the &#x60;GET /volumes/json&#x60; endpoint. Enter the correct name and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="volumesNameJsonGet"></a>
# **volumesNameJsonGet**
> Volume volumesNameJsonGet(xAuthToken, xAuthProjectId, name)

Retrieve detailed information about a volume. 

Retrieve a detailed list of information about a volume that is identified by the volume name (corresponding IBM Containers command: &#x60;cf ic volume inspect VOLNAME&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String name = "name_example"; // String | The name of the volume, for which you want to retrieve detailed information. Run `cf ic volume list` or call the `GET /volumes/json` endpoint to retrieve a list of all volumes that are available in your space.
    try {
      Volume result = apiInstance.volumesNameJsonGet(xAuthToken, xAuthProjectId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesNameJsonGet");
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
| **name** | **String**| The name of the volume, for which you want to retrieve detailed information. Run &#x60;cf ic volume list&#x60; or call the &#x60;GET /volumes/json&#x60; endpoint to retrieve a list of all volumes that are available in your space. | |

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok. A list with detailed information about the volume is returned.  |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not found. The specified volume could not be found. Verify that the name is correct by running the &#x60;cf ic volume list&#x60; command or by calling the &#x60;GET /volumes/json&#x60; endpoint. Enter the correct name and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesNamePost"></a>
# **volumesNamePost**
> Volume volumesNamePost(xAuthToken, xAuthProjectId, name, updateVolume)

Share a volume with another space

This endpoint provisions an existing volume that was created in one space to another space within the same organization. Single containers and container groups in each space can read and write to the shared volume. The volume remains owned by the original space it was created in, including management and billing. For example, the volume can be deleted from the original space only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String name = "name_example"; // String | The name of the volume that you want to share with another space in your organization.
    UpdateVolume updateVolume = new UpdateVolume(); // UpdateVolume | Input parameter that are required to provision an existing volume to a new space and to unprovision it from a space.
    try {
      Volume result = apiInstance.volumesNamePost(xAuthToken, xAuthProjectId, name, updateVolume);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesNamePost");
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
| **name** | **String**| The name of the volume that you want to share with another space in your organization. | |
| **updateVolume** | [**UpdateVolume**](UpdateVolume.md)| Input parameter that are required to provision an existing volume to a new space and to unprovision it from a space. | |

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok. A list with detailed information about the volume is returned. Review the changes in the &#x60;otherSpaceVisibility&#x60; property. |  -  |
| **400** | Bad request. The data that you entered in the request body are either incomplete or in the wrong format. Be sure to include either the space ID where you want to provision your volume, or the space ID from which you want to unprovision your volume in JSON format.  |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | Not found. The specified volume could not be found. Verify that the name is correct by running the &#x60;cf ic volume list&#x60; command or by calling the &#x60;GET /volumes/json&#x60; endpoint. Enter the correct name and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

