# BeezUpMerchantApi.InputFileReadConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csvFileReadProperties** | [**InputFileReadCsvConfiguration**](InputFileReadCsvConfiguration.md) |  | [optional] 
**cultureName** | **String** | The culture name of the file.  (i.e. fr-FR). If null then Invariant culture will be used. | [optional] [default to &#39;&#39;]
**encodingTypeName** | **String** | The encoding type. UTF-8 by default. | [optional] [default to &#39;UTF-8&#39;]
**format** | [**FileFormatStrategy**](FileFormatStrategy.md) |  | 
**xmlFileReadProperties** | [**InputFileReadXmlConfiguration**](InputFileReadXmlConfiguration.md) |  | [optional] 


