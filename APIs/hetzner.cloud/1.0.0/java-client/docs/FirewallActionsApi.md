# FirewallActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**firewallsIdActionsActionIdGet**](FirewallActionsApi.md#firewallsIdActionsActionIdGet) | **GET** /firewalls/{id}/actions/{action_id} | Get an Action for a Firewall |
| [**firewallsIdActionsApplyToResourcesPost**](FirewallActionsApi.md#firewallsIdActionsApplyToResourcesPost) | **POST** /firewalls/{id}/actions/apply_to_resources | Apply to Resources |
| [**firewallsIdActionsGet**](FirewallActionsApi.md#firewallsIdActionsGet) | **GET** /firewalls/{id}/actions | Get all Actions for a Firewall |
| [**firewallsIdActionsRemoveFromResourcesPost**](FirewallActionsApi.md#firewallsIdActionsRemoveFromResourcesPost) | **POST** /firewalls/{id}/actions/remove_from_resources | Remove from Resources |
| [**firewallsIdActionsSetRulesPost**](FirewallActionsApi.md#firewallsIdActionsSetRulesPost) | **POST** /firewalls/{id}/actions/set_rules | Set Rules |


<a id="firewallsIdActionsActionIdGet"></a>
# **firewallsIdActionsActionIdGet**
> ActionResponse firewallsIdActionsActionIdGet(id, actionId)

Get an Action for a Firewall

Returns a specific Action for a Firewall.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallActionsApi apiInstance = new FirewallActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Firewall
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.firewallsIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallActionsApi#firewallsIdActionsActionIdGet");
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
| **id** | **Integer**| ID of the Firewall | |
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
| **200** | The &#x60;action&#x60; key contains the Firewall Action |  -  |

<a id="firewallsIdActionsApplyToResourcesPost"></a>
# **firewallsIdActionsApplyToResourcesPost**
> ActionsResponse firewallsIdActionsApplyToResourcesPost(id, applyToResourcesRequest)

Apply to Resources

Applies one Firewall to multiple resources.  Currently servers (public network interface) and label selectors are supported.  #### Call specific error codes  | Code                          | Description                                                   | |-------------------------------|---------------------------------------------------------------| | &#x60;firewall_already_applied&#x60;    | Firewall was already applied on resource                      | | &#x60;incompatible_network_type&#x60;   | The Network type is incompatible for the given resource       | | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallActionsApi apiInstance = new FirewallActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Firewall
    ApplyToResourcesRequest applyToResourcesRequest = new ApplyToResourcesRequest(); // ApplyToResourcesRequest | 
    try {
      ActionsResponse result = apiInstance.firewallsIdActionsApplyToResourcesPost(id, applyToResourcesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallActionsApi#firewallsIdActionsApplyToResourcesPost");
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
| **id** | **Integer**| ID of the Firewall | |
| **applyToResourcesRequest** | [**ApplyToResourcesRequest**](ApplyToResourcesRequest.md)|  | [optional] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;actions&#x60; key contains multiple &#x60;apply_firewall&#x60; Actions |  -  |

<a id="firewallsIdActionsGet"></a>
# **firewallsIdActionsGet**
> ActionsResponse firewallsIdActionsGet(id, sort, status)

Get all Actions for a Firewall

Returns all Action objects for a Firewall. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallActionsApi apiInstance = new FirewallActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Resource
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.firewallsIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallActionsApi#firewallsIdActionsGet");
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
| **id** | **Integer**| ID of the Resource | |
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

<a id="firewallsIdActionsRemoveFromResourcesPost"></a>
# **firewallsIdActionsRemoveFromResourcesPost**
> ActionsResponse firewallsIdActionsRemoveFromResourcesPost(id, removeFromResourcesRequest)

Remove from Resources

Removes one Firewall from multiple resources.  Currently only Servers (and their public network interfaces) are supported.  #### Call specific error codes  | Code                                  | Description                                                            | |---------------------------------------|------------------------------------------------------------------------| | &#x60;firewall_already_removed&#x60;            | Firewall was already removed from the resource                         | | &#x60;firewall_resource_not_found&#x60;         | The resource the Firewall should be attached to was not found          | | &#x60;firewall_managed_by_label_selector&#x60;  | Firewall was applied via label selector and cannot be removed manually | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallActionsApi apiInstance = new FirewallActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Firewall
    RemoveFromResourcesRequest removeFromResourcesRequest = new RemoveFromResourcesRequest(); // RemoveFromResourcesRequest | 
    try {
      ActionsResponse result = apiInstance.firewallsIdActionsRemoveFromResourcesPost(id, removeFromResourcesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallActionsApi#firewallsIdActionsRemoveFromResourcesPost");
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
| **id** | **Integer**| ID of the Firewall | |
| **removeFromResourcesRequest** | [**RemoveFromResourcesRequest**](RemoveFromResourcesRequest.md)|  | [optional] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;actions&#x60; key contains multiple &#x60;remove_firewall&#x60; Actions |  -  |

<a id="firewallsIdActionsSetRulesPost"></a>
# **firewallsIdActionsSetRulesPost**
> ActionsResponse firewallsIdActionsSetRulesPost(id, setRulesRequest)

Set Rules

Sets the rules of a Firewall.  All existing rules will be overwritten. Pass an empty &#x60;rules&#x60; array to remove all rules. The maximum amount of rules that can be defined is 50.  #### Call specific error codes  | Code                          | Description                                                   | |-------------------------------|---------------------------------------------------------------| | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FirewallActionsApi apiInstance = new FirewallActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Firewall
    SetRulesRequest setRulesRequest = new SetRulesRequest(); // SetRulesRequest | 
    try {
      ActionsResponse result = apiInstance.firewallsIdActionsSetRulesPost(id, setRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallActionsApi#firewallsIdActionsSetRulesPost");
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
| **id** | **Integer**| ID of the Firewall | |
| **setRulesRequest** | [**SetRulesRequest**](SetRulesRequest.md)|  | [optional] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains one &#x60;set_firewall_rules&#x60; Action plus one &#x60;apply_firewall&#x60; Action per resource where the Firewall is active |  -  |

