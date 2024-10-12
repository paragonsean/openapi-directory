

# DemographicsDependentWithIdModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**birthDate** | **OffsetDateTime** |  |  [optional] |
|**demographicsId** | **Integer** |  |  [optional] |
|**dependentId** | **Integer** |  |  [optional] |
|**dependentOf** | [**DependentOfEnum**](#DependentOfEnum) |  |  [optional] |
|**externalDestinationId** | **String** |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**links** | [**List&lt;ObjectLink&gt;**](ObjectLink.md) |  |  [optional] |
|**relationship** | [**RelationshipEnum**](#RelationshipEnum) |  |  [optional] |



## Enum: DependentOfEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| JOINT | &quot;Joint&quot; |
| OTHER | &quot;Other&quot; |



## Enum: RelationshipEnum

| Name | Value |
|---- | -----|
| SON | &quot;Son&quot; |
| DAUGHTER | &quot;Daughter&quot; |
| FOSTER_SON | &quot;FosterSon&quot; |
| FOSTER_DAUGHTER | &quot;FosterDaughter&quot; |
| GRANDSON | &quot;Grandson&quot; |
| GRANDDAUGHTER | &quot;Granddaughter&quot; |
| NEPHEW | &quot;Nephew&quot; |
| NIECE | &quot;Niece&quot; |
| MALE_COUSIN | &quot;MaleCousin&quot; |
| FEMALE_COUSIN | &quot;FemaleCousin&quot; |
| FATHER | &quot;Father&quot; |
| MOTHER | &quot;Mother&quot; |
| GRANDFATHER | &quot;Grandfather&quot; |
| GRANDMOTHER | &quot;Grandmother&quot; |
| UNCLE | &quot;Uncle&quot; |
| AUNT | &quot;Aunt&quot; |
| BROTHER | &quot;Brother&quot; |
| SISTER | &quot;Sister&quot; |
| SON_IN_LAW | &quot;SonInLaw&quot; |
| DAUGHTER_IN_LAW | &quot;DaughterInLaw&quot; |
| MALE_OTHER | &quot;MaleOther&quot; |
| FEMALE_OTHER | &quot;FemaleOther&quot; |



