

# NetworkAccessConfiguration

<p>The configuration settings for in-bound network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization are still required.</p> <p>Access is granted to a caller that is in either the IP address list or the VPC endpoint list - they do not need to be in both.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints are allowed. Standard Grafana authentication and authorization are still required.</p> <note> <p>While both <code>prefixListIds</code> and <code>vpceIds</code> are required, you can pass in an empty array of strings for either parameter if you do not want to allow any of that type.</p> <p>If both are passed as empty arrays, no traffic is allowed to the workspace, because only <i>explicitly</i> allowed connections are accepted.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**prefixListIds** | [**List**](List.md) |  |  |
|**vpceIds** | [**List**](List.md) |  |  |



