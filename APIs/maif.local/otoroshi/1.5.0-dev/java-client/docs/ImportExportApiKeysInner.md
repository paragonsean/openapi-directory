

# ImportExportApiKeysInner

An Otoroshi Api Key. An Api Key is defined for a group of services to allow usage of the same Api Key for multiple services.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedEntities** | **List&lt;String&gt;** | The group/service ids (prefixed by group_ or service_ on which the key is authorized |  |
|**clientId** | **String** | The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything |  |
|**clientName** | **String** | The name of the api key, for humans ;-) |  |
|**clientSecret** | **String** | The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything |  |
|**dailyQuota** | **Long** | Authorized number of calls per day |  [optional] |
|**enabled** | **Boolean** | Whether or not the key is enabled. If disabled, resources won&#39;t be available to calls using this key |  |
|**metadata** | **Map&lt;String, String&gt;** | Bunch of metadata for the key |  [optional] |
|**monthlyQuota** | **Long** | Authorized number of calls per month |  [optional] |
|**throttlingQuota** | **Long** | Authorized number of calls per second, measured on 10 seconds |  [optional] |



