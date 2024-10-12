

# GoogleDevtoolsRemotebuildbotCommandDurations

CommandDuration contains the various duration metrics tracked when a bot performs a command.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**casRelease** | **String** | The time spent to release the CAS blobs used by the task. |  [optional] |
|**cmWaitForAssignment** | **String** | The time spent waiting for Container Manager to assign an asynchronous container for execution. |  [optional] |
|**dockerPrep** | **String** | The time spent preparing the command to be run in a Docker container (includes pulling the Docker image, if necessary). |  [optional] |
|**dockerPrepStartTime** | **String** | The timestamp when docker preparation begins. |  [optional] |
|**download** | **String** | The time spent downloading the input files and constructing the working directory. |  [optional] |
|**downloadStartTime** | **String** | The timestamp when downloading the input files begins. |  [optional] |
|**execStartTime** | **String** | The timestamp when execution begins. |  [optional] |
|**execution** | **String** | The time spent executing the command (i.e., doing useful work). |  [optional] |
|**isoPrepDone** | **String** | The timestamp when preparation is done and bot starts downloading files. |  [optional] |
|**overall** | **String** | The time spent completing the command, in total. |  [optional] |
|**stderr** | **String** | The time spent uploading the stderr logs. |  [optional] |
|**stdout** | **String** | The time spent uploading the stdout logs. |  [optional] |
|**upload** | **String** | The time spent uploading the output files. |  [optional] |
|**uploadStartTime** | **String** | The timestamp when uploading the output files begins. |  [optional] |



