

# SymbolUploadBeginRequest

A request containing information pertaining to starting a symbol upload process

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**build** | **String** | The build number. Optional for Apple. Required for Android. |  [optional] |
|**clientCallback** | **String** | The callback URL that the client can optionally provide to get status updates for the current symbol upload |  [optional] |
|**fileName** | **String** | The file name for the symbol upload |  [optional] |
|**symbolType** | [**SymbolTypeEnum**](#SymbolTypeEnum) | The type of the symbol for the current symbol upload |  |
|**version** | **String** | The version number. Optional for Apple. Required for Android. |  [optional] |



## Enum: SymbolTypeEnum

| Name | Value |
|---- | -----|
| APPLE | &quot;Apple&quot; |
| JAVA_SCRIPT | &quot;JavaScript&quot; |
| BREAKPAD | &quot;Breakpad&quot; |
| ANDROID_PROGUARD | &quot;AndroidProguard&quot; |
| UWP | &quot;UWP&quot; |



