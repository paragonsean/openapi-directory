# ServersApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serversGet**](ServersApi.md#serversGet) | **GET** /servers | Get all Servers |
| [**serversIdDelete**](ServersApi.md#serversIdDelete) | **DELETE** /servers/{id} | Delete a Server |
| [**serversIdGet**](ServersApi.md#serversIdGet) | **GET** /servers/{id} | Get a Server |
| [**serversIdMetricsGet**](ServersApi.md#serversIdMetricsGet) | **GET** /servers/{id}/metrics | Get Metrics for a Server |
| [**serversIdPut**](ServersApi.md#serversIdPut) | **PUT** /servers/{id} | Update a Server |
| [**serversPost**](ServersApi.md#serversPost) | **POST** /servers | Create a Server |


<a id="serversGet"></a>
# **serversGet**
> ServersGet200Response serversGet(name, labelSelector, sort, status)

Get all Servers

Returns all existing Server objects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    String sort = "id"; // String | Can be used multiple times.
    String status = "initializing"; // String | Can be used multiple times. The response will only contain Server matching the status
    try {
      ServersGet200Response result = apiInstance.serversGet(name, labelSelector, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversGet");
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
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc, created, created:asc, created:desc] |
| **status** | **String**| Can be used multiple times. The response will only contain Server matching the status | [optional] [enum: initializing, starting, running, stopping, false, deleting, rebuilding, migrating, unknown] |

### Return type

[**ServersGet200Response**](ServersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paged array of servers |  * x-next - A link to the next page of responses <br>  |

<a id="serversIdDelete"></a>
# **serversIdDelete**
> ServersIdDelete200Response serversIdDelete(id)

Delete a Server

Deletes a Server. This immediately removes the Server from your account, and it is no longer accessible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServersApi apiInstance = new ServersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Server
    try {
      ServersIdDelete200Response result = apiInstance.serversIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversIdDelete");
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
| **id** | **Integer**| ID of the Server | |

### Return type

[**ServersIdDelete200Response**](ServersIdDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;action&#x60; key in the reply contains an Action object with this structure |  -  |

<a id="serversIdGet"></a>
# **serversIdGet**
> ServersIdGet200Response serversIdGet(id)

Get a Server

Returns a specific Server object. The Server must exist inside the Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServersApi apiInstance = new ServersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Server
    try {
      ServersIdGet200Response result = apiInstance.serversIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversIdGet");
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
| **id** | **Integer**| ID of the Server | |

### Return type

[**ServersIdGet200Response**](ServersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;server&#x60; key in the reply contains a Server object with this structure |  -  |

<a id="serversIdMetricsGet"></a>
# **serversIdMetricsGet**
> LoadBalancersIdMetricsGet200Response serversIdMetricsGet(id, type, start, end, step)

Get Metrics for a Server

Get Metrics for specified Server.  You must specify the type of metric to get: cpu, disk or network. You can also specify more than one type by comma separation, e.g. cpu,disk.  Depending on the type you will get different time series data  | Type    | Timeseries              | Unit      | Description                                          | |---------|-------------------------|-----------|------------------------------------------------------| | cpu     | cpu                     | percent   | Percent CPU usage                                    | | disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              | |         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             | |         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                | |         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             | | network | network.0.pps.in        | packets/s | Public Network interface packets per second received | |         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     | |         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            | |         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |  Metrics are available for the last 30 days only.  If you do not provide the step argument we will automatically adjust it so that a maximum of 200 samples are returned.  We limit the number of samples returned to a maximum of 500 and will adjust the step parameter accordingly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServersApi apiInstance = new ServersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Server
    String type = "cpu"; // String | Type of metrics to get
    String start = "start_example"; // String | Start of period to get Metrics for (in ISO-8601 format)
    String end = "end_example"; // String | End of period to get Metrics for (in ISO-8601 format)
    String step = "step_example"; // String | Resolution of results in seconds
    try {
      LoadBalancersIdMetricsGet200Response result = apiInstance.serversIdMetricsGet(id, type, start, end, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversIdMetricsGet");
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
| **id** | **Integer**| ID of the Server | |
| **type** | **String**| Type of metrics to get | [enum: cpu, disk, network] |
| **start** | **String**| Start of period to get Metrics for (in ISO-8601 format) | |
| **end** | **String**| End of period to get Metrics for (in ISO-8601 format) | |
| **step** | **String**| Resolution of results in seconds | [optional] |

### Return type

[**LoadBalancersIdMetricsGet200Response**](LoadBalancersIdMetricsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;metrics&#x60; key in the reply contains a metrics object with this structure |  -  |

<a id="serversIdPut"></a>
# **serversIdPut**
> ServersIdGet200Response serversIdPut(id, updateServerRequest)

Update a Server

Updates a Server. You can update a Server’s name and a Server’s labels. Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes). Also note that when updating labels, the Server’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServersApi apiInstance = new ServersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Server
    UpdateServerRequest updateServerRequest = new UpdateServerRequest(); // UpdateServerRequest | 
    try {
      ServersIdGet200Response result = apiInstance.serversIdPut(id, updateServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversIdPut");
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
| **id** | **Integer**| ID of the Server | |
| **updateServerRequest** | [**UpdateServerRequest**](UpdateServerRequest.md)|  | [optional] |

### Return type

[**ServersIdGet200Response**](ServersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;server&#x60; key in the reply contains the updated Server |  -  |

<a id="serversPost"></a>
# **serversPost**
> CreateServerResponse serversPost(createServerRequest)

Create a Server

Creates a new Server. Returns preliminary information about the Server as well as an Action that covers progress of creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServersApi apiInstance = new ServersApi(defaultClient);
    CreateServerRequest createServerRequest = new CreateServerRequest(); // CreateServerRequest | Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).  For `server_type` you can either use the ID as listed in `/server_types` or its name.  For `image` you can either use the ID as listed in `/images` or its name.  If you want to create the Server in a Location, you must set `location` to the ID or name as listed in `/locations`. This is the recommended way. You can be even more specific by setting `datacenter` to the ID or name as listed in `/datacenters`. However we only recommend this if you want to assign a specific Primary IP to the Server which is located in the specified Datacenter.  Some properties like `start_after_create` or `automount` will trigger Actions after the Server is created. Those Actions are listed in the `next_actions` field in the response.  For accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in `ssh_keys`. If you do not specify any `ssh_keys` we will generate a root password for you and return it in the response.  Please note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.  #### Call specific error codes  | Code                             | Description                                                | |----------------------------------|------------------------------------------------------------| | `placement_error`                | An error during the placement occurred                     | | `primary_ip_assigned`            | The specified Primary IP is already assigned to a server   | | `primary_ip_datacenter_mismatch` | The specified Primary IP is in a different datacenter      | | `primary_ip_version_mismatch`    | The specified Primary IP has the wrong IP Version          | 
    try {
      CreateServerResponse result = apiInstance.serversPost(createServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversPost");
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
| **createServerRequest** | [**CreateServerRequest**](CreateServerRequest.md)| Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).  For &#x60;server_type&#x60; you can either use the ID as listed in &#x60;/server_types&#x60; or its name.  For &#x60;image&#x60; you can either use the ID as listed in &#x60;/images&#x60; or its name.  If you want to create the Server in a Location, you must set &#x60;location&#x60; to the ID or name as listed in &#x60;/locations&#x60;. This is the recommended way. You can be even more specific by setting &#x60;datacenter&#x60; to the ID or name as listed in &#x60;/datacenters&#x60;. However we only recommend this if you want to assign a specific Primary IP to the Server which is located in the specified Datacenter.  Some properties like &#x60;start_after_create&#x60; or &#x60;automount&#x60; will trigger Actions after the Server is created. Those Actions are listed in the &#x60;next_actions&#x60; field in the response.  For accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in &#x60;ssh_keys&#x60;. If you do not specify any &#x60;ssh_keys&#x60; we will generate a root password for you and return it in the response.  Please note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.  #### Call specific error codes  | Code                             | Description                                                | |----------------------------------|------------------------------------------------------------| | &#x60;placement_error&#x60;                | An error during the placement occurred                     | | &#x60;primary_ip_assigned&#x60;            | The specified Primary IP is already assigned to a server   | | &#x60;primary_ip_datacenter_mismatch&#x60; | The specified Primary IP is in a different datacenter      | | &#x60;primary_ip_version_mismatch&#x60;    | The specified Primary IP has the wrong IP Version          |  | [optional] |

### Return type

[**CreateServerResponse**](CreateServerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;server&#x60; key in the reply contains a Server object with this structure |  -  |

