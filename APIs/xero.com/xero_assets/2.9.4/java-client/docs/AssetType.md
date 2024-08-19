

# AssetType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accumulatedDepreciationAccountId** | **UUID** | The account for accumulated depreciation of fixed assets of this type |  [optional] |
|**assetTypeId** | **UUID** | Xero generated unique identifier for asset types |  [optional] |
|**assetTypeName** | **String** | The name of the asset type |  |
|**bookDepreciationSetting** | [**BookDepreciationSetting**](BookDepreciationSetting.md) |  |  |
|**depreciationExpenseAccountId** | **UUID** | The expense account for the depreciation of fixed assets of this type |  [optional] |
|**fixedAssetAccountId** | **UUID** | The asset account for fixed assets of this type |  [optional] |
|**locks** | **Integer** | All asset types that have accumulated depreciation for any assets that use them are deemed ‘locked’ and cannot be removed. |  [optional] |



