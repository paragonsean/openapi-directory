# CloudRunAdminApi.GoogleCloudRunV2VpcAccess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector** | **String** | VPC Access connector name. Format: projects/{project}/locations/{location}/connectors/{connector}, where {project} can be project id or number. For more information on sending traffic to a VPC network via a connector, visit https://cloud.google.com/run/docs/configuring/vpc-connectors. | [optional] 
**egress** | **String** | Traffic VPC egress settings. If not provided, it defaults to PRIVATE_RANGES_ONLY. | [optional] 
**networkInterfaces** | [**[GoogleCloudRunV2NetworkInterface]**](GoogleCloudRunV2NetworkInterface.md) | Direct VPC egress settings. Currently only single network interface is supported. | [optional] 



## Enum: EgressEnum


* `VPC_EGRESS_UNSPECIFIED` (value: `"VPC_EGRESS_UNSPECIFIED"`)

* `ALL_TRAFFIC` (value: `"ALL_TRAFFIC"`)

* `PRIVATE_RANGES_ONLY` (value: `"PRIVATE_RANGES_ONLY"`)




