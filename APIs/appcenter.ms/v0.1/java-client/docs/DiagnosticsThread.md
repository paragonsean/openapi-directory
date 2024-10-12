

# DiagnosticsThread

a thread representation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crashed** | **Boolean** | True if this thread crashed |  [optional] |
|**exception** | [**DiagnosticsException**](DiagnosticsException.md) |  |  [optional] |
|**frames** | [**List&lt;DiagnosticsExceptionFramesInner&gt;**](DiagnosticsExceptionFramesInner.md) | frames of that thread |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | SDK/Platform this thread is beeing generated from |  [optional] |
|**relevant** | **Boolean** | Shows if a thread is relevant or not. Is false if all frames are non relevant, otherwise true |  [optional] |
|**title** | **String** | name of the thread |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| IOS | &quot;ios&quot; |
| ANDROID | &quot;android&quot; |
| XAMARIN | &quot;xamarin&quot; |
| REACT_NATIVE | &quot;react-native&quot; |
| NDK | &quot;ndk&quot; |
| UNITY | &quot;unity&quot; |
| OTHER | &quot;other&quot; |



