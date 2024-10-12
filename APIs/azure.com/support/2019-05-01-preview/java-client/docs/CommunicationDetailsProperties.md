

# CommunicationDetailsProperties

Describes the properties of a communication resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body of the communication |  |
|**communicationDirection** | [**CommunicationDirectionEnum**](#CommunicationDirectionEnum) | Direction of communication |  [optional] [readonly] |
|**communicationType** | [**CommunicationTypeEnum**](#CommunicationTypeEnum) | Communication type |  [optional] [readonly] |
|**createdDate** | **OffsetDateTime** | Time in UTC (ISO 8601 format) when the communication was created. |  [optional] [readonly] |
|**sender** | **String** | Email address of the sender |  [optional] |
|**subject** | **String** | Subject of the communication |  |



## Enum: CommunicationDirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



## Enum: CommunicationTypeEnum

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| PHONE | &quot;phone&quot; |



