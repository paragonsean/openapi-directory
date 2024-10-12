

# ContentV1Content


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | A string name used to describe the Content resource. Not visible to the end recipient. |  [optional] |
|**language** | **String** | Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in. |  [optional] |
|**links** | **Object** | A list of links related to the Content resource, such as approval_fetch and approval_create |  [optional] |
|**sid** | **String** | The unique string that that we created to identify the Content resource. |  [optional] |
|**types** | **Object** | The [Content types](https://www.twilio.com/docs/content/content-types-overview) (e.g. twilio/text) for this Content resource. |  [optional] |
|**url** | **URI** | The URL of the resource, relative to &#x60;https://content.twilio.com&#x60;. |  [optional] |
|**variables** | **Object** | Defines the default placeholder values for variables included in the Content resource. e.g. {\&quot;1\&quot;: \&quot;Customer_Name\&quot;}. |  [optional] |



