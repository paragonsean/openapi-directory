

# InputFileReadConfiguration

Describe how to read the file. If FileFormatStrategy is CSV, csvFileReadProperties is required. Otherwise the xmlFileReadProperties is required. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csvFileReadProperties** | [**InputFileReadCsvConfiguration**](InputFileReadCsvConfiguration.md) |  |  [optional] |
|**cultureName** | **String** | The culture name of the file.  (i.e. fr-FR). If null then Invariant culture will be used. |  [optional] |
|**encodingTypeName** | **String** | The encoding type. UTF-8 by default. |  [optional] |
|**format** | **FileFormatStrategy** |  |  |
|**xmlFileReadProperties** | [**InputFileReadXmlConfiguration**](InputFileReadXmlConfiguration.md) |  |  [optional] |



