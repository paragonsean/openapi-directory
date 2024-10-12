

# CreateOrganizationActionBatch201ResponseStatus

Status of action batch

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completed** | **Boolean** | Flag describing whether all actions in the action batch have completed |  [optional] |
|**createdResources** | [**List&lt;CreateOrganizationActionBatch201ResponseStatusCreatedResourcesInner&gt;**](CreateOrganizationActionBatch201ResponseStatusCreatedResourcesInner.md) | Resources created as a result of this action batch |  |
|**errors** | **List&lt;String&gt;** | List of errors encountered when running actions in the action batch |  [optional] |
|**failed** | **Boolean** | Flag describing whether any actions in the action batch failed |  [optional] |



