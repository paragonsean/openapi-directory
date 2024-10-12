

# DriveActivity

A single Drive activity comprising one or more Actions by one or more Actors on one or more Targets. Some Action groupings occur spontaneously, such as moving an item into a shared folder triggering a permission change. Other groupings of related Actions, such as multiple Actors editing one item or moving multiple files into a new folder, are controlled by the selection of a ConsolidationStrategy in the QueryDriveActivityRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;Action&gt;**](Action.md) | Details on all actions in this activity. |  [optional] |
|**actors** | [**List&lt;Actor&gt;**](Actor.md) | All actor(s) responsible for the activity. |  [optional] |
|**primaryActionDetail** | [**ActionDetail**](ActionDetail.md) |  |  [optional] |
|**targets** | [**List&lt;Target&gt;**](Target.md) | All Google Drive objects this activity is about (e.g. file, folder, drive). This represents the state of the target immediately after the actions occurred. |  [optional] |
|**timeRange** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**timestamp** | **String** | The activity occurred at this specific time. |  [optional] |



