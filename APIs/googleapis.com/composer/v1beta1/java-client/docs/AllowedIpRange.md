

# AllowedIpRange

Allowed IP range with user-provided description.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. User-provided description. It must contain at most 300 characters. |  [optional] |
|**value** | **String** | IP address or range, defined using CIDR notation, of requests that this rule applies to. Examples: &#x60;192.168.1.1&#x60; or &#x60;192.168.0.0/16&#x60; or &#x60;2001:db8::/32&#x60; or &#x60;2001:0db8:0000:0042:0000:8a2e:0370:7334&#x60;. IP range prefixes should be properly truncated. For example, &#x60;1.2.3.4/24&#x60; should be truncated to &#x60;1.2.3.0/24&#x60;. Similarly, for IPv6, &#x60;2001:db8::1/32&#x60; should be truncated to &#x60;2001:db8::/32&#x60;. |  [optional] |



