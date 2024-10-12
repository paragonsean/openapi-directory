

# SqlIpConfig

IP Management configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedNetworks** | [**List&lt;SqlAclEntry&gt;**](SqlAclEntry.md) | The list of external networks that are allowed to connect to the instance using the IP. See https://en.wikipedia.org/wiki/CIDR_notation#CIDR_notation, also known as &#39;slash&#39; notation (e.g. &#x60;192.168.100.0/24&#x60;). |  [optional] |
|**enableIpv4** | **Boolean** | Whether the instance is assigned a public IP address or not. |  [optional] |
|**privateNetwork** | **String** | The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, &#x60;/projects/myProject/global/networks/default&#x60;. This setting can be updated, but it cannot be removed after it is set. |  [optional] |
|**requireSsl** | **Boolean** | Whether SSL connections over IP should be enforced or not. |  [optional] |



