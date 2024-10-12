# CloudChannelApi.GoogleCloudChannelV1alpha1EntitlementEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement** | **String** | Resource name of an entitlement of the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} | [optional] 
**eventType** | **String** | Type of event which happened on the entitlement. | [optional] 



## Enum: EventTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `CREATED` (value: `"CREATED"`)

* `PRICE_PLAN_SWITCHED` (value: `"PRICE_PLAN_SWITCHED"`)

* `COMMITMENT_CHANGED` (value: `"COMMITMENT_CHANGED"`)

* `RENEWED` (value: `"RENEWED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `ACTIVATED` (value: `"ACTIVATED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SKU_CHANGED` (value: `"SKU_CHANGED"`)

* `RENEWAL_SETTING_CHANGED` (value: `"RENEWAL_SETTING_CHANGED"`)

* `PAID_SERVICE_STARTED` (value: `"PAID_SERVICE_STARTED"`)

* `LICENSE_ASSIGNMENT_CHANGED` (value: `"LICENSE_ASSIGNMENT_CHANGED"`)

* `LICENSE_CAP_CHANGED` (value: `"LICENSE_CAP_CHANGED"`)




