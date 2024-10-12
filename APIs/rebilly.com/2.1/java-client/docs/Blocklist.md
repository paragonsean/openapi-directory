

# Blocklist


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | The blocklist created time. |  [optional] [readonly] |
|**expirationTime** | **OffsetDateTime** | The blocklist expiration time. |  [optional] |
|**id** | **String** | The blocklist identifier string. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The blocklist type. |  |
|**updatedTime** | **OffsetDateTime** | The blocklist updated time. |  [optional] [readonly] |
|**value** | **String** | The blocklist value. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAYMENT_CARD | &quot;payment-card&quot; |
| BANK_ACCOUNT | &quot;bank-account&quot; |
| CUSTOMER_ID | &quot;customer-id&quot; |
| EMAIL | &quot;email&quot; |
| EMAIL_DOMAIN | &quot;email-domain&quot; |
| IP_ADDRESS | &quot;ip-address&quot; |
| COUNTRY | &quot;country&quot; |
| FINGERPRINT | &quot;fingerprint&quot; |
| BIN | &quot;bin&quot; |
| ADDRESS | &quot;address&quot; |



