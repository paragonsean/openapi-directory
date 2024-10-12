

# EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard

An answer card for a list of people that are related to the subject of the query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disambiguationInfo** | [**EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo**](EnterpriseTopazSidekickPeopleAnswerDisambiguationInfo.md) |  |  [optional] |
|**header** | [**EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader**](EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeader.md) |  |  [optional] |
|**relatedPeople** | [**List&lt;EnterpriseTopazSidekickCommonPerson&gt;**](EnterpriseTopazSidekickCommonPerson.md) | A list of people that are related to the query subject. |  [optional] |
|**relationType** | [**RelationTypeEnum**](#RelationTypeEnum) | Defines the type of relation the list of people have with the subject of the card. |  [optional] |
|**responseStatus** | [**ResponseStatusEnum**](#ResponseStatusEnum) | The response status. |  [optional] |
|**statusMessage** | **String** | Localized user friendly message to display to the user in the case of missing data or an error. |  [optional] |
|**subject** | [**EnterpriseTopazSidekickCommonPerson**](EnterpriseTopazSidekickCommonPerson.md) |  |  [optional] |



## Enum: RelationTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| DIRECT_REPORTS | &quot;DIRECT_REPORTS&quot; |
| MANAGER | &quot;MANAGER&quot; |
| PEERS | &quot;PEERS&quot; |



## Enum: ResponseStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| MISSING_PERSON | &quot;MISSING_PERSON&quot; |
| MISSING_DATA | &quot;MISSING_DATA&quot; |



