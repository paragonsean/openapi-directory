

# CustomerPersonDTO

CustomerPerson

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** |  |  [optional] |
|**contact** | [**PersonContactDTO**](PersonContactDTO.md) |  |  [optional] |
|**customFields** |  |  |  [optional] |
|**customerId** | **Long** |  |  [optional] |
|**firstProjectDate** | **OffsetDateTime** |  |  [optional] |
|**firstQuoteDate** | **OffsetDateTime** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**lastProjectDate** | **OffsetDateTime** |  |  [optional] |
|**lastQuoteDate** | **OffsetDateTime** |  |  [optional] |
|**motherTonguesIds** | **Set&lt;Long&gt;** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**numberOfProjects** | **Integer** |  |  [optional] |
|**numberOfQuotes** | **Integer** |  |  [optional] |
|**positionId** | **Long** |  |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| FEMALE | &quot;FEMALE&quot; |
| MALE | &quot;MALE&quot; |



