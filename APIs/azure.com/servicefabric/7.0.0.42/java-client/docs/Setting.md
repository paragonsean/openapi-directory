

# Setting

Describes a setting for the container. The setting file path can be fetched from environment variable \"Fabric_SettingPath\". The path for Windows container is \"C:\\\\secrets\". The path for Linux container is \"/var/secrets\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the setting. |  [optional] |
|**type** | **SettingType** |  |  [optional] |
|**value** | **String** | The value of the setting, will be processed based on the type provided. |  [optional] |



