# VertexAiApi.GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailAlertConfig** | [**GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig**](GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig.md) |  | [optional] 
**enableLogging** | **Boolean** | Dump the anomalies to Cloud Logging. The anomalies will be put to json payload encoded from proto google.cloud.aiplatform.logging.ModelMonitoringAnomaliesLogEntry. This can be further sinked to Pub/Sub or any other services supported by Cloud Logging. | [optional] 
**notificationChannels** | **[String]** | Resource names of the NotificationChannels to send alert. Must be of the format &#x60;projects//notificationChannels/&#x60; | [optional] 


