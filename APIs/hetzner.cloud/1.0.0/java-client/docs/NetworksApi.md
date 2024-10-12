# NetworksApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networksGet**](NetworksApi.md#networksGet) | **GET** /networks | Get all Networks |
| [**networksIdDelete**](NetworksApi.md#networksIdDelete) | **DELETE** /networks/{id} | Delete a Network |
| [**networksIdGet**](NetworksApi.md#networksIdGet) | **GET** /networks/{id} | Get a Network |
| [**networksIdPut**](NetworksApi.md#networksIdPut) | **PUT** /networks/{id} | Update a Network |
| [**networksPost**](NetworksApi.md#networksPost) | **POST** /networks | Create a Network |


<a id="networksGet"></a>
# **networksGet**
> NetworksGet200Response networksGet(name, labelSelector)

Get all Networks

Gets all existing networks that you have available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter networks by their name. The response will only contain the networks matching the specified name.
    String labelSelector = "labelSelector_example"; // String | Can be used to filter networks by labels. The response will only contain networks with a matching label selector pattern.
    try {
      NetworksGet200Response result = apiInstance.networksGet(name, labelSelector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networksGet");
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
| **name** | **String**| Can be used to filter networks by their name. The response will only contain the networks matching the specified name. | [optional] |
| **labelSelector** | **String**| Can be used to filter networks by labels. The response will only contain networks with a matching label selector pattern. | [optional] |

### Return type

[**NetworksGet200Response**](NetworksGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;networks&#x60; key contains a list of networks |  -  |

<a id="networksIdDelete"></a>
# **networksIdDelete**
> networksIdDelete(id)

Delete a Network

Deletes a network. If there are Servers attached they will be detached in the background.  Note: if the network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    Integer id = 56; // Integer | ID of the network
    try {
      apiInstance.networksIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networksIdDelete");
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
| **id** | **Integer**| ID of the network | |

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
| **204** | Network deleted |  -  |

<a id="networksIdGet"></a>
# **networksIdGet**
> NetworksPost201Response networksIdGet(id)

Get a Network

Gets a specific network object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    Integer id = 56; // Integer | ID of the network
    try {
      NetworksPost201Response result = apiInstance.networksIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networksIdGet");
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
| **id** | **Integer**| ID of the network | |

### Return type

[**NetworksPost201Response**](NetworksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;network&#x60; key contains the network |  -  |

<a id="networksIdPut"></a>
# **networksIdPut**
> NetworksPost201Response networksIdPut(id, updateNetworkRequest)

Update a Network

Updates the network properties.  Note that when updating labels, the network’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    Integer id = 56; // Integer | ID of the network
    UpdateNetworkRequest updateNetworkRequest = new UpdateNetworkRequest(); // UpdateNetworkRequest | 
    try {
      NetworksPost201Response result = apiInstance.networksIdPut(id, updateNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networksIdPut");
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
| **id** | **Integer**| ID of the network | |
| **updateNetworkRequest** | [**UpdateNetworkRequest**](UpdateNetworkRequest.md)|  | [optional] |

### Return type

[**NetworksPost201Response**](NetworksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;network&#x60; key contains the updated network |  -  |

<a id="networksPost"></a>
# **networksPost**
> NetworksPost201Response networksPost(createNetworkRequest)

Create a Network

Creates a network with the specified &#x60;ip_range&#x60;.  You may specify one or more &#x60;subnets&#x60;. You can also add more Subnets later by using the [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network). If you do not specify an &#x60;ip_range&#x60; in the subnet we will automatically pick the first available /24 range for you.  You may specify one or more routes in &#x60;routes&#x60;. You can also add more routes later by using the [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    CreateNetworkRequest createNetworkRequest = new CreateNetworkRequest(); // CreateNetworkRequest | 
    try {
      NetworksPost201Response result = apiInstance.networksPost(createNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networksPost");
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
| **createNetworkRequest** | [**CreateNetworkRequest**](CreateNetworkRequest.md)|  | [optional] |

### Return type

[**NetworksPost201Response**](NetworksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;network&#x60; key contains the network that was just created |  -  |

