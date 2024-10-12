# BeyondCorpApi.CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationEndpoint** | **String** | application_endpoint is the endpoint of the application the form of host:port. For example, \&quot;localhost:80\&quot;. | [optional] 
**applicationName** | **String** | application_name represents the given name of the application the connection is connecting with. | [optional] 
**gateway** | [**[CloudSecurityZerotrustApplinkAppConnectorProtoGateway]**](CloudSecurityZerotrustApplinkAppConnectorProtoGateway.md) | gateway lists all instances running a gateway in GCP. They all connect to a connector on the host. | [optional] 
**name** | **String** | name is the unique ID for each connection. TODO(b/190732451) returns connection name from user-specified name in config. Now, name &#x3D; ${application_name}:${application_endpoint} | [optional] 
**project** | **String** | project represents the consumer project the connection belongs to. | [optional] 
**tunnelsPerGateway** | **Number** | tunnels_per_gateway reflects the number of tunnels between a connector and a gateway. | [optional] 
**userPort** | **Number** | user_port specifies the reserved port on gateways for user connections. | [optional] 


