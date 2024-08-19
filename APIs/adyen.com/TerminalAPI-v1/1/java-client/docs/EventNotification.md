

# EventNotification

It conveys Information related to the event, and possible action (maintenance, message to display). Content of the EventNotification message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerLanguage** | **String** | If the language is selected by the Sale System before the request to the POI. |  [optional] |
|**displayOutput** | [**List&lt;DisplayOutput&gt;**](DisplayOutput.md) |  |  [optional] |
|**eventDetails** | **String** | If present, the Sale logs it for further examination. |  [optional] |
|**eventToNotify** | **EventToNotify** |  |  |
|**maintenanceRequiredFlag** | **Boolean** | Indicates if the occurred event requires maintenance call or action. |  [optional] |
|**rejectedMessage** | **String** | Mandatory if EventToNotify is Reject, absent in other cases. |  [optional] |
|**timeStamp** | **OffsetDateTime** | Date and time of a transaction for the Sale System, the POI System or the Acquirer. |  |



