# AppCenterClient.Thread

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crashed** | **Boolean** | True if this thread crashed | [optional] 
**exception** | [**Exception**](Exception.md) |  | [optional] 
**frames** | [**[ExceptionFramesInner]**](ExceptionFramesInner.md) | frames of that thread | 
**platform** | **String** | SDK/Platform this thread is beeing generated from | [optional] 
**relevant** | **Boolean** | Shows if a thread is relevant or not. Is false if all frames are non relevant, otherwise true | [optional] 
**title** | **String** | name of the thread | 



## Enum: PlatformEnum


* `ios` (value: `"ios"`)

* `android` (value: `"android"`)

* `xamarin` (value: `"xamarin"`)

* `react-native` (value: `"react-native"`)

* `ndk` (value: `"ndk"`)

* `unity` (value: `"unity"`)

* `other` (value: `"other"`)




