

# WatchVariableRequest

Request for the `WatchVariable()` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newerThan** | **String** | If specified, checks the current timestamp of the variable and if the current timestamp is newer than &#x60;newerThan&#x60; timestamp, the method returns immediately. If not specified or the variable has an older timestamp, the watcher waits for a the value to change before returning. |  [optional] |



