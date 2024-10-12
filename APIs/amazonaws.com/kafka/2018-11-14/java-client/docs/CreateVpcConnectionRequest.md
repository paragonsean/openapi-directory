

# CreateVpcConnectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetClusterArn** | **String** |              &lt;p&gt;The cluster Amazon Resource Name (ARN) for the VPC connection.&lt;/p&gt;           |  |
|**authentication** | **String** |              &lt;p&gt;The authentication type of VPC connection.&lt;/p&gt;           |  |
|**vpcId** | **String** |              &lt;p&gt;The VPC ID of VPC connection.&lt;/p&gt;           |  |
|**clientSubnets** | **List&lt;String&gt;** |              &lt;p&gt;The list of client subnets.&lt;/p&gt;           |  |
|**securityGroups** | **List&lt;String&gt;** |              &lt;p&gt;The list of security groups.&lt;/p&gt;           |  |
|**tags** | **Map&lt;String, String&gt;** |              &lt;p&gt;A map of tags for the VPC connection.&lt;/p&gt;           |  [optional] |



