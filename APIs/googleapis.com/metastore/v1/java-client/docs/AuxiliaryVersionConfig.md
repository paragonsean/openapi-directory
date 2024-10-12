

# AuxiliaryVersionConfig

Configuration information for the auxiliary service versions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configOverrides** | **Map&lt;String, String&gt;** | A mapping of Hive metastore configuration key-value pairs to apply to the auxiliary Hive metastore (configured in hive-site.xml) in addition to the primary version&#39;s overrides. If keys are present in both the auxiliary version&#39;s overrides and the primary version&#39;s overrides, the value from the auxiliary version&#39;s overrides takes precedence. |  [optional] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**version** | **String** | The Hive metastore version of the auxiliary service. It must be less than the primary Hive metastore service&#39;s version. |  [optional] |



