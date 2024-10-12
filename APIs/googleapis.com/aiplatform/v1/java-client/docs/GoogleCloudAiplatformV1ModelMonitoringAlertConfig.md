

# GoogleCloudAiplatformV1ModelMonitoringAlertConfig

The alert config for model monitoring.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAlertConfig** | [**GoogleCloudAiplatformV1ModelMonitoringAlertConfigEmailAlertConfig**](GoogleCloudAiplatformV1ModelMonitoringAlertConfigEmailAlertConfig.md) |  |  [optional] |
|**enableLogging** | **Boolean** | Dump the anomalies to Cloud Logging. The anomalies will be put to json payload encoded from proto google.cloud.aiplatform.logging.ModelMonitoringAnomaliesLogEntry. This can be further sinked to Pub/Sub or any other services supported by Cloud Logging. |  [optional] |
|**notificationChannels** | **List&lt;String&gt;** | Resource names of the NotificationChannels to send alert. Must be of the format &#x60;projects//notificationChannels/&#x60; |  [optional] |



