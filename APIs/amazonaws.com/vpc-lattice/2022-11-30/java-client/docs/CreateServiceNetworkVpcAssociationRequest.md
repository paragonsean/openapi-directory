

# CreateServiceNetworkVpcAssociationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. |  [optional] |
|**securityGroupIds** | **List&lt;String&gt;** | The IDs of the security groups. Security groups aren&#39;t added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html\&quot;&gt;Control traffic to resources using security groups&lt;/a&gt; in the &lt;i&gt;Amazon VPC User Guide&lt;/i&gt;. |  [optional] |
|**serviceNetworkIdentifier** | **String** | The ID or Amazon Resource Name (ARN) of the service network. You must use the ARN when the resources specified in the operation are in different accounts. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags for the association. |  [optional] |
|**vpcIdentifier** | **String** | The ID of the VPC. |  |



