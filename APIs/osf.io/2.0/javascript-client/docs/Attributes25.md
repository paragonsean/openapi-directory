# OsfApiv2Documentation.Attributes25

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateCreated** | **Number** | The date the Schema Response was created | [optional] 
**dateModified** | **Number** | The date the Schema Response was most recently changed. | [optional] 
**dateSubmitted** | **Number** | The date the Schema Response was submitted for approval. | [optional] 
**isOriginalResponse** | **Boolean** | A bool that represents whether the Schema Response is the original one that was made when the registration was created. | [optional] 
**isPendingCurrentUserApproval** | **Boolean** | A bool that represents whether the Schema Response needs the current user to approve the state transition. | [optional] 
**reviewsState** | **String** | A string that represents Schema Response state. &#x60;initial&#x60; is the state of a Schema Response on a newly registered Registration, to edit a Schema Response you must create a Schema Response Action that triggers a new submission. | [optional] 
**revisionJustification** | **String** | A user provided string representing the reason a new Schema Response was needed. | [optional] 
**revisionResponses** | **[Object]** | A dictionary object representing responses to to the revision where the key is the block key for that the response. For example in the registration response &#x60;{\&quot;q1\&quot;: \&quot;Answer 1\&quot;}&#x60; the block key is &#x60;q1&#x60;.. | [optional] 
**updatedResponseKeys** | **[Object]** | A list of strings which the response keys for Registration Response Blocks that were updated from the previous schema. | [optional] [readonly] 



## Enum: ReviewsStateEnum


* `initial` (value: `"initial"`)

* `in_progress` (value: `"in_progress"`)

* `approved` (value: `"approved"`)

* `pending_moderation` (value: `"pending_moderation"`)




