# CloudChannelApi.GoogleCloudChannelV1EntitlementChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationReason** | **String** | The Entitlement&#39;s activation reason | [optional] 
**cancellationReason** | **String** | Cancellation reason for the Entitlement. | [optional] 
**changeType** | **String** | The change action type. | [optional] 
**createTime** | **String** | The submitted time of the change. | [optional] 
**entitlement** | **String** | Required. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} | [optional] 
**offer** | **String** | Required. Resource name of the Offer at the time of change. Takes the form: accounts/{account_id}/offers/{offer_id}. | [optional] 
**operator** | **String** | Human-readable identifier that shows what operator made a change. When the operator_type is RESELLER, this is the user&#39;s email address. For all other operator types, this is empty. | [optional] 
**operatorType** | **String** | Operator type responsible for the change. | [optional] 
**otherChangeReason** | **String** | e.g. purchase_number change reason, entered by CRS. | [optional] 
**parameters** | [**[GoogleCloudChannelV1Parameter]**](GoogleCloudChannelV1Parameter.md) | Extended parameters, such as: purchase_order_number, gcp_details; internal_correlation_id, long_running_operation_id, order_id; etc. | [optional] 
**provisionedService** | [**GoogleCloudChannelV1ProvisionedService**](GoogleCloudChannelV1ProvisionedService.md) |  | [optional] 
**suspensionReason** | **String** | Suspension reason for the Entitlement. | [optional] 



## Enum: ActivationReasonEnum


* `ACTIVATION_REASON_UNSPECIFIED` (value: `"ACTIVATION_REASON_UNSPECIFIED"`)

* `RESELLER_REVOKED_SUSPENSION` (value: `"RESELLER_REVOKED_SUSPENSION"`)

* `CUSTOMER_ACCEPTED_PENDING_TOS` (value: `"CUSTOMER_ACCEPTED_PENDING_TOS"`)

* `RENEWAL_SETTINGS_CHANGED` (value: `"RENEWAL_SETTINGS_CHANGED"`)

* `OTHER_ACTIVATION_REASON` (value: `"OTHER_ACTIVATION_REASON"`)





## Enum: CancellationReasonEnum


* `CANCELLATION_REASON_UNSPECIFIED` (value: `"CANCELLATION_REASON_UNSPECIFIED"`)

* `SERVICE_TERMINATED` (value: `"SERVICE_TERMINATED"`)

* `RELATIONSHIP_ENDED` (value: `"RELATIONSHIP_ENDED"`)

* `PARTIAL_TRANSFER` (value: `"PARTIAL_TRANSFER"`)





## Enum: ChangeTypeEnum


* `CHANGE_TYPE_UNSPECIFIED` (value: `"CHANGE_TYPE_UNSPECIFIED"`)

* `CREATED` (value: `"CREATED"`)

* `PRICE_PLAN_SWITCHED` (value: `"PRICE_PLAN_SWITCHED"`)

* `COMMITMENT_CHANGED` (value: `"COMMITMENT_CHANGED"`)

* `RENEWED` (value: `"RENEWED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `ACTIVATED` (value: `"ACTIVATED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SKU_CHANGED` (value: `"SKU_CHANGED"`)

* `RENEWAL_SETTING_CHANGED` (value: `"RENEWAL_SETTING_CHANGED"`)

* `PAID_SUBSCRIPTION_STARTED` (value: `"PAID_SUBSCRIPTION_STARTED"`)

* `LICENSE_CAP_CHANGED` (value: `"LICENSE_CAP_CHANGED"`)

* `SUSPENSION_DETAILS_CHANGED` (value: `"SUSPENSION_DETAILS_CHANGED"`)

* `TRIAL_END_DATE_EXTENDED` (value: `"TRIAL_END_DATE_EXTENDED"`)

* `TRIAL_STARTED` (value: `"TRIAL_STARTED"`)





## Enum: OperatorTypeEnum


* `OPERATOR_TYPE_UNSPECIFIED` (value: `"OPERATOR_TYPE_UNSPECIFIED"`)

* `CUSTOMER_SERVICE_REPRESENTATIVE` (value: `"CUSTOMER_SERVICE_REPRESENTATIVE"`)

* `SYSTEM` (value: `"SYSTEM"`)

* `CUSTOMER` (value: `"CUSTOMER"`)

* `RESELLER` (value: `"RESELLER"`)





## Enum: SuspensionReasonEnum


* `SUSPENSION_REASON_UNSPECIFIED` (value: `"SUSPENSION_REASON_UNSPECIFIED"`)

* `RESELLER_INITIATED` (value: `"RESELLER_INITIATED"`)

* `TRIAL_ENDED` (value: `"TRIAL_ENDED"`)

* `RENEWAL_WITH_TYPE_CANCEL` (value: `"RENEWAL_WITH_TYPE_CANCEL"`)

* `PENDING_TOS_ACCEPTANCE` (value: `"PENDING_TOS_ACCEPTANCE"`)

* `OTHER` (value: `"OTHER"`)




