# GmailPostmasterToolsApi.DeliveryError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorClass** | **String** | The class of delivery error. | [optional] 
**errorRatio** | **Number** | The ratio of messages where the error occurred vs all authenticated traffic. | [optional] 
**errorType** | **String** | The type of delivery error. | [optional] 



## Enum: ErrorClassEnum


* `DELIVERY_ERROR_CLASS_UNSPECIFIED` (value: `"DELIVERY_ERROR_CLASS_UNSPECIFIED"`)

* `PERMANENT_ERROR` (value: `"PERMANENT_ERROR"`)

* `TEMPORARY_ERROR` (value: `"TEMPORARY_ERROR"`)





## Enum: ErrorTypeEnum


* `DELIVERY_ERROR_TYPE_UNSPECIFIED` (value: `"DELIVERY_ERROR_TYPE_UNSPECIFIED"`)

* `RATE_LIMIT_EXCEEDED` (value: `"RATE_LIMIT_EXCEEDED"`)

* `SUSPECTED_SPAM` (value: `"SUSPECTED_SPAM"`)

* `CONTENT_SPAMMY` (value: `"CONTENT_SPAMMY"`)

* `BAD_ATTACHMENT` (value: `"BAD_ATTACHMENT"`)

* `BAD_DMARC_POLICY` (value: `"BAD_DMARC_POLICY"`)

* `LOW_IP_REPUTATION` (value: `"LOW_IP_REPUTATION"`)

* `LOW_DOMAIN_REPUTATION` (value: `"LOW_DOMAIN_REPUTATION"`)

* `IP_IN_RBL` (value: `"IP_IN_RBL"`)

* `DOMAIN_IN_RBL` (value: `"DOMAIN_IN_RBL"`)

* `BAD_PTR_RECORD` (value: `"BAD_PTR_RECORD"`)




