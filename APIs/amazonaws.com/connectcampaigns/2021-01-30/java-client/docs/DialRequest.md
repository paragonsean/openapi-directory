

# DialRequest

A dial request for a campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in contact flows just like any other contact attributes. |  |
|**clientToken** | **String** | Client provided parameter used for idempotency. Its value must be unique for each request. |  |
|**expirationTime** | **OffsetDateTime** | Timestamp with no UTC offset or timezone |  |
|**phoneNumber** | **String** | The phone number of the customer, in E.164 format. |  |



