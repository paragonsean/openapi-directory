

# Firewall

<p>The firewall defines the configuration settings for an Network Firewall firewall. These settings include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall Amazon Web Services resource. </p> <p>The status of the firewall, for example whether it's ready to filter network traffic, is provided in the corresponding <a>FirewallStatus</a>. You can retrieve both objects by calling <a>DescribeFirewall</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firewallName** | [**String**](String.md) |  |  [optional] |
|**firewallArn** | [**String**](String.md) |  |  [optional] |
|**firewallPolicyArn** | [**String**](String.md) |  |  |
|**vpcId** | [**String**](String.md) |  |  |
|**subnetMappings** | [**List**](List.md) |  |  |
|**deleteProtection** | [**Boolean**](Boolean.md) |  |  [optional] |
|**subnetChangeProtection** | [**Boolean**](Boolean.md) |  |  [optional] |
|**firewallPolicyChangeProtection** | [**Boolean**](Boolean.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**firewallId** | [**String**](String.md) |  |  |
|**tags** | [**List**](List.md) |  |  [optional] |
|**encryptionConfiguration** | [**FirewallEncryptionConfiguration**](FirewallEncryptionConfiguration.md) |  |  [optional] |



