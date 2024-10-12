# AppCenterClient.Exception

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frames** | [**[ExceptionFramesInner]**](ExceptionFramesInner.md) | frames of the excetpion | 
**innerExceptions** | [**[Exception]**](Exception.md) |  | [optional] 
**platform** | **String** | SDK/Platform this thread is beeing generated from | [optional] 
**reason** | **String** | Reason of the exception | [optional] 
**relevant** | **Boolean** | relevant exception (crashed) | [optional] 
**type** | **String** | Type of the exception (NSSomethingException, NullPointerException) | [optional] 



## Enum: PlatformEnum


* `ios` (value: `"ios"`)

* `android` (value: `"android"`)

* `xamarin` (value: `"xamarin"`)

* `react-native` (value: `"react-native"`)

* `ndk` (value: `"ndk"`)

* `unity` (value: `"unity"`)

* `other` (value: `"other"`)




