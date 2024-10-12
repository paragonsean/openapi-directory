

# GoogleCloudChannelV1EntitlementChange

Change event entry for Entitlement order history

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationReason** | [**ActivationReasonEnum**](#ActivationReasonEnum) | The Entitlement&#39;s activation reason |  [optional] |
|**cancellationReason** | [**CancellationReasonEnum**](#CancellationReasonEnum) | Cancellation reason for the Entitlement. |  [optional] |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | The change action type. |  [optional] |
|**createTime** | **String** | The submitted time of the change. |  [optional] |
|**entitlement** | **String** | Required. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} |  [optional] |
|**offer** | **String** | Required. Resource name of the Offer at the time of change. Takes the form: accounts/{account_id}/offers/{offer_id}. |  [optional] |
|**operator** | **String** | Human-readable identifier that shows what operator made a change. When the operator_type is RESELLER, this is the user&#39;s email address. For all other operator types, this is empty. |  [optional] |
|**operatorType** | [**OperatorTypeEnum**](#OperatorTypeEnum) | Operator type responsible for the change. |  [optional] |
|**otherChangeReason** | **String** | e.g. purchase_number change reason, entered by CRS. |  [optional] |
|**parameters** | [**List&lt;GoogleCloudChannelV1Parameter&gt;**](GoogleCloudChannelV1Parameter.md) | Extended parameters, such as: purchase_order_number, gcp_details; internal_correlation_id, long_running_operation_id, order_id; etc. |  [optional] |
|**provisionedService** | [**GoogleCloudChannelV1ProvisionedService**](GoogleCloudChannelV1ProvisionedService.md) |  |  [optional] |
|**suspensionReason** | [**SuspensionReasonEnum**](#SuspensionReasonEnum) | Suspension reason for the Entitlement. |  [optional] |



## Enum: ActivationReasonEnum

| Name | Value |
|---- | -----|
| ACTIVATION_REASON_UNSPECIFIED | &quot;ACTIVATION_REASON_UNSPECIFIED&quot; |
| RESELLER_REVOKED_SUSPENSION | &quot;RESELLER_REVOKED_SUSPENSION&quot; |
| CUSTOMER_ACCEPTED_PENDING_TOS | &quot;CUSTOMER_ACCEPTED_PENDING_TOS&quot; |
| RENEWAL_SETTINGS_CHANGED | &quot;RENEWAL_SETTINGS_CHANGED&quot; |
| OTHER_ACTIVATION_REASON | &quot;OTHER_ACTIVATION_REASON&quot; |



## Enum: CancellationReasonEnum

| Name | Value |
|---- | -----|
| CANCELLATION_REASON_UNSPECIFIED | &quot;CANCELLATION_REASON_UNSPECIFIED&quot; |
| SERVICE_TERMINATED | &quot;SERVICE_TERMINATED&quot; |
| RELATIONSHIP_ENDED | &quot;RELATIONSHIP_ENDED&quot; |
| PARTIAL_TRANSFER | &quot;PARTIAL_TRANSFER&quot; |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| CHANGE_TYPE_UNSPECIFIED | &quot;CHANGE_TYPE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| PRICE_PLAN_SWITCHED | &quot;PRICE_PLAN_SWITCHED&quot; |
| COMMITMENT_CHANGED | &quot;COMMITMENT_CHANGED&quot; |
| RENEWED | &quot;RENEWED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| ACTIVATED | &quot;ACTIVATED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SKU_CHANGED | &quot;SKU_CHANGED&quot; |
| RENEWAL_SETTING_CHANGED | &quot;RENEWAL_SETTING_CHANGED&quot; |
| PAID_SUBSCRIPTION_STARTED | &quot;PAID_SUBSCRIPTION_STARTED&quot; |
| LICENSE_CAP_CHANGED | &quot;LICENSE_CAP_CHANGED&quot; |
| SUSPENSION_DETAILS_CHANGED | &quot;SUSPENSION_DETAILS_CHANGED&quot; |
| TRIAL_END_DATE_EXTENDED | &quot;TRIAL_END_DATE_EXTENDED&quot; |
| TRIAL_STARTED | &quot;TRIAL_STARTED&quot; |



## Enum: OperatorTypeEnum

| Name | Value |
|---- | -----|
| OPERATOR_TYPE_UNSPECIFIED | &quot;OPERATOR_TYPE_UNSPECIFIED&quot; |
| CUSTOMER_SERVICE_REPRESENTATIVE | &quot;CUSTOMER_SERVICE_REPRESENTATIVE&quot; |
| SYSTEM | &quot;SYSTEM&quot; |
| CUSTOMER | &quot;CUSTOMER&quot; |
| RESELLER | &quot;RESELLER&quot; |



## Enum: SuspensionReasonEnum

| Name | Value |
|---- | -----|
| SUSPENSION_REASON_UNSPECIFIED | &quot;SUSPENSION_REASON_UNSPECIFIED&quot; |
| RESELLER_INITIATED | &quot;RESELLER_INITIATED&quot; |
| TRIAL_ENDED | &quot;TRIAL_ENDED&quot; |
| RENEWAL_WITH_TYPE_CANCEL | &quot;RENEWAL_WITH_TYPE_CANCEL&quot; |
| PENDING_TOS_ACCEPTANCE | &quot;PENDING_TOS_ACCEPTANCE&quot; |
| OTHER | &quot;OTHER&quot; |



