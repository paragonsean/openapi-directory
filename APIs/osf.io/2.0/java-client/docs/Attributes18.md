

# Attributes18

The properties of the preprint entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateCreated** | **OffsetDateTime** | The time at which the preprint was created, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**dateModified** | **OffsetDateTime** | The time at which the preprint was last modified, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**datePublished** | **OffsetDateTime** | The time at which the preprint was published, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**doi** | **String** | The DOI of the associated journal article, as entered by the user, if the preprint is published. |  [optional] |
|**isPreprintOrphan** | **Boolean** | Whether or not the preprint is orphaned. A preprint can be orphaned if it&#39;s primary file was removed from the preprint node. This field may be deprecated in future versions. |  [optional] [readonly] |
|**licenseRecord** | **String** | The metadata (copyright year and holder) associated with a license, required for certain licenses. |  [optional] |
|**subjects** | **List&lt;String&gt;** | A nested array structure that describe subjects related to the preprint, in the BePress taxonomy. Each dictionary contains the text and ID of a subject. |  [optional] |



