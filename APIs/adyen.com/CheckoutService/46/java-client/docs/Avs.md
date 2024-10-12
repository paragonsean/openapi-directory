

# Avs


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressEditable** | **Boolean** | Indicates whether the shopper is allowed to modify the billing address for the current payment request. |  [optional] |
|**enabled** | [**EnabledEnum**](#EnabledEnum) | Specifies whether the shopper should enter their billing address during checkout.  Allowed values: * yes — Perform AVS checks for every card payment. * automatic — Perform AVS checks only when required to optimize the conversion rate. * no — Do not perform AVS checks. |  [optional] |



## Enum: EnabledEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| AUTOMATIC | &quot;automatic&quot; |



