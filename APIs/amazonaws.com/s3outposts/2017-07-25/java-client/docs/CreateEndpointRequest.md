

# CreateEndpointRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outpostId** | **String** | The ID of the Outposts.  |  |
|**subnetId** | **String** | The ID of the subnet in the selected VPC. The endpoint subnet must belong to the Outpost that has Amazon S3 on Outposts provisioned. |  |
|**securityGroupId** | **String** | The ID of the security group to use with the endpoint. |  |
|**accessType** | [**AccessTypeEnum**](#AccessTypeEnum) | &lt;p&gt;The type of access for the network connectivity for the Amazon S3 on Outposts endpoint. To use the Amazon Web Services VPC, choose &lt;code&gt;Private&lt;/code&gt;. To use the endpoint with an on-premises network, choose &lt;code&gt;CustomerOwnedIp&lt;/code&gt;. If you choose &lt;code&gt;CustomerOwnedIp&lt;/code&gt;, you must also provide the customer-owned IP address pool (CoIP pool).&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;Private&lt;/code&gt; is the default access type value.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**customerOwnedIpv4Pool** | **String** | The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses are allocated from this pool for the endpoint. |  [optional] |



## Enum: AccessTypeEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;Private&quot; |
| CUSTOMER_OWNED_IP | &quot;CustomerOwnedIp&quot; |



