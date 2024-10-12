# VRealizeNetworkInsightApiReference.EntitiesApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCluster**](EntitiesApi.md#getCluster) | **GET** /entities/clusters/{id} | Show cluster details
[**getDatacenter**](EntitiesApi.md#getDatacenter) | **GET** /entities/vc-datacenters/{id} | Show vCenter datacenter details
[**getDatastore**](EntitiesApi.md#getDatastore) | **GET** /entities/datastores/{id} | Show datastore details
[**getDistributedVirtualPortgroup**](EntitiesApi.md#getDistributedVirtualPortgroup) | **GET** /entities/distributed-virtual-portgroups/{id} | Show distributed virtual portgroup details
[**getDistributedVirtualSwitch**](EntitiesApi.md#getDistributedVirtualSwitch) | **GET** /entities/distributed-virtual-switches/{id} | Show distributed virtual switch details
[**getFirewall**](EntitiesApi.md#getFirewall) | **GET** /entities/firewalls/{id} | Show firewall details
[**getFirewallRule**](EntitiesApi.md#getFirewallRule) | **GET** /entities/firewall-rules/{id} | Show firewall rule details
[**getFlow**](EntitiesApi.md#getFlow) | **GET** /entities/flows/{id} | Show flow details
[**getFlows**](EntitiesApi.md#getFlows) | **GET** /entities/flows | List flows
[**getFolder**](EntitiesApi.md#getFolder) | **GET** /entities/folders/{id} | Show folder details
[**getHost**](EntitiesApi.md#getHost) | **GET** /entities/hosts/{id} | Show host details
[**getIPSet**](EntitiesApi.md#getIPSet) | **GET** /entities/ip-sets/{id} | Show ip set details
[**getLayer2Network**](EntitiesApi.md#getLayer2Network) | **GET** /entities/layer2-networks/{id} | Show layer2 network details
[**getNSXManager**](EntitiesApi.md#getNSXManager) | **GET** /entities/nsx-managers/{id} | Show nsx manager details
[**getName**](EntitiesApi.md#getName) | **GET** /entities/names/{id} | Get name of an entity
[**getNames**](EntitiesApi.md#getNames) | **POST** /entities/names | Get names for entities
[**getProblemEvent**](EntitiesApi.md#getProblemEvent) | **GET** /entities/problems/{id} | Show problem details
[**getSecurityGroup**](EntitiesApi.md#getSecurityGroup) | **GET** /entities/security-groups/{id} | Show security group details
[**getSecurityTag**](EntitiesApi.md#getSecurityTag) | **GET** /entities/security-tags/{id} | Show security tag details
[**getService**](EntitiesApi.md#getService) | **GET** /entities/services/{id} | Show service details
[**getServiceGroup**](EntitiesApi.md#getServiceGroup) | **GET** /entities/service-groups/{id} | Show service group details
[**getVcenterManager**](EntitiesApi.md#getVcenterManager) | **GET** /entities/vcenter-managers/{id} | Show vCenter manager details
[**getVm**](EntitiesApi.md#getVm) | **GET** /entities/vms/{id} | Show vm details
[**getVmknic**](EntitiesApi.md#getVmknic) | **GET** /entities/vmknics/{id} | Show vmknic details
[**getVnic**](EntitiesApi.md#getVnic) | **GET** /entities/vnics/{id} | Show vnic details
[**listClusters**](EntitiesApi.md#listClusters) | **GET** /entities/clusters | List clusters
[**listDatacenters**](EntitiesApi.md#listDatacenters) | **GET** /entities/vc-datacenters | List vCenter datacenters
[**listDatastores**](EntitiesApi.md#listDatastores) | **GET** /entities/datastores | List datastores
[**listDistributedVirtualPortgroups**](EntitiesApi.md#listDistributedVirtualPortgroups) | **GET** /entities/distributed-virtual-portgroups | List distributed virtual portgroups
[**listDistributedVirtualSwitches**](EntitiesApi.md#listDistributedVirtualSwitches) | **GET** /entities/distributed-virtual-switches | List distributed virtual switches
[**listFirewallRules**](EntitiesApi.md#listFirewallRules) | **GET** /entities/firewall-rules | List firewall rules
[**listFirewalls**](EntitiesApi.md#listFirewalls) | **GET** /entities/firewalls | List firewalls
[**listFolders**](EntitiesApi.md#listFolders) | **GET** /entities/folders | List folders
[**listHosts**](EntitiesApi.md#listHosts) | **GET** /entities/hosts | List hosts
[**listIPSets**](EntitiesApi.md#listIPSets) | **GET** /entities/ip-sets | List ip sets
[**listLayer2Networks**](EntitiesApi.md#listLayer2Networks) | **GET** /entities/layer2-networks | List layer2 networks
[**listNSXManagers**](EntitiesApi.md#listNSXManagers) | **GET** /entities/nsx-managers | List nsx managers
[**listProblemEvents**](EntitiesApi.md#listProblemEvents) | **GET** /entities/problems | List problems
[**listSecurityGroups**](EntitiesApi.md#listSecurityGroups) | **GET** /entities/security-groups | List security groups
[**listSecurityTags**](EntitiesApi.md#listSecurityTags) | **GET** /entities/security-tags | List security tags
[**listServiceGroups**](EntitiesApi.md#listServiceGroups) | **GET** /entities/service-groups | List service groups
[**listServices**](EntitiesApi.md#listServices) | **GET** /entities/services | List services
[**listVcenterManagers**](EntitiesApi.md#listVcenterManagers) | **GET** /entities/vcenter-managers | List vCenter managers
[**listVmknics**](EntitiesApi.md#listVmknics) | **GET** /entities/vmknics | List vmknics
[**listVms**](EntitiesApi.md#listVms) | **GET** /entities/vms | List vms
[**listVnics**](EntitiesApi.md#listVnics) | **GET** /entities/vnics | List vnics



## getCluster

> Cluster getCluster(id, opts)

Show cluster details

Show cluster details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getCluster(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, name, nsx_manager, num_cpu_cores, num_datastores, num_hosts, total_cpus, total_memory, vcenter_manager, vendor_id


## getDatacenter

> VCDatacenter getDatacenter(id, opts)

Show vCenter datacenter details

Show vCenter datacenter details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getDatacenter(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**VCDatacenter**](VCDatacenter.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, name, vcenter_manager, vendor_id


## getDatastore

> Datastore getDatastore(id, opts)

Show datastore details

Show datastore details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getDatastore(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**Datastore**](Datastore.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, name, vcenter_manager, vendor_id


## getDistributedVirtualPortgroup

> DistributedVirtualPortgroup getDistributedVirtualPortgroup(id, opts)

Show distributed virtual portgroup details

Show distributed virtual portgroup details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getDistributedVirtualPortgroup(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**DistributedVirtualPortgroup**](DistributedVirtualPortgroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, distributed_virtual_switch, entity_id, entity_type, name, vcenter_manager, vendor_id


## getDistributedVirtualSwitch

> DistributedVirtualSwitch getDistributedVirtualSwitch(id, opts)

Show distributed virtual switch details

Show distributed virtual switch details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getDistributedVirtualSwitch(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**DistributedVirtualSwitch**](DistributedVirtualSwitch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, hosts, name, vcenter_manager, vendor_id


## getFirewall

> BaseFirewallRule getFirewall(id, opts)

Show firewall details

Show firewall details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getFirewall(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseFirewallRule**](BaseFirewallRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, exclusions, firewall_rules, name


## getFirewallRule

> getFirewallRule(id, opts)

Show firewall rule details

Show firewall rule details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getFirewallRule(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: action, application/json, destination_any, destination_inversion, destinations, direction, disabled, entity_id, entity_type, logging_enabled, name, nsx_managers, port_ranges, rule_id, scope, section_id, section_name, sequence_number, service_any, services, source_any, source_inversion, sources


## getFlow

> Flow getFlow(id, opts)

Show flow details

Show flow details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getFlow(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**Flow**](Flow.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, destination_folders, destination_ip, destination_ip_sets, destination_security_groups, destination_security_tags, destination_vm_tags, entity_id, entity_type, firewall_action, flow_tag, name, port, protocol, source_folders, source_ip, source_ip_sets, source_security_groups, source_security_tags, source_vm_tags, traffic_type, within_host


## getFlows

> PagedListResponseWithTime getFlows(opts)

List flows

List flows

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.getFlows(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## getFolder

> Folder getFolder(id, opts)

Show folder details

Show folder details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getFolder(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, name, vcenter_manager, vendor_id


## getHost

> Host getHost(id, opts)

Show host details

Show host details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getHost(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**Host**](Host.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cluster, connection_state, datastores, entity_id, entity_type, maintenance_mode, name, nsx_manager, service_tag, vcenter_manager, vendor_id, vm_count, vmknics


## getIPSet

> BaseIPSet getIPSet(id, opts)

Show ip set details

Show ip set details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getIPSet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseIPSet**](BaseIPSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, direct_destination_rules, direct_source_rules, entity_id, entity_type, indirect_destination_rules, indirect_source_rules, ip_addresses, ip_numeric_ranges, ip_ranges, name, nsx_managers, parent_security_groups, scope, translated_vm_count, vendor, vendor_id


## getLayer2Network

> BaseL2Network getLayer2Network(id, opts)

Show layer2 network details

Show layer2 network details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getLayer2Network(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseL2Network**](BaseL2Network.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, gateways, name, network_addresses, nsx_managers, scope, segment_id, vteps


## getNSXManager

> BaseNSXManager getNSXManager(id, opts)

Show nsx manager details

Show nsx manager details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getNSXManager(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseNSXManager**](BaseNSXManager.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, ip_address, name, role, version


## getName

> EntityName getName(id, opts)

Get name of an entity

Get name of an entity

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getName(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**EntityName**](EntityName.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNames

> NamesResponse getNames(namesRequest)

Get names for entities

Get names for entities.Limit of 1000 entities in a single request.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let namesRequest = new VRealizeNetworkInsightApiReference.NamesRequest(); // NamesRequest | Names Request
apiInstance.getNames(namesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namesRequest** | [**NamesRequest**](NamesRequest.md)| Names Request | 

### Return type

[**NamesResponse**](NamesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getProblemEvent

> getProblemEvent(id, opts)

Show problem details

Show problem event details.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getProblemEvent(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: admin_state, anchor_entities, application/json, archived, entity_id, entity_type, event_tags, event_time_epoch_ms, message, name, related_entities, severity


## getSecurityGroup

> BaseSecurityGroup getSecurityGroup(id, opts)

Show security group details

Show security group details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getSecurityGroup(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseSecurityGroup**](BaseSecurityGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, direct_destination_rules, direct_members, direct_source_rules, entity_id, entity_type, excluded_members, indirect_destination_rules, indirect_source_rules, ip_sets, members, name, nsx_managers, parents, scope, security_tags, translated_vm_count, vendor_id


## getSecurityTag

> SecurityTag getSecurityTag(id, opts)

Show security tag details

Show security tag details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getSecurityTag(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**SecurityTag**](SecurityTag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, description, direct_security_groups, entity_id, entity_type, name, nsx_manager, security_groups, vendor_id


## getService

> BaseService getService(id, opts)

Show service details

Show service details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getService(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseService**](BaseService.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, name, nsx_managers, port_ranges, protocol, scope, vendor_id


## getServiceGroup

> BaseServiceGroup getServiceGroup(id, opts)

Show service group details

Show service group details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getServiceGroup(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseServiceGroup**](BaseServiceGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, members, name, nsx_managers, scope, vendor_id


## getVcenterManager

> VCenterManager getVcenterManager(id, opts)

Show vCenter manager details

Show vCenter manager details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getVcenterManager(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**VCenterManager**](VCenterManager.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, ip_address, name


## getVm

> BaseVirtualMachine getVm(id, opts)

Show vm details

Show vm details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getVm(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseVirtualMachine**](BaseVirtualMachine.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, applied_to_destination_rules, applied_to_source_rules, cluster, datacenter, datastores, default_gateway, destination_firewall_rules, destination_inversion_rules, entity_id, entity_type, folders, host, ip_addresses, ip_sets, layer2_networks, name, nsx_manager, resource_pool, security_groups, security_tags, source_firewall_rules, source_inversion_rules, vcenter_manager, vendor_id, vlans, vnics


## getVmknic

> Vmknic getVmknic(id, opts)

Show vmknic details

Show vmknic details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getVmknic(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**Vmknic**](Vmknic.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, host, ip_addresses, layer2_network, name, vlan


## getVnic

> BaseVnic getVnic(id, opts)

Show vnic details

Show vnic details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let id = "id_example"; // String | entity id
let opts = {
  'time': 789 // Number | time in epoch seconds
};
apiInstance.getVnic(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| entity id | 
 **time** | **Number**| time in epoch seconds | [optional] 

### Return type

[**BaseVnic**](BaseVnic.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_id, entity_type, ip_addresses, layer2_network, name, vlan, vm


## listClusters

> PagedListResponseWithTime listClusters(opts)

List clusters

List clusters

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listClusters(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listDatacenters

> PagedListResponseWithTime listDatacenters(opts)

List vCenter datacenters

List vCenter datacenters

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listDatacenters(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listDatastores

> PagedListResponseWithTime listDatastores(opts)

List datastores

List datastores

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listDatastores(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listDistributedVirtualPortgroups

> PagedListResponseWithTime listDistributedVirtualPortgroups(opts)

List distributed virtual portgroups

List distributed virtual portgroups

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listDistributedVirtualPortgroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listDistributedVirtualSwitches

> PagedListResponseWithTime listDistributedVirtualSwitches(opts)

List distributed virtual switches

List distributed virtual switches

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listDistributedVirtualSwitches(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listFirewallRules

> PagedListResponseWithTime listFirewallRules(opts)

List firewall rules

List firewall rules

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listFirewallRules(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listFirewalls

> PagedListResponseWithTime listFirewalls(opts)

List firewalls

List firewalls

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listFirewalls(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listFolders

> PagedListResponseWithTime listFolders(opts)

List folders

List folders

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listFolders(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listHosts

> PagedListResponseWithTime listHosts(opts)

List hosts

List hosts

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listHosts(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listIPSets

> PagedListResponseWithTime listIPSets(opts)

List ip sets

List ip sets

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listIPSets(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listLayer2Networks

> PagedListResponseWithTime listLayer2Networks(opts)

List layer2 networks

List layer2 networks

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listLayer2Networks(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listNSXManagers

> PagedListResponseWithTime listNSXManagers(opts)

List nsx managers

List nsx managers

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listNSXManagers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listProblemEvents

> PagedListResponseWithTime listProblemEvents(opts)

List problems

List problem events.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listProblemEvents(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listSecurityGroups

> PagedListResponseWithTime listSecurityGroups(opts)

List security groups

List security groups

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listSecurityGroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listSecurityTags

> PagedListResponseWithTime listSecurityTags(opts)

List security tags

List security tags

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listSecurityTags(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listServiceGroups

> PagedListResponseWithTime listServiceGroups(opts)

List service groups

List service groups

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listServiceGroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listServices

> PagedListResponseWithTime listServices(opts)

List services

List services

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listServices(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listVcenterManagers

> PagedListResponseWithTime listVcenterManagers(opts)

List vCenter managers

List vCenter managers

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listVcenterManagers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listVmknics

> PagedListResponseWithTime listVmknics(opts)

List vmknics

List vmknics

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listVmknics(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listVms

> PagedListResponseWithTime listVms(opts)

List vms

List vms

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listVms(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count


## listVnics

> PagedListResponseWithTime listVnics(opts)

List vnics

List vnics

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.EntitiesApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listVnics(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, cursor, end_time, results, start_time, total_count

