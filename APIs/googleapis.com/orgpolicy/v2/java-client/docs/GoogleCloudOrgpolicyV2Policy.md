

# GoogleCloudOrgpolicyV2Policy

Defines an organization policy which is used to specify constraints for configurations of Google Cloud resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternate** | [**GoogleCloudOrgpolicyV2AlternatePolicySpec**](GoogleCloudOrgpolicyV2AlternatePolicySpec.md) |  |  [optional] |
|**dryRunSpec** | [**GoogleCloudOrgpolicyV2PolicySpec**](GoogleCloudOrgpolicyV2PolicySpec.md) |  |  [optional] |
|**etag** | **String** | Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This &#39;etag&#39; is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**name** | **String** | Immutable. The resource name of the policy. Must be one of the following forms, where &#x60;constraint_name&#x60; is the name of the constraint which this policy configures: * &#x60;projects/{project_number}/policies/{constraint_name}&#x60; * &#x60;folders/{folder_id}/policies/{constraint_name}&#x60; * &#x60;organizations/{organization_id}/policies/{constraint_name}&#x60; For example, &#x60;projects/123/policies/compute.disableSerialPortAccess&#x60;. Note: &#x60;projects/{project_id}/policies/{constraint_name}&#x60; is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |  [optional] |
|**spec** | [**GoogleCloudOrgpolicyV2PolicySpec**](GoogleCloudOrgpolicyV2PolicySpec.md) |  |  [optional] |



