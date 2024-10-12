

# RegenerateAccessKeyParameters

Parameters supplied to the Regenerate Authorization Rule operation, specifies which key needs to be reset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Optional, if the key value provided, is reset for KeyType value or autogenerate Key value set for keyType |  [optional] |
|**keyType** | [**KeyTypeEnum**](#KeyTypeEnum) | The access key to regenerate. |  |



## Enum: KeyTypeEnum

| Name | Value |
|---- | -----|
| PRIMARY_KEY | &quot;PrimaryKey&quot; |
| SECONDARY_KEY | &quot;SecondaryKey&quot; |



