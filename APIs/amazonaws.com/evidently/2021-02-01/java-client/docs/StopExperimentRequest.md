

# StopExperimentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**desiredState** | [**DesiredStateEnum**](#DesiredStateEnum) | Specify whether the experiment is to be considered &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;CANCELLED&lt;/code&gt; after it stops. |  [optional] |
|**reason** | **String** | A string that describes why you are stopping the experiment. |  [optional] |



## Enum: DesiredStateEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;COMPLETED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



