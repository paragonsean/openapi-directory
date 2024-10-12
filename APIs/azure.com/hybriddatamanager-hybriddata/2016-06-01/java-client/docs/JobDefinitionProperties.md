

# JobDefinitionProperties

Job Definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerSecrets** | [**List&lt;CustomerSecret&gt;**](CustomerSecret.md) | List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys. |  [optional] |
|**dataServiceInput** | **Object** | A generic json used differently by each data service type. |  [optional] |
|**dataSinkId** | **String** | Data Sink Id associated to the job definition. |  |
|**dataSourceId** | **String** | Data Source Id associated to the job definition. |  |
|**lastModifiedTime** | **OffsetDateTime** | Last modified time of the job definition. |  [optional] |
|**runLocation** | [**RunLocationEnum**](#RunLocationEnum) | This is the preferred geo location for the job to run. |  [optional] |
|**schedules** | [**List&lt;Schedule&gt;**](Schedule.md) | Schedule for running the job definition |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the job definition. |  |
|**userConfirmation** | [**UserConfirmationEnum**](#UserConfirmationEnum) | Enum to detect if user confirmation is required. If not passed will default to NotRequired. |  [optional] |



## Enum: RunLocationEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| AUSTRALIAEAST | &quot;australiaeast&quot; |
| AUSTRALIASOUTHEAST | &quot;australiasoutheast&quot; |
| BRAZILSOUTH | &quot;brazilsouth&quot; |
| CANADACENTRAL | &quot;canadacentral&quot; |
| CANADAEAST | &quot;canadaeast&quot; |
| CENTRALINDIA | &quot;centralindia&quot; |
| CENTRALUS | &quot;centralus&quot; |
| EASTASIA | &quot;eastasia&quot; |
| EASTUS | &quot;eastus&quot; |
| EASTUS2 | &quot;eastus2&quot; |
| JAPANEAST | &quot;japaneast&quot; |
| JAPANWEST | &quot;japanwest&quot; |
| KOREACENTRAL | &quot;koreacentral&quot; |
| KOREASOUTH | &quot;koreasouth&quot; |
| SOUTHEASTASIA | &quot;southeastasia&quot; |
| SOUTHCENTRALUS | &quot;southcentralus&quot; |
| SOUTHINDIA | &quot;southindia&quot; |
| NORTHCENTRALUS | &quot;northcentralus&quot; |
| NORTHEUROPE | &quot;northeurope&quot; |
| UKSOUTH | &quot;uksouth&quot; |
| UKWEST | &quot;ukwest&quot; |
| WESTCENTRALUS | &quot;westcentralus&quot; |
| WESTEUROPE | &quot;westeurope&quot; |
| WESTINDIA | &quot;westindia&quot; |
| WESTUS | &quot;westus&quot; |
| WESTUS2 | &quot;westus2&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |
| SUPPORTED | &quot;Supported&quot; |



## Enum: UserConfirmationEnum

| Name | Value |
|---- | -----|
| NOT_REQUIRED | &quot;NotRequired&quot; |
| REQUIRED | &quot;Required&quot; |



