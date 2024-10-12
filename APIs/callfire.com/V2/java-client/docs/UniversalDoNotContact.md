

# UniversalDoNotContact

Represents a Universal (platform-wide) Do-Not-Contact object for a given phone number. Shows whether inbound/outbound actions are allowed for a given number.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromNumber** | **String** | Optional source number in E.164 format (11-digit). Example: 12132000384 |  [optional] |
|**inboundCall** | **Boolean** | If toNumber can receive calls or If toNumber can call fromNumber. |  [optional] |
|**inboundText** | **Boolean** | If toNumber can receive texts or If toNumber can text fromNumber. |  [optional] |
|**outboundCall** | **Boolean** | If toNumber can send calls or If fromNumber can call toNumber. |  [optional] |
|**outboundText** | **Boolean** | If toNumber can send texts or If fromNumber can text toNumber. |  [optional] |
|**toNumber** | **String** | destination DNC number in E.164 format (11-digit). Example: 12132000384 |  [optional] |



