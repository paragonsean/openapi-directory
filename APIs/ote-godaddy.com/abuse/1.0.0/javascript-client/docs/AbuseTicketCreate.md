# OpenapiJsClient.AbuseTicketCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **String** | Additional information that may assist the abuse investigator. ie: server logs or email headers/body for SPAM | [optional] 
**infoUrl** | **String** | Reporter URL if housing additional information that may assist the abuse investigator | [optional] 
**intentional** | **Boolean** | Do you believe this is intentional abuse by the domain holder? | [optional] [default to false]
**proxy** | **String** | The Proxy information required to view the abuse being reported. ie: Specific IP used, or country of IP viewing from | [optional] 
**source** | **String** | The URL or IP where live abuse content is located at. ie: https://www.example.com/bad_stuff/bad.php | [optional] 
**target** | **String** | The brand/company the abuse is targeting. ie: brand name/bank name | [optional] 
**type** | **String** | The type of abuse being reported. | [optional] 



## Enum: TypeEnum


* `A_RECORD` (value: `"A_RECORD"`)

* `CHILD_ABUSE` (value: `"CHILD_ABUSE"`)

* `CONTENT` (value: `"CONTENT"`)

* `FRAUD_WIRE` (value: `"FRAUD_WIRE"`)

* `IP_BLOCK` (value: `"IP_BLOCK"`)

* `MALWARE` (value: `"MALWARE"`)

* `NETWORK_ABUSE` (value: `"NETWORK_ABUSE"`)

* `PHISHING` (value: `"PHISHING"`)

* `SPAM` (value: `"SPAM"`)




