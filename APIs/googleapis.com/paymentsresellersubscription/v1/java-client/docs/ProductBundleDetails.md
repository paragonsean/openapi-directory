

# ProductBundleDetails

Details for a bundle product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundleElements** | [**List&lt;GoogleCloudPaymentsResellerSubscriptionV1ProductBundleDetailsBundleElement&gt;**](GoogleCloudPaymentsResellerSubscriptionV1ProductBundleDetailsBundleElement.md) | The individual products that are included in the bundle. |  [optional] |
|**entitlementMode** | [**EntitlementModeEnum**](#EntitlementModeEnum) | The entitlement mode of the bundle product. |  [optional] |



## Enum: EntitlementModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITLEMENT_MODE_UNSPECIFIED&quot; |
| FULL | &quot;ENTITLEMENT_MODE_FULL&quot; |
| INCREMENTAL | &quot;ENTITLEMENT_MODE_INCREMENTAL&quot; |



