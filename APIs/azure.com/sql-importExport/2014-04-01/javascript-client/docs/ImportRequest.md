# AzureSqlDatabaseImportExportSpec.ImportRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseName** | **String** | The name of the database to import. | 
**edition** | **String** | The edition for the database being created.    The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API or one of the following commands:    &#x60;&#x60;&#x60;azurecli  az sql db list-editions -l &lt;location&gt; -o table  &#x60;&#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;powershell  Get-AzSqlServerServiceObjective -Location &lt;location&gt;  &#x60;&#x60;&#x60;&#x60;   | 
**maxSizeBytes** | **String** | The maximum size for the newly imported database. | 
**serviceObjectiveName** | **String** | The name of the service objective to assign to the database. | 
**administratorLogin** | **String** | The name of the SQL administrator. | 
**administratorLoginPassword** | **String** | The password of the SQL administrator. | 
**authenticationType** | **String** | The authentication type. | [optional] [default to &#39;SQL&#39;]
**storageKey** | **String** | The storage key to use.  If storage key type is SharedAccessKey, it must be preceded with a \&quot;?.\&quot; | 
**storageKeyType** | **String** | The type of the storage key to use. | 
**storageUri** | **String** | The storage uri to use. | 



## Enum: EditionEnum


* `Web` (value: `"Web"`)

* `Business` (value: `"Business"`)

* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `PremiumRS` (value: `"PremiumRS"`)

* `Free` (value: `"Free"`)

* `Stretch` (value: `"Stretch"`)

* `DataWarehouse` (value: `"DataWarehouse"`)

* `System` (value: `"System"`)

* `System2` (value: `"System2"`)

* `GeneralPurpose` (value: `"GeneralPurpose"`)

* `BusinessCritical` (value: `"BusinessCritical"`)

* `Hyperscale` (value: `"Hyperscale"`)





## Enum: ServiceObjectiveNameEnum


* `System` (value: `"System"`)

* `System0` (value: `"System0"`)

* `System1` (value: `"System1"`)

* `System2` (value: `"System2"`)

* `System3` (value: `"System3"`)

* `System4` (value: `"System4"`)

* `System2L` (value: `"System2L"`)

* `System3L` (value: `"System3L"`)

* `System4L` (value: `"System4L"`)

* `Free` (value: `"Free"`)

* `Basic` (value: `"Basic"`)

* `S0` (value: `"S0"`)

* `S1` (value: `"S1"`)

* `S2` (value: `"S2"`)

* `S3` (value: `"S3"`)

* `S4` (value: `"S4"`)

* `S6` (value: `"S6"`)

* `S7` (value: `"S7"`)

* `S9` (value: `"S9"`)

* `S12` (value: `"S12"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P6` (value: `"P6"`)

* `P11` (value: `"P11"`)

* `P15` (value: `"P15"`)

* `PRS1` (value: `"PRS1"`)

* `PRS2` (value: `"PRS2"`)

* `PRS4` (value: `"PRS4"`)

* `PRS6` (value: `"PRS6"`)

* `DW100` (value: `"DW100"`)

* `DW200` (value: `"DW200"`)

* `DW300` (value: `"DW300"`)

* `DW400` (value: `"DW400"`)

* `DW500` (value: `"DW500"`)

* `DW600` (value: `"DW600"`)

* `DW1000` (value: `"DW1000"`)

* `DW1200` (value: `"DW1200"`)

* `DW1000c` (value: `"DW1000c"`)

* `DW1500` (value: `"DW1500"`)

* `DW1500c` (value: `"DW1500c"`)

* `DW2000` (value: `"DW2000"`)

* `DW2000c` (value: `"DW2000c"`)

* `DW3000` (value: `"DW3000"`)

* `DW2500c` (value: `"DW2500c"`)

* `DW3000c` (value: `"DW3000c"`)

* `DW6000` (value: `"DW6000"`)

* `DW5000c` (value: `"DW5000c"`)

* `DW6000c` (value: `"DW6000c"`)

* `DW7500c` (value: `"DW7500c"`)

* `DW10000c` (value: `"DW10000c"`)

* `DW15000c` (value: `"DW15000c"`)

* `DW30000c` (value: `"DW30000c"`)

* `DS100` (value: `"DS100"`)

* `DS200` (value: `"DS200"`)

* `DS300` (value: `"DS300"`)

* `DS400` (value: `"DS400"`)

* `DS500` (value: `"DS500"`)

* `DS600` (value: `"DS600"`)

* `DS1000` (value: `"DS1000"`)

* `DS1200` (value: `"DS1200"`)

* `DS1500` (value: `"DS1500"`)

* `DS2000` (value: `"DS2000"`)

* `ElasticPool` (value: `"ElasticPool"`)





## Enum: AuthenticationTypeEnum


* `SQL` (value: `"SQL"`)

* `ADPassword` (value: `"ADPassword"`)





## Enum: StorageKeyTypeEnum


* `StorageAccessKey` (value: `"StorageAccessKey"`)

* `SharedAccessKey` (value: `"SharedAccessKey"`)




