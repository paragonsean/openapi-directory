# CloudSqlAdminApi.DatabaseFlags

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the flag. These flags are passed at instance startup, so include both server options and system variables. Flags are specified with underscores, not hyphens. For more information, see [Configuring Database Flags](https://cloud.google.com/sql/docs/mysql/flags) in the Cloud SQL documentation. | [optional] 
**value** | **String** | The value of the flag. Boolean flags are set to &#x60;on&#x60; for true and &#x60;off&#x60; for false. This field must be omitted if the flag doesn&#39;t take a value. | [optional] 


