# TwilioTaskrouter.TaskrouterV1WorkspaceTaskTaskReservation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskReservation resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**links** | **Object** | The URLs of related resources. | [optional] 
**reservationStatus** | [**TaskReservationEnumStatus**](TaskReservationEnumStatus.md) |  | [optional] 
**sid** | **String** | The unique string that we created to identify the TaskReservation resource. | [optional] 
**taskSid** | **String** | The SID of the reserved Task resource. | [optional] 
**url** | **String** | The absolute URL of the TaskReservation reservation. | [optional] 
**workerName** | **String** | The &#x60;friendly_name&#x60; of the Worker that is reserved. | [optional] 
**workerSid** | **String** | The SID of the reserved Worker resource. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that this task is contained within. | [optional] 


