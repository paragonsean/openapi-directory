

# JobCreationReason

Reason about why a Job was created from a [`jobs.query`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query) method when used with `JOB_CREATION_OPTIONAL` Job creation mode. For [`jobs.insert`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert) method calls it will always be `REQUESTED`. This feature is not yet available. Jobs will always be created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Output only. Specifies the high level reason why a Job was created. |  [optional] [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| LONG_RUNNING | &quot;LONG_RUNNING&quot; |
| LARGE_RESULTS | &quot;LARGE_RESULTS&quot; |
| OTHER | &quot;OTHER&quot; |



