# EntitiesApi

All URIs are relative to *http://vmware.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCluster**](EntitiesApi.md#getCluster) | **GET** /entities/clusters/{id} | Show cluster details |
| [**getDatacenter**](EntitiesApi.md#getDatacenter) | **GET** /entities/vc-datacenters/{id} | Show vCenter datacenter details |
| [**getDatastore**](EntitiesApi.md#getDatastore) | **GET** /entities/datastores/{id} | Show datastore details |
| [**getDistributedVirtualPortgroup**](EntitiesApi.md#getDistributedVirtualPortgroup) | **GET** /entities/distributed-virtual-portgroups/{id} | Show distributed virtual portgroup details |
| [**getDistributedVirtualSwitch**](EntitiesApi.md#getDistributedVirtualSwitch) | **GET** /entities/distributed-virtual-switches/{id} | Show distributed virtual switch details |
| [**getFirewall**](EntitiesApi.md#getFirewall) | **GET** /entities/firewalls/{id} | Show firewall details |
| [**getFirewallRule**](EntitiesApi.md#getFirewallRule) | **GET** /entities/firewall-rules/{id} | Show firewall rule details |
| [**getFlow**](EntitiesApi.md#getFlow) | **GET** /entities/flows/{id} | Show flow details |
| [**getFlows**](EntitiesApi.md#getFlows) | **GET** /entities/flows | List flows |
| [**getFolder**](EntitiesApi.md#getFolder) | **GET** /entities/folders/{id} | Show folder details |
| [**getHost**](EntitiesApi.md#getHost) | **GET** /entities/hosts/{id} | Show host details |
| [**getIPSet**](EntitiesApi.md#getIPSet) | **GET** /entities/ip-sets/{id} | Show ip set details |
| [**getLayer2Network**](EntitiesApi.md#getLayer2Network) | **GET** /entities/layer2-networks/{id} | Show layer2 network details |
| [**getNSXManager**](EntitiesApi.md#getNSXManager) | **GET** /entities/nsx-managers/{id} | Show nsx manager details |
| [**getName**](EntitiesApi.md#getName) | **GET** /entities/names/{id} | Get name of an entity |
| [**getNames**](EntitiesApi.md#getNames) | **POST** /entities/names | Get names for entities |
| [**getProblemEvent**](EntitiesApi.md#getProblemEvent) | **GET** /entities/problems/{id} | Show problem details |
| [**getSecurityGroup**](EntitiesApi.md#getSecurityGroup) | **GET** /entities/security-groups/{id} | Show security group details |
| [**getSecurityTag**](EntitiesApi.md#getSecurityTag) | **GET** /entities/security-tags/{id} | Show security tag details |
| [**getService**](EntitiesApi.md#getService) | **GET** /entities/services/{id} | Show service details |
| [**getServiceGroup**](EntitiesApi.md#getServiceGroup) | **GET** /entities/service-groups/{id} | Show service group details |
| [**getVcenterManager**](EntitiesApi.md#getVcenterManager) | **GET** /entities/vcenter-managers/{id} | Show vCenter manager details |
| [**getVm**](EntitiesApi.md#getVm) | **GET** /entities/vms/{id} | Show vm details |
| [**getVmknic**](EntitiesApi.md#getVmknic) | **GET** /entities/vmknics/{id} | Show vmknic details |
| [**getVnic**](EntitiesApi.md#getVnic) | **GET** /entities/vnics/{id} | Show vnic details |
| [**listClusters**](EntitiesApi.md#listClusters) | **GET** /entities/clusters | List clusters |
| [**listDatacenters**](EntitiesApi.md#listDatacenters) | **GET** /entities/vc-datacenters | List vCenter datacenters |
| [**listDatastores**](EntitiesApi.md#listDatastores) | **GET** /entities/datastores | List datastores |
| [**listDistributedVirtualPortgroups**](EntitiesApi.md#listDistributedVirtualPortgroups) | **GET** /entities/distributed-virtual-portgroups | List distributed virtual portgroups |
| [**listDistributedVirtualSwitches**](EntitiesApi.md#listDistributedVirtualSwitches) | **GET** /entities/distributed-virtual-switches | List distributed virtual switches |
| [**listFirewallRules**](EntitiesApi.md#listFirewallRules) | **GET** /entities/firewall-rules | List firewall rules |
| [**listFirewalls**](EntitiesApi.md#listFirewalls) | **GET** /entities/firewalls | List firewalls |
| [**listFolders**](EntitiesApi.md#listFolders) | **GET** /entities/folders | List folders |
| [**listHosts**](EntitiesApi.md#listHosts) | **GET** /entities/hosts | List hosts |
| [**listIPSets**](EntitiesApi.md#listIPSets) | **GET** /entities/ip-sets | List ip sets |
| [**listLayer2Networks**](EntitiesApi.md#listLayer2Networks) | **GET** /entities/layer2-networks | List layer2 networks |
| [**listNSXManagers**](EntitiesApi.md#listNSXManagers) | **GET** /entities/nsx-managers | List nsx managers |
| [**listProblemEvents**](EntitiesApi.md#listProblemEvents) | **GET** /entities/problems | List problems |
| [**listSecurityGroups**](EntitiesApi.md#listSecurityGroups) | **GET** /entities/security-groups | List security groups |
| [**listSecurityTags**](EntitiesApi.md#listSecurityTags) | **GET** /entities/security-tags | List security tags |
| [**listServiceGroups**](EntitiesApi.md#listServiceGroups) | **GET** /entities/service-groups | List service groups |
| [**listServices**](EntitiesApi.md#listServices) | **GET** /entities/services | List services |
| [**listVcenterManagers**](EntitiesApi.md#listVcenterManagers) | **GET** /entities/vcenter-managers | List vCenter managers |
| [**listVmknics**](EntitiesApi.md#listVmknics) | **GET** /entities/vmknics | List vmknics |
| [**listVms**](EntitiesApi.md#listVms) | **GET** /entities/vms | List vms |
| [**listVnics**](EntitiesApi.md#listVnics) | **GET** /entities/vnics | List vnics |


<a id="getCluster"></a>
# **getCluster**
> Cluster getCluster(id, time)

Show cluster details

Show cluster details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      Cluster result = apiInstance.getCluster(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getCluster");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, name, nsx_manager, num_cpu_cores, num_datastores, num_hosts, total_cpus, total_memory, vcenter_manager, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getDatacenter"></a>
# **getDatacenter**
> VCDatacenter getDatacenter(id, time)

Show vCenter datacenter details

Show vCenter datacenter details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      VCDatacenter result = apiInstance.getDatacenter(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getDatacenter");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**VCDatacenter**](VCDatacenter.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, name, vcenter_manager, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getDatastore"></a>
# **getDatastore**
> Datastore getDatastore(id, time)

Show datastore details

Show datastore details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      Datastore result = apiInstance.getDatastore(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getDatastore");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**Datastore**](Datastore.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, name, vcenter_manager, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getDistributedVirtualPortgroup"></a>
# **getDistributedVirtualPortgroup**
> DistributedVirtualPortgroup getDistributedVirtualPortgroup(id, time)

Show distributed virtual portgroup details

Show distributed virtual portgroup details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      DistributedVirtualPortgroup result = apiInstance.getDistributedVirtualPortgroup(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getDistributedVirtualPortgroup");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**DistributedVirtualPortgroup**](DistributedVirtualPortgroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, distributed_virtual_switch, entity_id, entity_type, name, vcenter_manager, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getDistributedVirtualSwitch"></a>
# **getDistributedVirtualSwitch**
> DistributedVirtualSwitch getDistributedVirtualSwitch(id, time)

Show distributed virtual switch details

Show distributed virtual switch details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      DistributedVirtualSwitch result = apiInstance.getDistributedVirtualSwitch(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getDistributedVirtualSwitch");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**DistributedVirtualSwitch**](DistributedVirtualSwitch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, hosts, name, vcenter_manager, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getFirewall"></a>
# **getFirewall**
> BaseFirewallRule getFirewall(id, time)

Show firewall details

Show firewall details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseFirewallRule result = apiInstance.getFirewall(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getFirewall");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseFirewallRule**](BaseFirewallRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, exclusions, firewall_rules, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getFirewallRule"></a>
# **getFirewallRule**
> getFirewallRule(id, time)

Show firewall rule details

Show firewall rule details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      apiInstance.getFirewallRule(id, time);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getFirewallRule");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: action, application/json, destination_any, destination_inversion, destinations, direction, disabled, entity_id, entity_type, logging_enabled, name, nsx_managers, port_ranges, rule_id, scope, section_id, section_name, sequence_number, service_any, services, source_any, source_inversion, sources

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getFlow"></a>
# **getFlow**
> Flow getFlow(id, time)

Show flow details

Show flow details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      Flow result = apiInstance.getFlow(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getFlow");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**Flow**](Flow.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, destination_folders, destination_ip, destination_ip_sets, destination_security_groups, destination_security_tags, destination_vm_tags, entity_id, entity_type, firewall_action, flow_tag, name, port, protocol, source_folders, source_ip, source_ip_sets, source_security_groups, source_security_tags, source_vm_tags, traffic_type, within_host

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getFlows"></a>
# **getFlows**
> PagedListResponseWithTime getFlows(size, cursor, startTime, endTime)

List flows

List flows

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.getFlows(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getFlows");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="getFolder"></a>
# **getFolder**
> Folder getFolder(id, time)

Show folder details

Show folder details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      Folder result = apiInstance.getFolder(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getFolder");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, name, vcenter_manager, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getHost"></a>
# **getHost**
> Host getHost(id, time)

Show host details

Show host details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      Host result = apiInstance.getHost(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getHost");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**Host**](Host.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cluster, connection_state, datastores, entity_id, entity_type, maintenance_mode, name, nsx_manager, service_tag, vcenter_manager, vendor_id, vm_count, vmknics

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getIPSet"></a>
# **getIPSet**
> BaseIPSet getIPSet(id, time)

Show ip set details

Show ip set details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseIPSet result = apiInstance.getIPSet(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getIPSet");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseIPSet**](BaseIPSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, direct_destination_rules, direct_source_rules, entity_id, entity_type, indirect_destination_rules, indirect_source_rules, ip_addresses, ip_numeric_ranges, ip_ranges, name, nsx_managers, parent_security_groups, scope, translated_vm_count, vendor, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getLayer2Network"></a>
# **getLayer2Network**
> BaseL2Network getLayer2Network(id, time)

Show layer2 network details

Show layer2 network details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseL2Network result = apiInstance.getLayer2Network(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getLayer2Network");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseL2Network**](BaseL2Network.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, gateways, name, network_addresses, nsx_managers, scope, segment_id, vteps

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getNSXManager"></a>
# **getNSXManager**
> BaseNSXManager getNSXManager(id, time)

Show nsx manager details

Show nsx manager details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseNSXManager result = apiInstance.getNSXManager(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getNSXManager");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseNSXManager**](BaseNSXManager.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, ip_address, name, role, version

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getName"></a>
# **getName**
> EntityName getName(id, time)

Get name of an entity

Get name of an entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      EntityName result = apiInstance.getName(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getName");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**EntityName**](EntityName.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="getNames"></a>
# **getNames**
> NamesResponse getNames(namesRequest)

Get names for entities

Get names for entities.Limit of 1000 entities in a single request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    NamesRequest namesRequest = new NamesRequest(); // NamesRequest | Names Request
    try {
      NamesResponse result = apiInstance.getNames(namesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getNames");
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
| **namesRequest** | [**NamesRequest**](NamesRequest.md)| Names Request | |

### Return type

[**NamesResponse**](NamesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="getProblemEvent"></a>
# **getProblemEvent**
> getProblemEvent(id, time)

Show problem details

Show problem event details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      apiInstance.getProblemEvent(id, time);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getProblemEvent");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: admin_state, anchor_entities, application/json, archived, entity_id, entity_type, event_tags, event_time_epoch_ms, message, name, related_entities, severity

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getSecurityGroup"></a>
# **getSecurityGroup**
> BaseSecurityGroup getSecurityGroup(id, time)

Show security group details

Show security group details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseSecurityGroup result = apiInstance.getSecurityGroup(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getSecurityGroup");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseSecurityGroup**](BaseSecurityGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, direct_destination_rules, direct_members, direct_source_rules, entity_id, entity_type, excluded_members, indirect_destination_rules, indirect_source_rules, ip_sets, members, name, nsx_managers, parents, scope, security_tags, translated_vm_count, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getSecurityTag"></a>
# **getSecurityTag**
> SecurityTag getSecurityTag(id, time)

Show security tag details

Show security tag details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      SecurityTag result = apiInstance.getSecurityTag(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getSecurityTag");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**SecurityTag**](SecurityTag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, description, direct_security_groups, entity_id, entity_type, name, nsx_manager, security_groups, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getService"></a>
# **getService**
> BaseService getService(id, time)

Show service details

Show service details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseService result = apiInstance.getService(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getService");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseService**](BaseService.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, name, nsx_managers, port_ranges, protocol, scope, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getServiceGroup"></a>
# **getServiceGroup**
> BaseServiceGroup getServiceGroup(id, time)

Show service group details

Show service group details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseServiceGroup result = apiInstance.getServiceGroup(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getServiceGroup");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseServiceGroup**](BaseServiceGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, members, name, nsx_managers, scope, vendor_id

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getVcenterManager"></a>
# **getVcenterManager**
> VCenterManager getVcenterManager(id, time)

Show vCenter manager details

Show vCenter manager details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      VCenterManager result = apiInstance.getVcenterManager(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getVcenterManager");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**VCenterManager**](VCenterManager.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, ip_address, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getVm"></a>
# **getVm**
> BaseVirtualMachine getVm(id, time)

Show vm details

Show vm details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseVirtualMachine result = apiInstance.getVm(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getVm");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseVirtualMachine**](BaseVirtualMachine.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, applied_to_destination_rules, applied_to_source_rules, cluster, datacenter, datastores, default_gateway, destination_firewall_rules, destination_inversion_rules, entity_id, entity_type, folders, host, ip_addresses, ip_sets, layer2_networks, name, nsx_manager, resource_pool, security_groups, security_tags, source_firewall_rules, source_inversion_rules, vcenter_manager, vendor_id, vlans, vnics

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getVmknic"></a>
# **getVmknic**
> Vmknic getVmknic(id, time)

Show vmknic details

Show vmknic details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      Vmknic result = apiInstance.getVmknic(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getVmknic");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**Vmknic**](Vmknic.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, host, ip_addresses, layer2_network, name, vlan

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getVnic"></a>
# **getVnic**
> BaseVnic getVnic(id, time)

Show vnic details

Show vnic details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String id = "id_example"; // String | entity id
    Long time = 56L; // Long | time in epoch seconds
    try {
      BaseVnic result = apiInstance.getVnic(id, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getVnic");
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
| **id** | **String**| entity id | |
| **time** | **Long**| time in epoch seconds | [optional] |

### Return type

[**BaseVnic**](BaseVnic.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_id, entity_type, ip_addresses, layer2_network, name, vlan, vm

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="listClusters"></a>
# **listClusters**
> PagedListResponseWithTime listClusters(size, cursor, startTime, endTime)

List clusters

List clusters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listClusters(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listClusters");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listDatacenters"></a>
# **listDatacenters**
> PagedListResponseWithTime listDatacenters(size, cursor, startTime, endTime)

List vCenter datacenters

List vCenter datacenters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listDatacenters(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listDatacenters");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listDatastores"></a>
# **listDatastores**
> PagedListResponseWithTime listDatastores(size, cursor, startTime, endTime)

List datastores

List datastores

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listDatastores(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listDatastores");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listDistributedVirtualPortgroups"></a>
# **listDistributedVirtualPortgroups**
> PagedListResponseWithTime listDistributedVirtualPortgroups(size, cursor, startTime, endTime)

List distributed virtual portgroups

List distributed virtual portgroups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listDistributedVirtualPortgroups(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listDistributedVirtualPortgroups");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listDistributedVirtualSwitches"></a>
# **listDistributedVirtualSwitches**
> PagedListResponseWithTime listDistributedVirtualSwitches(size, cursor, startTime, endTime)

List distributed virtual switches

List distributed virtual switches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listDistributedVirtualSwitches(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listDistributedVirtualSwitches");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listFirewallRules"></a>
# **listFirewallRules**
> PagedListResponseWithTime listFirewallRules(size, cursor, startTime, endTime)

List firewall rules

List firewall rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listFirewallRules(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listFirewallRules");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listFirewalls"></a>
# **listFirewalls**
> PagedListResponseWithTime listFirewalls(size, cursor, startTime, endTime)

List firewalls

List firewalls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listFirewalls(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listFirewalls");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listFolders"></a>
# **listFolders**
> PagedListResponseWithTime listFolders(size, cursor, startTime, endTime)

List folders

List folders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listFolders(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listFolders");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listHosts"></a>
# **listHosts**
> PagedListResponseWithTime listHosts(size, cursor, startTime, endTime)

List hosts

List hosts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listHosts(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listHosts");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listIPSets"></a>
# **listIPSets**
> PagedListResponseWithTime listIPSets(size, cursor, startTime, endTime)

List ip sets

List ip sets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listIPSets(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listIPSets");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listLayer2Networks"></a>
# **listLayer2Networks**
> PagedListResponseWithTime listLayer2Networks(size, cursor, startTime, endTime)

List layer2 networks

List layer2 networks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listLayer2Networks(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listLayer2Networks");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listNSXManagers"></a>
# **listNSXManagers**
> PagedListResponseWithTime listNSXManagers(size, cursor, startTime, endTime)

List nsx managers

List nsx managers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listNSXManagers(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listNSXManagers");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listProblemEvents"></a>
# **listProblemEvents**
> PagedListResponseWithTime listProblemEvents(size, cursor, startTime, endTime)

List problems

List problem events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listProblemEvents(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listProblemEvents");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listSecurityGroups"></a>
# **listSecurityGroups**
> PagedListResponseWithTime listSecurityGroups(size, cursor, startTime, endTime)

List security groups

List security groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listSecurityGroups(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listSecurityGroups");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listSecurityTags"></a>
# **listSecurityTags**
> PagedListResponseWithTime listSecurityTags(size, cursor, startTime, endTime)

List security tags

List security tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listSecurityTags(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listSecurityTags");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listServiceGroups"></a>
# **listServiceGroups**
> PagedListResponseWithTime listServiceGroups(size, cursor, startTime, endTime)

List service groups

List service groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listServiceGroups(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listServiceGroups");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listServices"></a>
# **listServices**
> PagedListResponseWithTime listServices(size, cursor, startTime, endTime)

List services

List services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listServices(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listServices");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listVcenterManagers"></a>
# **listVcenterManagers**
> PagedListResponseWithTime listVcenterManagers(size, cursor, startTime, endTime)

List vCenter managers

List vCenter managers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listVcenterManagers(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listVcenterManagers");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listVmknics"></a>
# **listVmknics**
> PagedListResponseWithTime listVmknics(size, cursor, startTime, endTime)

List vmknics

List vmknics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listVmknics(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listVmknics");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listVms"></a>
# **listVms**
> PagedListResponseWithTime listVms(size, cursor, startTime, endTime)

List vms

List vms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listVms(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listVms");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listVnics"></a>
# **listVnics**
> PagedListResponseWithTime listVnics(size, cursor, startTime, endTime)

List vnics

List vnics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponseWithTime result = apiInstance.listVnics(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#listVnics");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, cursor, end_time, results, start_time, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

