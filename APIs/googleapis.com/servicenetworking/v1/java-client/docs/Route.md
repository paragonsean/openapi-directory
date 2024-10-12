

# Route

Represents a route that was created or discovered by a private access management service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destRange** | **String** | Destination CIDR range that this route applies to. |  [optional] |
|**name** | **String** | Route name. See https://cloud.google.com/vpc/docs/routes |  [optional] |
|**network** | **String** | Fully-qualified URL of the VPC network in the producer host tenant project that this route applies to. For example: &#x60;projects/123456/global/networks/host-network&#x60; |  [optional] |
|**nextHopGateway** | **String** | Fully-qualified URL of the gateway that should handle matching packets that this route applies to. For example: &#x60;projects/123456/global/gateways/default-internet-gateway&#x60; |  [optional] |



