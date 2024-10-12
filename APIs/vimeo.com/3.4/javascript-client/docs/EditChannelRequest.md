# Vimeo.EditChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the channel. | [optional] 
**link** | **String** | The link to access the channel. You can use a custom name in the URL in place of a numeric channel ID, as in &#x60;/channels/{url_custom}&#x60;. Submitting &#x60;\&quot;\&quot;&#x60; for this field removes the link alias. | [optional] 
**name** | **String** | The name of the channel. | [optional] 
**privacy** | **String** | The privacy level of the channel. | [optional] 



## Enum: PrivacyEnum


* `anybody` (value: `"anybody"`)

* `moderators` (value: `"moderators"`)

* `users` (value: `"users"`)




