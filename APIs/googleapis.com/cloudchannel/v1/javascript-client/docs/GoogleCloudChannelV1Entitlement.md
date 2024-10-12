# CloudChannelApi.GoogleCloudChannelV1Entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associationInfo** | [**GoogleCloudChannelV1AssociationInfo**](GoogleCloudChannelV1AssociationInfo.md) |  | [optional] 
**billingAccount** | **String** | Optional. The billing account resource name that is used to pay for this entitlement. | [optional] 
**commitmentSettings** | [**GoogleCloudChannelV1CommitmentSettings**](GoogleCloudChannelV1CommitmentSettings.md) |  | [optional] 
**createTime** | **String** | Output only. The time at which the entitlement is created. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}. | [optional] [readonly] 
**offer** | **String** | Required. The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}. | [optional] 
**parameters** | [**[GoogleCloudChannelV1Parameter]**](GoogleCloudChannelV1Parameter.md) | Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. For Google Workspace, the following Parameters may be accepted as input: - max_units: The maximum assignable units for a flexible offer OR - num_units: The total commitment for commitment-based offers The response may additionally include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. For Google Cloud billing subaccounts, the following Parameter may be accepted as input: - display_name: The display name of the billing subaccount. | [optional] 
**provisionedService** | [**GoogleCloudChannelV1ProvisionedService**](GoogleCloudChannelV1ProvisionedService.md) |  | [optional] 
**provisioningState** | **String** | Output only. Current provisioning state of the entitlement. | [optional] [readonly] 
**purchaseOrderId** | **String** | Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements. | [optional] 
**suspensionReasons** | **[String]** | Output only. Enumerable of all current suspension reasons for an entitlement. | [optional] [readonly] 
**trialSettings** | [**GoogleCloudChannelV1TrialSettings**](GoogleCloudChannelV1TrialSettings.md) |  | [optional] 
**updateTime** | **String** | Output only. The time at which the entitlement is updated. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `PROVISIONING_STATE_UNSPECIFIED` (value: `"PROVISIONING_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUSPENDED` (value: `"SUSPENDED"`)





## Enum: [SuspensionReasonsEnum]


* `SUSPENSION_REASON_UNSPECIFIED` (value: `"SUSPENSION_REASON_UNSPECIFIED"`)

* `RESELLER_INITIATED` (value: `"RESELLER_INITIATED"`)

* `TRIAL_ENDED` (value: `"TRIAL_ENDED"`)

* `RENEWAL_WITH_TYPE_CANCEL` (value: `"RENEWAL_WITH_TYPE_CANCEL"`)

* `PENDING_TOS_ACCEPTANCE` (value: `"PENDING_TOS_ACCEPTANCE"`)

* `OTHER` (value: `"OTHER"`)




