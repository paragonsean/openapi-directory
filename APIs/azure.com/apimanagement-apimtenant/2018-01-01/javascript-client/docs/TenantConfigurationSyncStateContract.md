# ApiManagementClient.TenantConfigurationSyncStateContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **String** | The name of Git branch. | [optional] 
**commitId** | **String** | The latest commit Id. | [optional] 
**configurationChangeDate** | **Date** | The date of the latest configuration change. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**isExport** | **Boolean** | value indicating if last sync was save (true) or deploy (false) operation. | [optional] 
**isGitEnabled** | **Boolean** | value indicating whether Git configuration access is enabled. | [optional] 
**isSynced** | **Boolean** | value indicating if last synchronization was later than the configuration change. | [optional] 
**syncDate** | **Date** | The date of the latest synchronization. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 


