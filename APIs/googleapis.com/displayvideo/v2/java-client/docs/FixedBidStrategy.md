

# FixedBidStrategy

A strategy that uses a fixed bidding price.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidAmountMicros** | **String** | The fixed bid amount, in micros of the advertiser&#39;s currency. For insertion order entity, bid_amount_micros should be set as 0. For line item entity, bid_amount_micros must be greater than or equal to billable unit of the given currency and smaller than or equal to the upper limit 1000000000. For example, 1500000 represents 1.5 standard units of the currency. |  [optional] |



