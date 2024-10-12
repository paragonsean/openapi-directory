

# ReconfigurationInformation

Information about current reconfiguration like phase, type, previous configuration role of replica and reconfiguration start date time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**previousConfigurationRole** | **ReplicaRole** |  |  [optional] |
|**reconfigurationPhase** | **ReconfigurationPhase** |  |  [optional] |
|**reconfigurationStartTimeUtc** | **OffsetDateTime** | Start time (in UTC) of the ongoing reconfiguration. If no reconfiguration is taking place then this value will be zero date-time. |  [optional] |
|**reconfigurationType** | **ReconfigurationType** |  |  [optional] |



