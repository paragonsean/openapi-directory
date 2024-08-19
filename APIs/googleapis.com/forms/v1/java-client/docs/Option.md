

# Option

An option for a Choice question.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**goToAction** | [**GoToActionEnum**](#GoToActionEnum) | Section navigation type. |  [optional] |
|**goToSectionId** | **String** | Item ID of section header to go to. |  [optional] |
|**image** | [**Image**](Image.md) |  |  [optional] |
|**isOther** | **Boolean** | Whether the option is \&quot;other\&quot;. Currently only applies to &#x60;RADIO&#x60; and &#x60;CHECKBOX&#x60; choice types, but is not allowed in a QuestionGroupItem. |  [optional] |
|**value** | **String** | Required. The choice as presented to the user. |  [optional] |



## Enum: GoToActionEnum

| Name | Value |
|---- | -----|
| GO_TO_ACTION_UNSPECIFIED | &quot;GO_TO_ACTION_UNSPECIFIED&quot; |
| NEXT_SECTION | &quot;NEXT_SECTION&quot; |
| RESTART_FORM | &quot;RESTART_FORM&quot; |
| SUBMIT_FORM | &quot;SUBMIT_FORM&quot; |



