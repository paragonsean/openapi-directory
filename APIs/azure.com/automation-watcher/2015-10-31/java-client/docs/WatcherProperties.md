

# WatcherProperties

Definition of the watcher properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time. |  [optional] [readonly] |
|**description** | **String** | Gets or sets the description. |  [optional] |
|**executionFrequencyInSeconds** | **Long** | Gets or sets the frequency at which the watcher is invoked. |  [optional] |
|**lastModifiedBy** | **String** | Details of the user who last modified the watcher. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the last modified time. |  [optional] [readonly] |
|**scriptName** | **String** | Gets or sets the name of the script the watcher is attached to, i.e. the name of an existing runbook. |  [optional] |
|**scriptParameters** | **Map&lt;String, String&gt;** | Gets or sets the parameters of the script. |  [optional] |
|**scriptRunOn** | **String** | Gets or sets the name of the hybrid worker group the watcher will run on. |  [optional] |
|**status** | **String** | Gets the current status of the watcher. |  [optional] [readonly] |



