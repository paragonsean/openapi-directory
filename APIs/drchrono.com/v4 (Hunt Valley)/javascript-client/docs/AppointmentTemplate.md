# OpenapiJsClient.AppointmentTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **Boolean** | Indicats that the object has been soft-deleted and should not be used | [optional] [readonly] 
**dateEnd** | **String** |  | [optional] 
**dateStart** | **String** |  | [optional] 
**duration** | **Number** | Length of an appointment in minutes | [optional] 
**examRoom** | **Number** | **1-based** index for the exam room | 
**id** | **Number** |  | [optional] [readonly] 
**office** | **Number** |  | 
**openSlots** | [**[OpenSlot]**](OpenSlot.md) | Array of time intervals during which the template is available. Only computed if the available and verbose query parameters are passed. Note that only slots long enough to fit an appointment with the corresponding profile are included. | [optional] 
**profile** | **Number** | ID of the appointment profile to default to | 
**scheduledTime** | **String** |  | 
**weekDays** | **[Number]** | Array of integers that indicate week days (&#x60;0&#x60; &#x3D; Monday, ..., &#x60;6&#x60; &#x3D; Sunday) | 


