# SwitchApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNetworkSwitchStack**](SwitchApi.md#addNetworkSwitchStack) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/add | Add a switch to a stack |
| [**cloneOrganizationSwitchDevices**](SwitchApi.md#cloneOrganizationSwitchDevices) | **POST** /organizations/{organizationId}/switch/devices/clone | Clone port-level and some switch-level configuration settings from a source switch to one or more target switches |
| [**createDeviceSwitchRoutingInterface**](SwitchApi.md#createDeviceSwitchRoutingInterface) | **POST** /devices/{serial}/switch/routing/interfaces | Create a layer 3 interface for a switch |
| [**createDeviceSwitchRoutingStaticRoute**](SwitchApi.md#createDeviceSwitchRoutingStaticRoute) | **POST** /devices/{serial}/switch/routing/staticRoutes | Create a layer 3 static route for a switch |
| [**createNetworkSwitchAccessPolicy**](SwitchApi.md#createNetworkSwitchAccessPolicy) | **POST** /networks/{networkId}/switch/accessPolicies | Create an access policy for a switch network |
| [**createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer**](SwitchApi.md#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer) | **POST** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Add a server to be trusted by Dynamic ARP Inspection on this network |
| [**createNetworkSwitchLinkAggregation**](SwitchApi.md#createNetworkSwitchLinkAggregation) | **POST** /networks/{networkId}/switch/linkAggregations | Create a link aggregation group |
| [**createNetworkSwitchPortSchedule**](SwitchApi.md#createNetworkSwitchPortSchedule) | **POST** /networks/{networkId}/switch/portSchedules | Add a switch port schedule |
| [**createNetworkSwitchQosRule**](SwitchApi.md#createNetworkSwitchQosRule) | **POST** /networks/{networkId}/switch/qosRules | Add a quality of service rule |
| [**createNetworkSwitchRoutingMulticastRendezvousPoint**](SwitchApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point |
| [**createNetworkSwitchStack**](SwitchApi.md#createNetworkSwitchStack) | **POST** /networks/{networkId}/switch/stacks | Create a stack |
| [**createNetworkSwitchStackRoutingInterface**](SwitchApi.md#createNetworkSwitchStackRoutingInterface) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | Create a layer 3 interface for a switch stack |
| [**createNetworkSwitchStackRoutingStaticRoute**](SwitchApi.md#createNetworkSwitchStackRoutingStaticRoute) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | Create a layer 3 static route for a switch stack |
| [**cycleDeviceSwitchPorts**](SwitchApi.md#cycleDeviceSwitchPorts) | **POST** /devices/{serial}/switch/ports/cycle | Cycle a set of switch ports |
| [**deleteDeviceSwitchRoutingInterface**](SwitchApi.md#deleteDeviceSwitchRoutingInterface) | **DELETE** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Delete a layer 3 interface from the switch |
| [**deleteDeviceSwitchRoutingStaticRoute**](SwitchApi.md#deleteDeviceSwitchRoutingStaticRoute) | **DELETE** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch |
| [**deleteNetworkSwitchAccessPolicy**](SwitchApi.md#deleteNetworkSwitchAccessPolicy) | **DELETE** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Delete an access policy for a switch network |
| [**deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer**](SwitchApi.md#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer) | **DELETE** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Remove a server from being trusted by Dynamic ARP Inspection on this network |
| [**deleteNetworkSwitchLinkAggregation**](SwitchApi.md#deleteNetworkSwitchLinkAggregation) | **DELETE** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Split a link aggregation group into separate ports |
| [**deleteNetworkSwitchPortSchedule**](SwitchApi.md#deleteNetworkSwitchPortSchedule) | **DELETE** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Delete a switch port schedule |
| [**deleteNetworkSwitchQosRule**](SwitchApi.md#deleteNetworkSwitchQosRule) | **DELETE** /networks/{networkId}/switch/qosRules/{qosRuleId} | Delete a quality of service rule |
| [**deleteNetworkSwitchRoutingMulticastRendezvousPoint**](SwitchApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point |
| [**deleteNetworkSwitchStack**](SwitchApi.md#deleteNetworkSwitchStack) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId} | Delete a stack |
| [**deleteNetworkSwitchStackRoutingInterface**](SwitchApi.md#deleteNetworkSwitchStackRoutingInterface) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Delete a layer 3 interface from a switch stack |
| [**deleteNetworkSwitchStackRoutingStaticRoute**](SwitchApi.md#deleteNetworkSwitchStackRoutingStaticRoute) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch stack |
| [**getDeviceSwitchPort**](SwitchApi.md#getDeviceSwitchPort) | **GET** /devices/{serial}/switch/ports/{portId} | Return a switch port |
| [**getDeviceSwitchPorts**](SwitchApi.md#getDeviceSwitchPorts) | **GET** /devices/{serial}/switch/ports | List the switch ports for a switch |
| [**getDeviceSwitchPortsStatuses**](SwitchApi.md#getDeviceSwitchPortsStatuses) | **GET** /devices/{serial}/switch/ports/statuses | Return the status for all the ports of a switch |
| [**getDeviceSwitchPortsStatusesPackets**](SwitchApi.md#getDeviceSwitchPortsStatusesPackets) | **GET** /devices/{serial}/switch/ports/statuses/packets | Return the packet counters for all the ports of a switch |
| [**getDeviceSwitchRoutingInterface**](SwitchApi.md#getDeviceSwitchRoutingInterface) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Return a layer 3 interface for a switch |
| [**getDeviceSwitchRoutingInterfaceDhcp**](SwitchApi.md#getDeviceSwitchRoutingInterfaceDhcp) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch |
| [**getDeviceSwitchRoutingInterfaces**](SwitchApi.md#getDeviceSwitchRoutingInterfaces) | **GET** /devices/{serial}/switch/routing/interfaces | List layer 3 interfaces for a switch |
| [**getDeviceSwitchRoutingStaticRoute**](SwitchApi.md#getDeviceSwitchRoutingStaticRoute) | **GET** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch |
| [**getDeviceSwitchRoutingStaticRoutes**](SwitchApi.md#getDeviceSwitchRoutingStaticRoutes) | **GET** /devices/{serial}/switch/routing/staticRoutes | List layer 3 static routes for a switch |
| [**getDeviceSwitchWarmSpare**](SwitchApi.md#getDeviceSwitchWarmSpare) | **GET** /devices/{serial}/switch/warmSpare | Return warm spare configuration for a switch |
| [**getNetworkSwitchAccessControlLists**](SwitchApi.md#getNetworkSwitchAccessControlLists) | **GET** /networks/{networkId}/switch/accessControlLists | Return the access control lists for a MS network |
| [**getNetworkSwitchAccessPolicies**](SwitchApi.md#getNetworkSwitchAccessPolicies) | **GET** /networks/{networkId}/switch/accessPolicies | List the access policies for a switch network |
| [**getNetworkSwitchAccessPolicy**](SwitchApi.md#getNetworkSwitchAccessPolicy) | **GET** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Return a specific access policy for a switch network |
| [**getNetworkSwitchAlternateManagementInterface**](SwitchApi.md#getNetworkSwitchAlternateManagementInterface) | **GET** /networks/{networkId}/switch/alternateManagementInterface | Return the switch alternate management interface for the network |
| [**getNetworkSwitchDhcpServerPolicy**](SwitchApi.md#getNetworkSwitchDhcpServerPolicy) | **GET** /networks/{networkId}/switch/dhcpServerPolicy | Return the DHCP server settings |
| [**getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers**](SwitchApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Return the list of servers trusted by Dynamic ARP Inspection on this network |
| [**getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice**](SwitchApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice | Return the devices that have a Dynamic ARP Inspection warning and their warnings |
| [**getNetworkSwitchDhcpV4ServersSeen**](SwitchApi.md#getNetworkSwitchDhcpV4ServersSeen) | **GET** /networks/{networkId}/switch/dhcp/v4/servers/seen | Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day) |
| [**getNetworkSwitchDscpToCosMappings**](SwitchApi.md#getNetworkSwitchDscpToCosMappings) | **GET** /networks/{networkId}/switch/dscpToCosMappings | Return the DSCP to CoS mappings |
| [**getNetworkSwitchLinkAggregations**](SwitchApi.md#getNetworkSwitchLinkAggregations) | **GET** /networks/{networkId}/switch/linkAggregations | List link aggregation groups |
| [**getNetworkSwitchMtu**](SwitchApi.md#getNetworkSwitchMtu) | **GET** /networks/{networkId}/switch/mtu | Return the MTU configuration |
| [**getNetworkSwitchPortSchedules**](SwitchApi.md#getNetworkSwitchPortSchedules) | **GET** /networks/{networkId}/switch/portSchedules | List switch port schedules |
| [**getNetworkSwitchQosRule**](SwitchApi.md#getNetworkSwitchQosRule) | **GET** /networks/{networkId}/switch/qosRules/{qosRuleId} | Return a quality of service rule |
| [**getNetworkSwitchQosRules**](SwitchApi.md#getNetworkSwitchQosRules) | **GET** /networks/{networkId}/switch/qosRules | List quality of service rules |
| [**getNetworkSwitchQosRulesOrder**](SwitchApi.md#getNetworkSwitchQosRulesOrder) | **GET** /networks/{networkId}/switch/qosRules/order | Return the quality of service rule IDs by order in which they will be processed by the switch |
| [**getNetworkSwitchRoutingMulticast**](SwitchApi.md#getNetworkSwitchRoutingMulticast) | **GET** /networks/{networkId}/switch/routing/multicast | Return multicast settings for a network |
| [**getNetworkSwitchRoutingMulticastRendezvousPoint**](SwitchApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point |
| [**getNetworkSwitchRoutingMulticastRendezvousPoints**](SwitchApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points |
| [**getNetworkSwitchRoutingOspf**](SwitchApi.md#getNetworkSwitchRoutingOspf) | **GET** /networks/{networkId}/switch/routing/ospf | Return layer 3 OSPF routing configuration |
| [**getNetworkSwitchSettings**](SwitchApi.md#getNetworkSwitchSettings) | **GET** /networks/{networkId}/switch/settings | Returns the switch network settings |
| [**getNetworkSwitchStack**](SwitchApi.md#getNetworkSwitchStack) | **GET** /networks/{networkId}/switch/stacks/{switchStackId} | Show a switch stack |
| [**getNetworkSwitchStackRoutingInterface**](SwitchApi.md#getNetworkSwitchStackRoutingInterface) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Return a layer 3 interface from a switch stack |
| [**getNetworkSwitchStackRoutingInterfaceDhcp**](SwitchApi.md#getNetworkSwitchStackRoutingInterfaceDhcp) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch stack |
| [**getNetworkSwitchStackRoutingInterfaces**](SwitchApi.md#getNetworkSwitchStackRoutingInterfaces) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | List layer 3 interfaces for a switch stack |
| [**getNetworkSwitchStackRoutingStaticRoute**](SwitchApi.md#getNetworkSwitchStackRoutingStaticRoute) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch stack |
| [**getNetworkSwitchStackRoutingStaticRoutes**](SwitchApi.md#getNetworkSwitchStackRoutingStaticRoutes) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | List layer 3 static routes for a switch stack |
| [**getNetworkSwitchStacks**](SwitchApi.md#getNetworkSwitchStacks) | **GET** /networks/{networkId}/switch/stacks | List the switch stacks in a network |
| [**getNetworkSwitchStormControl**](SwitchApi.md#getNetworkSwitchStormControl) | **GET** /networks/{networkId}/switch/stormControl | Return the storm control configuration for a switch network |
| [**getNetworkSwitchStp**](SwitchApi.md#getNetworkSwitchStp) | **GET** /networks/{networkId}/switch/stp | Returns STP settings |
| [**getOrganizationConfigTemplateSwitchProfilePort**](SwitchApi.md#getOrganizationConfigTemplateSwitchProfilePort) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Return a switch profile port |
| [**getOrganizationConfigTemplateSwitchProfilePorts**](SwitchApi.md#getOrganizationConfigTemplateSwitchProfilePorts) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports | Return all the ports of a switch profile |
| [**getOrganizationConfigTemplateSwitchProfiles**](SwitchApi.md#getOrganizationConfigTemplateSwitchProfiles) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles | List the switch profiles for your switch template configuration |
| [**getOrganizationSwitchPortsBySwitch**](SwitchApi.md#getOrganizationSwitchPortsBySwitch) | **GET** /organizations/{organizationId}/switch/ports/bySwitch | List the switchports in an organization by switch |
| [**removeNetworkSwitchStack**](SwitchApi.md#removeNetworkSwitchStack) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/remove | Remove a switch from a stack |
| [**updateDeviceSwitchPort**](SwitchApi.md#updateDeviceSwitchPort) | **PUT** /devices/{serial}/switch/ports/{portId} | Update a switch port |
| [**updateDeviceSwitchRoutingInterface**](SwitchApi.md#updateDeviceSwitchRoutingInterface) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch |
| [**updateDeviceSwitchRoutingInterfaceDhcp**](SwitchApi.md#updateDeviceSwitchRoutingInterfaceDhcp) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch |
| [**updateDeviceSwitchRoutingStaticRoute**](SwitchApi.md#updateDeviceSwitchRoutingStaticRoute) | **PUT** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch |
| [**updateDeviceSwitchWarmSpare**](SwitchApi.md#updateDeviceSwitchWarmSpare) | **PUT** /devices/{serial}/switch/warmSpare | Update warm spare configuration for a switch |
| [**updateNetworkSwitchAccessControlLists**](SwitchApi.md#updateNetworkSwitchAccessControlLists) | **PUT** /networks/{networkId}/switch/accessControlLists | Update the access control lists for a MS network |
| [**updateNetworkSwitchAccessPolicy**](SwitchApi.md#updateNetworkSwitchAccessPolicy) | **PUT** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Update an access policy for a switch network |
| [**updateNetworkSwitchAlternateManagementInterface**](SwitchApi.md#updateNetworkSwitchAlternateManagementInterface) | **PUT** /networks/{networkId}/switch/alternateManagementInterface | Update the switch alternate management interface for the network |
| [**updateNetworkSwitchDhcpServerPolicy**](SwitchApi.md#updateNetworkSwitchDhcpServerPolicy) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy | Update the DHCP server settings |
| [**updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer**](SwitchApi.md#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Update a server that is trusted by Dynamic ARP Inspection on this network |
| [**updateNetworkSwitchDscpToCosMappings**](SwitchApi.md#updateNetworkSwitchDscpToCosMappings) | **PUT** /networks/{networkId}/switch/dscpToCosMappings | Update the DSCP to CoS mappings |
| [**updateNetworkSwitchLinkAggregation**](SwitchApi.md#updateNetworkSwitchLinkAggregation) | **PUT** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Update a link aggregation group |
| [**updateNetworkSwitchMtu**](SwitchApi.md#updateNetworkSwitchMtu) | **PUT** /networks/{networkId}/switch/mtu | Update the MTU configuration |
| [**updateNetworkSwitchPortSchedule**](SwitchApi.md#updateNetworkSwitchPortSchedule) | **PUT** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Update a switch port schedule |
| [**updateNetworkSwitchQosRule**](SwitchApi.md#updateNetworkSwitchQosRule) | **PUT** /networks/{networkId}/switch/qosRules/{qosRuleId} | Update a quality of service rule |
| [**updateNetworkSwitchQosRulesOrder**](SwitchApi.md#updateNetworkSwitchQosRulesOrder) | **PUT** /networks/{networkId}/switch/qosRules/order | Update the order in which the rules should be processed by the switch |
| [**updateNetworkSwitchRoutingMulticast**](SwitchApi.md#updateNetworkSwitchRoutingMulticast) | **PUT** /networks/{networkId}/switch/routing/multicast | Update multicast settings for a network |
| [**updateNetworkSwitchRoutingMulticastRendezvousPoint**](SwitchApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point |
| [**updateNetworkSwitchRoutingOspf**](SwitchApi.md#updateNetworkSwitchRoutingOspf) | **PUT** /networks/{networkId}/switch/routing/ospf | Update layer 3 OSPF routing configuration |
| [**updateNetworkSwitchSettings**](SwitchApi.md#updateNetworkSwitchSettings) | **PUT** /networks/{networkId}/switch/settings | Update switch network settings |
| [**updateNetworkSwitchStackRoutingInterface**](SwitchApi.md#updateNetworkSwitchStackRoutingInterface) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch stack |
| [**updateNetworkSwitchStackRoutingInterfaceDhcp**](SwitchApi.md#updateNetworkSwitchStackRoutingInterfaceDhcp) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch stack |
| [**updateNetworkSwitchStackRoutingStaticRoute**](SwitchApi.md#updateNetworkSwitchStackRoutingStaticRoute) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch stack |
| [**updateNetworkSwitchStormControl**](SwitchApi.md#updateNetworkSwitchStormControl) | **PUT** /networks/{networkId}/switch/stormControl | Update the storm control configuration for a switch network |
| [**updateNetworkSwitchStp**](SwitchApi.md#updateNetworkSwitchStp) | **PUT** /networks/{networkId}/switch/stp | Updates STP settings |
| [**updateOrganizationConfigTemplateSwitchProfilePort**](SwitchApi.md#updateOrganizationConfigTemplateSwitchProfilePort) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Update a switch profile port |


<a id="addNetworkSwitchStack"></a>
# **addNetworkSwitchStack**
> Object addNetworkSwitchStack(networkId, switchStackId, addNetworkSwitchStackRequest)

Add a switch to a stack

Add a switch to a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    AddNetworkSwitchStackRequest addNetworkSwitchStackRequest = new AddNetworkSwitchStackRequest(); // AddNetworkSwitchStackRequest | 
    try {
      Object result = apiInstance.addNetworkSwitchStack(networkId, switchStackId, addNetworkSwitchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#addNetworkSwitchStack");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **addNetworkSwitchStackRequest** | [**AddNetworkSwitchStackRequest**](AddNetworkSwitchStackRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="cloneOrganizationSwitchDevices"></a>
# **cloneOrganizationSwitchDevices**
> Object cloneOrganizationSwitchDevices(organizationId, cloneOrganizationSwitchDevicesRequest)

Clone port-level and some switch-level configuration settings from a source switch to one or more target switches

Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CloneOrganizationSwitchDevicesRequest cloneOrganizationSwitchDevicesRequest = new CloneOrganizationSwitchDevicesRequest(); // CloneOrganizationSwitchDevicesRequest | 
    try {
      Object result = apiInstance.cloneOrganizationSwitchDevices(organizationId, cloneOrganizationSwitchDevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#cloneOrganizationSwitchDevices");
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
| **organizationId** | **String**|  | |
| **cloneOrganizationSwitchDevicesRequest** | [**CloneOrganizationSwitchDevicesRequest**](CloneOrganizationSwitchDevicesRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createDeviceSwitchRoutingInterface"></a>
# **createDeviceSwitchRoutingInterface**
> GetDeviceSwitchRoutingInterfaces200ResponseInner createDeviceSwitchRoutingInterface(serial, createDeviceSwitchRoutingInterfaceRequest)

Create a layer 3 interface for a switch

Create a layer 3 interface for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = new CreateDeviceSwitchRoutingInterfaceRequest(); // CreateDeviceSwitchRoutingInterfaceRequest | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.createDeviceSwitchRoutingInterface(serial, createDeviceSwitchRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createDeviceSwitchRoutingInterface");
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
| **serial** | **String**|  | |
| **createDeviceSwitchRoutingInterfaceRequest** | [**CreateDeviceSwitchRoutingInterfaceRequest**](CreateDeviceSwitchRoutingInterfaceRequest.md)|  | [optional] |

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createDeviceSwitchRoutingStaticRoute"></a>
# **createDeviceSwitchRoutingStaticRoute**
> Object createDeviceSwitchRoutingStaticRoute(serial, createDeviceSwitchRoutingStaticRouteRequest)

Create a layer 3 static route for a switch

Create a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceSwitchRoutingStaticRouteRequest createDeviceSwitchRoutingStaticRouteRequest = new CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.createDeviceSwitchRoutingStaticRoute(serial, createDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createDeviceSwitchRoutingStaticRoute");
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
| **serial** | **String**|  | |
| **createDeviceSwitchRoutingStaticRouteRequest** | [**CreateDeviceSwitchRoutingStaticRouteRequest**](CreateDeviceSwitchRoutingStaticRouteRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchAccessPolicy"></a>
# **createNetworkSwitchAccessPolicy**
> GetNetworkSwitchAccessPolicies200ResponseInner createNetworkSwitchAccessPolicy(networkId, createNetworkSwitchAccessPolicyRequest)

Create an access policy for a switch network

Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchAccessPolicyRequest createNetworkSwitchAccessPolicyRequest = new CreateNetworkSwitchAccessPolicyRequest(); // CreateNetworkSwitchAccessPolicyRequest | 
    try {
      GetNetworkSwitchAccessPolicies200ResponseInner result = apiInstance.createNetworkSwitchAccessPolicy(networkId, createNetworkSwitchAccessPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchAccessPolicy");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchAccessPolicyRequest** | [**CreateNetworkSwitchAccessPolicyRequest**](CreateNetworkSwitchAccessPolicyRequest.md)|  | |

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer"></a>
# **createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer**
> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

Add a server to be trusted by Dynamic ARP Inspection on this network

Add a server to be trusted by Dynamic ARP Inspection on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
    try {
      GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner result = apiInstance.createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest** | [**CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest**](CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.md)|  | |

### Return type

[**GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchLinkAggregation"></a>
# **createNetworkSwitchLinkAggregation**
> Object createNetworkSwitchLinkAggregation(networkId, createNetworkSwitchLinkAggregationRequest)

Create a link aggregation group

Create a link aggregation group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchLinkAggregationRequest createNetworkSwitchLinkAggregationRequest = new CreateNetworkSwitchLinkAggregationRequest(); // CreateNetworkSwitchLinkAggregationRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchLinkAggregation(networkId, createNetworkSwitchLinkAggregationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchLinkAggregation");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchLinkAggregationRequest** | [**CreateNetworkSwitchLinkAggregationRequest**](CreateNetworkSwitchLinkAggregationRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchPortSchedule"></a>
# **createNetworkSwitchPortSchedule**
> Object createNetworkSwitchPortSchedule(networkId, createNetworkSwitchPortScheduleRequest)

Add a switch port schedule

Add a switch port schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchPortScheduleRequest createNetworkSwitchPortScheduleRequest = new CreateNetworkSwitchPortScheduleRequest(); // CreateNetworkSwitchPortScheduleRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchPortSchedule(networkId, createNetworkSwitchPortScheduleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchPortSchedule");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchPortScheduleRequest** | [**CreateNetworkSwitchPortScheduleRequest**](CreateNetworkSwitchPortScheduleRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchQosRule"></a>
# **createNetworkSwitchQosRule**
> Object createNetworkSwitchQosRule(networkId, createNetworkSwitchQosRuleRequest)

Add a quality of service rule

Add a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchQosRuleRequest createNetworkSwitchQosRuleRequest = new CreateNetworkSwitchQosRuleRequest(); // CreateNetworkSwitchQosRuleRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchQosRule(networkId, createNetworkSwitchQosRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchQosRule");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchQosRuleRequest** | [**CreateNetworkSwitchQosRuleRequest**](CreateNetworkSwitchQosRuleRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchRoutingMulticastRendezvousPoint"></a>
# **createNetworkSwitchRoutingMulticastRendezvousPoint**
> Object createNetworkSwitchRoutingMulticastRendezvousPoint(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

Create a multicast rendezvous point

Create a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchRoutingMulticastRendezvousPointRequest createNetworkSwitchRoutingMulticastRendezvousPointRequest = new CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchRoutingMulticastRendezvousPoint");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**CreateNetworkSwitchRoutingMulticastRendezvousPointRequest**](CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchStack"></a>
# **createNetworkSwitchStack**
> Object createNetworkSwitchStack(networkId, createNetworkSwitchStackRequest)

Create a stack

Create a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchStackRequest createNetworkSwitchStackRequest = new CreateNetworkSwitchStackRequest(); // CreateNetworkSwitchStackRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStack(networkId, createNetworkSwitchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchStack");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchStackRequest** | [**CreateNetworkSwitchStackRequest**](CreateNetworkSwitchStackRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchStackRoutingInterface"></a>
# **createNetworkSwitchStackRoutingInterface**
> Object createNetworkSwitchStackRoutingInterface(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest)

Create a layer 3 interface for a switch stack

Create a layer 3 interface for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateNetworkSwitchStackRoutingInterfaceRequest createNetworkSwitchStackRoutingInterfaceRequest = new CreateNetworkSwitchStackRoutingInterfaceRequest(); // CreateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingInterface(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchStackRoutingInterface");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **createNetworkSwitchStackRoutingInterfaceRequest** | [**CreateNetworkSwitchStackRoutingInterfaceRequest**](CreateNetworkSwitchStackRoutingInterfaceRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchStackRoutingStaticRoute"></a>
# **createNetworkSwitchStackRoutingStaticRoute**
> Object createNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest)

Create a layer 3 static route for a switch stack

Create a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateDeviceSwitchRoutingStaticRouteRequest createDeviceSwitchRoutingStaticRouteRequest = new CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#createNetworkSwitchStackRoutingStaticRoute");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **createDeviceSwitchRoutingStaticRouteRequest** | [**CreateDeviceSwitchRoutingStaticRouteRequest**](CreateDeviceSwitchRoutingStaticRouteRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="cycleDeviceSwitchPorts"></a>
# **cycleDeviceSwitchPorts**
> Object cycleDeviceSwitchPorts(serial, cycleDeviceSwitchPortsRequest)

Cycle a set of switch ports

Cycle a set of switch ports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    CycleDeviceSwitchPortsRequest cycleDeviceSwitchPortsRequest = new CycleDeviceSwitchPortsRequest(); // CycleDeviceSwitchPortsRequest | 
    try {
      Object result = apiInstance.cycleDeviceSwitchPorts(serial, cycleDeviceSwitchPortsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#cycleDeviceSwitchPorts");
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
| **serial** | **String**|  | |
| **cycleDeviceSwitchPortsRequest** | [**CycleDeviceSwitchPortsRequest**](CycleDeviceSwitchPortsRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="deleteDeviceSwitchRoutingInterface"></a>
# **deleteDeviceSwitchRoutingInterface**
> deleteDeviceSwitchRoutingInterface(serial, interfaceId)

Delete a layer 3 interface from the switch

Delete a layer 3 interface from the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteDeviceSwitchRoutingInterface(serial, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteDeviceSwitchRoutingInterface");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteDeviceSwitchRoutingStaticRoute"></a>
# **deleteDeviceSwitchRoutingStaticRoute**
> deleteDeviceSwitchRoutingStaticRoute(serial, staticRouteId)

Delete a layer 3 static route for a switch

Delete a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteDeviceSwitchRoutingStaticRoute(serial, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteDeviceSwitchRoutingStaticRoute");
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
| **serial** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchAccessPolicy"></a>
# **deleteNetworkSwitchAccessPolicy**
> deleteNetworkSwitchAccessPolicy(networkId, accessPolicyNumber)

Delete an access policy for a switch network

Delete an access policy for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String accessPolicyNumber = "accessPolicyNumber_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchAccessPolicy(networkId, accessPolicyNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchAccessPolicy");
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
| **networkId** | **String**|  | |
| **accessPolicyNumber** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer"></a>
# **deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer**
> deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId, trustedServerId)

Remove a server from being trusted by Dynamic ARP Inspection on this network

Remove a server from being trusted by Dynamic ARP Inspection on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String trustedServerId = "trustedServerId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId, trustedServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer");
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
| **networkId** | **String**|  | |
| **trustedServerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchLinkAggregation"></a>
# **deleteNetworkSwitchLinkAggregation**
> deleteNetworkSwitchLinkAggregation(networkId, linkAggregationId)

Split a link aggregation group into separate ports

Split a link aggregation group into separate ports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String linkAggregationId = "linkAggregationId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchLinkAggregation(networkId, linkAggregationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchLinkAggregation");
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
| **networkId** | **String**|  | |
| **linkAggregationId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchPortSchedule"></a>
# **deleteNetworkSwitchPortSchedule**
> deleteNetworkSwitchPortSchedule(networkId, portScheduleId)

Delete a switch port schedule

Delete a switch port schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String portScheduleId = "portScheduleId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchPortSchedule(networkId, portScheduleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchPortSchedule");
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
| **networkId** | **String**|  | |
| **portScheduleId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchQosRule"></a>
# **deleteNetworkSwitchQosRule**
> deleteNetworkSwitchQosRule(networkId, qosRuleId)

Delete a quality of service rule

Delete a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchQosRule(networkId, qosRuleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchQosRule");
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
| **networkId** | **String**|  | |
| **qosRuleId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchRoutingMulticastRendezvousPoint"></a>
# **deleteNetworkSwitchRoutingMulticastRendezvousPoint**
> deleteNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId)

Delete a multicast rendezvous point

Delete a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchRoutingMulticastRendezvousPoint");
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
| **networkId** | **String**|  | |
| **rendezvousPointId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchStack"></a>
# **deleteNetworkSwitchStack**
> deleteNetworkSwitchStack(networkId, switchStackId)

Delete a stack

Delete a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStack(networkId, switchStackId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchStack");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchStackRoutingInterface"></a>
# **deleteNetworkSwitchStackRoutingInterface**
> deleteNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId)

Delete a layer 3 interface from a switch stack

Delete a layer 3 interface from a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchStackRoutingInterface");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchStackRoutingStaticRoute"></a>
# **deleteNetworkSwitchStackRoutingStaticRoute**
> deleteNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId)

Delete a layer 3 static route for a switch stack

Delete a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#deleteNetworkSwitchStackRoutingStaticRoute");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getDeviceSwitchPort"></a>
# **getDeviceSwitchPort**
> GetDeviceSwitchPorts200ResponseInner getDeviceSwitchPort(serial, portId)

Return a switch port

Return a switch port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String portId = "portId_example"; // String | 
    try {
      GetDeviceSwitchPorts200ResponseInner result = apiInstance.getDeviceSwitchPort(serial, portId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchPort");
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
| **serial** | **String**|  | |
| **portId** | **String**|  | |

### Return type

[**GetDeviceSwitchPorts200ResponseInner**](GetDeviceSwitchPorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchPorts"></a>
# **getDeviceSwitchPorts**
> List&lt;GetDeviceSwitchPorts200ResponseInner&gt; getDeviceSwitchPorts(serial)

List the switch ports for a switch

List the switch ports for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<GetDeviceSwitchPorts200ResponseInner> result = apiInstance.getDeviceSwitchPorts(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchPorts");
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
| **serial** | **String**|  | |

### Return type

[**List&lt;GetDeviceSwitchPorts200ResponseInner&gt;**](GetDeviceSwitchPorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchPortsStatuses"></a>
# **getDeviceSwitchPortsStatuses**
> List&lt;GetDeviceSwitchPortsStatuses200ResponseInner&gt; getDeviceSwitchPortsStatuses(serial, t0, timespan)

Return the status for all the ports of a switch

Return the status for all the ports of a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetDeviceSwitchPortsStatuses200ResponseInner> result = apiInstance.getDeviceSwitchPortsStatuses(serial, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchPortsStatuses");
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
| **serial** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetDeviceSwitchPortsStatuses200ResponseInner&gt;**](GetDeviceSwitchPortsStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchPortsStatusesPackets"></a>
# **getDeviceSwitchPortsStatusesPackets**
> List&lt;Object&gt; getDeviceSwitchPortsStatusesPackets(serial, t0, timespan)

Return the packet counters for all the ports of a switch

Return the packet counters for all the ports of a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    try {
      List<Object> result = apiInstance.getDeviceSwitchPortsStatusesPackets(serial, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchPortsStatusesPackets");
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
| **serial** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 1 day from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingInterface"></a>
# **getDeviceSwitchRoutingInterface**
> GetDeviceSwitchRoutingInterfaces200ResponseInner getDeviceSwitchRoutingInterface(serial, interfaceId)

Return a layer 3 interface for a switch

Return a layer 3 interface for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.getDeviceSwitchRoutingInterface(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchRoutingInterface");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingInterfaceDhcp"></a>
# **getDeviceSwitchRoutingInterfaceDhcp**
> Object getDeviceSwitchRoutingInterfaceDhcp(serial, interfaceId)

Return a layer 3 interface DHCP configuration for a switch

Return a layer 3 interface DHCP configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getDeviceSwitchRoutingInterfaceDhcp(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchRoutingInterfaceDhcp");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingInterfaces"></a>
# **getDeviceSwitchRoutingInterfaces**
> List&lt;GetDeviceSwitchRoutingInterfaces200ResponseInner&gt; getDeviceSwitchRoutingInterfaces(serial)

List layer 3 interfaces for a switch

List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<GetDeviceSwitchRoutingInterfaces200ResponseInner> result = apiInstance.getDeviceSwitchRoutingInterfaces(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchRoutingInterfaces");
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
| **serial** | **String**|  | |

### Return type

[**List&lt;GetDeviceSwitchRoutingInterfaces200ResponseInner&gt;**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingStaticRoute"></a>
# **getDeviceSwitchRoutingStaticRoute**
> GetDeviceSwitchRoutingStaticRoute200Response getDeviceSwitchRoutingStaticRoute(serial, staticRouteId)

Return a layer 3 static route for a switch

Return a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      GetDeviceSwitchRoutingStaticRoute200Response result = apiInstance.getDeviceSwitchRoutingStaticRoute(serial, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchRoutingStaticRoute");
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
| **serial** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

[**GetDeviceSwitchRoutingStaticRoute200Response**](GetDeviceSwitchRoutingStaticRoute200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingStaticRoutes"></a>
# **getDeviceSwitchRoutingStaticRoutes**
> List&lt;Object&gt; getDeviceSwitchRoutingStaticRoutes(serial)

List layer 3 static routes for a switch

List layer 3 static routes for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceSwitchRoutingStaticRoutes(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchRoutingStaticRoutes");
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
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchWarmSpare"></a>
# **getDeviceSwitchWarmSpare**
> Object getDeviceSwitchWarmSpare(serial)

Return warm spare configuration for a switch

Return warm spare configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceSwitchWarmSpare(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getDeviceSwitchWarmSpare");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchAccessControlLists"></a>
# **getNetworkSwitchAccessControlLists**
> GetNetworkSwitchAccessControlLists200Response getNetworkSwitchAccessControlLists(networkId)

Return the access control lists for a MS network

Return the access control lists for a MS network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchAccessControlLists200Response result = apiInstance.getNetworkSwitchAccessControlLists(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchAccessControlLists");
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
| **networkId** | **String**|  | |

### Return type

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchAccessPolicies"></a>
# **getNetworkSwitchAccessPolicies**
> List&lt;GetNetworkSwitchAccessPolicies200ResponseInner&gt; getNetworkSwitchAccessPolicies(networkId)

List the access policies for a switch network

List the access policies for a switch network. Only returns access policies with &#39;my RADIUS server&#39; as authentication method

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSwitchAccessPolicies200ResponseInner> result = apiInstance.getNetworkSwitchAccessPolicies(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchAccessPolicies");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSwitchAccessPolicies200ResponseInner&gt;**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchAccessPolicy"></a>
# **getNetworkSwitchAccessPolicy**
> GetNetworkSwitchAccessPolicies200ResponseInner getNetworkSwitchAccessPolicy(networkId, accessPolicyNumber)

Return a specific access policy for a switch network

Return a specific access policy for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String accessPolicyNumber = "accessPolicyNumber_example"; // String | 
    try {
      GetNetworkSwitchAccessPolicies200ResponseInner result = apiInstance.getNetworkSwitchAccessPolicy(networkId, accessPolicyNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchAccessPolicy");
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
| **networkId** | **String**|  | |
| **accessPolicyNumber** | **String**|  | |

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchAlternateManagementInterface"></a>
# **getNetworkSwitchAlternateManagementInterface**
> Object getNetworkSwitchAlternateManagementInterface(networkId)

Return the switch alternate management interface for the network

Return the switch alternate management interface for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchAlternateManagementInterface(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchAlternateManagementInterface");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchDhcpServerPolicy"></a>
# **getNetworkSwitchDhcpServerPolicy**
> Object getNetworkSwitchDhcpServerPolicy(networkId)

Return the DHCP server settings

Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchDhcpServerPolicy(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchDhcpServerPolicy");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers"></a>
# **getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers**
> List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner&gt; getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId, perPage, startingAfter, endingBefore)

Return the list of servers trusted by Dynamic ARP Inspection on this network

Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner> result = apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers");
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
| **networkId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner&gt;**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice"></a>
# **getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice**
> List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner&gt; getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId, perPage, startingAfter, endingBefore)

Return the devices that have a Dynamic ARP Inspection warning and their warnings

Return the devices that have a Dynamic ARP Inspection warning and their warnings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner> result = apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice");
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
| **networkId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner&gt;**](GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSwitchDhcpV4ServersSeen"></a>
# **getNetworkSwitchDhcpV4ServersSeen**
> List&lt;GetNetworkSwitchDhcpV4ServersSeen200ResponseInner&gt; getNetworkSwitchDhcpV4ServersSeen(networkId, t0, timespan, perPage, startingAfter, endingBefore)

Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpV4ServersSeen200ResponseInner> result = apiInstance.getNetworkSwitchDhcpV4ServersSeen(networkId, t0, timespan, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchDhcpV4ServersSeen");
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
| **networkId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSwitchDhcpV4ServersSeen200ResponseInner&gt;**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSwitchDscpToCosMappings"></a>
# **getNetworkSwitchDscpToCosMappings**
> Object getNetworkSwitchDscpToCosMappings(networkId)

Return the DSCP to CoS mappings

Return the DSCP to CoS mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchDscpToCosMappings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchDscpToCosMappings");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchLinkAggregations"></a>
# **getNetworkSwitchLinkAggregations**
> List&lt;Object&gt; getNetworkSwitchLinkAggregations(networkId)

List link aggregation groups

List link aggregation groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchLinkAggregations(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchLinkAggregations");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchMtu"></a>
# **getNetworkSwitchMtu**
> GetNetworkSwitchMtu200Response getNetworkSwitchMtu(networkId)

Return the MTU configuration

Return the MTU configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchMtu200Response result = apiInstance.getNetworkSwitchMtu(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchMtu");
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
| **networkId** | **String**|  | |

### Return type

[**GetNetworkSwitchMtu200Response**](GetNetworkSwitchMtu200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchPortSchedules"></a>
# **getNetworkSwitchPortSchedules**
> List&lt;Object&gt; getNetworkSwitchPortSchedules(networkId)

List switch port schedules

List switch port schedules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchPortSchedules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchPortSchedules");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchQosRule"></a>
# **getNetworkSwitchQosRule**
> Object getNetworkSwitchQosRule(networkId, qosRuleId)

Return a quality of service rule

Return a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchQosRule(networkId, qosRuleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchQosRule");
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
| **networkId** | **String**|  | |
| **qosRuleId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchQosRules"></a>
# **getNetworkSwitchQosRules**
> List&lt;Object&gt; getNetworkSwitchQosRules(networkId)

List quality of service rules

List quality of service rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchQosRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchQosRules");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchQosRulesOrder"></a>
# **getNetworkSwitchQosRulesOrder**
> Object getNetworkSwitchQosRulesOrder(networkId)

Return the quality of service rule IDs by order in which they will be processed by the switch

Return the quality of service rule IDs by order in which they will be processed by the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchQosRulesOrder(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchQosRulesOrder");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchRoutingMulticast"></a>
# **getNetworkSwitchRoutingMulticast**
> Object getNetworkSwitchRoutingMulticast(networkId)

Return multicast settings for a network

Return multicast settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticast(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchRoutingMulticast");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchRoutingMulticastRendezvousPoint"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoint**
> Object getNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId)

Return a multicast rendezvous point

Return a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchRoutingMulticastRendezvousPoint");
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
| **networkId** | **String**|  | |
| **rendezvousPointId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchRoutingMulticastRendezvousPoints"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoints**
> List&lt;List&lt;Object&gt;&gt; getNetworkSwitchRoutingMulticastRendezvousPoints(networkId)

List multicast rendezvous points

List multicast rendezvous points

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<List<Object>> result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchRoutingMulticastRendezvousPoints");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;List&lt;Object&gt;&gt;**](List.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchRoutingOspf"></a>
# **getNetworkSwitchRoutingOspf**
> Object getNetworkSwitchRoutingOspf(networkId)

Return layer 3 OSPF routing configuration

Return layer 3 OSPF routing configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingOspf(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchRoutingOspf");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchSettings"></a>
# **getNetworkSwitchSettings**
> GetNetworkSwitchSettings200Response getNetworkSwitchSettings(networkId)

Returns the switch network settings

Returns the switch network settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchSettings200Response result = apiInstance.getNetworkSwitchSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchSettings");
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
| **networkId** | **String**|  | |

### Return type

[**GetNetworkSwitchSettings200Response**](GetNetworkSwitchSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStack"></a>
# **getNetworkSwitchStack**
> GetNetworkSwitchStack200Response getNetworkSwitchStack(networkId, switchStackId)

Show a switch stack

Show a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      GetNetworkSwitchStack200Response result = apiInstance.getNetworkSwitchStack(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStack");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

[**GetNetworkSwitchStack200Response**](GetNetworkSwitchStack200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterface"></a>
# **getNetworkSwitchStackRoutingInterface**
> Object getNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId)

Return a layer 3 interface from a switch stack

Return a layer 3 interface from a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStackRoutingInterface");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterfaceDhcp"></a>
# **getNetworkSwitchStackRoutingInterfaceDhcp**
> Object getNetworkSwitchStackRoutingInterfaceDhcp(networkId, switchStackId, interfaceId)

Return a layer 3 interface DHCP configuration for a switch stack

Return a layer 3 interface DHCP configuration for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterfaceDhcp(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStackRoutingInterfaceDhcp");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterfaces"></a>
# **getNetworkSwitchStackRoutingInterfaces**
> List&lt;Object&gt; getNetworkSwitchStackRoutingInterfaces(networkId, switchStackId)

List layer 3 interfaces for a switch stack

List layer 3 interfaces for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingInterfaces(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStackRoutingInterfaces");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingStaticRoute"></a>
# **getNetworkSwitchStackRoutingStaticRoute**
> Object getNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId)

Return a layer 3 static route for a switch stack

Return a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStackRoutingStaticRoute");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingStaticRoutes"></a>
# **getNetworkSwitchStackRoutingStaticRoutes**
> List&lt;Object&gt; getNetworkSwitchStackRoutingStaticRoutes(networkId, switchStackId)

List layer 3 static routes for a switch stack

List layer 3 static routes for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingStaticRoutes(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStackRoutingStaticRoutes");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStacks"></a>
# **getNetworkSwitchStacks**
> List&lt;Object&gt; getNetworkSwitchStacks(networkId)

List the switch stacks in a network

List the switch stacks in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStacks(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStacks");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStormControl"></a>
# **getNetworkSwitchStormControl**
> GetNetworkSwitchStormControl200Response getNetworkSwitchStormControl(networkId)

Return the storm control configuration for a switch network

Return the storm control configuration for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchStormControl200Response result = apiInstance.getNetworkSwitchStormControl(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStormControl");
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
| **networkId** | **String**|  | |

### Return type

[**GetNetworkSwitchStormControl200Response**](GetNetworkSwitchStormControl200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStp"></a>
# **getNetworkSwitchStp**
> Object getNetworkSwitchStp(networkId)

Returns STP settings

Returns STP settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStp(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getNetworkSwitchStp");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplateSwitchProfilePort"></a>
# **getOrganizationConfigTemplateSwitchProfilePort**
> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner getOrganizationConfigTemplateSwitchProfilePort(organizationId, configTemplateId, profileId, portId)

Return a switch profile port

Return a switch profile port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    String portId = "portId_example"; // String | 
    try {
      GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner result = apiInstance.getOrganizationConfigTemplateSwitchProfilePort(organizationId, configTemplateId, profileId, portId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getOrganizationConfigTemplateSwitchProfilePort");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **profileId** | **String**|  | |
| **portId** | **String**|  | |

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplateSwitchProfilePorts"></a>
# **getOrganizationConfigTemplateSwitchProfilePorts**
> List&lt;GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner&gt; getOrganizationConfigTemplateSwitchProfilePorts(organizationId, configTemplateId, profileId)

Return all the ports of a switch profile

Return all the ports of a switch profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    try {
      List<GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner> result = apiInstance.getOrganizationConfigTemplateSwitchProfilePorts(organizationId, configTemplateId, profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getOrganizationConfigTemplateSwitchProfilePorts");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **profileId** | **String**|  | |

### Return type

[**List&lt;GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner&gt;**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplateSwitchProfiles"></a>
# **getOrganizationConfigTemplateSwitchProfiles**
> GetOrganizationConfigTemplateSwitchProfiles200Response getOrganizationConfigTemplateSwitchProfiles(organizationId, configTemplateId)

List the switch profiles for your switch template configuration

List the switch profiles for your switch template configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    try {
      GetOrganizationConfigTemplateSwitchProfiles200Response result = apiInstance.getOrganizationConfigTemplateSwitchProfiles(organizationId, configTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getOrganizationConfigTemplateSwitchProfiles");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |

### Return type

[**GetOrganizationConfigTemplateSwitchProfiles200Response**](GetOrganizationConfigTemplateSwitchProfiles200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationSwitchPortsBySwitch"></a>
# **getOrganizationSwitchPortsBySwitch**
> List&lt;GetOrganizationSwitchPortsBySwitch200ResponseInner&gt; getOrganizationSwitchPortsBySwitch(organizationId, perPage, startingAfter, endingBefore, networkIds, portProfileIds, name, mac, macs, serial, serials, configurationUpdatedAfter)

List the switchports in an organization by switch

List the switchports in an organization by switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter switchports by network.
    List<String> portProfileIds = Arrays.asList(); // List<String> | Optional parameter to filter switchports belonging to the specified switchport profiles.
    String name = "name_example"; // String | Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
    String mac = "mac_example"; // String | Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
    List<String> macs = Arrays.asList(); // List<String> | Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
    String serial = "serial_example"; // String | Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
    String configurationUpdatedAfter = "configurationUpdatedAfter_example"; // String | Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
    try {
      List<GetOrganizationSwitchPortsBySwitch200ResponseInner> result = apiInstance.getOrganizationSwitchPortsBySwitch(organizationId, perPage, startingAfter, endingBefore, networkIds, portProfileIds, name, mac, macs, serial, serials, configurationUpdatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#getOrganizationSwitchPortsBySwitch");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports by network. | [optional] |
| **portProfileIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports belonging to the specified switchport profiles. | [optional] |
| **name** | **String**| Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match. | [optional] |
| **mac** | **String**| Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match. | [optional] |
| **macs** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match. | [optional] |
| **serial** | **String**| Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match. | [optional] |
| **configurationUpdatedAfter** | **String**| Optional parameter to filter results by switches where the configuration has been updated after the given timestamp. | [optional] |

### Return type

[**List&lt;GetOrganizationSwitchPortsBySwitch200ResponseInner&gt;**](GetOrganizationSwitchPortsBySwitch200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="removeNetworkSwitchStack"></a>
# **removeNetworkSwitchStack**
> Object removeNetworkSwitchStack(networkId, switchStackId, removeNetworkSwitchStackRequest)

Remove a switch from a stack

Remove a switch from a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    RemoveNetworkSwitchStackRequest removeNetworkSwitchStackRequest = new RemoveNetworkSwitchStackRequest(); // RemoveNetworkSwitchStackRequest | 
    try {
      Object result = apiInstance.removeNetworkSwitchStack(networkId, switchStackId, removeNetworkSwitchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#removeNetworkSwitchStack");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **removeNetworkSwitchStackRequest** | [**RemoveNetworkSwitchStackRequest**](RemoveNetworkSwitchStackRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceSwitchPort"></a>
# **updateDeviceSwitchPort**
> GetDeviceSwitchPorts200ResponseInner updateDeviceSwitchPort(serial, portId, updateDeviceSwitchPortRequest)

Update a switch port

Update a switch port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String portId = "portId_example"; // String | 
    UpdateDeviceSwitchPortRequest updateDeviceSwitchPortRequest = new UpdateDeviceSwitchPortRequest(); // UpdateDeviceSwitchPortRequest | 
    try {
      GetDeviceSwitchPorts200ResponseInner result = apiInstance.updateDeviceSwitchPort(serial, portId, updateDeviceSwitchPortRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateDeviceSwitchPort");
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
| **serial** | **String**|  | |
| **portId** | **String**|  | |
| **updateDeviceSwitchPortRequest** | [**UpdateDeviceSwitchPortRequest**](UpdateDeviceSwitchPortRequest.md)|  | [optional] |

### Return type

[**GetDeviceSwitchPorts200ResponseInner**](GetDeviceSwitchPorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceSwitchRoutingInterface"></a>
# **updateDeviceSwitchRoutingInterface**
> GetDeviceSwitchRoutingInterfaces200ResponseInner updateDeviceSwitchRoutingInterface(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest)

Update a layer 3 interface for a switch

Update a layer 3 interface for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = new CreateDeviceSwitchRoutingInterfaceRequest(); // CreateDeviceSwitchRoutingInterfaceRequest | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.updateDeviceSwitchRoutingInterface(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateDeviceSwitchRoutingInterface");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |
| **createDeviceSwitchRoutingInterfaceRequest** | [**CreateDeviceSwitchRoutingInterfaceRequest**](CreateDeviceSwitchRoutingInterfaceRequest.md)|  | [optional] |

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceSwitchRoutingInterfaceDhcp"></a>
# **updateDeviceSwitchRoutingInterfaceDhcp**
> Object updateDeviceSwitchRoutingInterfaceDhcp(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest)

Update a layer 3 interface DHCP configuration for a switch

Update a layer 3 interface DHCP configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateDeviceSwitchRoutingInterfaceDhcpRequest updateDeviceSwitchRoutingInterfaceDhcpRequest = new UpdateDeviceSwitchRoutingInterfaceDhcpRequest(); // UpdateDeviceSwitchRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchRoutingInterfaceDhcp(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateDeviceSwitchRoutingInterfaceDhcp");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateDeviceSwitchRoutingInterfaceDhcpRequest** | [**UpdateDeviceSwitchRoutingInterfaceDhcpRequest**](UpdateDeviceSwitchRoutingInterfaceDhcpRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceSwitchRoutingStaticRoute"></a>
# **updateDeviceSwitchRoutingStaticRoute**
> Object updateDeviceSwitchRoutingStaticRoute(serial, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest)

Update a layer 3 static route for a switch

Update a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateDeviceSwitchRoutingStaticRouteRequest updateDeviceSwitchRoutingStaticRouteRequest = new UpdateDeviceSwitchRoutingStaticRouteRequest(); // UpdateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchRoutingStaticRoute(serial, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateDeviceSwitchRoutingStaticRoute");
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
| **serial** | **String**|  | |
| **staticRouteId** | **String**|  | |
| **updateDeviceSwitchRoutingStaticRouteRequest** | [**UpdateDeviceSwitchRoutingStaticRouteRequest**](UpdateDeviceSwitchRoutingStaticRouteRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceSwitchWarmSpare"></a>
# **updateDeviceSwitchWarmSpare**
> Object updateDeviceSwitchWarmSpare(serial, updateDeviceSwitchWarmSpareRequest)

Update warm spare configuration for a switch

Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceSwitchWarmSpareRequest updateDeviceSwitchWarmSpareRequest = new UpdateDeviceSwitchWarmSpareRequest(); // UpdateDeviceSwitchWarmSpareRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchWarmSpare(serial, updateDeviceSwitchWarmSpareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateDeviceSwitchWarmSpare");
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
| **serial** | **String**|  | |
| **updateDeviceSwitchWarmSpareRequest** | [**UpdateDeviceSwitchWarmSpareRequest**](UpdateDeviceSwitchWarmSpareRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchAccessControlLists"></a>
# **updateNetworkSwitchAccessControlLists**
> GetNetworkSwitchAccessControlLists200Response updateNetworkSwitchAccessControlLists(networkId, updateNetworkSwitchAccessControlListsRequest)

Update the access control lists for a MS network

Update the access control lists for a MS network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest = new UpdateNetworkSwitchAccessControlListsRequest(); // UpdateNetworkSwitchAccessControlListsRequest | 
    try {
      GetNetworkSwitchAccessControlLists200Response result = apiInstance.updateNetworkSwitchAccessControlLists(networkId, updateNetworkSwitchAccessControlListsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchAccessControlLists");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchAccessControlListsRequest** | [**UpdateNetworkSwitchAccessControlListsRequest**](UpdateNetworkSwitchAccessControlListsRequest.md)|  | |

### Return type

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchAccessPolicy"></a>
# **updateNetworkSwitchAccessPolicy**
> GetNetworkSwitchAccessPolicies200ResponseInner updateNetworkSwitchAccessPolicy(networkId, accessPolicyNumber, updateNetworkSwitchAccessPolicyRequest)

Update an access policy for a switch network

Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String accessPolicyNumber = "accessPolicyNumber_example"; // String | 
    UpdateNetworkSwitchAccessPolicyRequest updateNetworkSwitchAccessPolicyRequest = new UpdateNetworkSwitchAccessPolicyRequest(); // UpdateNetworkSwitchAccessPolicyRequest | 
    try {
      GetNetworkSwitchAccessPolicies200ResponseInner result = apiInstance.updateNetworkSwitchAccessPolicy(networkId, accessPolicyNumber, updateNetworkSwitchAccessPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchAccessPolicy");
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
| **networkId** | **String**|  | |
| **accessPolicyNumber** | **String**|  | |
| **updateNetworkSwitchAccessPolicyRequest** | [**UpdateNetworkSwitchAccessPolicyRequest**](UpdateNetworkSwitchAccessPolicyRequest.md)|  | [optional] |

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchAlternateManagementInterface"></a>
# **updateNetworkSwitchAlternateManagementInterface**
> Object updateNetworkSwitchAlternateManagementInterface(networkId, updateNetworkSwitchAlternateManagementInterfaceRequest)

Update the switch alternate management interface for the network

Update the switch alternate management interface for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchAlternateManagementInterfaceRequest updateNetworkSwitchAlternateManagementInterfaceRequest = new UpdateNetworkSwitchAlternateManagementInterfaceRequest(); // UpdateNetworkSwitchAlternateManagementInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchAlternateManagementInterface(networkId, updateNetworkSwitchAlternateManagementInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchAlternateManagementInterface");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchAlternateManagementInterfaceRequest** | [**UpdateNetworkSwitchAlternateManagementInterfaceRequest**](UpdateNetworkSwitchAlternateManagementInterfaceRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchDhcpServerPolicy"></a>
# **updateNetworkSwitchDhcpServerPolicy**
> Object updateNetworkSwitchDhcpServerPolicy(networkId, updateNetworkSwitchDhcpServerPolicyRequest)

Update the DHCP server settings

Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchDhcpServerPolicyRequest updateNetworkSwitchDhcpServerPolicyRequest = new UpdateNetworkSwitchDhcpServerPolicyRequest(); // UpdateNetworkSwitchDhcpServerPolicyRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchDhcpServerPolicy(networkId, updateNetworkSwitchDhcpServerPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchDhcpServerPolicy");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchDhcpServerPolicyRequest** | [**UpdateNetworkSwitchDhcpServerPolicyRequest**](UpdateNetworkSwitchDhcpServerPolicyRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer"></a>
# **updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer**
> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId, trustedServerId, updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

Update a server that is trusted by Dynamic ARP Inspection on this network

Update a server that is trusted by Dynamic ARP Inspection on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String trustedServerId = "trustedServerId_example"; // String | 
    UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
    try {
      GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner result = apiInstance.updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId, trustedServerId, updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer");
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
| **networkId** | **String**|  | |
| **trustedServerId** | **String**|  | |
| **updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest** | [**UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest**](UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.md)|  | [optional] |

### Return type

[**GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchDscpToCosMappings"></a>
# **updateNetworkSwitchDscpToCosMappings**
> Object updateNetworkSwitchDscpToCosMappings(networkId, updateNetworkSwitchDscpToCosMappingsRequest)

Update the DSCP to CoS mappings

Update the DSCP to CoS mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchDscpToCosMappingsRequest updateNetworkSwitchDscpToCosMappingsRequest = new UpdateNetworkSwitchDscpToCosMappingsRequest(); // UpdateNetworkSwitchDscpToCosMappingsRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchDscpToCosMappings(networkId, updateNetworkSwitchDscpToCosMappingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchDscpToCosMappings");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchDscpToCosMappingsRequest** | [**UpdateNetworkSwitchDscpToCosMappingsRequest**](UpdateNetworkSwitchDscpToCosMappingsRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchLinkAggregation"></a>
# **updateNetworkSwitchLinkAggregation**
> Object updateNetworkSwitchLinkAggregation(networkId, linkAggregationId, updateNetworkSwitchLinkAggregationRequest)

Update a link aggregation group

Update a link aggregation group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String linkAggregationId = "linkAggregationId_example"; // String | 
    UpdateNetworkSwitchLinkAggregationRequest updateNetworkSwitchLinkAggregationRequest = new UpdateNetworkSwitchLinkAggregationRequest(); // UpdateNetworkSwitchLinkAggregationRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchLinkAggregation(networkId, linkAggregationId, updateNetworkSwitchLinkAggregationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchLinkAggregation");
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
| **networkId** | **String**|  | |
| **linkAggregationId** | **String**|  | |
| **updateNetworkSwitchLinkAggregationRequest** | [**UpdateNetworkSwitchLinkAggregationRequest**](UpdateNetworkSwitchLinkAggregationRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchMtu"></a>
# **updateNetworkSwitchMtu**
> Object updateNetworkSwitchMtu(networkId, updateNetworkSwitchMtuRequest)

Update the MTU configuration

Update the MTU configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchMtuRequest updateNetworkSwitchMtuRequest = new UpdateNetworkSwitchMtuRequest(); // UpdateNetworkSwitchMtuRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchMtu(networkId, updateNetworkSwitchMtuRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchMtu");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchMtuRequest** | [**UpdateNetworkSwitchMtuRequest**](UpdateNetworkSwitchMtuRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchPortSchedule"></a>
# **updateNetworkSwitchPortSchedule**
> Object updateNetworkSwitchPortSchedule(networkId, portScheduleId, updateNetworkSwitchPortScheduleRequest)

Update a switch port schedule

Update a switch port schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String portScheduleId = "portScheduleId_example"; // String | 
    UpdateNetworkSwitchPortScheduleRequest updateNetworkSwitchPortScheduleRequest = new UpdateNetworkSwitchPortScheduleRequest(); // UpdateNetworkSwitchPortScheduleRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchPortSchedule(networkId, portScheduleId, updateNetworkSwitchPortScheduleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchPortSchedule");
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
| **networkId** | **String**|  | |
| **portScheduleId** | **String**|  | |
| **updateNetworkSwitchPortScheduleRequest** | [**UpdateNetworkSwitchPortScheduleRequest**](UpdateNetworkSwitchPortScheduleRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchQosRule"></a>
# **updateNetworkSwitchQosRule**
> Object updateNetworkSwitchQosRule(networkId, qosRuleId, updateNetworkSwitchQosRuleRequest)

Update a quality of service rule

Update a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    UpdateNetworkSwitchQosRuleRequest updateNetworkSwitchQosRuleRequest = new UpdateNetworkSwitchQosRuleRequest(); // UpdateNetworkSwitchQosRuleRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchQosRule(networkId, qosRuleId, updateNetworkSwitchQosRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchQosRule");
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
| **networkId** | **String**|  | |
| **qosRuleId** | **String**|  | |
| **updateNetworkSwitchQosRuleRequest** | [**UpdateNetworkSwitchQosRuleRequest**](UpdateNetworkSwitchQosRuleRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchQosRulesOrder"></a>
# **updateNetworkSwitchQosRulesOrder**
> Object updateNetworkSwitchQosRulesOrder(networkId, updateNetworkSwitchQosRulesOrderRequest)

Update the order in which the rules should be processed by the switch

Update the order in which the rules should be processed by the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchQosRulesOrderRequest updateNetworkSwitchQosRulesOrderRequest = new UpdateNetworkSwitchQosRulesOrderRequest(); // UpdateNetworkSwitchQosRulesOrderRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchQosRulesOrder(networkId, updateNetworkSwitchQosRulesOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchQosRulesOrder");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchQosRulesOrderRequest** | [**UpdateNetworkSwitchQosRulesOrderRequest**](UpdateNetworkSwitchQosRulesOrderRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchRoutingMulticast"></a>
# **updateNetworkSwitchRoutingMulticast**
> Object updateNetworkSwitchRoutingMulticast(networkId, updateNetworkSwitchRoutingMulticastRequest)

Update multicast settings for a network

Update multicast settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRequest updateNetworkSwitchRoutingMulticastRequest = new UpdateNetworkSwitchRoutingMulticastRequest(); // UpdateNetworkSwitchRoutingMulticastRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticast(networkId, updateNetworkSwitchRoutingMulticastRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchRoutingMulticast");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchRoutingMulticastRequest** | [**UpdateNetworkSwitchRoutingMulticastRequest**](UpdateNetworkSwitchRoutingMulticastRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchRoutingMulticastRendezvousPoint"></a>
# **updateNetworkSwitchRoutingMulticastRendezvousPoint**
> Object updateNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

Update a multicast rendezvous point

Update a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchRoutingMulticastRendezvousPoint");
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
| **networkId** | **String**|  | |
| **rendezvousPointId** | **String**|  | |
| **updateNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest**](UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchRoutingOspf"></a>
# **updateNetworkSwitchRoutingOspf**
> Object updateNetworkSwitchRoutingOspf(networkId, updateNetworkSwitchRoutingOspfRequest)

Update layer 3 OSPF routing configuration

Update layer 3 OSPF routing configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchRoutingOspfRequest updateNetworkSwitchRoutingOspfRequest = new UpdateNetworkSwitchRoutingOspfRequest(); // UpdateNetworkSwitchRoutingOspfRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingOspf(networkId, updateNetworkSwitchRoutingOspfRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchRoutingOspf");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchRoutingOspfRequest** | [**UpdateNetworkSwitchRoutingOspfRequest**](UpdateNetworkSwitchRoutingOspfRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchSettings"></a>
# **updateNetworkSwitchSettings**
> GetNetworkSwitchSettings200Response updateNetworkSwitchSettings(networkId, updateNetworkSwitchSettingsRequest)

Update switch network settings

Update switch network settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchSettingsRequest updateNetworkSwitchSettingsRequest = new UpdateNetworkSwitchSettingsRequest(); // UpdateNetworkSwitchSettingsRequest | 
    try {
      GetNetworkSwitchSettings200Response result = apiInstance.updateNetworkSwitchSettings(networkId, updateNetworkSwitchSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchSettings");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchSettingsRequest** | [**UpdateNetworkSwitchSettingsRequest**](UpdateNetworkSwitchSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkSwitchSettings200Response**](GetNetworkSwitchSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingInterface"></a>
# **updateNetworkSwitchStackRoutingInterface**
> Object updateNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest)

Update a layer 3 interface for a switch stack

Update a layer 3 interface for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceRequest updateNetworkSwitchStackRoutingInterfaceRequest = new UpdateNetworkSwitchStackRoutingInterfaceRequest(); // UpdateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchStackRoutingInterface");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateNetworkSwitchStackRoutingInterfaceRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceRequest**](UpdateNetworkSwitchStackRoutingInterfaceRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingInterfaceDhcp"></a>
# **updateNetworkSwitchStackRoutingInterfaceDhcp**
> Object updateNetworkSwitchStackRoutingInterfaceDhcp(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest)

Update a layer 3 interface DHCP configuration for a switch stack

Update a layer 3 interface DHCP configuration for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest updateNetworkSwitchStackRoutingInterfaceDhcpRequest = new UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest(); // UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterfaceDhcp(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchStackRoutingInterfaceDhcp");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateNetworkSwitchStackRoutingInterfaceDhcpRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest**](UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingStaticRoute"></a>
# **updateNetworkSwitchStackRoutingStaticRoute**
> Object updateNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest)

Update a layer 3 static route for a switch stack

Update a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateDeviceSwitchRoutingStaticRouteRequest updateDeviceSwitchRoutingStaticRouteRequest = new UpdateDeviceSwitchRoutingStaticRouteRequest(); // UpdateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchStackRoutingStaticRoute");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **staticRouteId** | **String**|  | |
| **updateDeviceSwitchRoutingStaticRouteRequest** | [**UpdateDeviceSwitchRoutingStaticRouteRequest**](UpdateDeviceSwitchRoutingStaticRouteRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStormControl"></a>
# **updateNetworkSwitchStormControl**
> Object updateNetworkSwitchStormControl(networkId, updateNetworkSwitchStormControlRequest)

Update the storm control configuration for a switch network

Update the storm control configuration for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchStormControlRequest updateNetworkSwitchStormControlRequest = new UpdateNetworkSwitchStormControlRequest(); // UpdateNetworkSwitchStormControlRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStormControl(networkId, updateNetworkSwitchStormControlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchStormControl");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchStormControlRequest** | [**UpdateNetworkSwitchStormControlRequest**](UpdateNetworkSwitchStormControlRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStp"></a>
# **updateNetworkSwitchStp**
> Object updateNetworkSwitchStp(networkId, updateNetworkSwitchStpRequest)

Updates STP settings

Updates STP settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchStpRequest updateNetworkSwitchStpRequest = new UpdateNetworkSwitchStpRequest(); // UpdateNetworkSwitchStpRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStp(networkId, updateNetworkSwitchStpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateNetworkSwitchStp");
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
| **networkId** | **String**|  | |
| **updateNetworkSwitchStpRequest** | [**UpdateNetworkSwitchStpRequest**](UpdateNetworkSwitchStpRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationConfigTemplateSwitchProfilePort"></a>
# **updateOrganizationConfigTemplateSwitchProfilePort**
> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner updateOrganizationConfigTemplateSwitchProfilePort(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest)

Update a switch profile port

Update a switch profile port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchApi apiInstance = new SwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    String portId = "portId_example"; // String | 
    UpdateOrganizationConfigTemplateSwitchProfilePortRequest updateOrganizationConfigTemplateSwitchProfilePortRequest = new UpdateOrganizationConfigTemplateSwitchProfilePortRequest(); // UpdateOrganizationConfigTemplateSwitchProfilePortRequest | 
    try {
      GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner result = apiInstance.updateOrganizationConfigTemplateSwitchProfilePort(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchApi#updateOrganizationConfigTemplateSwitchProfilePort");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **profileId** | **String**|  | |
| **portId** | **String**|  | |
| **updateOrganizationConfigTemplateSwitchProfilePortRequest** | [**UpdateOrganizationConfigTemplateSwitchProfilePortRequest**](UpdateOrganizationConfigTemplateSwitchProfilePortRequest.md)|  | [optional] |

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

