

# BillingAssignment

List account, subaccount, advertiser, and campaign associated with a given Billing Profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the account associated with the billing assignment.This is a read-only, auto-generated field. |  [optional] |
|**advertiserId** | **String** | ID of the advertiser associated with the billing assignment.Wildcard (*) means this assignment is not limited to a single advertiser |  [optional] |
|**campaignId** | **String** | ID of the campaign associated with the billing assignment. Wildcard (*) means this assignment is not limited to a single campaign |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#billingAssignment\&quot;. |  [optional] |
|**subaccountId** | **String** | ID of the subaccount associated with the billing assignment.Wildcard (*) means this assignment is not limited to a single subaccountThis is a read-only, auto-generated field. |  [optional] |



