# SensitiveDataProtectionDlp.GooglePrivacyDlpV2InfoType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the information type. Either a name of your choosing when creating a CustomInfoType, or one of the names listed at https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference when specifying a built-in type. When sending Cloud DLP results to Data Catalog, infoType names should conform to the pattern &#x60;[A-Za-z0-9$_-]{1,64}&#x60;. | [optional] 
**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  | [optional] 
**version** | **String** | Optional version name for this InfoType. | [optional] 


