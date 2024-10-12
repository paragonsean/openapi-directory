# CalendarApi.EventFocusTimeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoDeclineMode** | **String** | Whether to decline meeting invitations which overlap Focus Time events. Valid values are declineNone, meaning that no meeting invitations are declined; declineAllConflictingInvitations, meaning that all conflicting meeting invitations that conflict with the event are declined; and declineOnlyNewConflictingInvitations, meaning that only new conflicting meeting invitations which arrive while the Focus Time event is present are to be declined. | [optional] 
**chatStatus** | **String** | The status to mark the user in Chat and related products. This can be available or doNotDisturb. | [optional] 
**declineMessage** | **String** | Response message to set if an existing event or new invitation is automatically declined by Calendar. | [optional] 


