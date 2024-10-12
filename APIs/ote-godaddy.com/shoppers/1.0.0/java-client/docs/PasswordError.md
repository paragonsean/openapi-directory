

# PasswordError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Short identifier for the error, suitable for indicating the specific error within client code |  [optional] |
|**message** | **String** | Human-readable, English description of the error |  [optional] |
|**type** | **String** | Response type, always &#39;error&#39; |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| BLACK_LIST | &quot;PW_BLACK_LIST&quot; |
| TOO_SHORT | &quot;PW_TOO_SHORT&quot; |
| TOO_LONG | &quot;PW_TOO_LONG&quot; |
| MISSING_UC | &quot;PW_MISSING_UC&quot; |
| MISSING_NUM | &quot;PW_MISSING_NUM&quot; |
| RECENTLY_USED | &quot;PW_RECENTLY_USED&quot; |
| NOT_UNIQUE | &quot;PW_NOT_UNIQUE&quot; |



