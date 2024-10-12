

# HoldInfoObject

Provides information about the amount at which a transaction was in the `HELD` status. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**MoneyObject**](MoneyObject.md) | The amount of this transaction while in the &#x60;HELD&#x60; status, in Australian dollars.  |  |
|**foreignAmount** | [**MoneyObject**](MoneyObject.md) | The foreign currency amount of this transaction while in the &#x60;HELD&#x60; status. This field will be &#x60;null&#x60; for domestic transactions. The amount was converted to the AUD amount reflected in the &#x60;amount&#x60; field.  |  |



