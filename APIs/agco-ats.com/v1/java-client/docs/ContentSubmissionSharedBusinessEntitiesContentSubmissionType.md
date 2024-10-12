

# ContentSubmissionSharedBusinessEntitiesContentSubmissionType

A type of content available for submission

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeTemplate** | **String** | A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName} |  [optional] |
|**buildDefinitionID** | **Integer** | The ID of the Azure DevOps Build Definition for which to create a Build. Either &#39;BuildDefinitionID&#39; or &#39;JobID&#39; is required. |  [optional] |
|**categoryTemplate** | **String** | A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName} |  [optional] |
|**description** | **String** | A description for the Content Submission Type |  |
|**enabled** | **Boolean** | Indicates whether this submission type is available to be used |  [optional] |
|**ID** | **Integer** | The ID of the Content Submission Type |  [optional] |
|**inventoryPackageID** | **String** | The ID of the Inventory Package from which to read the version of the package installed. |  [optional] |
|**jobID** | **Integer** | The ID of the JobDefinition for which to initiate a Job. A value of &#39;0&#39; will cause a submission to fail. Either &#39;BuildDefinitionID&#39; or &#39;JobID&#39; is required. |  [optional] |
|**name** | **String** | The Name of the Content Submission Type |  |
|**releaseNotesDescription** | **String** | A description of how release notes for this Content Submission Type are used |  [optional] |



