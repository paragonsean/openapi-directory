

# Attributes25

The properties of the Schema Response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateCreated** | **Integer** | The date the Schema Response was created |  [optional] |
|**dateModified** | **Integer** | The date the Schema Response was most recently changed. |  [optional] |
|**dateSubmitted** | **Integer** | The date the Schema Response was submitted for approval. |  [optional] |
|**isOriginalResponse** | **Boolean** | A bool that represents whether the Schema Response is the original one that was made when the registration was created. |  [optional] |
|**isPendingCurrentUserApproval** | **Boolean** | A bool that represents whether the Schema Response needs the current user to approve the state transition. |  [optional] |
|**reviewsState** | [**ReviewsStateEnum**](#ReviewsStateEnum) | A string that represents Schema Response state. &#x60;initial&#x60; is the state of a Schema Response on a newly registered Registration, to edit a Schema Response you must create a Schema Response Action that triggers a new submission. |  [optional] |
|**revisionJustification** | **String** | A user provided string representing the reason a new Schema Response was needed. |  [optional] |
|**revisionResponses** | **List&lt;Object&gt;** | A dictionary object representing responses to to the revision where the key is the block key for that the response. For example in the registration response &#x60;{\&quot;q1\&quot;: \&quot;Answer 1\&quot;}&#x60; the block key is &#x60;q1&#x60;.. |  [optional] |
|**updatedResponseKeys** | **List&lt;Object&gt;** | A list of strings which the response keys for Registration Response Blocks that were updated from the previous schema. |  [optional] [readonly] |



## Enum: ReviewsStateEnum

| Name | Value |
|---- | -----|
| INITIAL | &quot;initial&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| APPROVED | &quot;approved&quot; |
| PENDING_MODERATION | &quot;pending_moderation&quot; |



