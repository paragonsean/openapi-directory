

# SqlIpConfig

IP Management configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocatedIpRange** | **String** | Optional. The name of the allocated IP address range for the private IP Cloud SQL instance. This name refers to an already allocated IP range address. If set, the instance IP address will be created in the allocated range. Note that this IP address range can&#39;t be modified after the instance is created. If you change the VPC when configuring connectivity settings for the migration job, this field is not relevant. |  [optional] |
|**authorizedNetworks** | [**List&lt;SqlAclEntry&gt;**](SqlAclEntry.md) | The list of external networks that are allowed to connect to the instance using the IP. See https://en.wikipedia.org/wiki/CIDR_notation#CIDR_notation, also known as &#39;slash&#39; notation (e.g. &#x60;192.168.100.0/24&#x60;). |  [optional] |
|**enableIpv4** | **Boolean** | Whether the instance should be assigned an IPv4 address or not. |  [optional] |
|**privateNetwork** | **String** | The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, &#x60;projects/myProject/global/networks/default&#x60;. This setting can be updated, but it cannot be removed after it is set. |  [optional] |
|**requireSsl** | **Boolean** | Whether SSL connections over IP should be enforced or not. |  [optional] |



