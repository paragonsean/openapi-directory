# CloudLifeSciencesApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerKilled** | [**ContainerKilledEvent**](ContainerKilledEvent.md) |  | [optional] 
**containerStarted** | [**ContainerStartedEvent**](ContainerStartedEvent.md) |  | [optional] 
**containerStopped** | [**ContainerStoppedEvent**](ContainerStoppedEvent.md) |  | [optional] 
**delayed** | [**DelayedEvent**](DelayedEvent.md) |  | [optional] 
**description** | **String** | A human-readable description of the event. Note that these strings can change at any time without notice. Any application logic must use the information in the &#x60;details&#x60; field. | [optional] 
**failed** | [**FailedEvent**](FailedEvent.md) |  | [optional] 
**pullStarted** | [**PullStartedEvent**](PullStartedEvent.md) |  | [optional] 
**pullStopped** | [**PullStoppedEvent**](PullStoppedEvent.md) |  | [optional] 
**timestamp** | **String** | The time at which the event occurred. | [optional] 
**unexpectedExitStatus** | [**UnexpectedExitStatusEvent**](UnexpectedExitStatusEvent.md) |  | [optional] 
**workerAssigned** | [**WorkerAssignedEvent**](WorkerAssignedEvent.md) |  | [optional] 
**workerReleased** | [**WorkerReleasedEvent**](WorkerReleasedEvent.md) |  | [optional] 


