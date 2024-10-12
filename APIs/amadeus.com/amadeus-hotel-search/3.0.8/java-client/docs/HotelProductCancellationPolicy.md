

# HotelProductCancellationPolicy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **String** | Amount of the cancellation fee. |  [optional] |
|**deadline** | **OffsetDateTime** | Represents the deadline after which the penalty applies. DateTime is in ISO 8601 [https://www.w3.org/TR/NOTE-datetime]. Example: 2010-08-14T12:00:00+01:00 Example: 2010-08-14T12:00:00Z Example: 2010-08-14T12:00:00-01:00 The value is expressed in the hotel local time zone, with the added time zone difference. So you can compute the deadline in UTC(GMT) if desired. |  [optional] |
|**description** | [**QualifiedFreeText**](QualifiedFreeText.md) |  |  [optional] |
|**numberOfNights** | **Integer** | Number of nights due as fee in case of cancellation. |  [optional] |
|**percentage** | **String** | Percentage of the total stay amount to be paid in case of cancellation. Value is between 0 and 100. |  [optional] |
|**type** | **CancellationType** |  |  [optional] |



