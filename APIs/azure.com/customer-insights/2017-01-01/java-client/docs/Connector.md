

# Connector

Properties of connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectorId** | **Integer** | ID of the connector. |  [optional] [readonly] |
|**connectorName** | **String** | Name of the connector. |  [optional] |
|**connectorProperties** | **Map&lt;String, Object&gt;** | The connector properties. |  |
|**connectorType** | **ConnectorType** |  |  |
|**created** | **OffsetDateTime** | The created time. |  [optional] [readonly] |
|**description** | **String** | Description of the connector. |  [optional] |
|**displayName** | **String** | Display name of the connector. |  [optional] |
|**isInternal** | **Boolean** | If this is an internal connector. |  [optional] |
|**lastModified** | **OffsetDateTime** | The last modified time. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | State of connector. |  [optional] [readonly] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| CREATED | &quot;Created&quot; |
| READY | &quot;Ready&quot; |
| EXPIRING | &quot;Expiring&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



