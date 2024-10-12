# CallFireApiDocumentation.BillingPlanUsage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervalEnd** | **Number** | End of usage period formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**intervalStart** | **Number** | Start of usage period formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**remainingPayAsYouGoCredits** | **Number** | Remaining pay as you go credits are rounded to nearest whole value | [optional] [readonly] 
**remainingPlanCredits** | **Number** | Remaining credits are rounded to nearest whole value associated with a plan | [optional] [readonly] 
**totalRemainingCredits** | **Number** | Total number of remaining credits (remainingPlanCredits + remainingPayAsYouGoCredits) | [optional] [readonly] 


