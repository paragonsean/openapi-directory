

# ResourceManagerTags

A map of resource manager tag keys and values to be attached to the nodes for managing Compute Engine firewalls using Network Firewall Policies. Tags must be according to specifications in https://cloud.google.com/vpc/docs/tags-firewalls-overview#specifications. A maximum of 5 tag key-value pairs can be specified. Existing tags will be replaced with new values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tags** | **Map&lt;String, String&gt;** | Tags must be in one of the following formats ([KEY]&#x3D;[VALUE]) 1. &#x60;tagKeys/{tag_key_id}&#x3D;tagValues/{tag_value_id}&#x60; 2. &#x60;{org_id}/{tag_key_name}&#x3D;{tag_value_name}&#x60; 3. &#x60;{project_id}/{tag_key_name}&#x3D;{tag_value_name}&#x60; |  [optional] |



