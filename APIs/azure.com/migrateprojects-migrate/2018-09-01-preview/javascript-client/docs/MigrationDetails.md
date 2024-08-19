# AzureMigrateHub.MigrationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biosId** | **String** | Gets or sets the BIOS ID of the machine. | [optional] 
**enqueueTime** | **String** | Gets or sets the time the message was enqueued. | [optional] 
**extendedInfo** | **{String: String}** | Gets or sets the ISV specific extended information. | [optional] 
**fabricType** | **String** | Gets or sets the fabric type. | [optional] 
**fqdn** | **String** | Gets or sets the FQDN of the machine. | [optional] 
**ipAddresses** | **[String]** | Gets or sets the list of IP addresses of the machine. IP addresses could be IP V4 or IP V6. | [optional] 
**lastUpdatedTime** | **Date** | Gets or sets the time of the last modification of the machine details. | [optional] 
**macAddresses** | **[String]** | Gets or sets the list of MAC addresses of the machine. | [optional] 
**machineId** | **String** | Gets or sets the unique identifier of the machine. | [optional] 
**machineManagerId** | **String** | Gets or sets the unique identifier of the virtual machine manager(vCenter/VMM). | [optional] 
**machineName** | **String** | Gets or sets the name of the machine. | [optional] 
**migrationPhase** | **String** | Gets or sets the phase of migration of the machine. | [optional] 
**migrationTested** | **Boolean** | Gets or sets a value indicating whether migration was tested on the machine. | [optional] 
**replicationProgressPercentage** | **Number** | Gets or sets the progress percentage of migration on the machine. | [optional] 
**solutionName** | **String** | Gets or sets the name of the solution that sent the data. | [optional] 
**targetVMArmId** | **String** | Gets or sets the ARM id the migrated VM. | [optional] 


