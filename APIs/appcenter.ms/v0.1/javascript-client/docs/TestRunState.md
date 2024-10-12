# AppCenterClient.TestRunState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exitCode** | **Number** | The exit code that the client should use when exiting. Used for indicating status to the caller of the client. 0: test run completes with no failing tests 1: test run completes with at least one failing test 2: test run failed to complete. Status for test run is unknown  | [optional] 
**message** | **[String]** | Multi-line message that describes the status | [optional] 
**waitTime** | **Number** | Time (in seconds) that the client should wait for before checking the status again | [optional] 


