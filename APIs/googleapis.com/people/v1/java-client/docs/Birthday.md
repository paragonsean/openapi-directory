

# Birthday

A person's birthday. At least one of the `date` and `text` fields are specified. The `date` and `text` fields typically represent the same date, but are not guaranteed to. Clients should always set the `date` field when mutating birthdays.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | [**Date**](Date.md) |  |  [optional] |
|**metadata** | [**FieldMetadata**](FieldMetadata.md) |  |  [optional] |
|**text** | **String** | Prefer to use the &#x60;date&#x60; field if set. A free-form string representing the user&#39;s birthday. This value is not validated. |  [optional] |



