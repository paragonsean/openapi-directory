# KustoManagementClient.IotHubConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerGroup** | **String** | The iot hub consumer group. | 
**dataFormat** | [**DataFormat**](DataFormat.md) |  | [optional] 
**eventSystemProperties** | **[String]** | System properties of the iot hub | [optional] 
**iotHubResourceId** | **String** | The resource ID of the Iot hub to be used to create a data connection. | 
**mappingRuleName** | **String** | The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message. | [optional] 
**sharedAccessPolicyName** | **String** | The name of the share access policy name | 
**tableName** | **String** | The table where the data should be ingested. Optionally the table information can be added to each message. | [optional] 


