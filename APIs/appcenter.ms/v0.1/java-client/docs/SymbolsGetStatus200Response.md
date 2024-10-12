

# SymbolsGetStatus200Response

A response containing information pertaining to a symbol status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The application that this symbol belongs to |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the symbol is ignored. |  |
|**symbolId** | **String** | The unique id for this symbol (uuid) |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| IGNORED | &quot;ignored&quot; |
| MISSING | &quot;missing&quot; |



