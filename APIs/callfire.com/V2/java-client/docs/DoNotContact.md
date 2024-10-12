

# DoNotContact

Represents an opted out contact

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**call** | **Boolean** | A number on Do-Not-Call list |  [optional] |
|**campaignId** | **Long** | An Id of a campaign which was used to send a message to DNC number |  [optional] [readonly] |
|**created** | **Long** | A time when a given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**inboundCall** | **Boolean** | ~ |  [optional] |
|**inboundText** | **Boolean** | ~ |  [optional] |
|**number** | **String** | A single DNC number in E.164 format (11-digit). Example: 12132000384 |  [optional] |
|**source** | **String** | The name of DNC source (can be the name of DNC list that user uploads to CallFire) |  [optional] |
|**text** | **Boolean** | A number on Do-Not-Text list |  [optional] |



