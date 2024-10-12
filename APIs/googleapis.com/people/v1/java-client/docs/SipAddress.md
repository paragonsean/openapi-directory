

# SipAddress

A person's SIP address. Session Initial Protocol addresses are used for VoIP communications to make voice or video calls over the internet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formattedType** | **String** | Output only. The type of the SIP address translated and formatted in the viewer&#39;s account locale or the &#x60;Accept-Language&#x60; HTTP header locale. |  [optional] [readonly] |
|**metadata** | [**FieldMetadata**](FieldMetadata.md) |  |  [optional] |
|**type** | **String** | The type of the SIP address. The type can be custom or or one of these predefined values: * &#x60;home&#x60; * &#x60;work&#x60; * &#x60;mobile&#x60; * &#x60;other&#x60; |  [optional] |
|**value** | **String** | The SIP address in the [RFC 3261 19.1](https://tools.ietf.org/html/rfc3261#section-19.1) SIP URI format. |  [optional] |



