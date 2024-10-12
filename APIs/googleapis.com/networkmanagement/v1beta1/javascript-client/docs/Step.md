# NetworkManagementApi.Step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort** | [**AbortInfo**](AbortInfo.md) |  | [optional] 
**appEngineVersion** | [**AppEngineVersionInfo**](AppEngineVersionInfo.md) |  | [optional] 
**causesDrop** | **Boolean** | This is a step that leads to the final state Drop. | [optional] 
**cloudFunction** | [**CloudFunctionInfo**](CloudFunctionInfo.md) |  | [optional] 
**cloudRunRevision** | [**CloudRunRevisionInfo**](CloudRunRevisionInfo.md) |  | [optional] 
**cloudSqlInstance** | [**CloudSQLInstanceInfo**](CloudSQLInstanceInfo.md) |  | [optional] 
**deliver** | [**DeliverInfo**](DeliverInfo.md) |  | [optional] 
**description** | **String** | A description of the step. Usually this is a summary of the state. | [optional] 
**drop** | [**DropInfo**](DropInfo.md) |  | [optional] 
**endpoint** | [**EndpointInfo**](EndpointInfo.md) |  | [optional] 
**firewall** | [**FirewallInfo**](FirewallInfo.md) |  | [optional] 
**forward** | [**ForwardInfo**](ForwardInfo.md) |  | [optional] 
**forwardingRule** | [**ForwardingRuleInfo**](ForwardingRuleInfo.md) |  | [optional] 
**gkeMaster** | [**GKEMasterInfo**](GKEMasterInfo.md) |  | [optional] 
**googleService** | [**GoogleServiceInfo**](GoogleServiceInfo.md) |  | [optional] 
**instance** | [**InstanceInfo**](InstanceInfo.md) |  | [optional] 
**loadBalancer** | [**LoadBalancerInfo**](LoadBalancerInfo.md) |  | [optional] 
**loadBalancerBackendInfo** | [**LoadBalancerBackendInfo**](LoadBalancerBackendInfo.md) |  | [optional] 
**nat** | [**NatInfo**](NatInfo.md) |  | [optional] 
**network** | [**NetworkInfo**](NetworkInfo.md) |  | [optional] 
**projectId** | **String** | Project ID that contains the configuration this step is validating. | [optional] 
**proxyConnection** | [**ProxyConnectionInfo**](ProxyConnectionInfo.md) |  | [optional] 
**route** | [**RouteInfo**](RouteInfo.md) |  | [optional] 
**state** | **String** | Each step is in one of the pre-defined states. | [optional] 
**storageBucket** | [**StorageBucketInfo**](StorageBucketInfo.md) |  | [optional] 
**vpcConnector** | [**VpcConnectorInfo**](VpcConnectorInfo.md) |  | [optional] 
**vpnGateway** | [**VpnGatewayInfo**](VpnGatewayInfo.md) |  | [optional] 
**vpnTunnel** | [**VpnTunnelInfo**](VpnTunnelInfo.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `START_FROM_INSTANCE` (value: `"START_FROM_INSTANCE"`)

* `START_FROM_INTERNET` (value: `"START_FROM_INTERNET"`)

* `START_FROM_GOOGLE_SERVICE` (value: `"START_FROM_GOOGLE_SERVICE"`)

* `START_FROM_PRIVATE_NETWORK` (value: `"START_FROM_PRIVATE_NETWORK"`)

* `START_FROM_GKE_MASTER` (value: `"START_FROM_GKE_MASTER"`)

* `START_FROM_CLOUD_SQL_INSTANCE` (value: `"START_FROM_CLOUD_SQL_INSTANCE"`)

* `START_FROM_CLOUD_FUNCTION` (value: `"START_FROM_CLOUD_FUNCTION"`)

* `START_FROM_APP_ENGINE_VERSION` (value: `"START_FROM_APP_ENGINE_VERSION"`)

* `START_FROM_CLOUD_RUN_REVISION` (value: `"START_FROM_CLOUD_RUN_REVISION"`)

* `START_FROM_STORAGE_BUCKET` (value: `"START_FROM_STORAGE_BUCKET"`)

* `START_FROM_PSC_PUBLISHED_SERVICE` (value: `"START_FROM_PSC_PUBLISHED_SERVICE"`)

* `APPLY_INGRESS_FIREWALL_RULE` (value: `"APPLY_INGRESS_FIREWALL_RULE"`)

* `APPLY_EGRESS_FIREWALL_RULE` (value: `"APPLY_EGRESS_FIREWALL_RULE"`)

* `APPLY_ROUTE` (value: `"APPLY_ROUTE"`)

* `APPLY_FORWARDING_RULE` (value: `"APPLY_FORWARDING_RULE"`)

* `ANALYZE_LOAD_BALANCER_BACKEND` (value: `"ANALYZE_LOAD_BALANCER_BACKEND"`)

* `SPOOFING_APPROVED` (value: `"SPOOFING_APPROVED"`)

* `ARRIVE_AT_INSTANCE` (value: `"ARRIVE_AT_INSTANCE"`)

* `ARRIVE_AT_INTERNAL_LOAD_BALANCER` (value: `"ARRIVE_AT_INTERNAL_LOAD_BALANCER"`)

* `ARRIVE_AT_EXTERNAL_LOAD_BALANCER` (value: `"ARRIVE_AT_EXTERNAL_LOAD_BALANCER"`)

* `ARRIVE_AT_VPN_GATEWAY` (value: `"ARRIVE_AT_VPN_GATEWAY"`)

* `ARRIVE_AT_VPN_TUNNEL` (value: `"ARRIVE_AT_VPN_TUNNEL"`)

* `ARRIVE_AT_VPC_CONNECTOR` (value: `"ARRIVE_AT_VPC_CONNECTOR"`)

* `NAT` (value: `"NAT"`)

* `PROXY_CONNECTION` (value: `"PROXY_CONNECTION"`)

* `DELIVER` (value: `"DELIVER"`)

* `DROP` (value: `"DROP"`)

* `FORWARD` (value: `"FORWARD"`)

* `ABORT` (value: `"ABORT"`)

* `VIEWER_PERMISSION_MISSING` (value: `"VIEWER_PERMISSION_MISSING"`)




