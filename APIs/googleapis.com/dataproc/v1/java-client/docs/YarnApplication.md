

# YarnApplication

A YARN application created by a job. Application information is a subset of org.apache.hadoop.yarn.proto.YarnProtos.ApplicationReportProto.Beta Feature: This report is available for testing purposes only. It may be changed before final release.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The application name. |  [optional] |
|**progress** | **Float** | Required. The numerical progress of the application, from 1 to 100. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Required. The application state. |  [optional] |
|**trackingUrl** | **String** | Optional. The HTTP URL of the ApplicationMaster, HistoryServer, or TimelineServer that provides application-specific information. The URL uses the internal hostname, and requires a proxy server for resolution and, possibly, access. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NEW | &quot;NEW&quot; |
| NEW_SAVING | &quot;NEW_SAVING&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FINISHED | &quot;FINISHED&quot; |
| FAILED | &quot;FAILED&quot; |
| KILLED | &quot;KILLED&quot; |



