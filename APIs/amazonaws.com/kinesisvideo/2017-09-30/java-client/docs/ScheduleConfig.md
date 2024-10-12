

# ScheduleConfig

<p>This API enables you to specify the duration that the camera, or local media file, should record onto the Edge Agent. The <code>ScheduleConfig</code> consists of the <code>ScheduleExpression</code> and the <code>DurationInMinutes</code> attributes. </p> <p>If the <code>ScheduleConfig</code> is not provided in the <code>RecorderConfig</code>, then the Edge Agent will always be set to recording mode.</p> <p>If the <code>ScheduleConfig</code> is not provided in the <code>UploaderConfig</code>, then the Edge Agent will upload at regular intervals (every 1 hour).</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scheduleExpression** | [**String**](String.md) |  |  |
|**durationInSeconds** | [**Integer**](Integer.md) |  |  |



