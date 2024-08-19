

# Individual

The Individual resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;IndividualAddress&gt;**](IndividualAddress.md) |  |  [optional] |
|**dateOfBirth** | **LocalDate** | The individual&#39;s date of birth, for example, &#x60;1979-01-13&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format). |  |
|**electronicAddresses** | [**List&lt;ElectronicAddress&gt;**](ElectronicAddress.md) |  |  [optional] |
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**gender** | [**GenderEnum**](#GenderEnum) | The individual&#39;s gender. |  [optional] |
|**id** | [**PartyId**](PartyId.md) | The party&#39;s unique identifier. |  [optional] [readonly] |
|**names** | [**List&lt;IndividualName&gt;**](IndividualName.md) |  |  [optional] |
|**placeOfBirth** | **String** | The individual&#39;s place of birth, for example, &#x60;Tamworth&#x60;. |  |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| FEMALE | &quot;Female&quot; |
| MALE | &quot;Male&quot; |
| NOT_APPLICABLE | &quot;Not Applicable&quot; |
| NOT_KNOWN | &quot;Not Known&quot; |



