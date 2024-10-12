# PrimaryIpsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**primaryIpsGet**](PrimaryIpsApi.md#primaryIpsGet) | **GET** /primary_ips | Get all Primary IPs |
| [**primaryIpsIdDelete**](PrimaryIpsApi.md#primaryIpsIdDelete) | **DELETE** /primary_ips/{id} | Delete a Primary IP |
| [**primaryIpsIdGet**](PrimaryIpsApi.md#primaryIpsIdGet) | **GET** /primary_ips/{id} | Get a Primary IP |
| [**primaryIpsIdPut**](PrimaryIpsApi.md#primaryIpsIdPut) | **PUT** /primary_ips/{id} | Update a Primary IP |
| [**primaryIpsPost**](PrimaryIpsApi.md#primaryIpsPost) | **POST** /primary_ips | Create a Primary IP |


<a id="primaryIpsGet"></a>
# **primaryIpsGet**
> PrimaryIPsResponse primaryIpsGet(name, labelSelector, ip, sort)

Get all Primary IPs

Returns all Primary IP objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpsApi apiInstance = new PrimaryIpsApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    String ip = "127.0.0.1"; // String | Can be used to filter resources by their ip. The response will only contain the resources matching the specified ip.
    String sort = "id"; // String | Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc
    try {
      PrimaryIPsResponse result = apiInstance.primaryIpsGet(name, labelSelector, ip, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpsApi#primaryIpsGet");
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
| **ip** | **String**| Can be used to filter resources by their ip. The response will only contain the resources matching the specified ip. | [optional] |
| **sort** | **String**| Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc | [optional] [enum: id, id:asc, id:desc, created, created:asc, created:desc] |

### Return type

[**PrimaryIPsResponse**](PrimaryIPsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;primary_ips&#x60; key contains an array of Primary IP objects |  -  |

<a id="primaryIpsIdDelete"></a>
# **primaryIpsIdDelete**
> primaryIpsIdDelete(id)

Delete a Primary IP

Deletes a Primary IP.  The Primary IP may be assigned to a Server. In this case it is unassigned automatically. The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpsApi apiInstance = new PrimaryIpsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      apiInstance.primaryIpsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpsApi#primaryIpsIdDelete");
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
| **id** | **Integer**| ID of the resource | |

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
| **204** | Primary IP deleted |  -  |

<a id="primaryIpsIdGet"></a>
# **primaryIpsIdGet**
> PrimaryIPResponse primaryIpsIdGet(id)

Get a Primary IP

Returns a specific Primary IP object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpsApi apiInstance = new PrimaryIpsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      PrimaryIPResponse result = apiInstance.primaryIpsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpsApi#primaryIpsIdGet");
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
| **id** | **Integer**| ID of the resource | |

### Return type

[**PrimaryIPResponse**](PrimaryIPResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;primary_ip&#x60; key contains a Primary IP object |  -  |

<a id="primaryIpsIdPut"></a>
# **primaryIpsIdPut**
> PrimaryIPResponse primaryIpsIdPut(id, updatePrimaryIPRequest)

Update a Primary IP

Updates the Primary IP.  Note that when updating labels, the Primary IP&#39;s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  If the Primary IP object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpsApi apiInstance = new PrimaryIpsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    UpdatePrimaryIPRequest updatePrimaryIPRequest = new UpdatePrimaryIPRequest(); // UpdatePrimaryIPRequest | 
    try {
      PrimaryIPResponse result = apiInstance.primaryIpsIdPut(id, updatePrimaryIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpsApi#primaryIpsIdPut");
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
| **id** | **Integer**| ID of the resource | |
| **updatePrimaryIPRequest** | [**UpdatePrimaryIPRequest**](UpdatePrimaryIPRequest.md)|  | [optional] |

### Return type

[**PrimaryIPResponse**](PrimaryIPResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;primary_ip&#x60; key contains the Primary IP that was just updated |  -  |

<a id="primaryIpsPost"></a>
# **primaryIpsPost**
> CreatePrimaryIPResponse primaryIpsPost(createPrimaryIPRequest)

Create a Primary IP

Creates a new Primary IP, optionally assigned to a Server.  If you want to create a Primary IP that is not assigned to a Server, you need to provide the &#x60;datacenter&#x60; key instead of &#x60;assignee_id&#x60;. This can be either the ID or the name of the Datacenter this Primary IP shall be created in.  Note that a Primary IP can only be assigned to a Server in the same Datacenter later on.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;          | The specified server is running, but needs to be powered off  | | &#x60;server_has_ipv4&#x60;             | The server already has an ipv4 address                        | | &#x60;server_has_ipv6&#x60;             | The server already has an ipv6 address                        | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpsApi apiInstance = new PrimaryIpsApi(defaultClient);
    CreatePrimaryIPRequest createPrimaryIPRequest = new CreatePrimaryIPRequest(); // CreatePrimaryIPRequest | The `type` argument is required while `datacenter` and `assignee_id` are mutually exclusive.
    try {
      CreatePrimaryIPResponse result = apiInstance.primaryIpsPost(createPrimaryIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpsApi#primaryIpsPost");
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
| **createPrimaryIPRequest** | [**CreatePrimaryIPRequest**](CreatePrimaryIPRequest.md)| The &#x60;type&#x60; argument is required while &#x60;datacenter&#x60; and &#x60;assignee_id&#x60; are mutually exclusive. | [optional] |

### Return type

[**CreatePrimaryIPResponse**](CreatePrimaryIPResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;primary_ip&#x60; key contains the Primary IP that was just created |  -  |

