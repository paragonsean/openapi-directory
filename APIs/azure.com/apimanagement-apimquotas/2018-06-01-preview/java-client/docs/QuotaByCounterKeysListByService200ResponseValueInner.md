

# QuotaByCounterKeysListByService200ResponseValueInner

Quota counter details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**counterKey** | **String** | The Key value of the Counter. Must not be empty. |  |
|**periodEndTime** | **OffsetDateTime** | The date of the end of Counter Period. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  |
|**periodKey** | **String** | Identifier of the Period for which the counter was collected. Must not be empty. |  |
|**periodStartTime** | **OffsetDateTime** | The date of the start of Counter Period. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  |
|**value** | [**QuotaByCounterKeysListByService200ResponseValueInnerValue**](QuotaByCounterKeysListByService200ResponseValueInnerValue.md) |  |  [optional] |



