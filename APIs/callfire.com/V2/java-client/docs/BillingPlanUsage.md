

# BillingPlanUsage

Contains statistics of billing plan usage

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intervalEnd** | **Long** | End of usage period formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**intervalStart** | **Long** | Start of usage period formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**remainingPayAsYouGoCredits** | **BigDecimal** | Remaining pay as you go credits are rounded to nearest whole value |  [optional] [readonly] |
|**remainingPlanCredits** | **BigDecimal** | Remaining credits are rounded to nearest whole value associated with a plan |  [optional] [readonly] |
|**totalRemainingCredits** | **BigDecimal** | Total number of remaining credits (remainingPlanCredits + remainingPayAsYouGoCredits) |  [optional] [readonly] |



