

# GoogleCloudChannelV1alpha1Entitlement

An entitlement is a representation of a customer's ability to use a service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedUnits** | **Integer** | The current number of users that are assigned a license for the product defined in provisioned_service.skuId. Read-only. Deprecated: Use &#x60;parameters&#x60; instead. |  [optional] |
|**associationInfo** | [**GoogleCloudChannelV1alpha1AssociationInfo**](GoogleCloudChannelV1alpha1AssociationInfo.md) |  |  [optional] |
|**billingAccount** | **String** | Optional. The billing account resource name that is used to pay for this entitlement. |  [optional] |
|**channelPartnerId** | **String** | Cloud Identity ID of a channel partner who will be the direct reseller for the customer&#39;s order. This field is generally used in 2-tier ordering, where the order is placed by a top-level distributor on behalf of their channel partner or reseller. Required for distributors. Deprecated: &#x60;channel_partner_id&#x60; has been moved to the Customer. |  [optional] |
|**commitmentSettings** | [**GoogleCloudChannelV1alpha1CommitmentSettings**](GoogleCloudChannelV1alpha1CommitmentSettings.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which the entitlement is created. |  [optional] [readonly] |
|**maxUnits** | **Integer** | Maximum number of units for a non commitment-based Offer, such as Flexible, Trial or Free entitlements. For commitment-based entitlements, this is a read-only field, which only the internal support team can update. Deprecated: Use &#x60;parameters&#x60; instead. |  [optional] |
|**name** | **String** | Output only. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}. |  [optional] [readonly] |
|**numUnits** | **Integer** | Number of units for a commitment-based Offer. For example, for seat-based Offers, this would be the number of seats; for license-based Offers, this would be the number of licenses. Required for creating commitment-based Offers. Deprecated: Use &#x60;parameters&#x60; instead. |  [optional] |
|**offer** | **String** | Required. The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}. |  [optional] |
|**parameters** | [**List&lt;GoogleCloudChannelV1alpha1Parameter&gt;**](GoogleCloudChannelV1alpha1Parameter.md) | Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. For Google Workspace, the following Parameters may be accepted as input: - max_units: The maximum assignable units for a flexible offer OR - num_units: The total commitment for commitment-based offers The response may additionally include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. For Google Cloud billing subaccounts, the following Parameter may be accepted as input: - display_name: The display name of the billing subaccount. |  [optional] |
|**provisionedService** | [**GoogleCloudChannelV1alpha1ProvisionedService**](GoogleCloudChannelV1alpha1ProvisionedService.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Output only. Current provisioning state of the entitlement. |  [optional] [readonly] |
|**purchaseOrderId** | **String** | Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements. |  [optional] |
|**suspensionReasons** | [**List&lt;SuspensionReasonsEnum&gt;**](#List&lt;SuspensionReasonsEnum&gt;) | Output only. Enumerable of all current suspension reasons for an entitlement. |  [optional] [readonly] |
|**trialSettings** | [**GoogleCloudChannelV1alpha1TrialSettings**](GoogleCloudChannelV1alpha1TrialSettings.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time at which the entitlement is updated. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| PROVISIONING_STATE_UNSPECIFIED | &quot;PROVISIONING_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CANCELED | &quot;CANCELED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |
| PENDING | &quot;PENDING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |



## Enum: List&lt;SuspensionReasonsEnum&gt;

| Name | Value |
|---- | -----|
| SUSPENSION_REASON_UNSPECIFIED | &quot;SUSPENSION_REASON_UNSPECIFIED&quot; |
| RESELLER_INITIATED | &quot;RESELLER_INITIATED&quot; |
| TRIAL_ENDED | &quot;TRIAL_ENDED&quot; |
| RENEWAL_WITH_TYPE_CANCEL | &quot;RENEWAL_WITH_TYPE_CANCEL&quot; |
| PENDING_TOS_ACCEPTANCE | &quot;PENDING_TOS_ACCEPTANCE&quot; |
| OTHER | &quot;OTHER&quot; |



