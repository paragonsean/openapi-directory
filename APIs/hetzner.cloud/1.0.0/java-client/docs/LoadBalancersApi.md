# LoadBalancersApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loadBalancersGet**](LoadBalancersApi.md#loadBalancersGet) | **GET** /load_balancers | Get all Load Balancers |
| [**loadBalancersIdDelete**](LoadBalancersApi.md#loadBalancersIdDelete) | **DELETE** /load_balancers/{id} | Delete a Load Balancer |
| [**loadBalancersIdGet**](LoadBalancersApi.md#loadBalancersIdGet) | **GET** /load_balancers/{id} | Get a Load Balancer |
| [**loadBalancersIdMetricsGet**](LoadBalancersApi.md#loadBalancersIdMetricsGet) | **GET** /load_balancers/{id}/metrics | Get Metrics for a LoadBalancer |
| [**loadBalancersIdPut**](LoadBalancersApi.md#loadBalancersIdPut) | **PUT** /load_balancers/{id} | Update a Load Balancer |
| [**loadBalancersPost**](LoadBalancersApi.md#loadBalancersPost) | **POST** /load_balancers | Create a Load Balancer |


<a id="loadBalancersGet"></a>
# **loadBalancersGet**
> LoadBalancersGet200Response loadBalancersGet(sort, name, labelSelector)

Get all Load Balancers

Gets all existing Load Balancers that you have available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancersApi apiInstance = new LoadBalancersApi(defaultClient);
    String sort = "id"; // String | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    try {
      LoadBalancersGet200Response result = apiInstance.loadBalancersGet(sort, name, labelSelector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancersApi#loadBalancersGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc, created, created:asc, created:desc] |
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |

### Return type

[**LoadBalancersGet200Response**](LoadBalancersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;load_balancers&#x60; key contains a list of Load Balancers |  -  |

<a id="loadBalancersIdDelete"></a>
# **loadBalancersIdDelete**
> loadBalancersIdDelete(id)

Delete a Load Balancer

Deletes a Load Balancer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancersApi apiInstance = new LoadBalancersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    try {
      apiInstance.loadBalancersIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancersApi#loadBalancersIdDelete");
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
| **id** | **Integer**| ID of the Load Balancer | |

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
| **204** | Load Balancer deleted |  -  |

<a id="loadBalancersIdGet"></a>
# **loadBalancersIdGet**
> LoadBalancersIdGet200Response loadBalancersIdGet(id)

Get a Load Balancer

Gets a specific Load Balancer object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancersApi apiInstance = new LoadBalancersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    try {
      LoadBalancersIdGet200Response result = apiInstance.loadBalancersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancersApi#loadBalancersIdGet");
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
| **id** | **Integer**| ID of the Load Balancer | |

### Return type

[**LoadBalancersIdGet200Response**](LoadBalancersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;load_balancer&#x60; key contains the Load Balancer |  -  |

<a id="loadBalancersIdMetricsGet"></a>
# **loadBalancersIdMetricsGet**
> LoadBalancersIdMetricsGet200Response loadBalancersIdMetricsGet(id, type, start, end, step)

Get Metrics for a LoadBalancer

You must specify the type of metric to get: &#x60;open_connections&#x60;, &#x60;connections_per_second&#x60;, &#x60;requests_per_second&#x60; or &#x60;bandwidth&#x60;. You can also specify more than one type by comma separation, e.g. &#x60;requests_per_second,bandwidth&#x60;.  Depending on the type you will get different time series data:  |Type | Timeseries | Unit | Description | |---- |------------|------|-------------| | open_connections | open_connections | number | Open connections | | connections_per_second | connections_per_second | connections/s | Connections per second | | requests_per_second | requests_per_second | requests/s | Requests per second | | bandwidth | bandwidth.in | bytes/s | Ingress bandwidth | || bandwidth.out | bytes/s | Egress bandwidth |  Metrics are available for the last 30 days only.  If you do not provide the step argument we will automatically adjust it so that 200 samples are returned.  We limit the number of samples to a maximum of 500 and will adjust the step parameter accordingly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancersApi apiInstance = new LoadBalancersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    String type = "open_connections"; // String | Type of metrics to get
    String start = "start_example"; // String | Start of period to get Metrics for (in ISO-8601 format)
    String end = "end_example"; // String | End of period to get Metrics for (in ISO-8601 format)
    String step = "step_example"; // String | Resolution of results in seconds
    try {
      LoadBalancersIdMetricsGet200Response result = apiInstance.loadBalancersIdMetricsGet(id, type, start, end, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancersApi#loadBalancersIdMetricsGet");
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
| **id** | **Integer**| ID of the Load Balancer | |
| **type** | **String**| Type of metrics to get | [enum: open_connections, connections_per_second, requests_per_second, bandwidth] |
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

<a id="loadBalancersIdPut"></a>
# **loadBalancersIdPut**
> LoadBalancersIdGet200Response loadBalancersIdPut(id, loadBalancersIdPutRequest)

Update a Load Balancer

Updates a Load Balancer. You can update a Load Balancer’s name and a Load Balancer’s labels.  Note that when updating labels, the Load Balancer’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Load Balancer object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancersApi apiInstance = new LoadBalancersApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancersIdPutRequest loadBalancersIdPutRequest = new LoadBalancersIdPutRequest(); // LoadBalancersIdPutRequest | 
    try {
      LoadBalancersIdGet200Response result = apiInstance.loadBalancersIdPut(id, loadBalancersIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancersApi#loadBalancersIdPut");
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
| **id** | **Integer**| ID of the Load Balancer | |
| **loadBalancersIdPutRequest** | [**LoadBalancersIdPutRequest**](LoadBalancersIdPutRequest.md)|  | [optional] |

### Return type

[**LoadBalancersIdGet200Response**](LoadBalancersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;load_balancer&#x60; key contains the updated Load Balancer |  -  |

<a id="loadBalancersPost"></a>
# **loadBalancersPost**
> LoadBalancersPost201Response loadBalancersPost(createLoadBalancerRequest)

Create a Load Balancer

Creates a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP is not owned by the owner of the project of the Load Balancer                                  | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;source_port_already_used&#x60;              | The source port you are trying to add is already in use                                               | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancersApi apiInstance = new LoadBalancersApi(defaultClient);
    CreateLoadBalancerRequest createLoadBalancerRequest = new CreateLoadBalancerRequest(); // CreateLoadBalancerRequest | 
    try {
      LoadBalancersPost201Response result = apiInstance.loadBalancersPost(createLoadBalancerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancersApi#loadBalancersPost");
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
| **createLoadBalancerRequest** | [**CreateLoadBalancerRequest**](CreateLoadBalancerRequest.md)|  | [optional] |

### Return type

[**LoadBalancersPost201Response**](LoadBalancersPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;load_balancer&#x60; key contains the Load Balancer that was just created |  -  |

