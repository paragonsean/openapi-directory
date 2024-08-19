# AdyenTerminalApi.EventNotification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerLanguage** | **String** | If the language is selected by the Sale System before the request to the POI. | [optional] 
**displayOutput** | [**[DisplayOutput]**](DisplayOutput.md) |  | [optional] 
**eventDetails** | **String** | If present, the Sale logs it for further examination. | [optional] 
**eventToNotify** | [**EventToNotify**](EventToNotify.md) |  | 
**maintenanceRequiredFlag** | **Boolean** | Indicates if the occurred event requires maintenance call or action. | [optional] [default to false]
**rejectedMessage** | **String** | Mandatory if EventToNotify is Reject, absent in other cases. | [optional] 
**timeStamp** | **Date** | Date and time of a transaction for the Sale System, the POI System or the Acquirer. | 


