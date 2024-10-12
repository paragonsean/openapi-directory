

# NewBillPaymentAllocation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocationAmount** | **Double** | The Amount being allocated to the bill. Expects same currency as bill currency |  [optional] |
|**allocationDate** | **OffsetDateTime** | Optional. Defaults to the current time in the Avaza account&#39;s timezone. The date the allocation is applied to the bill. Can be different from the Payment Date when doing prepayments etc. |  [optional] |
|**billTransactionIDFK** | **Long** | The Avaza Bill TransactionID that is having a payment amount allocated to it. |  [optional] |



