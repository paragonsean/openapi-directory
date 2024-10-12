

# GoogleCloudDataplexV1Action

Action represents an issue requiring administrator action for resolution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | **String** | Output only. The relative resource name of the asset, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}. |  [optional] [readonly] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of issue associated with the action. |  [optional] |
|**dataLocations** | **List&lt;String&gt;** | The list of data locations associated with this action. Cloud Storage locations are represented as URI paths(E.g. gs://bucket/table1/year&#x3D;2020/month&#x3D;Jan/). BigQuery locations refer to resource names(E.g. bigquery.googleapis.com/projects/project-id/datasets/dataset-id). |  [optional] |
|**detectTime** | **String** | The time that the issue was detected. |  [optional] |
|**failedSecurityPolicyApply** | [**GoogleCloudDataplexV1ActionFailedSecurityPolicyApply**](GoogleCloudDataplexV1ActionFailedSecurityPolicyApply.md) |  |  [optional] |
|**incompatibleDataSchema** | [**GoogleCloudDataplexV1ActionIncompatibleDataSchema**](GoogleCloudDataplexV1ActionIncompatibleDataSchema.md) |  |  [optional] |
|**invalidDataFormat** | [**GoogleCloudDataplexV1ActionInvalidDataFormat**](GoogleCloudDataplexV1ActionInvalidDataFormat.md) |  |  [optional] |
|**invalidDataOrganization** | **Object** | Action details for invalid data arrangement. |  [optional] |
|**invalidDataPartition** | [**GoogleCloudDataplexV1ActionInvalidDataPartition**](GoogleCloudDataplexV1ActionInvalidDataPartition.md) |  |  [optional] |
|**issue** | **String** | Detailed description of the issue requiring action. |  [optional] |
|**lake** | **String** | Output only. The relative resource name of the lake, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}. |  [optional] [readonly] |
|**missingData** | **Object** | Action details for absence of data detected by discovery. |  [optional] |
|**missingResource** | **Object** | Action details for resource references in assets that cannot be located. |  [optional] |
|**name** | **String** | Output only. The relative resource name of the action, of the form: projects/{project}/locations/{location}/lakes/{lake}/actions/{action} projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/actions/{action} projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/assets/{asset}/actions/{action}. |  [optional] [readonly] |
|**unauthorizedResource** | **Object** | Action details for unauthorized resource issues raised to indicate that the service account associated with the lake instance is not authorized to access or manage the resource associated with an asset. |  [optional] |
|**zone** | **String** | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. |  [optional] [readonly] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CATEGORY_UNSPECIFIED | &quot;CATEGORY_UNSPECIFIED&quot; |
| RESOURCE_MANAGEMENT | &quot;RESOURCE_MANAGEMENT&quot; |
| SECURITY_POLICY | &quot;SECURITY_POLICY&quot; |
| DATA_DISCOVERY | &quot;DATA_DISCOVERY&quot; |



