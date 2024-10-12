

# AbuseTicket

The associated fields returned, given a unique abuse ticket id

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closed** | **Boolean** | Is this abuse ticket closed? |  |
|**closedAt** | **String** | The date the abuse ticket was closed |  |
|**createdAt** | **String** | The date the abuse ticket was created |  |
|**domainIp** | **String** | The domain or IP the suspected abuse was reported against |  |
|**reporter** | **String** | The shopper id of the person who reported the suspected abuse |  |
|**source** | **String** | The single URL or IP the suspected abuse was reported against |  |
|**target** | **String** | The company the suspected abuse is targeting |  |
|**ticketId** | **String** | Abuse ticket ID |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of abuse being reported |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| A_RECORD | &quot;A_RECORD&quot; |
| CHILD_ABUSE | &quot;CHILD_ABUSE&quot; |
| CONTENT | &quot;CONTENT&quot; |
| FRAUD_WIRE | &quot;FRAUD_WIRE&quot; |
| IP_BLOCK | &quot;IP_BLOCK&quot; |
| MALWARE | &quot;MALWARE&quot; |
| NETWORK_ABUSE | &quot;NETWORK_ABUSE&quot; |
| PHISHING | &quot;PHISHING&quot; |
| SPAM | &quot;SPAM&quot; |



