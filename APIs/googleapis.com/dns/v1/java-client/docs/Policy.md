

# Policy

A policy is a collection of DNS rules applied to one or more Virtual Private Cloud resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternativeNameServerConfig** | [**PolicyAlternativeNameServerConfig**](PolicyAlternativeNameServerConfig.md) |  |  [optional] |
|**description** | **String** | A mutable string of at most 1024 characters associated with this resource for the user&#39;s convenience. Has no effect on the policy&#39;s function. |  [optional] |
|**enableInboundForwarding** | **Boolean** | Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address is allocated from each of the subnetworks that are bound to this policy. |  [optional] |
|**enableLogging** | **Boolean** | Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set. |  [optional] |
|**id** | **String** | Unique identifier for the resource; defined by the server (output only). |  [optional] |
|**kind** | **String** |  |  [optional] |
|**name** | **String** | User-assigned name for this policy. |  [optional] |
|**networks** | [**List&lt;PolicyNetwork&gt;**](PolicyNetwork.md) | List of network names specifying networks to which this policy is applied. |  [optional] |



