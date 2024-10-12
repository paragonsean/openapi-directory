# CloudLoggingApi.Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryDataset** | [**BigQueryDataset**](BigQueryDataset.md) |  | [optional] 
**createTime** | **String** | Output only. The creation timestamp of the link. | [optional] [readonly] 
**description** | **String** | Optional. Describes this link.The maximum length of the description is 8000 characters. | [optional] 
**lifecycleState** | **String** | Output only. The resource lifecycle state. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the link. The name can have up to 100 characters. A valid link id (at the end of the link name) must only have alphanumeric characters and underscores within it. \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]\&quot; \&quot;organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]\&quot; \&quot;billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]\&quot; \&quot;folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]\&quot; For example:&#x60;projects/my-project/locations/global/buckets/my-bucket/links/my_link | [optional] [readonly] 



## Enum: LifecycleStateEnum


* `LIFECYCLE_STATE_UNSPECIFIED` (value: `"LIFECYCLE_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETE_REQUESTED` (value: `"DELETE_REQUESTED"`)

* `UPDATING` (value: `"UPDATING"`)

* `CREATING` (value: `"CREATING"`)

* `FAILED` (value: `"FAILED"`)




