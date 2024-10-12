# ApigeeApi.GoogleCloudApigeeV1EnvironmentGroupConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointChainingRules** | [**[GoogleCloudApigeeV1EndpointChainingRule]**](GoogleCloudApigeeV1EndpointChainingRule.md) | A list of proxies in each deployment group for proxy chaining calls. | [optional] 
**hostnames** | **[String]** | Host names for the environment group. | [optional] 
**location** | **String** | When this message appears in the top-level IngressConfig, this field will be populated in lieu of the inlined routing_rules and hostnames fields. Some URL for downloading the full EnvironmentGroupConfig for this group. | [optional] 
**name** | **String** | Name of the environment group in the following format: &#x60;organizations/{org}/envgroups/{envgroup}&#x60;. | [optional] 
**revisionId** | **String** | Revision id that defines the ordering of the EnvironmentGroupConfig resource. The higher the revision, the more recently the configuration was deployed. | [optional] 
**routingRules** | [**[GoogleCloudApigeeV1RoutingRule]**](GoogleCloudApigeeV1RoutingRule.md) | Ordered list of routing rules defining how traffic to this environment group&#39;s hostnames should be routed to different environments. | [optional] 
**uid** | **String** | A unique id for the environment group config that will only change if the environment group is deleted and recreated. | [optional] 


