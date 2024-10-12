# AndroidDeviceProvisioningPartnerApi.FindDevicesByOwnerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerId** | **[String]** | The list of customer IDs to search for. | [optional] 
**googleWorkspaceCustomerId** | **[String]** | The list of IDs of Google Workspace accounts to search for. | [optional] 
**limit** | **String** | Required. The maximum number of devices to show in a page of results. Must be between 1 and 100 inclusive. | [optional] 
**pageToken** | **String** | A token specifying which result page to return. | [optional] 
**sectionType** | **String** | Required. The section type of the device&#39;s provisioning record. | [optional] 



## Enum: SectionTypeEnum


* `UNSPECIFIED` (value: `"SECTION_TYPE_UNSPECIFIED"`)

* `SIM_LOCK` (value: `"SECTION_TYPE_SIM_LOCK"`)

* `ZERO_TOUCH` (value: `"SECTION_TYPE_ZERO_TOUCH"`)




