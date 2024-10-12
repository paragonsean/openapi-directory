

# AbuseTicketCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**info** | **String** | Additional information that may assist the abuse investigator. ie: server logs or email headers/body for SPAM |  [optional] |
|**infoUrl** | **String** | Reporter URL if housing additional information that may assist the abuse investigator |  [optional] |
|**intentional** | **Boolean** | Do you believe this is intentional abuse by the domain holder? |  [optional] |
|**proxy** | **String** | The Proxy information required to view the abuse being reported. ie: Specific IP used, or country of IP viewing from |  [optional] |
|**source** | **String** | The URL or IP where live abuse content is located at. ie: https://www.example.com/bad_stuff/bad.php |  [optional] |
|**target** | **String** | The brand/company the abuse is targeting. ie: brand name/bank name |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of abuse being reported. |  [optional] |



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



