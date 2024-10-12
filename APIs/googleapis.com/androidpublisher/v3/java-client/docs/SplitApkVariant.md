

# SplitApkVariant

Variant is a group of APKs that covers a part of the device configuration space. APKs from multiple variants are never combined on one device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apkSet** | [**List&lt;ApkSet&gt;**](ApkSet.md) | Set of APKs, one set per module. |  [optional] |
|**targeting** | [**VariantTargeting**](VariantTargeting.md) |  |  [optional] |
|**variantNumber** | **Integer** | Number of the variant, starting at 0 (unless overridden). A device will receive APKs from the first variant that matches the device configuration, with higher variant numbers having priority over lower variant numbers. |  [optional] |



