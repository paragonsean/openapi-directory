

# KeyUpdateParameters

The key update parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**KeyAttributes**](KeyAttributes.md) |  |  [optional] |
|**keyOps** | [**List&lt;KeyOpsEnum&gt;**](#List&lt;KeyOpsEnum&gt;) | Json web key operations. For more information on possible key operations, see JsonWebKeyOperation. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |



## Enum: List&lt;KeyOpsEnum&gt;

| Name | Value |
|---- | -----|
| ENCRYPT | &quot;encrypt&quot; |
| DECRYPT | &quot;decrypt&quot; |
| SIGN | &quot;sign&quot; |
| VERIFY | &quot;verify&quot; |
| WRAP_KEY | &quot;wrapKey&quot; |
| UNWRAP_KEY | &quot;unwrapKey&quot; |



