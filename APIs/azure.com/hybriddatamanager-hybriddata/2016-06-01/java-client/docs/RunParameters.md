

# RunParameters

Run parameters for a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerSecrets** | [**List&lt;CustomerSecret&gt;**](CustomerSecret.md) | List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys. |  [optional] |
|**dataServiceInput** | **Object** | A generic json used differently by each data service type. |  [optional] |
|**userConfirmation** | [**UserConfirmationEnum**](#UserConfirmationEnum) | Enum to detect if user confirmation is required. If not passed will default to NotRequired. |  [optional] |



## Enum: UserConfirmationEnum

| Name | Value |
|---- | -----|
| NOT_REQUIRED | &quot;NotRequired&quot; |
| REQUIRED | &quot;Required&quot; |



