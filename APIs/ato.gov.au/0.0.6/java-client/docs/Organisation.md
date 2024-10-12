

# Organisation

The Organisation resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;OrganisationAddress&gt;**](OrganisationAddress.md) |  |  [optional] |
|**electronicAddresses** | [**List&lt;ElectronicAddress&gt;**](ElectronicAddress.md) |  |  [optional] |
|**establishmentDate** | **LocalDate** | The organisation&#39;s establishment date, for example, &#x60;1928-03-03&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format). |  |
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**id** | [**PartyId**](PartyId.md) | The party&#39;s unique identifier. |  [optional] [readonly] |
|**legalEntityType** | [**LegalEntityTypeEnum**](#LegalEntityTypeEnum) | The organisation&#39;s legal entity type. |  |
|**names** | [**List&lt;OrganisationName&gt;**](OrganisationName.md) |  |  [optional] |
|**registeredIdentifiers** | [**List&lt;RegisteredIdentifier&gt;**](RegisteredIdentifier.md) |  |  [optional] |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: LegalEntityTypeEnum

| Name | Value |
|---- | -----|
| COMPANY | &quot;Company&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| TRUST | &quot;Trust&quot; |
| JOINT_VENTURE | &quot;Joint Venture&quot; |



