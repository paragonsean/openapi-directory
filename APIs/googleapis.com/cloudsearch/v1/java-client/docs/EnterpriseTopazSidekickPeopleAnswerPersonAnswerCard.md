

# EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard

An answer card for a single person.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answer** | [**List&lt;SafeHtmlProto&gt;**](SafeHtmlProto.md) | List of answers. |  [optional] |
|**answerText** | [**EnterpriseTopazSidekickAnswerAnswerList**](EnterpriseTopazSidekickAnswerAnswerList.md) |  |  [optional] |
|**disambiguationInfo** | [**EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo**](EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo.md) |  |  [optional] |
|**header** | [**EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader**](EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader.md) |  |  [optional] |
|**responseStatus** | [**ResponseStatusEnum**](#ResponseStatusEnum) | The response status. |  [optional] |
|**statusMessage** | **String** | Localized user friendly message to display to the user in the case of missing data or an error. |  [optional] |
|**subject** | [**EnterpriseTopazSidekickCommonPerson**](EnterpriseTopazSidekickCommonPerson.md) |  |  [optional] |



## Enum: ResponseStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| MISSING_PERSON | &quot;MISSING_PERSON&quot; |
| MISSING_DATA | &quot;MISSING_DATA&quot; |



