

# ImportRequest

Import database parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseName** | **String** | The name of the database to import. |  |
|**edition** | [**EditionEnum**](#EditionEnum) | The edition for the database being created.    The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API or one of the following commands:    &#x60;&#x60;&#x60;azurecli  az sql db list-editions -l &lt;location&gt; -o table  &#x60;&#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;powershell  Get-AzSqlServerServiceObjective -Location &lt;location&gt;  &#x60;&#x60;&#x60;&#x60;   |  |
|**maxSizeBytes** | **String** | The maximum size for the newly imported database. |  |
|**serviceObjectiveName** | [**ServiceObjectiveNameEnum**](#ServiceObjectiveNameEnum) | The name of the service objective to assign to the database. |  |
|**administratorLogin** | **String** | The name of the SQL administrator. |  |
|**administratorLoginPassword** | **String** | The password of the SQL administrator. |  |
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) | The authentication type. |  [optional] |
|**storageKey** | **String** | The storage key to use.  If storage key type is SharedAccessKey, it must be preceded with a \&quot;?.\&quot; |  |
|**storageKeyType** | [**StorageKeyTypeEnum**](#StorageKeyTypeEnum) | The type of the storage key to use. |  |
|**storageUri** | **String** | The storage uri to use. |  |



## Enum: EditionEnum

| Name | Value |
|---- | -----|
| WEB | &quot;Web&quot; |
| BUSINESS | &quot;Business&quot; |
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| PREMIUM_RS | &quot;PremiumRS&quot; |
| FREE | &quot;Free&quot; |
| STRETCH | &quot;Stretch&quot; |
| DATA_WAREHOUSE | &quot;DataWarehouse&quot; |
| SYSTEM | &quot;System&quot; |
| SYSTEM2 | &quot;System2&quot; |
| GENERAL_PURPOSE | &quot;GeneralPurpose&quot; |
| BUSINESS_CRITICAL | &quot;BusinessCritical&quot; |
| HYPERSCALE | &quot;Hyperscale&quot; |



## Enum: ServiceObjectiveNameEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;System&quot; |
| SYSTEM0 | &quot;System0&quot; |
| SYSTEM1 | &quot;System1&quot; |
| SYSTEM2 | &quot;System2&quot; |
| SYSTEM3 | &quot;System3&quot; |
| SYSTEM4 | &quot;System4&quot; |
| SYSTEM2_L | &quot;System2L&quot; |
| SYSTEM3_L | &quot;System3L&quot; |
| SYSTEM4_L | &quot;System4L&quot; |
| FREE | &quot;Free&quot; |
| BASIC | &quot;Basic&quot; |
| S0 | &quot;S0&quot; |
| S1 | &quot;S1&quot; |
| S2 | &quot;S2&quot; |
| S3 | &quot;S3&quot; |
| S4 | &quot;S4&quot; |
| S6 | &quot;S6&quot; |
| S7 | &quot;S7&quot; |
| S9 | &quot;S9&quot; |
| S12 | &quot;S12&quot; |
| P1 | &quot;P1&quot; |
| P2 | &quot;P2&quot; |
| P3 | &quot;P3&quot; |
| P4 | &quot;P4&quot; |
| P6 | &quot;P6&quot; |
| P11 | &quot;P11&quot; |
| P15 | &quot;P15&quot; |
| PRS1 | &quot;PRS1&quot; |
| PRS2 | &quot;PRS2&quot; |
| PRS4 | &quot;PRS4&quot; |
| PRS6 | &quot;PRS6&quot; |
| DW100 | &quot;DW100&quot; |
| DW200 | &quot;DW200&quot; |
| DW300 | &quot;DW300&quot; |
| DW400 | &quot;DW400&quot; |
| DW500 | &quot;DW500&quot; |
| DW600 | &quot;DW600&quot; |
| DW1000 | &quot;DW1000&quot; |
| DW1200 | &quot;DW1200&quot; |
| DW1000C | &quot;DW1000c&quot; |
| DW1500 | &quot;DW1500&quot; |
| DW1500C | &quot;DW1500c&quot; |
| DW2000 | &quot;DW2000&quot; |
| DW2000C | &quot;DW2000c&quot; |
| DW3000 | &quot;DW3000&quot; |
| DW2500C | &quot;DW2500c&quot; |
| DW3000C | &quot;DW3000c&quot; |
| DW6000 | &quot;DW6000&quot; |
| DW5000C | &quot;DW5000c&quot; |
| DW6000C | &quot;DW6000c&quot; |
| DW7500C | &quot;DW7500c&quot; |
| DW10000C | &quot;DW10000c&quot; |
| DW15000C | &quot;DW15000c&quot; |
| DW30000C | &quot;DW30000c&quot; |
| DS100 | &quot;DS100&quot; |
| DS200 | &quot;DS200&quot; |
| DS300 | &quot;DS300&quot; |
| DS400 | &quot;DS400&quot; |
| DS500 | &quot;DS500&quot; |
| DS600 | &quot;DS600&quot; |
| DS1000 | &quot;DS1000&quot; |
| DS1200 | &quot;DS1200&quot; |
| DS1500 | &quot;DS1500&quot; |
| DS2000 | &quot;DS2000&quot; |
| ELASTIC_POOL | &quot;ElasticPool&quot; |



## Enum: AuthenticationTypeEnum

| Name | Value |
|---- | -----|
| SQL | &quot;SQL&quot; |
| AD_PASSWORD | &quot;ADPassword&quot; |



## Enum: StorageKeyTypeEnum

| Name | Value |
|---- | -----|
| STORAGE_ACCESS_KEY | &quot;StorageAccessKey&quot; |
| SHARED_ACCESS_KEY | &quot;SharedAccessKey&quot; |



