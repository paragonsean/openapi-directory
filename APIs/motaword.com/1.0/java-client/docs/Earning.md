

# Earning


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Float** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**dueDate** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**words** | **Long** |  |  [optional] |
|**wordsApproved** | **Long** |  |  [optional] |
|**wordsTranslated** | **Long** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PAID | &quot;paid&quot; |
| PENDING | &quot;pending&quot; |
| FAILED | &quot;failed&quot; |



