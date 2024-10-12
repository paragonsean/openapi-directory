# KustoManagementClient.EventHubConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerGroup** | **String** | The event hub consumer group. | 
**dataFormat** | **String** | The data format of the message. Optionally the data format can be added to each message. | [optional] 
**eventHubResourceId** | **String** | The resource ID of the event hub to be used to create a data connection. | 
**mappingRuleName** | **String** | The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message. | [optional] 
**tableName** | **String** | The table where the data should be ingested. Optionally the table information can be added to each message. | [optional] 



## Enum: DataFormatEnum


* `MULTIJSON` (value: `"MULTIJSON"`)

* `JSON` (value: `"JSON"`)

* `CSV` (value: `"CSV"`)




