

# ResourceSku

The billing information of the SignalR resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Optional, integer. The unit count of SignalR resource. 1 by default.    If present, following values are allowed:      Free: 1      Standard: 1,2,5,10,20,50,100 |  [optional] |
|**family** | **String** | Optional string. For future use. |  [optional] |
|**name** | **String** | The name of the SKU. Required.    Allowed values: Standard_S1, Free_F1 |  |
|**size** | **String** | Optional string. For future use. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Optional tier of this particular SKU. &#39;Standard&#39; or &#39;Free&#39;.     &#x60;Basic&#x60; is deprecated, use &#x60;Standard&#x60; instead. |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| FREE | &quot;Free&quot; |
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



