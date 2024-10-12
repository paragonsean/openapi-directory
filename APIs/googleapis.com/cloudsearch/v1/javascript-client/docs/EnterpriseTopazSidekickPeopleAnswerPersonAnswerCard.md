# CloudSearchApi.EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | [**[SafeHtmlProto]**](SafeHtmlProto.md) | List of answers. | [optional] 
**answerText** | [**EnterpriseTopazSidekickAnswerAnswerList**](EnterpriseTopazSidekickAnswerAnswerList.md) |  | [optional] 
**disambiguationInfo** | [**EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo**](EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo.md) |  | [optional] 
**header** | [**EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader**](EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader.md) |  | [optional] 
**responseStatus** | **String** | The response status. | [optional] 
**statusMessage** | **String** | Localized user friendly message to display to the user in the case of missing data or an error. | [optional] 
**subject** | [**EnterpriseTopazSidekickCommonPerson**](EnterpriseTopazSidekickCommonPerson.md) |  | [optional] 



## Enum: ResponseStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `MISSING_PERSON` (value: `"MISSING_PERSON"`)

* `MISSING_DATA` (value: `"MISSING_DATA"`)




