

# VpcConfiguration

<p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p> <note> <p>Provided <code>securityGroupIds</code> and <code>subnetIds</code> must be part of the same VPC.</p> <p>Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**securityGroupIds** | [**List**](List.md) |  |  |
|**subnetIds** | [**List**](List.md) |  |  |



