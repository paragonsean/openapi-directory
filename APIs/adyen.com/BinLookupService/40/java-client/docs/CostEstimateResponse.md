

# CostEstimateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardBin** | [**CardBin**](CardBin.md) | Card BIN details. |  [optional] |
|**costEstimateAmount** | [**Amount**](Amount.md) | The estimated cost (scheme fee + interchange) in the settlement currency. If the settlement currency cannot be determined, the fee in EUR is returned. |  [optional] |
|**resultCode** | **String** | The result of the cost estimation. |  [optional] |
|**surchargeType** | **String** | Indicates the way the charges can be passed on to the cardholder. The following values are possible: * &#x60;ZERO&#x60; - the charges are not allowed to pass on * &#x60;PASSTHROUGH&#x60; - the charges can be passed on * &#x60;UNLIMITED&#x60; - there is no limit on how much surcharge is passed on |  [optional] |



