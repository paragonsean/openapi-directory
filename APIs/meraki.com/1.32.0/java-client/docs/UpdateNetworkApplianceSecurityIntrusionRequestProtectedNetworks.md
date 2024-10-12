

# UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks

Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in 'passthrough' mode

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludedCidr** | **List&lt;String&gt;** | list of IP addresses or subnets being excluded from protection (required if &#39;useDefault&#39; is false) |  [optional] |
|**includedCidr** | **List&lt;String&gt;** | list of IP addresses or subnets being protected (required if &#39;useDefault&#39; is false) |  [optional] |
|**useDefault** | **Boolean** | true/false whether to use special IPv4 addresses: https://tools.ietf.org/html/rfc5735 (required). Default value is true if none currently saved |  [optional] |



