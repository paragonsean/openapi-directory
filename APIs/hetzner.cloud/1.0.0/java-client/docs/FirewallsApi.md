# FirewallsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**firewallsGet**](FirewallsApi.md#firewallsGet) | **GET** /firewalls | Get all Firewalls |
| [**firewallsIdDelete**](FirewallsApi.md#firewallsIdDelete) | **DELETE** /firewalls/{id} | Delete a Firewall |
| [**firewallsIdGet**](FirewallsApi.md#firewallsIdGet) | **GET** /firewalls/{id} | Get a Firewall |
| [**firewallsIdPut**](FirewallsApi.md#firewallsIdPut) | **PUT** /firewalls/{id} | Update a Firewall |
| [**firewallsPost**](FirewallsApi.md#firewallsPost) | **POST** /firewalls | Create a Firewall |


<a id="firewallsGet"></a>
# **firewallsGet**
> FirewallsResponse firewallsGet(sort, name, labelSelector)

Get all Firewalls

Returns all Firewall objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallsApi apiInstance = new FirewallsApi(defaultClient);
    String sort = "id"; // String | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    try {
      FirewallsResponse result = apiInstance.firewallsGet(sort, name, labelSelector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallsApi#firewallsGet");
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

[**FirewallsResponse**](FirewallsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;firewalls&#x60; key contains an array of Firewall objects |  -  |

<a id="firewallsIdDelete"></a>
# **firewallsIdDelete**
> firewallsIdDelete(id)

Delete a Firewall

Deletes a Firewall.  #### Call specific error codes  | Code                 | Description                               | |--------------------- |-------------------------------------------| | &#x60;resource_in_use&#x60;    | Firewall must not be in use to be deleted | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallsApi apiInstance = new FirewallsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      apiInstance.firewallsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallsApi#firewallsIdDelete");
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
| **204** | Firewall deleted |  -  |

<a id="firewallsIdGet"></a>
# **firewallsIdGet**
> FirewallResponse firewallsIdGet(id)

Get a Firewall

Gets a specific Firewall object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallsApi apiInstance = new FirewallsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      FirewallResponse result = apiInstance.firewallsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallsApi#firewallsIdGet");
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

[**FirewallResponse**](FirewallResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;firewall&#x60; key contains a Firewall object |  -  |

<a id="firewallsIdPut"></a>
# **firewallsIdPut**
> FirewallResponse firewallsIdPut(id, updateFirewallRequest)

Update a Firewall

Updates the Firewall.  Note that when updating labels, the Firewall&#39;s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Firewall object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallsApi apiInstance = new FirewallsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    UpdateFirewallRequest updateFirewallRequest = new UpdateFirewallRequest(); // UpdateFirewallRequest | 
    try {
      FirewallResponse result = apiInstance.firewallsIdPut(id, updateFirewallRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallsApi#firewallsIdPut");
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
| **updateFirewallRequest** | [**UpdateFirewallRequest**](UpdateFirewallRequest.md)|  | [optional] |

### Return type

[**FirewallResponse**](FirewallResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;firewall&#x60; key contains the Firewall that was just updated |  -  |

<a id="firewallsPost"></a>
# **firewallsPost**
> CreateFirewallResponse firewallsPost(createFirewallRequest)

Create a Firewall

Creates a new Firewall.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_already_added&#x60;        | Server added more than one time to resource                   | | &#x60;incompatible_network_type&#x60;   | The Network type is incompatible for the given resource       | | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallsApi apiInstance = new FirewallsApi(defaultClient);
    CreateFirewallRequest createFirewallRequest = new CreateFirewallRequest(); // CreateFirewallRequest | 
    try {
      CreateFirewallResponse result = apiInstance.firewallsPost(createFirewallRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallsApi#firewallsPost");
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
| **createFirewallRequest** | [**CreateFirewallRequest**](CreateFirewallRequest.md)|  | [optional] |

### Return type

[**CreateFirewallResponse**](CreateFirewallResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;firewall&#x60; key contains the Firewall that was just created |  -  |

