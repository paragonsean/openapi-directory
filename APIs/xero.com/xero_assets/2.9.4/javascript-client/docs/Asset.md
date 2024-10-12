# XeroAssetsApi.Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountingBookValue** | **Number** | The accounting value of the asset | [optional] 
**assetId** | **String** | The Xero-generated Id for the asset | [optional] 
**assetName** | **String** | The name of the asset | 
**assetNumber** | **String** | Must be unique. | [optional] 
**assetStatus** | [**AssetStatus**](AssetStatus.md) |  | [optional] 
**assetTypeId** | **String** | The Xero-generated Id for the asset type | [optional] 
**bookDepreciationDetail** | [**BookDepreciationDetail**](BookDepreciationDetail.md) |  | [optional] 
**bookDepreciationSetting** | [**BookDepreciationSetting**](BookDepreciationSetting.md) |  | [optional] 
**canRollback** | **Boolean** | Boolean to indicate whether depreciation can be rolled back for this asset individually. This is true if it doesn&#39;t have &#39;legacy&#39; journal entries and if there is no lock period that would prevent this asset from rolling back. | [optional] 
**disposalDate** | **Date** | The date the asset was disposed | [optional] 
**disposalPrice** | **Number** | The price the asset was disposed at | [optional] 
**isDeleteEnabledForDate** | **Boolean** | Boolean to indicate whether delete is enabled | [optional] 
**purchaseDate** | **Date** | The date the asset was purchased YYYY-MM-DD | [optional] 
**purchasePrice** | **Number** | The purchase price of the asset | [optional] 
**serialNumber** | **String** | The asset&#39;s serial number | [optional] 
**warrantyExpiryDate** | **String** | The date the asset’s warranty expires (if needed) YYYY-MM-DD | [optional] 


