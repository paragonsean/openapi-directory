

# CreateExportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceSpecification** | [**CreateExportRequestResourceSpecification**](CreateExportRequestResourceSpecification.md) |  |  |
|**fileFormat** | [**FileFormatEnum**](#FileFormatEnum) | The file format of the bot or bot locale definition files. |  |
|**filePassword** | **String** | An password to use to encrypt the exported archive. Using a password is optional, but you should encrypt the archive to protect the data in transit between Amazon Lex and your local computer. |  [optional] |



## Enum: FileFormatEnum

| Name | Value |
|---- | -----|
| LEX_JSON | &quot;LexJson&quot; |
| TSV | &quot;TSV&quot; |
| CSV | &quot;CSV&quot; |



