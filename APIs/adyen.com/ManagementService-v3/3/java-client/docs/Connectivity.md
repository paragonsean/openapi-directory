

# Connectivity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**simcardStatus** | [**SimcardStatusEnum**](#SimcardStatusEnum) | Indicates the status of the SIM card in the payment terminal. Can be updated and received only at terminal level, and only for models that support cellular connectivity.  Possible values: * **ACTIVATED**: the SIM card is activated. Cellular connectivity may still need to be enabled on the terminal itself, in the **Network** settings. * **INVENTORY**: the SIM card is not activated. The terminal can&#39;t use cellular connectivity. |  [optional] |



## Enum: SimcardStatusEnum

| Name | Value |
|---- | -----|
| ACTIVATED | &quot;ACTIVATED&quot; |
| INVENTORY | &quot;INVENTORY&quot; |



