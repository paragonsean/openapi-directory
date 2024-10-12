

# GoogleCloudChannelV1alpha1EntitlementEvent

Represents Pub/Sub message content describing entitlement update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entitlement** | **String** | Resource name of an entitlement of the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Type of event which happened on the entitlement. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| PRICE_PLAN_SWITCHED | &quot;PRICE_PLAN_SWITCHED&quot; |
| COMMITMENT_CHANGED | &quot;COMMITMENT_CHANGED&quot; |
| RENEWED | &quot;RENEWED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| ACTIVATED | &quot;ACTIVATED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SKU_CHANGED | &quot;SKU_CHANGED&quot; |
| RENEWAL_SETTING_CHANGED | &quot;RENEWAL_SETTING_CHANGED&quot; |
| PAID_SERVICE_STARTED | &quot;PAID_SERVICE_STARTED&quot; |
| LICENSE_ASSIGNMENT_CHANGED | &quot;LICENSE_ASSIGNMENT_CHANGED&quot; |
| LICENSE_CAP_CHANGED | &quot;LICENSE_CAP_CHANGED&quot; |



