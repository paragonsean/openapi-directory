

# AutopilotV1Assistant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Assistant resource. |  [optional] |
|**callbackEvents** | **String** | Reserved. |  [optional] |
|**callbackUrl** | **URI** | Reserved. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**developmentStage** | **String** | A string describing the state of the assistant. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. It is not unique and can be up to 255 characters long. |  [optional] |
|**latestModelBuildSid** | **String** | Reserved. |  [optional] |
|**links** | **Object** | A list of the URLs of the Assistant&#39;s related resources. |  [optional] |
|**logQueries** | **Boolean** | Whether queries should be logged and kept after training. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. If &#x60;true&#x60;, queries are stored for 30 days, and then deleted. If &#x60;false&#x60;, no queries are stored. |  [optional] |
|**needsModelBuild** | **Boolean** | Whether model needs to be rebuilt. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Assistant resource. |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. It can be up to 64 characters long. |  [optional] |
|**url** | **URI** | The absolute URL of the Assistant resource. |  [optional] |



