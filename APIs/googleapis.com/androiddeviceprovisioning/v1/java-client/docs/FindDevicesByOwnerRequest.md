

# FindDevicesByOwnerRequest

Request to find devices by customers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **List&lt;String&gt;** | The list of customer IDs to search for. |  [optional] |
|**googleWorkspaceCustomerId** | **List&lt;String&gt;** | The list of IDs of Google Workspace accounts to search for. |  [optional] |
|**limit** | **String** | Required. The maximum number of devices to show in a page of results. Must be between 1 and 100 inclusive. |  [optional] |
|**pageToken** | **String** | A token specifying which result page to return. |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | Required. The section type of the device&#39;s provisioning record. |  [optional] |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| SIM_LOCK | &quot;SECTION_TYPE_SIM_LOCK&quot; |
| ZERO_TOUCH | &quot;SECTION_TYPE_ZERO_TOUCH&quot; |



