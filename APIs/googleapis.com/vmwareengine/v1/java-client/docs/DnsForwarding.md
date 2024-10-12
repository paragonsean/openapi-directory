

# DnsForwarding

DNS forwarding config. This config defines a list of domain to name server mappings, and is attached to the private cloud for custom domain resolution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**forwardingRules** | [**List&lt;ForwardingRule&gt;**](ForwardingRule.md) | Required. List of domain mappings to configure |  [optional] |
|**name** | **String** | Output only. The resource name of this DNS profile. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding&#x60; |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |



