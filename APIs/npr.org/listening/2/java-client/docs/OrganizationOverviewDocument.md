

# OrganizationOverviewDocument

a variety of details about an organization including various lists of recent audio items

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**OrganizationOverviewData**](OrganizationOverviewData.md) |  |  |
|**errors** | **List&lt;Object&gt;** | A list of encountered errors, ignored on POST, PUT |  |
|**href** | **String** | A URL representation of the resource; should generally be ignored by clients unless noted otherwise |  |
|**items** | [**List&lt;OrganizationCategoryAudioListDocument&gt;**](OrganizationCategoryAudioListDocument.md) | A list of separate documents which each include their own list of audio |  |
|**links** | [**OrganizationOverviewLinks**](OrganizationOverviewLinks.md) |  |  |
|**version** | **String** | The version of the Collection.Doc+JSON spec being used |  |



