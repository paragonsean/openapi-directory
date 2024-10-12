# FileSharesApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesFsCreatePost**](FileSharesApi.md#volumesFsCreatePost) | **POST** /volumes/fs/create | Create a file share in a space |
| [**volumesFsFlavorsJsonGet**](FileSharesApi.md#volumesFsFlavorsJsonGet) | **GET** /volumes/fs/flavors/json | List available file share sizes |
| [**volumesFsJsonGet**](FileSharesApi.md#volumesFsJsonGet) | **GET** /volumes/fs/json | List available file shares in a space |
| [**volumesFsNameDelete**](FileSharesApi.md#volumesFsNameDelete) | **DELETE** /volumes/fs/{name} | Delete a file share |
| [**volumesFsNameJsonGet**](FileSharesApi.md#volumesFsNameJsonGet) | **GET** /volumes/fs/{name}/json | Inspect a file share |


<a id="volumesFsCreatePost"></a>
# **volumesFsCreatePost**
> volumesFsCreatePost(xAuthToken, xAuthProjectId, fileshareParam)

Create a file share in a space

This endpoint creates a new file share in a space (corresponding IBM Containers command: &#x60;cf ic volume fs-create FSNAME FSSIZE FSIOPS&#x60;).    A file share is a persistent NFS-based (Network File System) storage system that hosts Docker volumes in a Bluemix space and allows a user to store and access container and app-related files. To store files in a file share, you must create a container volume and save the data into this volume.   As soon as you create your first volume in a space with the &#x60;cf ic volume create VOLNAME&#x60; command or the &#x60;POST /volumes/create&#x60; API endpoint, a default file share with 20 GB at 4 IOPS (Input Output operations Per Second) is created at no cost.   The organization manager can create file shares with specific storage size and IOPS to meet the storage needs of the space. File shares can be provisioned in sizes from 20 GB to 12 TB and at IOPS per GB of 0.25, 2 or 4. Run &#x60;cf ic volume fs-flavor-list&#x60; or call the &#x60;GET /volumes/fs/flavors/json&#x60; API endpoint to retrieve a list of available file share sizes. The file share size in relation to the number of IOPS impacts the speed that data can be read and written from and to the container volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    FileshareParam fileshareParam = new FileshareParam(); // FileshareParam | The input parameter to create a new file share in a space.
    try {
      apiInstance.volumesFsCreatePost(xAuthToken, xAuthProjectId, fileshareParam);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#volumesFsCreatePost");
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
| **fileshareParam** | [**FileshareParam**](FileshareParam.md)| The input parameter to create a new file share in a space. | |

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
| **202** | Accepted. A new fileshare has been created.  |  -  |
| **400** | Bad request. The input parameter in the request body are either incomplete or in the wrong format. Be sure to include the file share name, size and number of IOPS as part of your request in JSON format. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. If your access token and space ID are correct, verify that you have been granted organization manager rights. Only organization managers can create file shares in a space. |  -  |
| **409** | Conflict. A file share with the same name already exists. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; API endpoint to get a list with all available file shares in this space. Choose a new name for your file share and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesFsFlavorsJsonGet"></a>
# **volumesFsFlavorsJsonGet**
> List&lt;Integer&gt; volumesFsFlavorsJsonGet(xAuthToken, xAuthProjectId)

List available file share sizes

This endpoint returns a list of available file shares in gigabyte (corresponding IBM Containers command: &#x60;cf ic volume fs-flavor-list&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    try {
      List<Integer> result = apiInstance.volumesFsFlavorsJsonGet(xAuthToken, xAuthProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#volumesFsFlavorsJsonGet");
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

**List&lt;Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of available file share sizes in gigabyte is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesFsJsonGet"></a>
# **volumesFsJsonGet**
> List&lt;Fileshare&gt; volumesFsJsonGet(xAuthToken, xAuthProjectId)

List available file shares in a space

This endpoint returns a list of all file shares that are availble in a space (corresponding IBM Containers command: &#x60;cf ic volume fs-list&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    try {
      List<Fileshare> result = apiInstance.volumesFsJsonGet(xAuthToken, xAuthProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#volumesFsJsonGet");
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

[**List&lt;Fileshare&gt;**](Fileshare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of available file shares is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesFsNameDelete"></a>
# **volumesFsNameDelete**
> volumesFsNameDelete(xAuthToken, xAuthProjectId, name)

Delete a file share

This endpoint deletes a file share from a space (corresponding IBM Containers command: &#x60;cf ic volume fs-rm FSNAME&#x60;).   Before you can delete a file share, all mounted volumes must be deleted first. To delete a volume, run &#x60;cf ic volume rm VOLNAME&#x60; or call the &#x60;DELETE /volumes/{name}&#x60; API endpoint.    **Note:** To delete a file share you must have been granted organization developer rights.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String name = "name_example"; // String | The name of the file share that you want to delete. Run `cf ic volume fs-list` or call the `GET /volumes/fs/json` API endpoint to retrieve a list of available file shares in your space.
    try {
      apiInstance.volumesFsNameDelete(xAuthToken, xAuthProjectId, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#volumesFsNameDelete");
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
| **name** | **String**| The name of the file share that you want to delete. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; API endpoint to retrieve a list of available file shares in your space. | |

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
| **204** | No Content. The file share was successfully deleted. |  -  |
| **400** | Bad request. The specified file share could not be deleted as it has mounted volumes. Run &#x60;cf ic volume rm VOLNAME&#x60; or call the &#x60;DELETE /volumes/{name}&#x60; API endpoint to delete the volume. After all mounted volumes are deleted, delete the file share.  |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | The specified file share name could not be found. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; endpoint to retrieve a list of available file shares in your space. Enter the name for your file share and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

<a id="volumesFsNameJsonGet"></a>
# **volumesFsNameJsonGet**
> List&lt;GetFileshareDetails&gt; volumesFsNameJsonGet(xAuthToken, xAuthProjectId, name)

Inspect a file share

This endpoint returns detailed information about a file share (corresponding IBM Containers command: &#x60;cf ic volume fs-inspect FSNAME&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
    String name = "name_example"; // String | The name of the file share that you want to inspect. Run `cf ic volume fs-list` or call the `GET /volumes/fs/json` endpoint to retrieve a list of available file shares in your space.
    try {
      List<GetFileshareDetails> result = apiInstance.volumesFsNameJsonGet(xAuthToken, xAuthProjectId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#volumesFsNameJsonGet");
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
| **name** | **String**| The name of the file share that you want to inspect. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; endpoint to retrieve a list of available file shares in your space. | |

### Return type

[**List&lt;GetFileshareDetails&gt;**](GetFileshareDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Detailed information about a file share is returned. |  -  |
| **401** | Authentication failed. The Access Token is invalid, or the Space ID that you entered could not be found. Run &#x60;cf oauth-token&#x60; to retrieve your access token. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. |  -  |
| **404** | The specified file share name could not be found. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; endpoint to retrieve a list of available file shares in your space. Enter the name for your file share and re-run the API call. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support.  |  -  |

