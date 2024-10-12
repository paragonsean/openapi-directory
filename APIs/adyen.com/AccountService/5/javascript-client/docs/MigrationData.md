# AccountApi.MigrationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderId** | **String** | The unique identifier of the account holder in the balance platform. | [optional] 
**balancePlatform** | **String** | The unique identifier of the balance platfrom to which the account holder was migrated. | [optional] 
**migrated** | **Boolean** | Set to **true** if the account holder has been migrated. | [optional] 
**migratedAccounts** | [**[MigratedAccounts]**](MigratedAccounts.md) | Contains the mapping of virtual account codes (classic integration) to the balance account codes (balance platform) associated with the migrated account holder. | [optional] 
**migratedShareholders** | [**[MigratedShareholders]**](MigratedShareholders.md) | Contains the mapping of shareholders associated with the migrated legal entities. | [optional] 
**migratedStores** | [**[MigratedStores]**](MigratedStores.md) | Contains the mapping of business lines and stores associated with the migrated account holder. | [optional] 
**migrationDate** | **Date** | The date when account holder was migrated. | [optional] 


