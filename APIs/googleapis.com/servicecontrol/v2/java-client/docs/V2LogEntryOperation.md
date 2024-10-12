

# V2LogEntryOperation

Additional information about a potentially long-running operation with which a log entry is associated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**first** | **Boolean** | Optional. Set this to True if this is the first log entry in the operation. |  [optional] |
|**id** | **String** | Optional. An arbitrary operation identifier. Log entries with the same identifier are assumed to be part of the same operation. |  [optional] |
|**last** | **Boolean** | Optional. Set this to True if this is the last log entry in the operation. |  [optional] |
|**producer** | **String** | Optional. An arbitrary producer identifier. The combination of &#x60;id&#x60; and &#x60;producer&#x60; must be globally unique. Examples for &#x60;producer&#x60;: &#x60;\&quot;MyDivision.MyBigCompany.com\&quot;&#x60;, &#x60;\&quot;github.com/MyProject/MyApplication\&quot;&#x60;. |  [optional] |



