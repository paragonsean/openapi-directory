

# GlobalResourcesSharedModelsTranslationRequest

A request to translate specified strings into specified locales

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvalUserId** | **Integer** | The ID of the user from which approval for the request is required |  [optional] |
|**ccEmailAddresses** | **List&lt;String&gt;** | Additional email addresses to CC on emails pertaining to the request |  |
|**chargeToAccount** | **String** | The account to charge for the request |  |
|**deadline** | **OffsetDateTime** | The date by which the translations in the request are needed. Defaults to 30 days from the current date |  |
|**id** | **Integer** | The ID of the request |  [optional] |
|**localeIds** | **List&lt;Integer&gt;** | Locale IDs to which these strings are requested to be translated |  |
|**notes** | **String** | Additional notes or comments about the request |  |
|**questionsUserId** | **Integer** | The ID of the user to which to address questions regarding the request |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the request |  |
|**submittedBy** | **Integer** | The ID of the User that submitted the request |  [optional] |
|**translatorEmail** | **String** | The email address for the translator |  [optional] |
|**translatorName** | **String** | The name of the translator |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NOT_SUBMITTED | &quot;NotSubmitted&quot; |
| SUBMITTED | &quot;Submitted&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |



