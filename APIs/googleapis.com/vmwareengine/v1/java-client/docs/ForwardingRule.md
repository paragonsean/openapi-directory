

# ForwardingRule

A forwarding rule is a mapping of a `domain` to `name_servers`. This mapping allows VMware Engine to resolve domains for attached private clouds by forwarding DNS requests for a given domain to the specified nameservers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** | Required. Domain used to resolve a &#x60;name_servers&#x60; list. |  [optional] |
|**nameServers** | **List&lt;String&gt;** | Required. List of DNS servers to use for domain resolution |  [optional] |



