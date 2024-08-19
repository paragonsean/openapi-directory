

# AccountPayoutState


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowPayout** | **Boolean** | Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder&#39;s accounts. If this field is true, payouts will be permitted for any of the account holder&#39;s accounts. |  [optional] |
|**disableReason** | **String** | The reason why payouts (to all of the account holder&#39;s accounts) have been disabled (by the platform). If the &#x60;disabled&#x60; field is true, this field can be used to explain why. |  [optional] |
|**disabled** | **Boolean** | Indicates whether payouts have been disabled (by the platform) for all of the account holder&#39;s accounts. A platform may enable and disable this field at their discretion. If this field is true, &#x60;allowPayout&#x60; will be false and no payouts will be permitted for any of the account holder&#39;s accounts. If this field is false, &#x60;allowPayout&#x60; may or may not be enabled, depending on other factors. |  [optional] |
|**payoutLimit** | [**Amount**](Amount.md) | The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited. |  [optional] |
|**tierNumber** | **Integer** | The payout tier that the account holder occupies. |  [optional] |



