

# DnsResourceRecord

The structure describing the DNS Resource Record that needs to be added to DNS configuration for the authorization to be usable by certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **String** | Output only. Data of the DNS Resource Record. |  [optional] [readonly] |
|**name** | **String** | Output only. Fully qualified name of the DNS Resource Record. e.g. &#x60;_acme-challenge.example.com&#x60; |  [optional] [readonly] |
|**type** | **String** | Output only. Type of the DNS Resource Record. Currently always set to \&quot;CNAME\&quot;. |  [optional] [readonly] |



