# HybridDataManagementClient.RunParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerSecrets** | [**[CustomerSecret]**](CustomerSecret.md) | List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys. | [optional] 
**dataServiceInput** | **Object** | A generic json used differently by each data service type. | [optional] 
**userConfirmation** | **String** | Enum to detect if user confirmation is required. If not passed will default to NotRequired. | [optional] [default to &#39;NotRequired&#39;]



## Enum: UserConfirmationEnum


* `NotRequired` (value: `"NotRequired"`)

* `Required` (value: `"Required"`)




