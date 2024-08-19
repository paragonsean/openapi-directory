

# BodyUpdateOriginStatusV1OriginStatusPut


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**logId** | **UUID** | The log id to change the status |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The scope to change the status |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status id to change the details |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| ADDRESS_AND_COOKIE | &quot;address_and_cookie&quot; |
| ADDRESS | &quot;address&quot; |
| COOKIE | &quot;cookie&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PASS | &quot;pass&quot; |
| BLOCK | &quot;block&quot; |
| CHALLENGE | &quot;challenge&quot; |
| BYPASS | &quot;bypass&quot; |
| IGNORE | &quot;ignore&quot; |



