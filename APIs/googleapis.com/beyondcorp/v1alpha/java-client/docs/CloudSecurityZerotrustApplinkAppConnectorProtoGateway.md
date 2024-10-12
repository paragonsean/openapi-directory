

# CloudSecurityZerotrustApplinkAppConnectorProtoGateway

Gateway represents a GCE VM Instance endpoint for use by IAP TCP.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_interface** | **String** | interface specifies the network interface of the gateway to connect to. |  [optional] |
|**name** | **String** | name is the name of an instance running a gateway. It is the unique ID for a gateway. All gateways under the same connection have the same prefix. It is derived from the gateway URL. For example, name&#x3D;${instance} assuming a gateway URL. https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance} |  [optional] |
|**port** | **Integer** | port specifies the port of the gateway for tunnel connections from the connectors. |  [optional] |
|**project** | **String** | project is the tenant project the gateway belongs to. Different from the project in the connection, it is a BeyondCorpAPI internally created project to manage all the gateways. It is sharing the same network with the consumer project user owned. It is derived from the gateway URL. For example, project&#x3D;${project} assuming a gateway URL. https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance} |  [optional] |
|**selfLink** | **String** | self_link is the gateway URL in the form https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance} |  [optional] |
|**zone** | **String** | zone represents the zone the instance belongs. It is derived from the gateway URL. For example, zone&#x3D;${zone} assuming a gateway URL. https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance} |  [optional] |



