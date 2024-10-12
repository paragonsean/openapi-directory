# NetworksApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bindNetwork**](NetworksApi.md#bindNetwork) | **POST** /networks/{networkId}/bind | Bind a network to a template. |
| [**claimNetworkDevices**](NetworksApi.md#claimNetworkDevices) | **POST** /networks/{networkId}/devices/claim | Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed) |
| [**combineOrganizationNetworks_1**](NetworksApi.md#combineOrganizationNetworks_1) | **POST** /organizations/{organizationId}/networks/combine | Combine multiple networks into a single network |
| [**createNetworkFirmwareUpgradesRollback**](NetworksApi.md#createNetworkFirmwareUpgradesRollback) | **POST** /networks/{networkId}/firmwareUpgrades/rollbacks | Rollback a Firmware Upgrade For A Network |
| [**createNetworkFirmwareUpgradesStagedEvent**](NetworksApi.md#createNetworkFirmwareUpgradesStagedEvent) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events | Create a Staged Upgrade Event for a network |
| [**createNetworkFirmwareUpgradesStagedGroup**](NetworksApi.md#createNetworkFirmwareUpgradesStagedGroup) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network |
| [**createNetworkFloorPlan**](NetworksApi.md#createNetworkFloorPlan) | **POST** /networks/{networkId}/floorPlans | Upload a floor plan |
| [**createNetworkGroupPolicy**](NetworksApi.md#createNetworkGroupPolicy) | **POST** /networks/{networkId}/groupPolicies | Create a group policy |
| [**createNetworkMerakiAuthUser**](NetworksApi.md#createNetworkMerakiAuthUser) | **POST** /networks/{networkId}/merakiAuthUsers | Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap) |
| [**createNetworkMqttBroker**](NetworksApi.md#createNetworkMqttBroker) | **POST** /networks/{networkId}/mqttBrokers | Add an MQTT broker |
| [**createNetworkPiiRequest**](NetworksApi.md#createNetworkPiiRequest) | **POST** /networks/{networkId}/pii/requests | Submit a new delete or restrict processing PII request |
| [**createNetworkWebhooksHttpServer**](NetworksApi.md#createNetworkWebhooksHttpServer) | **POST** /networks/{networkId}/webhooks/httpServers | Add an HTTP server to a network |
| [**createNetworkWebhooksPayloadTemplate**](NetworksApi.md#createNetworkWebhooksPayloadTemplate) | **POST** /networks/{networkId}/webhooks/payloadTemplates | Create a webhook payload template for a network |
| [**createNetworkWebhooksWebhookTest**](NetworksApi.md#createNetworkWebhooksWebhookTest) | **POST** /networks/{networkId}/webhooks/webhookTests | Send a test webhook for a network |
| [**createOrganizationNetwork_1**](NetworksApi.md#createOrganizationNetwork_1) | **POST** /organizations/{organizationId}/networks | Create a network |
| [**deferNetworkFirmwareUpgradesStagedEvents**](NetworksApi.md#deferNetworkFirmwareUpgradesStagedEvents) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/defer | Postpone by 1 week all pending staged upgrade stages for a network |
| [**deleteNetwork**](NetworksApi.md#deleteNetwork) | **DELETE** /networks/{networkId} | Delete a network |
| [**deleteNetworkFirmwareUpgradesStagedGroup**](NetworksApi.md#deleteNetworkFirmwareUpgradesStagedGroup) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group |
| [**deleteNetworkFloorPlan**](NetworksApi.md#deleteNetworkFloorPlan) | **DELETE** /networks/{networkId}/floorPlans/{floorPlanId} | Destroy a floor plan |
| [**deleteNetworkGroupPolicy**](NetworksApi.md#deleteNetworkGroupPolicy) | **DELETE** /networks/{networkId}/groupPolicies/{groupPolicyId} | Delete a group policy |
| [**deleteNetworkMerakiAuthUser**](NetworksApi.md#deleteNetworkMerakiAuthUser) | **DELETE** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Deauthorize a user |
| [**deleteNetworkMqttBroker**](NetworksApi.md#deleteNetworkMqttBroker) | **DELETE** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Delete an MQTT broker |
| [**deleteNetworkPiiRequest**](NetworksApi.md#deleteNetworkPiiRequest) | **DELETE** /networks/{networkId}/pii/requests/{requestId} | Delete a restrict processing PII request |
| [**deleteNetworkWebhooksHttpServer**](NetworksApi.md#deleteNetworkWebhooksHttpServer) | **DELETE** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Delete an HTTP server from a network |
| [**deleteNetworkWebhooksPayloadTemplate**](NetworksApi.md#deleteNetworkWebhooksPayloadTemplate) | **DELETE** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Destroy a webhook payload template for a network |
| [**getNetwork**](NetworksApi.md#getNetwork) | **GET** /networks/{networkId} | Return a network |
| [**getNetworkAlertsHistory**](NetworksApi.md#getNetworkAlertsHistory) | **GET** /networks/{networkId}/alerts/history | Return the alert history for this network |
| [**getNetworkAlertsSettings**](NetworksApi.md#getNetworkAlertsSettings) | **GET** /networks/{networkId}/alerts/settings | Return the alert configuration for this network |
| [**getNetworkBluetoothClient**](NetworksApi.md#getNetworkBluetoothClient) | **GET** /networks/{networkId}/bluetoothClients/{bluetoothClientId} | Return a Bluetooth client |
| [**getNetworkBluetoothClients**](NetworksApi.md#getNetworkBluetoothClients) | **GET** /networks/{networkId}/bluetoothClients | List the Bluetooth clients seen by APs in this network |
| [**getNetworkClient**](NetworksApi.md#getNetworkClient) | **GET** /networks/{networkId}/clients/{clientId} | Return the client associated with the given identifier |
| [**getNetworkClientPolicy**](NetworksApi.md#getNetworkClientPolicy) | **GET** /networks/{networkId}/clients/{clientId}/policy | Return the policy assigned to a client on the network |
| [**getNetworkClientSplashAuthorizationStatus**](NetworksApi.md#getNetworkClientSplashAuthorizationStatus) | **GET** /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus | Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash |
| [**getNetworkClientTrafficHistory**](NetworksApi.md#getNetworkClientTrafficHistory) | **GET** /networks/{networkId}/clients/{clientId}/trafficHistory | Return the client&#39;s network traffic data over time |
| [**getNetworkClientUsageHistory**](NetworksApi.md#getNetworkClientUsageHistory) | **GET** /networks/{networkId}/clients/{clientId}/usageHistory | Return the client&#39;s daily usage history |
| [**getNetworkClients**](NetworksApi.md#getNetworkClients) | **GET** /networks/{networkId}/clients | List the clients that have used this network in the timespan |
| [**getNetworkClientsApplicationUsage**](NetworksApi.md#getNetworkClientsApplicationUsage) | **GET** /networks/{networkId}/clients/applicationUsage | Return the application usage data for clients |
| [**getNetworkClientsBandwidthUsageHistory**](NetworksApi.md#getNetworkClientsBandwidthUsageHistory) | **GET** /networks/{networkId}/clients/bandwidthUsageHistory | Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second. |
| [**getNetworkClientsOverview**](NetworksApi.md#getNetworkClientsOverview) | **GET** /networks/{networkId}/clients/overview | Return overview statistics for network clients |
| [**getNetworkClientsUsageHistories**](NetworksApi.md#getNetworkClientsUsageHistories) | **GET** /networks/{networkId}/clients/usageHistories | Return the usage histories for clients |
| [**getNetworkDevices**](NetworksApi.md#getNetworkDevices) | **GET** /networks/{networkId}/devices | List the devices in a network |
| [**getNetworkEvents**](NetworksApi.md#getNetworkEvents) | **GET** /networks/{networkId}/events | List the events for the network |
| [**getNetworkEventsEventTypes**](NetworksApi.md#getNetworkEventsEventTypes) | **GET** /networks/{networkId}/events/eventTypes | List the event type to human-readable description |
| [**getNetworkFirmwareUpgrades**](NetworksApi.md#getNetworkFirmwareUpgrades) | **GET** /networks/{networkId}/firmwareUpgrades | Get firmware upgrade information for a network |
| [**getNetworkFirmwareUpgradesStagedEvents**](NetworksApi.md#getNetworkFirmwareUpgradesStagedEvents) | **GET** /networks/{networkId}/firmwareUpgrades/staged/events | Get the Staged Upgrade Event from a network |
| [**getNetworkFirmwareUpgradesStagedGroup**](NetworksApi.md#getNetworkFirmwareUpgradesStagedGroup) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network |
| [**getNetworkFirmwareUpgradesStagedGroups**](NetworksApi.md#getNetworkFirmwareUpgradesStagedGroups) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network |
| [**getNetworkFirmwareUpgradesStagedStages**](NetworksApi.md#getNetworkFirmwareUpgradesStagedStages) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network |
| [**getNetworkFloorPlan**](NetworksApi.md#getNetworkFloorPlan) | **GET** /networks/{networkId}/floorPlans/{floorPlanId} | Find a floor plan by ID |
| [**getNetworkFloorPlans**](NetworksApi.md#getNetworkFloorPlans) | **GET** /networks/{networkId}/floorPlans | List the floor plans that belong to your network |
| [**getNetworkGroupPolicies**](NetworksApi.md#getNetworkGroupPolicies) | **GET** /networks/{networkId}/groupPolicies | List the group policies in a network |
| [**getNetworkGroupPolicy**](NetworksApi.md#getNetworkGroupPolicy) | **GET** /networks/{networkId}/groupPolicies/{groupPolicyId} | Display a group policy |
| [**getNetworkHealthAlerts**](NetworksApi.md#getNetworkHealthAlerts) | **GET** /networks/{networkId}/health/alerts | Return all global alerts on this network |
| [**getNetworkMerakiAuthUser**](NetworksApi.md#getNetworkMerakiAuthUser) | **GET** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Return the Meraki Auth splash guest, RADIUS, or client VPN user |
| [**getNetworkMerakiAuthUsers**](NetworksApi.md#getNetworkMerakiAuthUsers) | **GET** /networks/{networkId}/merakiAuthUsers | List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network) |
| [**getNetworkMqttBroker**](NetworksApi.md#getNetworkMqttBroker) | **GET** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Return an MQTT broker |
| [**getNetworkMqttBrokers**](NetworksApi.md#getNetworkMqttBrokers) | **GET** /networks/{networkId}/mqttBrokers | List the MQTT brokers for this network |
| [**getNetworkNetflow**](NetworksApi.md#getNetworkNetflow) | **GET** /networks/{networkId}/netflow | Return the NetFlow traffic reporting settings for a network |
| [**getNetworkNetworkHealthChannelUtilization**](NetworksApi.md#getNetworkNetworkHealthChannelUtilization) | **GET** /networks/{networkId}/networkHealth/channelUtilization | Get the channel utilization over each radio for all APs in a network. |
| [**getNetworkPiiPiiKeys**](NetworksApi.md#getNetworkPiiPiiKeys) | **GET** /networks/{networkId}/pii/piiKeys | List the keys required to access Personally Identifiable Information (PII) for a given identifier |
| [**getNetworkPiiRequest**](NetworksApi.md#getNetworkPiiRequest) | **GET** /networks/{networkId}/pii/requests/{requestId} | Return a PII request |
| [**getNetworkPiiRequests**](NetworksApi.md#getNetworkPiiRequests) | **GET** /networks/{networkId}/pii/requests | List the PII requests for this network or organization |
| [**getNetworkPiiSmDevicesForKey**](NetworksApi.md#getNetworkPiiSmDevicesForKey) | **GET** /networks/{networkId}/pii/smDevicesForKey | Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier |
| [**getNetworkPiiSmOwnersForKey**](NetworksApi.md#getNetworkPiiSmOwnersForKey) | **GET** /networks/{networkId}/pii/smOwnersForKey | Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier |
| [**getNetworkPoliciesByClient**](NetworksApi.md#getNetworkPoliciesByClient) | **GET** /networks/{networkId}/policies/byClient | Get policies for all clients with policies |
| [**getNetworkSettings**](NetworksApi.md#getNetworkSettings) | **GET** /networks/{networkId}/settings | Return the settings for a network |
| [**getNetworkSnmp**](NetworksApi.md#getNetworkSnmp) | **GET** /networks/{networkId}/snmp | Return the SNMP settings for a network |
| [**getNetworkSplashLoginAttempts**](NetworksApi.md#getNetworkSplashLoginAttempts) | **GET** /networks/{networkId}/splashLoginAttempts | List the splash login attempts for a network |
| [**getNetworkSyslogServers**](NetworksApi.md#getNetworkSyslogServers) | **GET** /networks/{networkId}/syslogServers | List the syslog servers for a network |
| [**getNetworkTopologyLinkLayer**](NetworksApi.md#getNetworkTopologyLinkLayer) | **GET** /networks/{networkId}/topology/linkLayer | List the LLDP and CDP information for all discovered devices and connections in a network. |
| [**getNetworkTraffic**](NetworksApi.md#getNetworkTraffic) | **GET** /networks/{networkId}/traffic | Return the traffic analysis data for this network |
| [**getNetworkTrafficAnalysis**](NetworksApi.md#getNetworkTrafficAnalysis) | **GET** /networks/{networkId}/trafficAnalysis | Return the traffic analysis settings for a network |
| [**getNetworkTrafficShapingApplicationCategories**](NetworksApi.md#getNetworkTrafficShapingApplicationCategories) | **GET** /networks/{networkId}/trafficShaping/applicationCategories | Returns the application categories for traffic shaping rules. |
| [**getNetworkTrafficShapingDscpTaggingOptions**](NetworksApi.md#getNetworkTrafficShapingDscpTaggingOptions) | **GET** /networks/{networkId}/trafficShaping/dscpTaggingOptions | Returns the available DSCP tagging options for your traffic shaping rules. |
| [**getNetworkWebhooksHttpServer**](NetworksApi.md#getNetworkWebhooksHttpServer) | **GET** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Return an HTTP server for a network |
| [**getNetworkWebhooksHttpServers**](NetworksApi.md#getNetworkWebhooksHttpServers) | **GET** /networks/{networkId}/webhooks/httpServers | List the HTTP servers for a network |
| [**getNetworkWebhooksPayloadTemplate**](NetworksApi.md#getNetworkWebhooksPayloadTemplate) | **GET** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Get the webhook payload template for a network |
| [**getNetworkWebhooksPayloadTemplates**](NetworksApi.md#getNetworkWebhooksPayloadTemplates) | **GET** /networks/{networkId}/webhooks/payloadTemplates | List the webhook payload templates for a network |
| [**getNetworkWebhooksWebhookTest**](NetworksApi.md#getNetworkWebhooksWebhookTest) | **GET** /networks/{networkId}/webhooks/webhookTests/{webhookTestId} | Return the status of a webhook test for a network |
| [**getOrganizationInventoryOnboardingCloudMonitoringNetworks_4**](NetworksApi.md#getOrganizationInventoryOnboardingCloudMonitoringNetworks_4) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks | Returns list of networks eligible for adding cloud monitored device |
| [**getOrganizationNetworks_1**](NetworksApi.md#getOrganizationNetworks_1) | **GET** /organizations/{organizationId}/networks | List the networks that the user has privileges on in an organization |
| [**provisionNetworkClients**](NetworksApi.md#provisionNetworkClients) | **POST** /networks/{networkId}/clients/provision | Provisions a client with a name and policy |
| [**removeNetworkDevices**](NetworksApi.md#removeNetworkDevices) | **POST** /networks/{networkId}/devices/remove | Remove a single device |
| [**rollbacksNetworkFirmwareUpgradesStagedEvents**](NetworksApi.md#rollbacksNetworkFirmwareUpgradesStagedEvents) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks | Rollback a Staged Upgrade Event for a network |
| [**splitNetwork**](NetworksApi.md#splitNetwork) | **POST** /networks/{networkId}/split | Split a combined network into individual networks for each type of device |
| [**unbindNetwork**](NetworksApi.md#unbindNetwork) | **POST** /networks/{networkId}/unbind | Unbind a network from a template. |
| [**updateNetwork**](NetworksApi.md#updateNetwork) | **PUT** /networks/{networkId} | Update a network |
| [**updateNetworkAlertsSettings**](NetworksApi.md#updateNetworkAlertsSettings) | **PUT** /networks/{networkId}/alerts/settings | Update the alert configuration for this network |
| [**updateNetworkClientPolicy**](NetworksApi.md#updateNetworkClientPolicy) | **PUT** /networks/{networkId}/clients/{clientId}/policy | Update the policy assigned to a client on the network |
| [**updateNetworkClientSplashAuthorizationStatus**](NetworksApi.md#updateNetworkClientSplashAuthorizationStatus) | **PUT** /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus | Update a client&#39;s splash authorization |
| [**updateNetworkFirmwareUpgrades**](NetworksApi.md#updateNetworkFirmwareUpgrades) | **PUT** /networks/{networkId}/firmwareUpgrades | Update firmware upgrade information for a network |
| [**updateNetworkFirmwareUpgradesStagedEvents**](NetworksApi.md#updateNetworkFirmwareUpgradesStagedEvents) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/events | Update the Staged Upgrade Event for a network |
| [**updateNetworkFirmwareUpgradesStagedGroup**](NetworksApi.md#updateNetworkFirmwareUpgradesStagedGroup) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network |
| [**updateNetworkFirmwareUpgradesStagedStages**](NetworksApi.md#updateNetworkFirmwareUpgradesStagedStages) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence. |
| [**updateNetworkFloorPlan**](NetworksApi.md#updateNetworkFloorPlan) | **PUT** /networks/{networkId}/floorPlans/{floorPlanId} | Update a floor plan&#39;s geolocation and other meta data |
| [**updateNetworkGroupPolicy**](NetworksApi.md#updateNetworkGroupPolicy) | **PUT** /networks/{networkId}/groupPolicies/{groupPolicyId} | Update a group policy |
| [**updateNetworkMerakiAuthUser**](NetworksApi.md#updateNetworkMerakiAuthUser) | **PUT** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated) |
| [**updateNetworkMqttBroker**](NetworksApi.md#updateNetworkMqttBroker) | **PUT** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Update an MQTT broker |
| [**updateNetworkNetflow**](NetworksApi.md#updateNetworkNetflow) | **PUT** /networks/{networkId}/netflow | Update the NetFlow traffic reporting settings for a network |
| [**updateNetworkSettings**](NetworksApi.md#updateNetworkSettings) | **PUT** /networks/{networkId}/settings | Update the settings for a network |
| [**updateNetworkSnmp**](NetworksApi.md#updateNetworkSnmp) | **PUT** /networks/{networkId}/snmp | Update the SNMP settings for a network |
| [**updateNetworkSyslogServers**](NetworksApi.md#updateNetworkSyslogServers) | **PUT** /networks/{networkId}/syslogServers | Update the syslog servers for a network |
| [**updateNetworkTrafficAnalysis**](NetworksApi.md#updateNetworkTrafficAnalysis) | **PUT** /networks/{networkId}/trafficAnalysis | Update the traffic analysis settings for a network |
| [**updateNetworkWebhooksHttpServer**](NetworksApi.md#updateNetworkWebhooksHttpServer) | **PUT** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Update an HTTP server |
| [**updateNetworkWebhooksPayloadTemplate**](NetworksApi.md#updateNetworkWebhooksPayloadTemplate) | **PUT** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Update a webhook payload template for a network |
| [**vmxNetworkDevicesClaim**](NetworksApi.md#vmxNetworkDevicesClaim) | **POST** /networks/{networkId}/devices/claim/vmx | Claim a vMX into a network |


<a id="bindNetwork"></a>
# **bindNetwork**
> Object bindNetwork(networkId, bindNetworkRequest)

Bind a network to a template.

Bind a network to a template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    BindNetworkRequest bindNetworkRequest = new BindNetworkRequest(); // BindNetworkRequest | 
    try {
      Object result = apiInstance.bindNetwork(networkId, bindNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#bindNetwork");
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
| **bindNetworkRequest** | [**BindNetworkRequest**](BindNetworkRequest.md)|  | |

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

<a id="claimNetworkDevices"></a>
# **claimNetworkDevices**
> claimNetworkDevices(networkId, claimNetworkDevicesRequest)

Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    ClaimNetworkDevicesRequest claimNetworkDevicesRequest = new ClaimNetworkDevicesRequest(); // ClaimNetworkDevicesRequest | 
    try {
      apiInstance.claimNetworkDevices(networkId, claimNetworkDevicesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#claimNetworkDevices");
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
| **claimNetworkDevicesRequest** | [**ClaimNetworkDevicesRequest**](ClaimNetworkDevicesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="combineOrganizationNetworks_1"></a>
# **combineOrganizationNetworks_1**
> CombineOrganizationNetworks200Response combineOrganizationNetworks_1(organizationId, combineOrganizationNetworksRequest)

Combine multiple networks into a single network

Combine multiple networks into a single network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CombineOrganizationNetworksRequest combineOrganizationNetworksRequest = new CombineOrganizationNetworksRequest(); // CombineOrganizationNetworksRequest | 
    try {
      CombineOrganizationNetworks200Response result = apiInstance.combineOrganizationNetworks_1(organizationId, combineOrganizationNetworksRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#combineOrganizationNetworks_1");
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
| **combineOrganizationNetworksRequest** | [**CombineOrganizationNetworksRequest**](CombineOrganizationNetworksRequest.md)|  | |

### Return type

[**CombineOrganizationNetworks200Response**](CombineOrganizationNetworks200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkFirmwareUpgradesRollback"></a>
# **createNetworkFirmwareUpgradesRollback**
> CreateNetworkFirmwareUpgradesRollback200Response createNetworkFirmwareUpgradesRollback(networkId, createNetworkFirmwareUpgradesRollbackRequest)

Rollback a Firmware Upgrade For A Network

Rollback a Firmware Upgrade For A Network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesRollbackRequest createNetworkFirmwareUpgradesRollbackRequest = new CreateNetworkFirmwareUpgradesRollbackRequest(); // CreateNetworkFirmwareUpgradesRollbackRequest | 
    try {
      CreateNetworkFirmwareUpgradesRollback200Response result = apiInstance.createNetworkFirmwareUpgradesRollback(networkId, createNetworkFirmwareUpgradesRollbackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkFirmwareUpgradesRollback");
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
| **createNetworkFirmwareUpgradesRollbackRequest** | [**CreateNetworkFirmwareUpgradesRollbackRequest**](CreateNetworkFirmwareUpgradesRollbackRequest.md)|  | |

### Return type

[**CreateNetworkFirmwareUpgradesRollback200Response**](CreateNetworkFirmwareUpgradesRollback200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkFirmwareUpgradesStagedEvent"></a>
# **createNetworkFirmwareUpgradesStagedEvent**
> GetNetworkFirmwareUpgradesStagedEvents200Response createNetworkFirmwareUpgradesStagedEvent(networkId, createNetworkFirmwareUpgradesStagedEventRequest)

Create a Staged Upgrade Event for a network

Create a Staged Upgrade Event for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedEventRequest createNetworkFirmwareUpgradesStagedEventRequest = new CreateNetworkFirmwareUpgradesStagedEventRequest(); // CreateNetworkFirmwareUpgradesStagedEventRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.createNetworkFirmwareUpgradesStagedEvent(networkId, createNetworkFirmwareUpgradesStagedEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkFirmwareUpgradesStagedEvent");
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
| **createNetworkFirmwareUpgradesStagedEventRequest** | [**CreateNetworkFirmwareUpgradesStagedEventRequest**](CreateNetworkFirmwareUpgradesStagedEventRequest.md)|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkFirmwareUpgradesStagedGroup"></a>
# **createNetworkFirmwareUpgradesStagedGroup**
> Object createNetworkFirmwareUpgradesStagedGroup(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

Create a Staged Upgrade Group for a network

Create a Staged Upgrade Group for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedGroupRequest createNetworkFirmwareUpgradesStagedGroupRequest = new CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
    try {
      Object result = apiInstance.createNetworkFirmwareUpgradesStagedGroup(networkId, createNetworkFirmwareUpgradesStagedGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkFirmwareUpgradesStagedGroup");
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
| **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | |

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

<a id="createNetworkFloorPlan"></a>
# **createNetworkFloorPlan**
> Object createNetworkFloorPlan(networkId, createNetworkFloorPlanRequest)

Upload a floor plan

Upload a floor plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFloorPlanRequest createNetworkFloorPlanRequest = new CreateNetworkFloorPlanRequest(); // CreateNetworkFloorPlanRequest | 
    try {
      Object result = apiInstance.createNetworkFloorPlan(networkId, createNetworkFloorPlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkFloorPlan");
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
| **createNetworkFloorPlanRequest** | [**CreateNetworkFloorPlanRequest**](CreateNetworkFloorPlanRequest.md)|  | |

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

<a id="createNetworkGroupPolicy"></a>
# **createNetworkGroupPolicy**
> Object createNetworkGroupPolicy(networkId, createNetworkGroupPolicyRequest)

Create a group policy

Create a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkGroupPolicyRequest createNetworkGroupPolicyRequest = new CreateNetworkGroupPolicyRequest(); // CreateNetworkGroupPolicyRequest | 
    try {
      Object result = apiInstance.createNetworkGroupPolicy(networkId, createNetworkGroupPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkGroupPolicy");
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
| **createNetworkGroupPolicyRequest** | [**CreateNetworkGroupPolicyRequest**](CreateNetworkGroupPolicyRequest.md)|  | |

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

<a id="createNetworkMerakiAuthUser"></a>
# **createNetworkMerakiAuthUser**
> GetNetworkMerakiAuthUsers200ResponseInner createNetworkMerakiAuthUser(networkId, createNetworkMerakiAuthUserRequest)

Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkMerakiAuthUserRequest createNetworkMerakiAuthUserRequest = new CreateNetworkMerakiAuthUserRequest(); // CreateNetworkMerakiAuthUserRequest | 
    try {
      GetNetworkMerakiAuthUsers200ResponseInner result = apiInstance.createNetworkMerakiAuthUser(networkId, createNetworkMerakiAuthUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkMerakiAuthUser");
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
| **createNetworkMerakiAuthUserRequest** | [**CreateNetworkMerakiAuthUserRequest**](CreateNetworkMerakiAuthUserRequest.md)|  | |

### Return type

[**GetNetworkMerakiAuthUsers200ResponseInner**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkMqttBroker"></a>
# **createNetworkMqttBroker**
> Object createNetworkMqttBroker(networkId, createNetworkMqttBrokerRequest)

Add an MQTT broker

Add an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkMqttBrokerRequest createNetworkMqttBrokerRequest = new CreateNetworkMqttBrokerRequest(); // CreateNetworkMqttBrokerRequest | 
    try {
      Object result = apiInstance.createNetworkMqttBroker(networkId, createNetworkMqttBrokerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkMqttBroker");
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
| **createNetworkMqttBrokerRequest** | [**CreateNetworkMqttBrokerRequest**](CreateNetworkMqttBrokerRequest.md)|  | |

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

<a id="createNetworkPiiRequest"></a>
# **createNetworkPiiRequest**
> Object createNetworkPiiRequest(networkId, createNetworkPiiRequestRequest)

Submit a new delete or restrict processing PII request

Submit a new delete or restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkPiiRequestRequest createNetworkPiiRequestRequest = new CreateNetworkPiiRequestRequest(); // CreateNetworkPiiRequestRequest | 
    try {
      Object result = apiInstance.createNetworkPiiRequest(networkId, createNetworkPiiRequestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkPiiRequest");
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
| **createNetworkPiiRequestRequest** | [**CreateNetworkPiiRequestRequest**](CreateNetworkPiiRequestRequest.md)|  | [optional] |

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

<a id="createNetworkWebhooksHttpServer"></a>
# **createNetworkWebhooksHttpServer**
> GetNetworkWebhooksHttpServers200ResponseInner createNetworkWebhooksHttpServer(networkId, createNetworkWebhooksHttpServerRequest)

Add an HTTP server to a network

Add an HTTP server to a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksHttpServerRequest createNetworkWebhooksHttpServerRequest = new CreateNetworkWebhooksHttpServerRequest(); // CreateNetworkWebhooksHttpServerRequest | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.createNetworkWebhooksHttpServer(networkId, createNetworkWebhooksHttpServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkWebhooksHttpServer");
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
| **createNetworkWebhooksHttpServerRequest** | [**CreateNetworkWebhooksHttpServerRequest**](CreateNetworkWebhooksHttpServerRequest.md)|  | |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkWebhooksPayloadTemplate"></a>
# **createNetworkWebhooksPayloadTemplate**
> GetNetworkWebhooksPayloadTemplates200ResponseInner createNetworkWebhooksPayloadTemplate(networkId, createNetworkWebhooksPayloadTemplateRequest)

Create a webhook payload template for a network

Create a webhook payload template for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksPayloadTemplateRequest createNetworkWebhooksPayloadTemplateRequest = new CreateNetworkWebhooksPayloadTemplateRequest(); // CreateNetworkWebhooksPayloadTemplateRequest | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.createNetworkWebhooksPayloadTemplate(networkId, createNetworkWebhooksPayloadTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkWebhooksPayloadTemplate");
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
| **createNetworkWebhooksPayloadTemplateRequest** | [**CreateNetworkWebhooksPayloadTemplateRequest**](CreateNetworkWebhooksPayloadTemplateRequest.md)|  | |

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkWebhooksWebhookTest"></a>
# **createNetworkWebhooksWebhookTest**
> CreateNetworkWebhooksWebhookTest201Response createNetworkWebhooksWebhookTest(networkId, createNetworkWebhooksWebhookTestRequest)

Send a test webhook for a network

Send a test webhook for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksWebhookTestRequest createNetworkWebhooksWebhookTestRequest = new CreateNetworkWebhooksWebhookTestRequest(); // CreateNetworkWebhooksWebhookTestRequest | 
    try {
      CreateNetworkWebhooksWebhookTest201Response result = apiInstance.createNetworkWebhooksWebhookTest(networkId, createNetworkWebhooksWebhookTestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createNetworkWebhooksWebhookTest");
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
| **createNetworkWebhooksWebhookTestRequest** | [**CreateNetworkWebhooksWebhookTestRequest**](CreateNetworkWebhooksWebhookTestRequest.md)|  | |

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createOrganizationNetwork_1"></a>
# **createOrganizationNetwork_1**
> GetNetwork200Response createOrganizationNetwork_1(organizationId, createOrganizationNetworkRequest)

Create a network

Create a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationNetworkRequest createOrganizationNetworkRequest = new CreateOrganizationNetworkRequest(); // CreateOrganizationNetworkRequest | 
    try {
      GetNetwork200Response result = apiInstance.createOrganizationNetwork_1(organizationId, createOrganizationNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createOrganizationNetwork_1");
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
| **createOrganizationNetworkRequest** | [**CreateOrganizationNetworkRequest**](CreateOrganizationNetworkRequest.md)|  | |

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deferNetworkFirmwareUpgradesStagedEvents"></a>
# **deferNetworkFirmwareUpgradesStagedEvents**
> GetNetworkFirmwareUpgradesStagedEvents200Response deferNetworkFirmwareUpgradesStagedEvents(networkId)

Postpone by 1 week all pending staged upgrade stages for a network

Postpone by 1 week all pending staged upgrade stages for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.deferNetworkFirmwareUpgradesStagedEvents(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deferNetworkFirmwareUpgradesStagedEvents");
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

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="deleteNetwork"></a>
# **deleteNetwork**
> deleteNetwork(networkId)

Delete a network

Delete a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      apiInstance.deleteNetwork(networkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetwork");
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

<a id="deleteNetworkFirmwareUpgradesStagedGroup"></a>
# **deleteNetworkFirmwareUpgradesStagedGroup**
> deleteNetworkFirmwareUpgradesStagedGroup(networkId, groupId)

Delete a Staged Upgrade Group

Delete a Staged Upgrade Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.deleteNetworkFirmwareUpgradesStagedGroup(networkId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkFirmwareUpgradesStagedGroup");
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
| **groupId** | **String**|  | |

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

<a id="deleteNetworkFloorPlan"></a>
# **deleteNetworkFloorPlan**
> deleteNetworkFloorPlan(networkId, floorPlanId)

Destroy a floor plan

Destroy a floor plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String floorPlanId = "floorPlanId_example"; // String | 
    try {
      apiInstance.deleteNetworkFloorPlan(networkId, floorPlanId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkFloorPlan");
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
| **floorPlanId** | **String**|  | |

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

<a id="deleteNetworkGroupPolicy"></a>
# **deleteNetworkGroupPolicy**
> deleteNetworkGroupPolicy(networkId, groupPolicyId)

Delete a group policy

Delete a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupPolicyId = "groupPolicyId_example"; // String | 
    try {
      apiInstance.deleteNetworkGroupPolicy(networkId, groupPolicyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkGroupPolicy");
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
| **groupPolicyId** | **String**|  | |

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

<a id="deleteNetworkMerakiAuthUser"></a>
# **deleteNetworkMerakiAuthUser**
> deleteNetworkMerakiAuthUser(networkId, merakiAuthUserId)

Deauthorize a user

Deauthorize a user. To reauthorize a user after deauthorizing them, POST to this endpoint. (Currently, 802.1X RADIUS, splash guest, and client VPN users can be deauthorized.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String merakiAuthUserId = "merakiAuthUserId_example"; // String | 
    try {
      apiInstance.deleteNetworkMerakiAuthUser(networkId, merakiAuthUserId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkMerakiAuthUser");
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
| **merakiAuthUserId** | **String**|  | |

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

<a id="deleteNetworkMqttBroker"></a>
# **deleteNetworkMqttBroker**
> deleteNetworkMqttBroker(networkId, mqttBrokerId)

Delete an MQTT broker

Delete an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String mqttBrokerId = "mqttBrokerId_example"; // String | 
    try {
      apiInstance.deleteNetworkMqttBroker(networkId, mqttBrokerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkMqttBroker");
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
| **mqttBrokerId** | **String**|  | |

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

<a id="deleteNetworkPiiRequest"></a>
# **deleteNetworkPiiRequest**
> deleteNetworkPiiRequest(networkId, requestId)

Delete a restrict processing PII request

Delete a restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String requestId = "requestId_example"; // String | 
    try {
      apiInstance.deleteNetworkPiiRequest(networkId, requestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkPiiRequest");
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
| **requestId** | **String**|  | |

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

<a id="deleteNetworkWebhooksHttpServer"></a>
# **deleteNetworkWebhooksHttpServer**
> deleteNetworkWebhooksHttpServer(networkId, httpServerId)

Delete an HTTP server from a network

Delete an HTTP server from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    try {
      apiInstance.deleteNetworkWebhooksHttpServer(networkId, httpServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkWebhooksHttpServer");
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
| **httpServerId** | **String**|  | |

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

<a id="deleteNetworkWebhooksPayloadTemplate"></a>
# **deleteNetworkWebhooksPayloadTemplate**
> deleteNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId)

Destroy a webhook payload template for a network

Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    try {
      apiInstance.deleteNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetworkWebhooksPayloadTemplate");
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
| **payloadTemplateId** | **String**|  | |

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

<a id="getNetwork"></a>
# **getNetwork**
> GetNetwork200Response getNetwork(networkId)

Return a network

Return a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetwork200Response result = apiInstance.getNetwork(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetwork");
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

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkAlertsHistory"></a>
# **getNetworkAlertsHistory**
> List&lt;GetNetworkAlertsHistory200ResponseInner&gt; getNetworkAlertsHistory(networkId, perPage, startingAfter, endingBefore)

Return the alert history for this network

Return the alert history for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkAlertsHistory200ResponseInner> result = apiInstance.getNetworkAlertsHistory(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkAlertsHistory");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkAlertsHistory200ResponseInner&gt;**](GetNetworkAlertsHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkAlertsSettings"></a>
# **getNetworkAlertsSettings**
> Object getNetworkAlertsSettings(networkId)

Return the alert configuration for this network

Return the alert configuration for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkAlertsSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkAlertsSettings");
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

<a id="getNetworkBluetoothClient"></a>
# **getNetworkBluetoothClient**
> Object getNetworkBluetoothClient(networkId, bluetoothClientId, includeConnectivityHistory, connectivityHistoryTimespan)

Return a Bluetooth client

Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String bluetoothClientId = "bluetoothClientId_example"; // String | 
    Boolean includeConnectivityHistory = true; // Boolean | Include the connectivity history for this client
    Integer connectivityHistoryTimespan = 56; // Integer | The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.
    try {
      Object result = apiInstance.getNetworkBluetoothClient(networkId, bluetoothClientId, includeConnectivityHistory, connectivityHistoryTimespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkBluetoothClient");
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
| **bluetoothClientId** | **String**|  | |
| **includeConnectivityHistory** | **Boolean**| Include the connectivity history for this client | [optional] |
| **connectivityHistoryTimespan** | **Integer**| The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used. | [optional] |

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

<a id="getNetworkBluetoothClients"></a>
# **getNetworkBluetoothClients**
> List&lt;Object&gt; getNetworkBluetoothClients(networkId, t0, timespan, perPage, startingAfter, endingBefore, includeConnectivityHistory)

List the Bluetooth clients seen by APs in this network

List the Bluetooth clients seen by APs in this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    Boolean includeConnectivityHistory = true; // Boolean | Include the connectivity history for this client
    try {
      List<Object> result = apiInstance.getNetworkBluetoothClients(networkId, t0, timespan, perPage, startingAfter, endingBefore, includeConnectivityHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkBluetoothClients");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 7 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **includeConnectivityHistory** | **Boolean**| Include the connectivity history for this client | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkClient"></a>
# **getNetworkClient**
> GetNetworkClient200Response getNetworkClient(networkId, clientId)

Return the client associated with the given identifier

Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    try {
      GetNetworkClient200Response result = apiInstance.getNetworkClient(networkId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClient");
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
| **clientId** | **String**|  | |

### Return type

[**GetNetworkClient200Response**](GetNetworkClient200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkClientPolicy"></a>
# **getNetworkClientPolicy**
> Object getNetworkClientPolicy(networkId, clientId)

Return the policy assigned to a client on the network

Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkClientPolicy(networkId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientPolicy");
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
| **clientId** | **String**|  | |

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

<a id="getNetworkClientSplashAuthorizationStatus"></a>
# **getNetworkClientSplashAuthorizationStatus**
> Object getNetworkClientSplashAuthorizationStatus(networkId, clientId)

Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash

Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkClientSplashAuthorizationStatus(networkId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientSplashAuthorizationStatus");
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
| **clientId** | **String**|  | |

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

<a id="getNetworkClientTrafficHistory"></a>
# **getNetworkClientTrafficHistory**
> List&lt;Object&gt; getNetworkClientTrafficHistory(networkId, clientId, perPage, startingAfter, endingBefore)

Return the client&#39;s network traffic data over time

Return the client&#39;s network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide &gt; General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<Object> result = apiInstance.getNetworkClientTrafficHistory(networkId, clientId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientTrafficHistory");
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
| **clientId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkClientUsageHistory"></a>
# **getNetworkClientUsageHistory**
> List&lt;Object&gt; getNetworkClientUsageHistory(networkId, clientId)

Return the client&#39;s daily usage history

Return the client&#39;s daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkClientUsageHistory(networkId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientUsageHistory");
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
| **clientId** | **String**|  | |

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

<a id="getNetworkClients"></a>
# **getNetworkClients**
> GetNetworkClients200Response getNetworkClients(networkId, t0, timespan, perPage, startingAfter, endingBefore, statuses, ip, ip6, ip6Local, mac, os, description, vlan, recentDeviceConnections)

List the clients that have used this network in the timespan

List the clients that have used this network in the timespan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> statuses = Arrays.asList(); // List<String> | Filters clients based on status. Can be one of 'Online' or 'Offline'.
    String ip = "ip_example"; // String | Filters clients based on a partial or full match for the ip address field.
    String ip6 = "ip6_example"; // String | Filters clients based on a partial or full match for the ip6 address field.
    String ip6Local = "ip6Local_example"; // String | Filters clients based on a partial or full match for the ip6Local address field.
    String mac = "mac_example"; // String | Filters clients based on a partial or full match for the mac address field.
    String os = "os_example"; // String | Filters clients based on a partial or full match for the os (operating system) field.
    String description = "description_example"; // String | Filters clients based on a partial or full match for the description field.
    String vlan = "vlan_example"; // String | Filters clients based on the full match for the VLAN field.
    List<String> recentDeviceConnections = Arrays.asList(); // List<String> | Filters clients based on recent connection type. Can be one of 'Wired' or 'Wireless'.
    try {
      GetNetworkClients200Response result = apiInstance.getNetworkClients(networkId, t0, timespan, perPage, startingAfter, endingBefore, statuses, ip, ip6, ip6Local, mac, os, description, vlan, recentDeviceConnections);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClients");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **statuses** | [**List&lt;String&gt;**](String.md)| Filters clients based on status. Can be one of &#39;Online&#39; or &#39;Offline&#39;. | [optional] [enum: Offline, Online] |
| **ip** | **String**| Filters clients based on a partial or full match for the ip address field. | [optional] |
| **ip6** | **String**| Filters clients based on a partial or full match for the ip6 address field. | [optional] |
| **ip6Local** | **String**| Filters clients based on a partial or full match for the ip6Local address field. | [optional] |
| **mac** | **String**| Filters clients based on a partial or full match for the mac address field. | [optional] |
| **os** | **String**| Filters clients based on a partial or full match for the os (operating system) field. | [optional] |
| **description** | **String**| Filters clients based on a partial or full match for the description field. | [optional] |
| **vlan** | **String**| Filters clients based on the full match for the VLAN field. | [optional] |
| **recentDeviceConnections** | [**List&lt;String&gt;**](String.md)| Filters clients based on recent connection type. Can be one of &#39;Wired&#39; or &#39;Wireless&#39;. | [optional] [enum: Wired, Wireless] |

### Return type

[**GetNetworkClients200Response**](GetNetworkClients200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkClientsApplicationUsage"></a>
# **getNetworkClientsApplicationUsage**
> List&lt;Object&gt; getNetworkClientsApplicationUsage(networkId, clients, ssidNumber, perPage, startingAfter, endingBefore, t0, t1, timespan)

Return the application usage data for clients

Return the application usage data for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clients = "clients_example"; // String | A list of client keys, MACs or IPs separated by comma.
    Integer ssidNumber = 0; // Integer | An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<Object> result = apiInstance.getNetworkClientsApplicationUsage(networkId, clients, ssidNumber, perPage, startingAfter, endingBefore, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientsApplicationUsage");
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
| **clients** | **String**| A list of client keys, MACs or IPs separated by comma. | |
| **ssidNumber** | **Integer**| An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned. | [optional] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkClientsBandwidthUsageHistory"></a>
# **getNetworkClientsBandwidthUsageHistory**
> List&lt;Object&gt; getNetworkClientsBandwidthUsageHistory(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore)

Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<Object> result = apiInstance.getNetworkClientsBandwidthUsageHistory(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientsBandwidthUsageHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 30 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkClientsOverview"></a>
# **getNetworkClientsOverview**
> Object getNetworkClientsOverview(networkId, t0, t1, timespan, resolution)

Return overview statistics for network clients

Return overview statistics for network clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800.
    try {
      Object result = apiInstance.getNetworkClientsOverview(networkId, t0, t1, timespan, resolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientsOverview");
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
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800. | [optional] |

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

<a id="getNetworkClientsUsageHistories"></a>
# **getNetworkClientsUsageHistories**
> List&lt;Object&gt; getNetworkClientsUsageHistories(networkId, clients, ssidNumber, perPage, startingAfter, endingBefore, t0, t1, timespan)

Return the usage histories for clients

Return the usage histories for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clients = "clients_example"; // String | A list of client keys, MACs or IPs separated by comma.
    Integer ssidNumber = 0; // Integer | An SSID number to include. If not specified, events for all SSIDs will be returned.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<Object> result = apiInstance.getNetworkClientsUsageHistories(networkId, clients, ssidNumber, perPage, startingAfter, endingBefore, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkClientsUsageHistories");
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
| **clients** | **String**| A list of client keys, MACs or IPs separated by comma. | |
| **ssidNumber** | **Integer**| An SSID number to include. If not specified, events for all SSIDs will be returned. | [optional] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkDevices"></a>
# **getNetworkDevices**
> List&lt;Object&gt; getNetworkDevices(networkId)

List the devices in a network

List the devices in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkDevices(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkDevices");
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

<a id="getNetworkEvents"></a>
# **getNetworkEvents**
> GetNetworkEvents200Response getNetworkEvents(networkId, productType, includedEventTypes, excludedEventTypes, deviceMac, deviceSerial, deviceName, clientIp, clientMac, clientName, smDeviceMac, smDeviceName, perPage, startingAfter, endingBefore)

List the events for the network

List the events for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String productType = "appliance"; // String | The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway
    List<String> includedEventTypes = Arrays.asList(); // List<String> | A list of event types. The returned events will be filtered to only include events with these types.
    List<String> excludedEventTypes = Arrays.asList(); // List<String> | A list of event types. The returned events will be filtered to exclude events with these types.
    String deviceMac = "deviceMac_example"; // String | The MAC address of the Meraki device which the list of events will be filtered with
    String deviceSerial = "deviceSerial_example"; // String | The serial of the Meraki device which the list of events will be filtered with
    String deviceName = "deviceName_example"; // String | The name of the Meraki device which the list of events will be filtered with
    String clientIp = "clientIp_example"; // String | The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
    String clientMac = "clientMac_example"; // String | The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
    String clientName = "clientName_example"; // String | The name, or partial name, of the client which the list of events will be filtered with
    String smDeviceMac = "smDeviceMac_example"; // String | The MAC address of the Systems Manager device which the list of events will be filtered with
    String smDeviceName = "smDeviceName_example"; // String | The name of the Systems Manager device which the list of events will be filtered with
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      GetNetworkEvents200Response result = apiInstance.getNetworkEvents(networkId, productType, includedEventTypes, excludedEventTypes, deviceMac, deviceSerial, deviceName, clientIp, clientMac, clientName, smDeviceMac, smDeviceName, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkEvents");
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
| **productType** | **String**| The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway | [optional] [enum: appliance, camera, cellularGateway, switch, systemsManager, wireless] |
| **includedEventTypes** | [**List&lt;String&gt;**](String.md)| A list of event types. The returned events will be filtered to only include events with these types. | [optional] |
| **excludedEventTypes** | [**List&lt;String&gt;**](String.md)| A list of event types. The returned events will be filtered to exclude events with these types. | [optional] |
| **deviceMac** | **String**| The MAC address of the Meraki device which the list of events will be filtered with | [optional] |
| **deviceSerial** | **String**| The serial of the Meraki device which the list of events will be filtered with | [optional] |
| **deviceName** | **String**| The name of the Meraki device which the list of events will be filtered with | [optional] |
| **clientIp** | **String**| The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks. | [optional] |
| **clientMac** | **String**| The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks. | [optional] |
| **clientName** | **String**| The name, or partial name, of the client which the list of events will be filtered with | [optional] |
| **smDeviceMac** | **String**| The MAC address of the Systems Manager device which the list of events will be filtered with | [optional] |
| **smDeviceName** | **String**| The name of the Systems Manager device which the list of events will be filtered with | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**GetNetworkEvents200Response**](GetNetworkEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkEventsEventTypes"></a>
# **getNetworkEventsEventTypes**
> List&lt;GetNetworkEventsEventTypes200ResponseInner&gt; getNetworkEventsEventTypes(networkId)

List the event type to human-readable description

List the event type to human-readable description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkEventsEventTypes200ResponseInner> result = apiInstance.getNetworkEventsEventTypes(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkEventsEventTypes");
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

[**List&lt;GetNetworkEventsEventTypes200ResponseInner&gt;**](GetNetworkEventsEventTypes200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgrades"></a>
# **getNetworkFirmwareUpgrades**
> GetNetworkFirmwareUpgrades200Response getNetworkFirmwareUpgrades(networkId)

Get firmware upgrade information for a network

Get firmware upgrade information for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgrades200Response result = apiInstance.getNetworkFirmwareUpgrades(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFirmwareUpgrades");
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

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedEvents"></a>
# **getNetworkFirmwareUpgradesStagedEvents**
> GetNetworkFirmwareUpgradesStagedEvents200Response getNetworkFirmwareUpgradesStagedEvents(networkId)

Get the Staged Upgrade Event from a network

Get the Staged Upgrade Event from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.getNetworkFirmwareUpgradesStagedEvents(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFirmwareUpgradesStagedEvents");
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

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedGroup"></a>
# **getNetworkFirmwareUpgradesStagedGroup**
> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup(networkId, groupId)

Get a Staged Upgrade Group from a network

Get a Staged Upgrade Group from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedGroups200ResponseInner result = apiInstance.getNetworkFirmwareUpgradesStagedGroup(networkId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFirmwareUpgradesStagedGroup");
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
| **groupId** | **String**|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedGroups200ResponseInner**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedGroups"></a>
# **getNetworkFirmwareUpgradesStagedGroups**
> List&lt;GetNetworkFirmwareUpgradesStagedGroups200ResponseInner&gt; getNetworkFirmwareUpgradesStagedGroups(networkId)

List of Staged Upgrade Groups in a network

List of Staged Upgrade Groups in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedGroups200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedGroups(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFirmwareUpgradesStagedGroups");
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

[**List&lt;GetNetworkFirmwareUpgradesStagedGroups200ResponseInner&gt;**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedStages"></a>
# **getNetworkFirmwareUpgradesStagedStages**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; getNetworkFirmwareUpgradesStagedStages(networkId)

Order of Staged Upgrade Groups in a network

Order of Staged Upgrade Groups in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedStages(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFirmwareUpgradesStagedStages");
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

[**List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt;**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFloorPlan"></a>
# **getNetworkFloorPlan**
> Object getNetworkFloorPlan(networkId, floorPlanId)

Find a floor plan by ID

Find a floor plan by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String floorPlanId = "floorPlanId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkFloorPlan(networkId, floorPlanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFloorPlan");
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
| **floorPlanId** | **String**|  | |

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

<a id="getNetworkFloorPlans"></a>
# **getNetworkFloorPlans**
> List&lt;Object&gt; getNetworkFloorPlans(networkId)

List the floor plans that belong to your network

List the floor plans that belong to your network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkFloorPlans(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkFloorPlans");
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

<a id="getNetworkGroupPolicies"></a>
# **getNetworkGroupPolicies**
> List&lt;Object&gt; getNetworkGroupPolicies(networkId)

List the group policies in a network

List the group policies in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkGroupPolicies(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkGroupPolicies");
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

<a id="getNetworkGroupPolicy"></a>
# **getNetworkGroupPolicy**
> Object getNetworkGroupPolicy(networkId, groupPolicyId)

Display a group policy

Display a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupPolicyId = "groupPolicyId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkGroupPolicy(networkId, groupPolicyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkGroupPolicy");
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
| **groupPolicyId** | **String**|  | |

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

<a id="getNetworkHealthAlerts"></a>
# **getNetworkHealthAlerts**
> List&lt;GetNetworkHealthAlerts200ResponseInner&gt; getNetworkHealthAlerts(networkId)

Return all global alerts on this network

Return all global alerts on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkHealthAlerts200ResponseInner> result = apiInstance.getNetworkHealthAlerts(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkHealthAlerts");
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

[**List&lt;GetNetworkHealthAlerts200ResponseInner&gt;**](GetNetworkHealthAlerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkMerakiAuthUser"></a>
# **getNetworkMerakiAuthUser**
> GetNetworkMerakiAuthUsers200ResponseInner getNetworkMerakiAuthUser(networkId, merakiAuthUserId)

Return the Meraki Auth splash guest, RADIUS, or client VPN user

Return the Meraki Auth splash guest, RADIUS, or client VPN user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String merakiAuthUserId = "merakiAuthUserId_example"; // String | 
    try {
      GetNetworkMerakiAuthUsers200ResponseInner result = apiInstance.getNetworkMerakiAuthUser(networkId, merakiAuthUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkMerakiAuthUser");
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
| **merakiAuthUserId** | **String**|  | |

### Return type

[**GetNetworkMerakiAuthUsers200ResponseInner**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkMerakiAuthUsers"></a>
# **getNetworkMerakiAuthUsers**
> List&lt;GetNetworkMerakiAuthUsers200ResponseInner&gt; getNetworkMerakiAuthUsers(networkId)

List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkMerakiAuthUsers200ResponseInner> result = apiInstance.getNetworkMerakiAuthUsers(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkMerakiAuthUsers");
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

[**List&lt;GetNetworkMerakiAuthUsers200ResponseInner&gt;**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkMqttBroker"></a>
# **getNetworkMqttBroker**
> Object getNetworkMqttBroker(networkId, mqttBrokerId)

Return an MQTT broker

Return an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String mqttBrokerId = "mqttBrokerId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkMqttBroker(networkId, mqttBrokerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkMqttBroker");
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
| **mqttBrokerId** | **String**|  | |

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

<a id="getNetworkMqttBrokers"></a>
# **getNetworkMqttBrokers**
> List&lt;Object&gt; getNetworkMqttBrokers(networkId)

List the MQTT brokers for this network

List the MQTT brokers for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkMqttBrokers(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkMqttBrokers");
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

<a id="getNetworkNetflow"></a>
# **getNetworkNetflow**
> Object getNetworkNetflow(networkId)

Return the NetFlow traffic reporting settings for a network

Return the NetFlow traffic reporting settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkNetflow(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkNetflow");
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

<a id="getNetworkNetworkHealthChannelUtilization"></a>
# **getNetworkNetworkHealthChannelUtilization**
> List&lt;Object&gt; getNetworkNetworkHealthChannelUtilization(networkId, t0, t1, timespan, resolution, perPage, startingAfter, endingBefore)

Get the channel utilization over each radio for all APs in a network.

Get the channel utilization over each radio for all APs in a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<Object> result = apiInstance.getNetworkNetworkHealthChannelUtilization(networkId, t0, t1, timespan, resolution, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkNetworkHealthChannelUtilization");
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
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 100. Default is 10. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkPiiPiiKeys"></a>
# **getNetworkPiiPiiKeys**
> Object getNetworkPiiPiiKeys(networkId, username, email, mac, serial, imei, bluetoothMac)

List the keys required to access Personally Identifiable Information (PII) for a given identifier

List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \&quot;0\&quot; containing the applicable keys.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/piiKeys &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiPiiKeys(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkPiiPiiKeys");
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
| **username** | **String**| The username of a Systems Manager user | [optional] |
| **email** | **String**| The email of a network user account or a Systems Manager device | [optional] |
| **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] |
| **serial** | **String**| The serial of a Systems Manager device | [optional] |
| **imei** | **String**| The IMEI of a Systems Manager device | [optional] |
| **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] |

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

<a id="getNetworkPiiRequest"></a>
# **getNetworkPiiRequest**
> Object getNetworkPiiRequest(networkId, requestId)

Return a PII request

Return a PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String requestId = "requestId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkPiiRequest(networkId, requestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkPiiRequest");
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
| **requestId** | **String**|  | |

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

<a id="getNetworkPiiRequests"></a>
# **getNetworkPiiRequests**
> List&lt;Object&gt; getNetworkPiiRequests(networkId)

List the PII requests for this network or organization

List the PII requests for this network or organization  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkPiiRequests(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkPiiRequests");
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

<a id="getNetworkPiiSmDevicesForKey"></a>
# **getNetworkPiiSmDevicesForKey**
> Object getNetworkPiiSmDevicesForKey(networkId, username, email, mac, serial, imei, bluetoothMac)

Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier

Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smDevicesForKey &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiSmDevicesForKey(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkPiiSmDevicesForKey");
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
| **username** | **String**| The username of a Systems Manager user | [optional] |
| **email** | **String**| The email of a network user account or a Systems Manager device | [optional] |
| **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] |
| **serial** | **String**| The serial of a Systems Manager device | [optional] |
| **imei** | **String**| The IMEI of a Systems Manager device | [optional] |
| **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] |

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

<a id="getNetworkPiiSmOwnersForKey"></a>
# **getNetworkPiiSmOwnersForKey**
> Object getNetworkPiiSmOwnersForKey(networkId, username, email, mac, serial, imei, bluetoothMac)

Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier

Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smOwnersForKey &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiSmOwnersForKey(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkPiiSmOwnersForKey");
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
| **username** | **String**| The username of a Systems Manager user | [optional] |
| **email** | **String**| The email of a network user account or a Systems Manager device | [optional] |
| **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] |
| **serial** | **String**| The serial of a Systems Manager device | [optional] |
| **imei** | **String**| The IMEI of a Systems Manager device | [optional] |
| **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] |

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

<a id="getNetworkPoliciesByClient"></a>
# **getNetworkPoliciesByClient**
> List&lt;GetNetworkPoliciesByClient200ResponseInner&gt; getNetworkPoliciesByClient(networkId, perPage, startingAfter, endingBefore, t0, timespan)

Get policies for all clients with policies

Get policies for all clients with policies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetNetworkPoliciesByClient200ResponseInner> result = apiInstance.getNetworkPoliciesByClient(networkId, perPage, startingAfter, endingBefore, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkPoliciesByClient");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetNetworkPoliciesByClient200ResponseInner&gt;**](GetNetworkPoliciesByClient200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSettings"></a>
# **getNetworkSettings**
> GetNetworkSettings200Response getNetworkSettings(networkId)

Return the settings for a network

Return the settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSettings200Response result = apiInstance.getNetworkSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkSettings");
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

[**GetNetworkSettings200Response**](GetNetworkSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSnmp"></a>
# **getNetworkSnmp**
> Object getNetworkSnmp(networkId)

Return the SNMP settings for a network

Return the SNMP settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSnmp(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkSnmp");
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

<a id="getNetworkSplashLoginAttempts"></a>
# **getNetworkSplashLoginAttempts**
> List&lt;Object&gt; getNetworkSplashLoginAttempts(networkId, ssidNumber, loginIdentifier, timespan)

List the splash login attempts for a network

List the splash login attempts for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer ssidNumber = 0; // Integer | Only return the login attempts for the specified SSID
    String loginIdentifier = "loginIdentifier_example"; // String | The username, email, or phone number used during login
    Integer timespan = 56; // Integer | The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months
    try {
      List<Object> result = apiInstance.getNetworkSplashLoginAttempts(networkId, ssidNumber, loginIdentifier, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkSplashLoginAttempts");
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
| **ssidNumber** | **Integer**| Only return the login attempts for the specified SSID | [optional] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] |
| **loginIdentifier** | **String**| The username, email, or phone number used during login | [optional] |
| **timespan** | **Integer**| The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months | [optional] |

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

<a id="getNetworkSyslogServers"></a>
# **getNetworkSyslogServers**
> GetNetworkSyslogServers200Response getNetworkSyslogServers(networkId)

List the syslog servers for a network

List the syslog servers for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSyslogServers200Response result = apiInstance.getNetworkSyslogServers(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkSyslogServers");
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

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkTopologyLinkLayer"></a>
# **getNetworkTopologyLinkLayer**
> Object getNetworkTopologyLinkLayer(networkId)

List the LLDP and CDP information for all discovered devices and connections in a network.

List the LLDP and CDP information for all discovered devices and connections in a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkTopologyLinkLayer(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkTopologyLinkLayer");
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

<a id="getNetworkTraffic"></a>
# **getNetworkTraffic**
> List&lt;Object&gt; getNetworkTraffic(networkId, t0, timespan, deviceType)

Return the traffic analysis data for this network

Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
    String deviceType = "appliance"; // String | Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage.
    try {
      List<Object> result = apiInstance.getNetworkTraffic(networkId, t0, timespan, deviceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkTraffic");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 30 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. | [optional] |
| **deviceType** | **String**| Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage. | [optional] [enum: appliance, combined, switch, wireless] |

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

<a id="getNetworkTrafficAnalysis"></a>
# **getNetworkTrafficAnalysis**
> Object getNetworkTrafficAnalysis(networkId)

Return the traffic analysis settings for a network

Return the traffic analysis settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkTrafficAnalysis(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkTrafficAnalysis");
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

<a id="getNetworkTrafficShapingApplicationCategories"></a>
# **getNetworkTrafficShapingApplicationCategories**
> Object getNetworkTrafficShapingApplicationCategories(networkId)

Returns the application categories for traffic shaping rules.

Returns the application categories for traffic shaping rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkTrafficShapingApplicationCategories(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkTrafficShapingApplicationCategories");
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

<a id="getNetworkTrafficShapingDscpTaggingOptions"></a>
# **getNetworkTrafficShapingDscpTaggingOptions**
> List&lt;Object&gt; getNetworkTrafficShapingDscpTaggingOptions(networkId)

Returns the available DSCP tagging options for your traffic shaping rules.

Returns the available DSCP tagging options for your traffic shaping rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkTrafficShapingDscpTaggingOptions(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkTrafficShapingDscpTaggingOptions");
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

<a id="getNetworkWebhooksHttpServer"></a>
# **getNetworkWebhooksHttpServer**
> GetNetworkWebhooksHttpServers200ResponseInner getNetworkWebhooksHttpServer(networkId, httpServerId)

Return an HTTP server for a network

Return an HTTP server for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.getNetworkWebhooksHttpServer(networkId, httpServerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkWebhooksHttpServer");
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
| **httpServerId** | **String**|  | |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksHttpServers"></a>
# **getNetworkWebhooksHttpServers**
> List&lt;GetNetworkWebhooksHttpServers200ResponseInner&gt; getNetworkWebhooksHttpServers(networkId)

List the HTTP servers for a network

List the HTTP servers for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkWebhooksHttpServers200ResponseInner> result = apiInstance.getNetworkWebhooksHttpServers(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkWebhooksHttpServers");
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

[**List&lt;GetNetworkWebhooksHttpServers200ResponseInner&gt;**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksPayloadTemplate"></a>
# **getNetworkWebhooksPayloadTemplate**
> GetNetworkWebhooksPayloadTemplates200ResponseInner getNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId)

Get the webhook payload template for a network

Get the webhook payload template for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.getNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkWebhooksPayloadTemplate");
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
| **payloadTemplateId** | **String**|  | |

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksPayloadTemplates"></a>
# **getNetworkWebhooksPayloadTemplates**
> List&lt;GetNetworkWebhooksPayloadTemplates200ResponseInner&gt; getNetworkWebhooksPayloadTemplates(networkId)

List the webhook payload templates for a network

List the webhook payload templates for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkWebhooksPayloadTemplates200ResponseInner> result = apiInstance.getNetworkWebhooksPayloadTemplates(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkWebhooksPayloadTemplates");
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

[**List&lt;GetNetworkWebhooksPayloadTemplates200ResponseInner&gt;**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksWebhookTest"></a>
# **getNetworkWebhooksWebhookTest**
> CreateNetworkWebhooksWebhookTest201Response getNetworkWebhooksWebhookTest(networkId, webhookTestId)

Return the status of a webhook test for a network

Return the status of a webhook test for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String webhookTestId = "webhookTestId_example"; // String | 
    try {
      CreateNetworkWebhooksWebhookTest201Response result = apiInstance.getNetworkWebhooksWebhookTest(networkId, webhookTestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkWebhooksWebhookTest");
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
| **webhookTestId** | **String**|  | |

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInventoryOnboardingCloudMonitoringNetworks_4"></a>
# **getOrganizationInventoryOnboardingCloudMonitoringNetworks_4**
> List&lt;GetNetwork200Response&gt; getOrganizationInventoryOnboardingCloudMonitoringNetworks_4(organizationId, deviceType, perPage, startingAfter, endingBefore)

Returns list of networks eligible for adding cloud monitored device

Returns list of networks eligible for adding cloud monitored device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String deviceType = "switch"; // String | Device Type switch or wireless controller
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetwork200Response> result = apiInstance.getOrganizationInventoryOnboardingCloudMonitoringNetworks_4(organizationId, deviceType, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getOrganizationInventoryOnboardingCloudMonitoringNetworks_4");
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
| **deviceType** | **String**| Device Type switch or wireless controller | [enum: switch, wireless_controller] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetwork200Response&gt;**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationNetworks_1"></a>
# **getOrganizationNetworks_1**
> List&lt;GetNetwork200Response&gt; getOrganizationNetworks_1(organizationId, configTemplateId, isBoundToConfigTemplate, tags, tagsFilterType, perPage, startingAfter, endingBefore)

List the networks that the user has privileges on in an organization

List the networks that the user has privileges on in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | An optional parameter that is the ID of a config template. Will return all networks bound to that template.
    Boolean isBoundToConfigTemplate = true; // Boolean | An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
    List<String> tags = Arrays.asList(); // List<String> | An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
    String tagsFilterType = "withAllTags"; // String | An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetwork200Response> result = apiInstance.getOrganizationNetworks_1(organizationId, configTemplateId, isBoundToConfigTemplate, tags, tagsFilterType, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getOrganizationNetworks_1");
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
| **configTemplateId** | **String**| An optional parameter that is the ID of a config template. Will return all networks bound to that template. | [optional] |
| **isBoundToConfigTemplate** | **Boolean**| An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). | [optional] |
| **tagsFilterType** | **String**| An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] [enum: withAllTags, withAnyTags] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetwork200Response&gt;**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="provisionNetworkClients"></a>
# **provisionNetworkClients**
> Object provisionNetworkClients(networkId, provisionNetworkClientsRequest)

Provisions a client with a name and policy

Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    ProvisionNetworkClientsRequest provisionNetworkClientsRequest = new ProvisionNetworkClientsRequest(); // ProvisionNetworkClientsRequest | 
    try {
      Object result = apiInstance.provisionNetworkClients(networkId, provisionNetworkClientsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#provisionNetworkClients");
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
| **provisionNetworkClientsRequest** | [**ProvisionNetworkClientsRequest**](ProvisionNetworkClientsRequest.md)|  | |

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

<a id="removeNetworkDevices"></a>
# **removeNetworkDevices**
> removeNetworkDevices(networkId, removeNetworkDevicesRequest)

Remove a single device

Remove a single device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    RemoveNetworkDevicesRequest removeNetworkDevicesRequest = new RemoveNetworkDevicesRequest(); // RemoveNetworkDevicesRequest | 
    try {
      apiInstance.removeNetworkDevices(networkId, removeNetworkDevicesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#removeNetworkDevices");
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
| **removeNetworkDevicesRequest** | [**RemoveNetworkDevicesRequest**](RemoveNetworkDevicesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="rollbacksNetworkFirmwareUpgradesStagedEvents"></a>
# **rollbacksNetworkFirmwareUpgradesStagedEvents**
> GetNetworkFirmwareUpgradesStagedEvents200Response rollbacksNetworkFirmwareUpgradesStagedEvents(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest)

Rollback a Staged Upgrade Event for a network

Rollback a Staged Upgrade Event for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    RollbacksNetworkFirmwareUpgradesStagedEventsRequest rollbacksNetworkFirmwareUpgradesStagedEventsRequest = new RollbacksNetworkFirmwareUpgradesStagedEventsRequest(); // RollbacksNetworkFirmwareUpgradesStagedEventsRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.rollbacksNetworkFirmwareUpgradesStagedEvents(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#rollbacksNetworkFirmwareUpgradesStagedEvents");
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
| **rollbacksNetworkFirmwareUpgradesStagedEventsRequest** | [**RollbacksNetworkFirmwareUpgradesStagedEventsRequest**](RollbacksNetworkFirmwareUpgradesStagedEventsRequest.md)|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="splitNetwork"></a>
# **splitNetwork**
> SplitNetwork200Response splitNetwork(networkId)

Split a combined network into individual networks for each type of device

Split a combined network into individual networks for each type of device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      SplitNetwork200Response result = apiInstance.splitNetwork(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#splitNetwork");
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

[**SplitNetwork200Response**](SplitNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="unbindNetwork"></a>
# **unbindNetwork**
> GetNetwork200Response unbindNetwork(networkId, unbindNetworkRequest)

Unbind a network from a template.

Unbind a network from a template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UnbindNetworkRequest unbindNetworkRequest = new UnbindNetworkRequest(); // UnbindNetworkRequest | 
    try {
      GetNetwork200Response result = apiInstance.unbindNetwork(networkId, unbindNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#unbindNetwork");
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
| **unbindNetworkRequest** | [**UnbindNetworkRequest**](UnbindNetworkRequest.md)|  | [optional] |

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetwork"></a>
# **updateNetwork**
> GetNetwork200Response updateNetwork(networkId, updateNetworkRequest)

Update a network

Update a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkRequest updateNetworkRequest = new UpdateNetworkRequest(); // UpdateNetworkRequest | 
    try {
      GetNetwork200Response result = apiInstance.updateNetwork(networkId, updateNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetwork");
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
| **updateNetworkRequest** | [**UpdateNetworkRequest**](UpdateNetworkRequest.md)|  | [optional] |

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkAlertsSettings"></a>
# **updateNetworkAlertsSettings**
> Object updateNetworkAlertsSettings(networkId, updateNetworkAlertsSettingsRequest)

Update the alert configuration for this network

Update the alert configuration for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkAlertsSettingsRequest updateNetworkAlertsSettingsRequest = new UpdateNetworkAlertsSettingsRequest(); // UpdateNetworkAlertsSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkAlertsSettings(networkId, updateNetworkAlertsSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkAlertsSettings");
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
| **updateNetworkAlertsSettingsRequest** | [**UpdateNetworkAlertsSettingsRequest**](UpdateNetworkAlertsSettingsRequest.md)|  | [optional] |

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

<a id="updateNetworkClientPolicy"></a>
# **updateNetworkClientPolicy**
> Object updateNetworkClientPolicy(networkId, clientId, updateNetworkClientPolicyRequest)

Update the policy assigned to a client on the network

Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    UpdateNetworkClientPolicyRequest updateNetworkClientPolicyRequest = new UpdateNetworkClientPolicyRequest(); // UpdateNetworkClientPolicyRequest | 
    try {
      Object result = apiInstance.updateNetworkClientPolicy(networkId, clientId, updateNetworkClientPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkClientPolicy");
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
| **clientId** | **String**|  | |
| **updateNetworkClientPolicyRequest** | [**UpdateNetworkClientPolicyRequest**](UpdateNetworkClientPolicyRequest.md)|  | |

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

<a id="updateNetworkClientSplashAuthorizationStatus"></a>
# **updateNetworkClientSplashAuthorizationStatus**
> Object updateNetworkClientSplashAuthorizationStatus(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest)

Update a client&#39;s splash authorization

Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest = new UpdateNetworkClientSplashAuthorizationStatusRequest(); // UpdateNetworkClientSplashAuthorizationStatusRequest | 
    try {
      Object result = apiInstance.updateNetworkClientSplashAuthorizationStatus(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkClientSplashAuthorizationStatus");
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
| **clientId** | **String**|  | |
| **updateNetworkClientSplashAuthorizationStatusRequest** | [**UpdateNetworkClientSplashAuthorizationStatusRequest**](UpdateNetworkClientSplashAuthorizationStatusRequest.md)|  | |

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

<a id="updateNetworkFirmwareUpgrades"></a>
# **updateNetworkFirmwareUpgrades**
> GetNetworkFirmwareUpgrades200Response updateNetworkFirmwareUpgrades(networkId, updateNetworkFirmwareUpgradesRequest)

Update firmware upgrade information for a network

Update firmware upgrade information for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesRequest updateNetworkFirmwareUpgradesRequest = new UpdateNetworkFirmwareUpgradesRequest(); // UpdateNetworkFirmwareUpgradesRequest | 
    try {
      GetNetworkFirmwareUpgrades200Response result = apiInstance.updateNetworkFirmwareUpgrades(networkId, updateNetworkFirmwareUpgradesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkFirmwareUpgrades");
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
| **updateNetworkFirmwareUpgradesRequest** | [**UpdateNetworkFirmwareUpgradesRequest**](UpdateNetworkFirmwareUpgradesRequest.md)|  | [optional] |

### Return type

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkFirmwareUpgradesStagedEvents"></a>
# **updateNetworkFirmwareUpgradesStagedEvents**
> GetNetworkFirmwareUpgradesStagedEvents200Response updateNetworkFirmwareUpgradesStagedEvents(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest)

Update the Staged Upgrade Event for a network

Update the Staged Upgrade Event for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedEventsRequest updateNetworkFirmwareUpgradesStagedEventsRequest = new UpdateNetworkFirmwareUpgradesStagedEventsRequest(); // UpdateNetworkFirmwareUpgradesStagedEventsRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.updateNetworkFirmwareUpgradesStagedEvents(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkFirmwareUpgradesStagedEvents");
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
| **updateNetworkFirmwareUpgradesStagedEventsRequest** | [**UpdateNetworkFirmwareUpgradesStagedEventsRequest**](UpdateNetworkFirmwareUpgradesStagedEventsRequest.md)|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkFirmwareUpgradesStagedGroup"></a>
# **updateNetworkFirmwareUpgradesStagedGroup**
> Object updateNetworkFirmwareUpgradesStagedGroup(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

Update a Staged Upgrade Group for a network

Update a Staged Upgrade Group for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedGroupRequest createNetworkFirmwareUpgradesStagedGroupRequest = new CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
    try {
      Object result = apiInstance.updateNetworkFirmwareUpgradesStagedGroup(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkFirmwareUpgradesStagedGroup");
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
| **groupId** | **String**|  | |
| **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | |

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

<a id="updateNetworkFirmwareUpgradesStagedStages"></a>
# **updateNetworkFirmwareUpgradesStagedStages**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; updateNetworkFirmwareUpgradesStagedStages(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest)

Assign Staged Upgrade Group order in the sequence.

Assign Staged Upgrade Group order in the sequence.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedStagesRequest updateNetworkFirmwareUpgradesStagedStagesRequest = new UpdateNetworkFirmwareUpgradesStagedStagesRequest(); // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.updateNetworkFirmwareUpgradesStagedStages(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkFirmwareUpgradesStagedStages");
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
| **updateNetworkFirmwareUpgradesStagedStagesRequest** | [**UpdateNetworkFirmwareUpgradesStagedStagesRequest**](UpdateNetworkFirmwareUpgradesStagedStagesRequest.md)|  | [optional] |

### Return type

[**List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt;**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkFloorPlan"></a>
# **updateNetworkFloorPlan**
> Object updateNetworkFloorPlan(networkId, floorPlanId, updateNetworkFloorPlanRequest)

Update a floor plan&#39;s geolocation and other meta data

Update a floor plan&#39;s geolocation and other meta data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String floorPlanId = "floorPlanId_example"; // String | 
    UpdateNetworkFloorPlanRequest updateNetworkFloorPlanRequest = new UpdateNetworkFloorPlanRequest(); // UpdateNetworkFloorPlanRequest | 
    try {
      Object result = apiInstance.updateNetworkFloorPlan(networkId, floorPlanId, updateNetworkFloorPlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkFloorPlan");
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
| **floorPlanId** | **String**|  | |
| **updateNetworkFloorPlanRequest** | [**UpdateNetworkFloorPlanRequest**](UpdateNetworkFloorPlanRequest.md)|  | [optional] |

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

<a id="updateNetworkGroupPolicy"></a>
# **updateNetworkGroupPolicy**
> Object updateNetworkGroupPolicy(networkId, groupPolicyId, updateNetworkGroupPolicyRequest)

Update a group policy

Update a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupPolicyId = "groupPolicyId_example"; // String | 
    UpdateNetworkGroupPolicyRequest updateNetworkGroupPolicyRequest = new UpdateNetworkGroupPolicyRequest(); // UpdateNetworkGroupPolicyRequest | 
    try {
      Object result = apiInstance.updateNetworkGroupPolicy(networkId, groupPolicyId, updateNetworkGroupPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkGroupPolicy");
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
| **groupPolicyId** | **String**|  | |
| **updateNetworkGroupPolicyRequest** | [**UpdateNetworkGroupPolicyRequest**](UpdateNetworkGroupPolicyRequest.md)|  | [optional] |

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

<a id="updateNetworkMerakiAuthUser"></a>
# **updateNetworkMerakiAuthUser**
> GetNetworkMerakiAuthUsers200ResponseInner updateNetworkMerakiAuthUser(networkId, merakiAuthUserId, updateNetworkMerakiAuthUserRequest)

Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String merakiAuthUserId = "merakiAuthUserId_example"; // String | 
    UpdateNetworkMerakiAuthUserRequest updateNetworkMerakiAuthUserRequest = new UpdateNetworkMerakiAuthUserRequest(); // UpdateNetworkMerakiAuthUserRequest | 
    try {
      GetNetworkMerakiAuthUsers200ResponseInner result = apiInstance.updateNetworkMerakiAuthUser(networkId, merakiAuthUserId, updateNetworkMerakiAuthUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkMerakiAuthUser");
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
| **merakiAuthUserId** | **String**|  | |
| **updateNetworkMerakiAuthUserRequest** | [**UpdateNetworkMerakiAuthUserRequest**](UpdateNetworkMerakiAuthUserRequest.md)|  | [optional] |

### Return type

[**GetNetworkMerakiAuthUsers200ResponseInner**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkMqttBroker"></a>
# **updateNetworkMqttBroker**
> Object updateNetworkMqttBroker(networkId, mqttBrokerId, updateNetworkMqttBrokerRequest)

Update an MQTT broker

Update an MQTT broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String mqttBrokerId = "mqttBrokerId_example"; // String | 
    UpdateNetworkMqttBrokerRequest updateNetworkMqttBrokerRequest = new UpdateNetworkMqttBrokerRequest(); // UpdateNetworkMqttBrokerRequest | 
    try {
      Object result = apiInstance.updateNetworkMqttBroker(networkId, mqttBrokerId, updateNetworkMqttBrokerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkMqttBroker");
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
| **mqttBrokerId** | **String**|  | |
| **updateNetworkMqttBrokerRequest** | [**UpdateNetworkMqttBrokerRequest**](UpdateNetworkMqttBrokerRequest.md)|  | [optional] |

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

<a id="updateNetworkNetflow"></a>
# **updateNetworkNetflow**
> Object updateNetworkNetflow(networkId, updateNetworkNetflowRequest)

Update the NetFlow traffic reporting settings for a network

Update the NetFlow traffic reporting settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkNetflowRequest updateNetworkNetflowRequest = new UpdateNetworkNetflowRequest(); // UpdateNetworkNetflowRequest | 
    try {
      Object result = apiInstance.updateNetworkNetflow(networkId, updateNetworkNetflowRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkNetflow");
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
| **updateNetworkNetflowRequest** | [**UpdateNetworkNetflowRequest**](UpdateNetworkNetflowRequest.md)|  | [optional] |

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

<a id="updateNetworkSettings"></a>
# **updateNetworkSettings**
> GetNetworkSettings200Response updateNetworkSettings(networkId, updateNetworkSettingsRequest)

Update the settings for a network

Update the settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSettingsRequest updateNetworkSettingsRequest = new UpdateNetworkSettingsRequest(); // UpdateNetworkSettingsRequest | 
    try {
      GetNetworkSettings200Response result = apiInstance.updateNetworkSettings(networkId, updateNetworkSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkSettings");
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
| **updateNetworkSettingsRequest** | [**UpdateNetworkSettingsRequest**](UpdateNetworkSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkSettings200Response**](GetNetworkSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSnmp"></a>
# **updateNetworkSnmp**
> Object updateNetworkSnmp(networkId, updateNetworkSnmpRequest)

Update the SNMP settings for a network

Update the SNMP settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSnmpRequest updateNetworkSnmpRequest = new UpdateNetworkSnmpRequest(); // UpdateNetworkSnmpRequest | 
    try {
      Object result = apiInstance.updateNetworkSnmp(networkId, updateNetworkSnmpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkSnmp");
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
| **updateNetworkSnmpRequest** | [**UpdateNetworkSnmpRequest**](UpdateNetworkSnmpRequest.md)|  | [optional] |

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

<a id="updateNetworkSyslogServers"></a>
# **updateNetworkSyslogServers**
> GetNetworkSyslogServers200Response updateNetworkSyslogServers(networkId, updateNetworkSyslogServersRequest)

Update the syslog servers for a network

Update the syslog servers for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSyslogServersRequest updateNetworkSyslogServersRequest = new UpdateNetworkSyslogServersRequest(); // UpdateNetworkSyslogServersRequest | 
    try {
      GetNetworkSyslogServers200Response result = apiInstance.updateNetworkSyslogServers(networkId, updateNetworkSyslogServersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkSyslogServers");
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
| **updateNetworkSyslogServersRequest** | [**UpdateNetworkSyslogServersRequest**](UpdateNetworkSyslogServersRequest.md)|  | |

### Return type

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkTrafficAnalysis"></a>
# **updateNetworkTrafficAnalysis**
> Object updateNetworkTrafficAnalysis(networkId, updateNetworkTrafficAnalysisRequest)

Update the traffic analysis settings for a network

Update the traffic analysis settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkTrafficAnalysisRequest updateNetworkTrafficAnalysisRequest = new UpdateNetworkTrafficAnalysisRequest(); // UpdateNetworkTrafficAnalysisRequest | 
    try {
      Object result = apiInstance.updateNetworkTrafficAnalysis(networkId, updateNetworkTrafficAnalysisRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkTrafficAnalysis");
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
| **updateNetworkTrafficAnalysisRequest** | [**UpdateNetworkTrafficAnalysisRequest**](UpdateNetworkTrafficAnalysisRequest.md)|  | [optional] |

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

<a id="updateNetworkWebhooksHttpServer"></a>
# **updateNetworkWebhooksHttpServer**
> GetNetworkWebhooksHttpServers200ResponseInner updateNetworkWebhooksHttpServer(networkId, httpServerId, updateNetworkWebhooksHttpServerRequest)

Update an HTTP server

Update an HTTP server. To change a URL, create a new HTTP server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    UpdateNetworkWebhooksHttpServerRequest updateNetworkWebhooksHttpServerRequest = new UpdateNetworkWebhooksHttpServerRequest(); // UpdateNetworkWebhooksHttpServerRequest | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.updateNetworkWebhooksHttpServer(networkId, httpServerId, updateNetworkWebhooksHttpServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkWebhooksHttpServer");
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
| **httpServerId** | **String**|  | |
| **updateNetworkWebhooksHttpServerRequest** | [**UpdateNetworkWebhooksHttpServerRequest**](UpdateNetworkWebhooksHttpServerRequest.md)|  | [optional] |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWebhooksPayloadTemplate"></a>
# **updateNetworkWebhooksPayloadTemplate**
> GetNetworkWebhooksPayloadTemplates200ResponseInner updateNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId, updateNetworkWebhooksPayloadTemplateRequest)

Update a webhook payload template for a network

Update a webhook payload template for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    UpdateNetworkWebhooksPayloadTemplateRequest updateNetworkWebhooksPayloadTemplateRequest = new UpdateNetworkWebhooksPayloadTemplateRequest(); // UpdateNetworkWebhooksPayloadTemplateRequest | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.updateNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId, updateNetworkWebhooksPayloadTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkWebhooksPayloadTemplate");
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
| **payloadTemplateId** | **String**|  | |
| **updateNetworkWebhooksPayloadTemplateRequest** | [**UpdateNetworkWebhooksPayloadTemplateRequest**](UpdateNetworkWebhooksPayloadTemplateRequest.md)|  | [optional] |

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="vmxNetworkDevicesClaim"></a>
# **vmxNetworkDevicesClaim**
> Object vmxNetworkDevicesClaim(networkId, vmxNetworkDevicesClaimRequest)

Claim a vMX into a network

Claim a vMX into a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    VmxNetworkDevicesClaimRequest vmxNetworkDevicesClaimRequest = new VmxNetworkDevicesClaimRequest(); // VmxNetworkDevicesClaimRequest | 
    try {
      Object result = apiInstance.vmxNetworkDevicesClaim(networkId, vmxNetworkDevicesClaimRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#vmxNetworkDevicesClaim");
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
| **vmxNetworkDevicesClaimRequest** | [**VmxNetworkDevicesClaimRequest**](VmxNetworkDevicesClaimRequest.md)|  | |

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

