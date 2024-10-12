# AppCenterClient.TestRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appVersion** | **String** | The compiled version of the app binary | [optional] 
**date** | **String** | The date and time the test was uploaded | [optional] 
**description** | **String** | Human readable explanation of the current test status | [optional] 
**id** | **String** | The unique id of the test upload | [optional] 
**platform** | **String** | The device platform targeted by the test. Possible values are &#39;ios&#39; or &#39;android&#39; | [optional] 
**resultStatus** | **String** | The passed/failed state | [optional] 
**runStatus** | **String** | The current status of the test run, in relation to the various phases | [optional] 
**state** | **String** | Deprecated. Use runStatus instead. | [optional] 
**stats** | [**TestRunStatistics**](TestRunStatistics.md) |  | [optional] 
**status** | **String** | Deprecated. Use resultStatus instead. | [optional] 
**testSeries** | **String** | The name of the test series with which this test upload is associated | [optional] 
**testType** | **String** | The name of the test framework used to run this test | [optional] 


