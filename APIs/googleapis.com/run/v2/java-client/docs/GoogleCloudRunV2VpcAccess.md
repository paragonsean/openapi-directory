

# GoogleCloudRunV2VpcAccess

VPC Access settings. For more information on sending traffic to a VPC network, visit https://cloud.google.com/run/docs/configuring/connecting-vpc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connector** | **String** | VPC Access connector name. Format: projects/{project}/locations/{location}/connectors/{connector}, where {project} can be project id or number. For more information on sending traffic to a VPC network via a connector, visit https://cloud.google.com/run/docs/configuring/vpc-connectors. |  [optional] |
|**egress** | [**EgressEnum**](#EgressEnum) | Traffic VPC egress settings. If not provided, it defaults to PRIVATE_RANGES_ONLY. |  [optional] |
|**networkInterfaces** | [**List&lt;GoogleCloudRunV2NetworkInterface&gt;**](GoogleCloudRunV2NetworkInterface.md) | Direct VPC egress settings. Currently only single network interface is supported. |  [optional] |



## Enum: EgressEnum

| Name | Value |
|---- | -----|
| VPC_EGRESS_UNSPECIFIED | &quot;VPC_EGRESS_UNSPECIFIED&quot; |
| ALL_TRAFFIC | &quot;ALL_TRAFFIC&quot; |
| PRIVATE_RANGES_ONLY | &quot;PRIVATE_RANGES_ONLY&quot; |



