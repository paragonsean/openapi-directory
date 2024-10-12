# CustomerInsightsManagementClient.Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorId** | **Number** | ID of the connector. | [optional] [readonly] 
**connectorName** | **String** | Name of the connector. | [optional] 
**connectorProperties** | **{String: Object}** | The connector properties. | 
**connectorType** | [**ConnectorType**](ConnectorType.md) |  | 
**created** | **Date** | The created time. | [optional] [readonly] 
**description** | **String** | Description of the connector. | [optional] 
**displayName** | **String** | Display name of the connector. | [optional] 
**isInternal** | **Boolean** | If this is an internal connector. | [optional] 
**lastModified** | **Date** | The last modified time. | [optional] [readonly] 
**state** | **String** | State of connector. | [optional] [readonly] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 



## Enum: StateEnum


* `Creating` (value: `"Creating"`)

* `Created` (value: `"Created"`)

* `Ready` (value: `"Ready"`)

* `Expiring` (value: `"Expiring"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




