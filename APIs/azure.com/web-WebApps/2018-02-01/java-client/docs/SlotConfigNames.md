

# SlotConfigNames

Names for connection strings, application settings, and external Azure storage account configuration identifiers to be marked as sticky to the deployment slot and not moved during a swap operation. This is valid for all deployment slots in an app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appSettingNames** | **List&lt;String&gt;** | List of application settings names. |  [optional] |
|**azureStorageConfigNames** | **List&lt;String&gt;** | List of external Azure storage account identifiers. |  [optional] |
|**connectionStringNames** | **List&lt;String&gt;** | List of connection string names. |  [optional] |



