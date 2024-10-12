

# SymbolUploadsList200ResponseInner

A single symbol upload entity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The application that this symbol upload belongs to |  |
|**fileName** | **String** | The file name for the symbol upload |  [optional] |
|**fileSize** | **BigDecimal** | The size of the file in Mebibytes. This may be 0 until the status is indexed |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The origin of the symbol upload |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status for the symbol upload |  |
|**symbolType** | [**SymbolTypeEnum**](#SymbolTypeEnum) | The type of the symbol for the current symbol upload |  |
|**symbolUploadId** | **String** | The id for the current symbol upload |  |
|**symbolsUploaded** | [**List&lt;SymbolUploadsList200ResponseInnerSymbolsUploadedInner&gt;**](SymbolUploadsList200ResponseInnerSymbolsUploadedInner.md) | The symbols found in the upload. This may be empty until the status is indexed |  [optional] |
|**timestamp** | **OffsetDateTime** | When the symbol upload was committed, or last transaction time if not committed |  [optional] |
|**user** | [**SymbolUploadsList200ResponseInnerUser**](SymbolUploadsList200ResponseInnerUser.md) |  |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| USER | &quot;User&quot; |
| SYSTEM | &quot;System&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;created&quot; |
| COMMITTED | &quot;committed&quot; |
| ABORTED | &quot;aborted&quot; |
| PROCESSING | &quot;processing&quot; |
| INDEXED | &quot;indexed&quot; |
| FAILED | &quot;failed&quot; |



## Enum: SymbolTypeEnum

| Name | Value |
|---- | -----|
| APPLE | &quot;Apple&quot; |
| JAVA_SCRIPT | &quot;JavaScript&quot; |
| BREAKPAD | &quot;Breakpad&quot; |
| ANDROID_PROGUARD | &quot;AndroidProguard&quot; |
| UWP | &quot;UWP&quot; |



