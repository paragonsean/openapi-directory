

# SymbolsList200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateSymbolIds** | **List&lt;String&gt;** | The other symbols in the same file |  |
|**appId** | **String** | The application that this symbol belongs to |  |
|**build** | **String** | The build number. Optional for Apple. Required for Android. |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The origin of the symbol file |  |
|**platform** | **String** | The platform that this symbol is associated with |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the symbol is ignored. |  |
|**symbolId** | **String** | The unique id for this symbol (uuid) |  |
|**symbolUploadId** | **String** | The id of the symbol upload this symbol belongs to. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the symbol for the current symbol upload |  |
|**url** | **String** | The path name of the symbol file in blob storage |  |
|**version** | **String** | The version number. Optional for Apple. Required for Android. |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;System&quot; |
| USER | &quot;User&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| IGNORED | &quot;ignored&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APPLE | &quot;Apple&quot; |
| JAVA_SCRIPT | &quot;JavaScript&quot; |
| BREAKPAD | &quot;Breakpad&quot; |
| ANDROID_PROGUARD | &quot;AndroidProguard&quot; |
| UWP | &quot;UWP&quot; |



