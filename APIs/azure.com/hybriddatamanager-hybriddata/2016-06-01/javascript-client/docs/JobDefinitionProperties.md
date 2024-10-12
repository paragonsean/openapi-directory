# HybridDataManagementClient.JobDefinitionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerSecrets** | [**[CustomerSecret]**](CustomerSecret.md) | List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys. | [optional] 
**dataServiceInput** | **Object** | A generic json used differently by each data service type. | [optional] 
**dataSinkId** | **String** | Data Sink Id associated to the job definition. | 
**dataSourceId** | **String** | Data Source Id associated to the job definition. | 
**lastModifiedTime** | **Date** | Last modified time of the job definition. | [optional] 
**runLocation** | **String** | This is the preferred geo location for the job to run. | [optional] 
**schedules** | [**[Schedule]**](Schedule.md) | Schedule for running the job definition | [optional] 
**state** | **String** | State of the job definition. | 
**userConfirmation** | **String** | Enum to detect if user confirmation is required. If not passed will default to NotRequired. | [optional] [default to &#39;NotRequired&#39;]



## Enum: RunLocationEnum


* `none` (value: `"none"`)

* `australiaeast` (value: `"australiaeast"`)

* `australiasoutheast` (value: `"australiasoutheast"`)

* `brazilsouth` (value: `"brazilsouth"`)

* `canadacentral` (value: `"canadacentral"`)

* `canadaeast` (value: `"canadaeast"`)

* `centralindia` (value: `"centralindia"`)

* `centralus` (value: `"centralus"`)

* `eastasia` (value: `"eastasia"`)

* `eastus` (value: `"eastus"`)

* `eastus2` (value: `"eastus2"`)

* `japaneast` (value: `"japaneast"`)

* `japanwest` (value: `"japanwest"`)

* `koreacentral` (value: `"koreacentral"`)

* `koreasouth` (value: `"koreasouth"`)

* `southeastasia` (value: `"southeastasia"`)

* `southcentralus` (value: `"southcentralus"`)

* `southindia` (value: `"southindia"`)

* `northcentralus` (value: `"northcentralus"`)

* `northeurope` (value: `"northeurope"`)

* `uksouth` (value: `"uksouth"`)

* `ukwest` (value: `"ukwest"`)

* `westcentralus` (value: `"westcentralus"`)

* `westeurope` (value: `"westeurope"`)

* `westindia` (value: `"westindia"`)

* `westus` (value: `"westus"`)

* `westus2` (value: `"westus2"`)





## Enum: StateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)

* `Supported` (value: `"Supported"`)





## Enum: UserConfirmationEnum


* `NotRequired` (value: `"NotRequired"`)

* `Required` (value: `"Required"`)




