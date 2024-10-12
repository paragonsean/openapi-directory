

# ScheduledUpdateGroupActionRequest

Describes information used for one or more scheduled scaling action updates in a <a>BatchPutScheduledUpdateGroupAction</a> operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scheduledActionName** | [**String**](String.md) |  |  |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**recurrence** | [**String**](String.md) |  |  [optional] |
|**minSize** | [**Integer**](Integer.md) |  |  [optional] |
|**maxSize** | [**Integer**](Integer.md) |  |  [optional] |
|**desiredCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**timeZone** | [**String**](String.md) |  |  [optional] |



