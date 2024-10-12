

# Step

A simulated forwarding path is composed of multiple steps. Each step has a well-defined state and an associated configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abort** | [**AbortInfo**](AbortInfo.md) |  |  [optional] |
|**appEngineVersion** | [**AppEngineVersionInfo**](AppEngineVersionInfo.md) |  |  [optional] |
|**causesDrop** | **Boolean** | This is a step that leads to the final state Drop. |  [optional] |
|**cloudFunction** | [**CloudFunctionInfo**](CloudFunctionInfo.md) |  |  [optional] |
|**cloudRunRevision** | [**CloudRunRevisionInfo**](CloudRunRevisionInfo.md) |  |  [optional] |
|**cloudSqlInstance** | [**CloudSQLInstanceInfo**](CloudSQLInstanceInfo.md) |  |  [optional] |
|**deliver** | [**DeliverInfo**](DeliverInfo.md) |  |  [optional] |
|**description** | **String** | A description of the step. Usually this is a summary of the state. |  [optional] |
|**drop** | [**DropInfo**](DropInfo.md) |  |  [optional] |
|**endpoint** | [**EndpointInfo**](EndpointInfo.md) |  |  [optional] |
|**firewall** | [**FirewallInfo**](FirewallInfo.md) |  |  [optional] |
|**forward** | [**ForwardInfo**](ForwardInfo.md) |  |  [optional] |
|**forwardingRule** | [**ForwardingRuleInfo**](ForwardingRuleInfo.md) |  |  [optional] |
|**gkeMaster** | [**GKEMasterInfo**](GKEMasterInfo.md) |  |  [optional] |
|**googleService** | [**GoogleServiceInfo**](GoogleServiceInfo.md) |  |  [optional] |
|**instance** | [**InstanceInfo**](InstanceInfo.md) |  |  [optional] |
|**loadBalancer** | [**LoadBalancerInfo**](LoadBalancerInfo.md) |  |  [optional] |
|**loadBalancerBackendInfo** | [**LoadBalancerBackendInfo**](LoadBalancerBackendInfo.md) |  |  [optional] |
|**nat** | [**NatInfo**](NatInfo.md) |  |  [optional] |
|**network** | [**NetworkInfo**](NetworkInfo.md) |  |  [optional] |
|**projectId** | **String** | Project ID that contains the configuration this step is validating. |  [optional] |
|**proxyConnection** | [**ProxyConnectionInfo**](ProxyConnectionInfo.md) |  |  [optional] |
|**route** | [**RouteInfo**](RouteInfo.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Each step is in one of the pre-defined states. |  [optional] |
|**storageBucket** | [**StorageBucketInfo**](StorageBucketInfo.md) |  |  [optional] |
|**vpcConnector** | [**VpcConnectorInfo**](VpcConnectorInfo.md) |  |  [optional] |
|**vpnGateway** | [**VpnGatewayInfo**](VpnGatewayInfo.md) |  |  [optional] |
|**vpnTunnel** | [**VpnTunnelInfo**](VpnTunnelInfo.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| START_FROM_INSTANCE | &quot;START_FROM_INSTANCE&quot; |
| START_FROM_INTERNET | &quot;START_FROM_INTERNET&quot; |
| START_FROM_GOOGLE_SERVICE | &quot;START_FROM_GOOGLE_SERVICE&quot; |
| START_FROM_PRIVATE_NETWORK | &quot;START_FROM_PRIVATE_NETWORK&quot; |
| START_FROM_GKE_MASTER | &quot;START_FROM_GKE_MASTER&quot; |
| START_FROM_CLOUD_SQL_INSTANCE | &quot;START_FROM_CLOUD_SQL_INSTANCE&quot; |
| START_FROM_CLOUD_FUNCTION | &quot;START_FROM_CLOUD_FUNCTION&quot; |
| START_FROM_APP_ENGINE_VERSION | &quot;START_FROM_APP_ENGINE_VERSION&quot; |
| START_FROM_CLOUD_RUN_REVISION | &quot;START_FROM_CLOUD_RUN_REVISION&quot; |
| START_FROM_STORAGE_BUCKET | &quot;START_FROM_STORAGE_BUCKET&quot; |
| START_FROM_PSC_PUBLISHED_SERVICE | &quot;START_FROM_PSC_PUBLISHED_SERVICE&quot; |
| APPLY_INGRESS_FIREWALL_RULE | &quot;APPLY_INGRESS_FIREWALL_RULE&quot; |
| APPLY_EGRESS_FIREWALL_RULE | &quot;APPLY_EGRESS_FIREWALL_RULE&quot; |
| APPLY_ROUTE | &quot;APPLY_ROUTE&quot; |
| APPLY_FORWARDING_RULE | &quot;APPLY_FORWARDING_RULE&quot; |
| ANALYZE_LOAD_BALANCER_BACKEND | &quot;ANALYZE_LOAD_BALANCER_BACKEND&quot; |
| SPOOFING_APPROVED | &quot;SPOOFING_APPROVED&quot; |
| ARRIVE_AT_INSTANCE | &quot;ARRIVE_AT_INSTANCE&quot; |
| ARRIVE_AT_INTERNAL_LOAD_BALANCER | &quot;ARRIVE_AT_INTERNAL_LOAD_BALANCER&quot; |
| ARRIVE_AT_EXTERNAL_LOAD_BALANCER | &quot;ARRIVE_AT_EXTERNAL_LOAD_BALANCER&quot; |
| ARRIVE_AT_VPN_GATEWAY | &quot;ARRIVE_AT_VPN_GATEWAY&quot; |
| ARRIVE_AT_VPN_TUNNEL | &quot;ARRIVE_AT_VPN_TUNNEL&quot; |
| ARRIVE_AT_VPC_CONNECTOR | &quot;ARRIVE_AT_VPC_CONNECTOR&quot; |
| NAT | &quot;NAT&quot; |
| PROXY_CONNECTION | &quot;PROXY_CONNECTION&quot; |
| DELIVER | &quot;DELIVER&quot; |
| DROP | &quot;DROP&quot; |
| FORWARD | &quot;FORWARD&quot; |
| ABORT | &quot;ABORT&quot; |
| VIEWER_PERMISSION_MISSING | &quot;VIEWER_PERMISSION_MISSING&quot; |



