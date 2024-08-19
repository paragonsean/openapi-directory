

# RegisteredIdentifier

The Registered Identifier resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**id** | **String** | The resource&#39;s unique identifier. |  [optional] [readonly] |
|**identifier** | **String** | The registered identifier. |  [optional] |
|**identifierType** | [**IdentifierTypeEnum**](#IdentifierTypeEnum) | The registered identifier type. |  [optional] |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: IdentifierTypeEnum

| Name | Value |
|---- | -----|
| ACN | &quot;ACN&quot; |
| ABN | &quot;ABN&quot; |



