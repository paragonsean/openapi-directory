# AkeneoPimRestApi.PostPamAssetsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **[String]** | Codes of the PAM asset categories in which the asset is classified | [optional] 
**code** | **String** | PAM asset code | 
**description** | **String** | Description of the PAM asset | [optional] 
**endOfUse** | **String** | Date on which the PAM asset expire | [optional] 
**localizable** | **Boolean** | Whether the asset is localized or not, meaning if you want to have different reference files for each of your locale | [optional] [default to false]
**referenceFiles** | [**[PAMAssetsAllOfEmbeddedItemsInnerAllOfReferenceFilesInner]**](PAMAssetsAllOfEmbeddedItemsInnerAllOfReferenceFilesInner.md) | Reference files of the PAM asset | [optional] 
**tags** | **[String]** | Tags of the PAM asset | [optional] 
**variationFiles** | [**[PAMAssetsAllOfEmbeddedItemsInnerAllOfVariationFilesInner]**](PAMAssetsAllOfEmbeddedItemsInnerAllOfVariationFilesInner.md) | Variations of the PAM asset | [optional] 


