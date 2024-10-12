# LoadBalancerActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loadBalancersIdActionsActionIdGet**](LoadBalancerActionsApi.md#loadBalancersIdActionsActionIdGet) | **GET** /load_balancers/{id}/actions/{action_id} | Get an Action for a Load Balancer |
| [**loadBalancersIdActionsAddServicePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsAddServicePost) | **POST** /load_balancers/{id}/actions/add_service | Add Service |
| [**loadBalancersIdActionsAddTargetPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsAddTargetPost) | **POST** /load_balancers/{id}/actions/add_target | Add Target |
| [**loadBalancersIdActionsAttachToNetworkPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsAttachToNetworkPost) | **POST** /load_balancers/{id}/actions/attach_to_network | Attach a Load Balancer to a Network |
| [**loadBalancersIdActionsChangeAlgorithmPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeAlgorithmPost) | **POST** /load_balancers/{id}/actions/change_algorithm | Change Algorithm |
| [**loadBalancersIdActionsChangeDnsPtrPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeDnsPtrPost) | **POST** /load_balancers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Load Balancer |
| [**loadBalancersIdActionsChangeProtectionPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeProtectionPost) | **POST** /load_balancers/{id}/actions/change_protection | Change Load Balancer Protection |
| [**loadBalancersIdActionsChangeTypePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeTypePost) | **POST** /load_balancers/{id}/actions/change_type | Change the Type of a Load Balancer |
| [**loadBalancersIdActionsDeleteServicePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsDeleteServicePost) | **POST** /load_balancers/{id}/actions/delete_service | Delete Service |
| [**loadBalancersIdActionsDetachFromNetworkPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsDetachFromNetworkPost) | **POST** /load_balancers/{id}/actions/detach_from_network | Detach a Load Balancer from a Network |
| [**loadBalancersIdActionsDisablePublicInterfacePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsDisablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/disable_public_interface | Disable the public interface of a Load Balancer |
| [**loadBalancersIdActionsEnablePublicInterfacePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsEnablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/enable_public_interface | Enable the public interface of a Load Balancer |
| [**loadBalancersIdActionsGet**](LoadBalancerActionsApi.md#loadBalancersIdActionsGet) | **GET** /load_balancers/{id}/actions | Get all Actions for a Load Balancer |
| [**loadBalancersIdActionsRemoveTargetPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsRemoveTargetPost) | **POST** /load_balancers/{id}/actions/remove_target | Remove Target |
| [**loadBalancersIdActionsUpdateServicePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsUpdateServicePost) | **POST** /load_balancers/{id}/actions/update_service | Update Service |


<a id="loadBalancersIdActionsActionIdGet"></a>
# **loadBalancersIdActionsActionIdGet**
> ActionResponse loadBalancersIdActionsActionIdGet(id, actionId)

Get an Action for a Load Balancer

Returns a specific Action for a Load Balancer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsActionIdGet");
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
| **actionId** | **Integer**| ID of the Action | |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;action&#x60; key contains the Load Balancer Action |  -  |

<a id="loadBalancersIdActionsAddServicePost"></a>
# **loadBalancersIdActionsAddServicePost**
> ActionResponse loadBalancersIdActionsAddServicePost(id, loadBalancerService)

Add Service

Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancerService loadBalancerService = new LoadBalancerService(); // LoadBalancerService | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsAddServicePost(id, loadBalancerService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsAddServicePost");
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
| **loadBalancerService** | [**LoadBalancerService**](LoadBalancerService.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;add_service&#x60; Action |  -  |

<a id="loadBalancersIdActionsAddTargetPost"></a>
# **loadBalancersIdActionsAddTargetPost**
> ActionResponse loadBalancersIdActionsAddTargetPost(id, addTargetRequest)

Add Target

Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    AddTargetRequest addTargetRequest = new AddTargetRequest(); // AddTargetRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsAddTargetPost(id, addTargetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsAddTargetPost");
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
| **addTargetRequest** | [**AddTargetRequest**](AddTargetRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;add_target&#x60; Action |  -  |

<a id="loadBalancersIdActionsAttachToNetworkPost"></a>
# **loadBalancersIdActionsAttachToNetworkPost**
> ActionResponse loadBalancersIdActionsAttachToNetworkPost(id, loadBalancersIdActionsAttachToNetworkPostRequest)

Attach a Load Balancer to a Network

Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest = new LoadBalancersIdActionsAttachToNetworkPostRequest(); // LoadBalancersIdActionsAttachToNetworkPostRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsAttachToNetworkPost(id, loadBalancersIdActionsAttachToNetworkPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsAttachToNetworkPost");
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
| **loadBalancersIdActionsAttachToNetworkPostRequest** | [**LoadBalancersIdActionsAttachToNetworkPostRequest**](LoadBalancersIdActionsAttachToNetworkPostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;attach_to_network&#x60; Action |  -  |

<a id="loadBalancersIdActionsChangeAlgorithmPost"></a>
# **loadBalancersIdActionsChangeAlgorithmPost**
> ActionResponse loadBalancersIdActionsChangeAlgorithmPost(id, loadBalancersIdActionsChangeAlgorithmPostRequest)

Change Algorithm

Change the algorithm that determines to which target new requests are sent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest = new LoadBalancersIdActionsChangeAlgorithmPostRequest(); // LoadBalancersIdActionsChangeAlgorithmPostRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsChangeAlgorithmPost(id, loadBalancersIdActionsChangeAlgorithmPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsChangeAlgorithmPost");
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
| **loadBalancersIdActionsChangeAlgorithmPostRequest** | [**LoadBalancersIdActionsChangeAlgorithmPostRequest**](LoadBalancersIdActionsChangeAlgorithmPostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;change_algorithm&#x60; Action |  -  |

<a id="loadBalancersIdActionsChangeDnsPtrPost"></a>
# **loadBalancersIdActionsChangeDnsPtrPost**
> ActionResponse loadBalancersIdActionsChangeDnsPtrPost(id, changeLoadbalancerDnsPtrRequest)

Change reverse DNS entry for this Load Balancer

Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest = new ChangeLoadbalancerDnsPtrRequest(); // ChangeLoadbalancerDnsPtrRequest | Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsChangeDnsPtrPost(id, changeLoadbalancerDnsPtrRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsChangeDnsPtrPost");
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
| **changeLoadbalancerDnsPtrRequest** | [**ChangeLoadbalancerDnsPtrRequest**](ChangeLoadbalancerDnsPtrRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key in the reply contains an Action object with this structure |  -  |

<a id="loadBalancersIdActionsChangeProtectionPost"></a>
# **loadBalancersIdActionsChangeProtectionPost**
> ActionResponse loadBalancersIdActionsChangeProtectionPost(id, loadBalancersIdActionsChangeProtectionPostRequest)

Change Load Balancer Protection

Changes the protection configuration of a Load Balancer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest = new LoadBalancersIdActionsChangeProtectionPostRequest(); // LoadBalancersIdActionsChangeProtectionPostRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsChangeProtectionPost(id, loadBalancersIdActionsChangeProtectionPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsChangeProtectionPost");
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
| **loadBalancersIdActionsChangeProtectionPostRequest** | [**LoadBalancersIdActionsChangeProtectionPostRequest**](LoadBalancersIdActionsChangeProtectionPostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action |  -  |

<a id="loadBalancersIdActionsChangeTypePost"></a>
# **loadBalancersIdActionsChangeTypePost**
> ActionResponse loadBalancersIdActionsChangeTypePost(id, changeTypeRequest)

Change the Type of a Load Balancer

Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    ChangeTypeRequest changeTypeRequest = new ChangeTypeRequest(); // ChangeTypeRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsChangeTypePost(id, changeTypeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsChangeTypePost");
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
| **changeTypeRequest** | [**ChangeTypeRequest**](ChangeTypeRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;change_load_balancer_type&#x60; Action |  -  |

<a id="loadBalancersIdActionsDeleteServicePost"></a>
# **loadBalancersIdActionsDeleteServicePost**
> ActionResponse loadBalancersIdActionsDeleteServicePost(id, loadBalancersIdActionsDeleteServicePostRequest)

Delete Service

Delete a service of a Load Balancer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest = new LoadBalancersIdActionsDeleteServicePostRequest(); // LoadBalancersIdActionsDeleteServicePostRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsDeleteServicePost(id, loadBalancersIdActionsDeleteServicePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsDeleteServicePost");
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
| **loadBalancersIdActionsDeleteServicePostRequest** | [**LoadBalancersIdActionsDeleteServicePostRequest**](LoadBalancersIdActionsDeleteServicePostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;delete_service&#x60; Action |  -  |

<a id="loadBalancersIdActionsDetachFromNetworkPost"></a>
# **loadBalancersIdActionsDetachFromNetworkPost**
> ActionResponse loadBalancersIdActionsDetachFromNetworkPost(id, loadBalancersIdActionsDetachFromNetworkPostRequest)

Detach a Load Balancer from a Network

Detaches a Load Balancer from a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest = new LoadBalancersIdActionsDetachFromNetworkPostRequest(); // LoadBalancersIdActionsDetachFromNetworkPostRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsDetachFromNetworkPost(id, loadBalancersIdActionsDetachFromNetworkPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsDetachFromNetworkPost");
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
| **loadBalancersIdActionsDetachFromNetworkPostRequest** | [**LoadBalancersIdActionsDetachFromNetworkPostRequest**](LoadBalancersIdActionsDetachFromNetworkPostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;detach_from_network&#x60; Action |  -  |

<a id="loadBalancersIdActionsDisablePublicInterfacePost"></a>
# **loadBalancersIdActionsDisablePublicInterfacePost**
> ActionResponse loadBalancersIdActionsDisablePublicInterfacePost(id)

Disable the public interface of a Load Balancer

Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsDisablePublicInterfacePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsDisablePublicInterfacePost");
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

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;disable_public_interface&#x60; Action |  -  |

<a id="loadBalancersIdActionsEnablePublicInterfacePost"></a>
# **loadBalancersIdActionsEnablePublicInterfacePost**
> ActionResponse loadBalancersIdActionsEnablePublicInterfacePost(id)

Enable the public interface of a Load Balancer

Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsEnablePublicInterfacePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsEnablePublicInterfacePost");
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

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;enable_public_interface&#x60; Action |  -  |

<a id="loadBalancersIdActionsGet"></a>
# **loadBalancersIdActionsGet**
> ActionsResponse loadBalancersIdActionsGet(id, sort, status)

Get all Actions for a Load Balancer

Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.loadBalancersIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, command, command:asc, command:desc, status, status:asc, status:desc, progress, progress:asc, progress:desc, started, started:asc, started:desc, finished, finished:asc, finished:desc] |
| **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] [enum: running, success, error] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;actions&#x60; key contains a list of Actions |  -  |

<a id="loadBalancersIdActionsRemoveTargetPost"></a>
# **loadBalancersIdActionsRemoveTargetPost**
> ActionResponse loadBalancersIdActionsRemoveTargetPost(id, removeTargetRequest)

Remove Target

Removes a target from a Load Balancer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    RemoveTargetRequest removeTargetRequest = new RemoveTargetRequest(); // RemoveTargetRequest | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsRemoveTargetPost(id, removeTargetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsRemoveTargetPost");
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
| **removeTargetRequest** | [**RemoveTargetRequest**](RemoveTargetRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;remove_target&#x60; Action |  -  |

<a id="loadBalancersIdActionsUpdateServicePost"></a>
# **loadBalancersIdActionsUpdateServicePost**
> ActionResponse loadBalancersIdActionsUpdateServicePost(id, loadBalancerService)

Update Service

Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerActionsApi apiInstance = new LoadBalancerActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Load Balancer
    LoadBalancerService loadBalancerService = new LoadBalancerService(); // LoadBalancerService | 
    try {
      ActionResponse result = apiInstance.loadBalancersIdActionsUpdateServicePost(id, loadBalancerService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerActionsApi#loadBalancersIdActionsUpdateServicePost");
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
| **loadBalancerService** | [**LoadBalancerService**](LoadBalancerService.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;update_service&#x60; Action |  -  |

