# GoogleFormsApi.Option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goToAction** | **String** | Section navigation type. | [optional] 
**goToSectionId** | **String** | Item ID of section header to go to. | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**isOther** | **Boolean** | Whether the option is \&quot;other\&quot;. Currently only applies to &#x60;RADIO&#x60; and &#x60;CHECKBOX&#x60; choice types, but is not allowed in a QuestionGroupItem. | [optional] 
**value** | **String** | Required. The choice as presented to the user. | [optional] 



## Enum: GoToActionEnum


* `GO_TO_ACTION_UNSPECIFIED` (value: `"GO_TO_ACTION_UNSPECIFIED"`)

* `NEXT_SECTION` (value: `"NEXT_SECTION"`)

* `RESTART_FORM` (value: `"RESTART_FORM"`)

* `SUBMIT_FORM` (value: `"SUBMIT_FORM"`)




