# MotaWordApi.EarningWithTQS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** |  | [optional] 
**currency** | **String** |  | [optional] [default to &#39;usd&#39;]
**dueDate** | **Date** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z | [optional] 
**status** | **String** |  | [optional] 
**words** | **Number** |  | [optional] 
**wordsApproved** | **Number** |  | [optional] 
**wordsTranslated** | **Number** |  | [optional] 
**isAboveAverage** | **Boolean** | Is this score above or below the average among other vendors in the same project? | [optional] 
**score** | **Number** |  | [optional] 
**stringsEdited** | **Number** | The number of translated strings by this translator which was edited by a proofreader. | [optional] 
**stringsTranslated** | **Number** | The number of translated strings by this translator. | [optional] 
**projectId** | **Number** |  | [optional] 



## Enum: StatusEnum


* `paid` (value: `"paid"`)

* `pending` (value: `"pending"`)

* `failed` (value: `"failed"`)




