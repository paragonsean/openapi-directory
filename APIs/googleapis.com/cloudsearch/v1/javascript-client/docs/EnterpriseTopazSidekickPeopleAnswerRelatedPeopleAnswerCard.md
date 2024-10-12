# CloudSearchApi.EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disambiguationInfo** | [**EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo**](EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo.md) |  | [optional] 
**header** | [**EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader**](EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader.md) |  | [optional] 
**relatedPeople** | [**[EnterpriseTopazSidekickCommonPerson]**](EnterpriseTopazSidekickCommonPerson.md) | A list of people that are related to the query subject. | [optional] 
**relationType** | **String** | Defines the type of relation the list of people have with the subject of the card. | [optional] 
**responseStatus** | **String** | The response status. | [optional] 
**statusMessage** | **String** | Localized user friendly message to display to the user in the case of missing data or an error. | [optional] 
**subject** | [**EnterpriseTopazSidekickCommonPerson**](EnterpriseTopazSidekickCommonPerson.md) |  | [optional] 



## Enum: RelationTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `DIRECT_REPORTS` (value: `"DIRECT_REPORTS"`)

* `MANAGER` (value: `"MANAGER"`)

* `PEERS` (value: `"PEERS"`)





## Enum: ResponseStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `MISSING_PERSON` (value: `"MISSING_PERSON"`)

* `MISSING_DATA` (value: `"MISSING_DATA"`)




