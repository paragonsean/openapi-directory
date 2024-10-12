

# GoogleCloudApigeeV1ReportInstanceStatusRequest

Request for ReportInstanceStatus.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceUid** | **String** | A unique ID for the instance which is guaranteed to be unique in case the user installs multiple hybrid runtimes with the same instance ID. |  [optional] |
|**reportTime** | **String** | The time the report was generated in the runtime. Used to prevent an old status from overwriting a newer one. An instance should space out it&#39;s status reports so that clock skew does not play a factor. |  [optional] |
|**resources** | [**List&lt;GoogleCloudApigeeV1ResourceStatus&gt;**](GoogleCloudApigeeV1ResourceStatus.md) | Status for config resources |  [optional] |



