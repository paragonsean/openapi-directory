# KustoManagementClient.EventGridConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerGroup** | **String** | The event hub consumer group. | 
**dataFormat** | [**DataFormat**](DataFormat.md) |  | 
**eventHubResourceId** | **String** | The resource ID where the event grid is configured to send events. | 
**mappingRuleName** | **String** | The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message. | [optional] 
**storageAccountResourceId** | **String** | The resource ID of the storage account where the data resides. | 
**tableName** | **String** | The table where the data should be ingested. Optionally the table information can be added to each message. | 


