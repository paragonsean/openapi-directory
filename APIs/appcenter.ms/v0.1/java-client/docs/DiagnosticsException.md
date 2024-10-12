

# DiagnosticsException

a exception

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frames** | [**List&lt;DiagnosticsExceptionFramesInner&gt;**](DiagnosticsExceptionFramesInner.md) | frames of the excetpion |  |
|**innerExceptions** | [**List&lt;DiagnosticsException&gt;**](DiagnosticsException.md) |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | SDK/Platform this thread is beeing generated from |  [optional] |
|**reason** | **String** | Reason of the exception |  [optional] |
|**relevant** | **Boolean** | relevant exception (crashed) |  [optional] |
|**type** | **String** | Type of the exception (NSSomethingException, NullPointerException) |  [optional] |



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



