

# CreateOrganizationActionBatch201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;CreateOrganizationActionBatch201ResponseActionsInner&gt;**](CreateOrganizationActionBatch201ResponseActionsInner.md) | A set of changes made as part of this action (&lt;a href&#x3D;&#39;https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/&#39;&gt;more details&lt;/a&gt;) |  |
|**confirmed** | **Boolean** | Flag describing whether the action should be previewed before executing or not |  [optional] |
|**id** | **String** | ID of the action batch. Can be used to check the status of the action batch at /organizations/{organizationId}/actionBatches/{actionBatchId} |  [optional] |
|**organizationId** | **String** | ID of the organization this action batch belongs to |  [optional] |
|**status** | [**CreateOrganizationActionBatch201ResponseStatus**](CreateOrganizationActionBatch201ResponseStatus.md) |  |  [optional] |
|**synchronous** | **Boolean** | Flag describing whether actions should run synchronously or asynchronously |  [optional] |



