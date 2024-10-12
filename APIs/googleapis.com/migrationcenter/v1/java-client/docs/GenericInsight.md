

# GenericInsight

A generic insight about an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInformation** | **List&lt;String&gt;** | Output only. Additional information about the insight, each entry can be a logical entry and must make sense if it is displayed with line breaks between each entry. Text can contain md style links. |  [optional] [readonly] |
|**defaultMessage** | **String** | Output only. In case message_code is not yet known by the client default_message will be the message to be used instead. |  [optional] [readonly] |
|**messageId** | **String** | Output only. Represents a globally unique message id for this insight, can be used for localization purposes, in case message_code is not yet known by the client use default_message instead. |  [optional] [readonly] |



