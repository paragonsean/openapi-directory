

# PrescriptionMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] [readonly] |
|**doctor** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**jsonData** | **String** | Data sent along with &#x60;NewRx&#x60;, &#x60;RefillRequest&#x60;, and &#x60;RefillResponses&#x60; messages. The format varies, but most likely it will contain &#x60;BenefitsCoordination&#x60; section with insurance info and &#x60;MedicationPrescribed&#x60; with medication info. &#x60;Patient&#x60;, &#x60;Pharmacy&#x60;, and &#x60;Prescriber&#x60; are also usually present. |  [optional] [readonly] |
|**messageDirection** | [**MessageDirectionEnum**](#MessageDirectionEnum) | Possible values are &#x60;Outgoing&#x60; and &#x60;Incoming&#x60;. |  [optional] [readonly] |
|**messageStatus** | **String** | Message status for Incoming and Outgoing values. Success message for message_type are: &#x60;NewRx&#x60; : &#x60;Sent&#x60;, &#x60;RefillRequest&#x60; : &#x60;Received&#x60;, &#x60;RefillResponse&#x60; : &#x60;Sent&#x60;. |  [optional] [readonly] |
|**messageType** | **String** | Possible values are &#x60;NewRx&#x60; for outgoing new prescriptions, &#x60;RefillRequest&#x60; for incoming refill requests, &#x60;RefillResponse&#x60; for outgoing refill responses, &#x60;Error&#x60; for incoming errors, &#x60;Status&#x60; and &#x60;Verify&#x60; for incoming status reports from Surescripts. |  [optional] |
|**parentMessage** | **String** | Refers to the parent message, used for refill responses and incoming error/status reports. |  [optional] [readonly] |
|**patient** | **Integer** | An optional field which refers to a patient. |  [optional] |
|**pharmacy** | **String** | NCPDPID allocated #ID of the Pharmacy |  [optional] |



## Enum: MessageDirectionEnum

| Name | Value |
|---- | -----|
| I | &quot;I&quot; |
| O | &quot;O&quot; |



