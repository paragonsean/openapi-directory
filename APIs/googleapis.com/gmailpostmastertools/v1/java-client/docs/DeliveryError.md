

# DeliveryError

Metric on a particular delivery error type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorClass** | [**ErrorClassEnum**](#ErrorClassEnum) | The class of delivery error. |  [optional] |
|**errorRatio** | **Double** | The ratio of messages where the error occurred vs all authenticated traffic. |  [optional] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) | The type of delivery error. |  [optional] |



## Enum: ErrorClassEnum

| Name | Value |
|---- | -----|
| DELIVERY_ERROR_CLASS_UNSPECIFIED | &quot;DELIVERY_ERROR_CLASS_UNSPECIFIED&quot; |
| PERMANENT_ERROR | &quot;PERMANENT_ERROR&quot; |
| TEMPORARY_ERROR | &quot;TEMPORARY_ERROR&quot; |



## Enum: ErrorTypeEnum

| Name | Value |
|---- | -----|
| DELIVERY_ERROR_TYPE_UNSPECIFIED | &quot;DELIVERY_ERROR_TYPE_UNSPECIFIED&quot; |
| RATE_LIMIT_EXCEEDED | &quot;RATE_LIMIT_EXCEEDED&quot; |
| SUSPECTED_SPAM | &quot;SUSPECTED_SPAM&quot; |
| CONTENT_SPAMMY | &quot;CONTENT_SPAMMY&quot; |
| BAD_ATTACHMENT | &quot;BAD_ATTACHMENT&quot; |
| BAD_DMARC_POLICY | &quot;BAD_DMARC_POLICY&quot; |
| LOW_IP_REPUTATION | &quot;LOW_IP_REPUTATION&quot; |
| LOW_DOMAIN_REPUTATION | &quot;LOW_DOMAIN_REPUTATION&quot; |
| IP_IN_RBL | &quot;IP_IN_RBL&quot; |
| DOMAIN_IN_RBL | &quot;DOMAIN_IN_RBL&quot; |
| BAD_PTR_RECORD | &quot;BAD_PTR_RECORD&quot; |



