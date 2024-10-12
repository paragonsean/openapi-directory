

# ShutdownNotificationContent

The contents of a shutdown notification. Webhooks can use this type to deserialize the request body when they get notified of an imminent shutdown.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delayUrl120** | **String** | The URL to delay shutdown by 2 hours. |  [optional] |
|**delayUrl60** | **String** | The URL to delay shutdown by 60 minutes. |  [optional] |
|**eventType** | **String** | The event for which a notification will be sent. |  [optional] |
|**guid** | **String** | The GUID for the virtual machine to be shut down. |  [optional] |
|**labName** | **String** | The lab for the schedule. |  [optional] |
|**owner** | **String** | The owner of the virtual machine. |  [optional] |
|**resourceGroupName** | **String** | The resource group name for the schedule. |  [optional] |
|**skipUrl** | **String** | The URL to skip auto-shutdown. |  [optional] |
|**subscriptionId** | **String** | The subscription ID for the schedule. |  [optional] |
|**text** | **String** | The text for the notification. |  [optional] |
|**vmName** | **String** | The virtual machine to be shut down. |  [optional] |



