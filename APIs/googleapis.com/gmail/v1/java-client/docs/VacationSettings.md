

# VacationSettings

Vacation auto-reply settings for an account. These settings correspond to the \"Vacation responder\" feature in the web interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableAutoReply** | **Boolean** | Flag that controls whether Gmail automatically replies to messages. |  [optional] |
|**endTime** | **String** | An optional end time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives before the end time. If both &#x60;startTime&#x60; and &#x60;endTime&#x60; are specified, &#x60;startTime&#x60; must precede &#x60;endTime&#x60;. |  [optional] |
|**responseBodyHtml** | **String** | Response body in HTML format. Gmail will sanitize the HTML before storing it. If both &#x60;response_body_plain_text&#x60; and &#x60;response_body_html&#x60; are specified, &#x60;response_body_html&#x60; will be used. |  [optional] |
|**responseBodyPlainText** | **String** | Response body in plain text format. If both &#x60;response_body_plain_text&#x60; and &#x60;response_body_html&#x60; are specified, &#x60;response_body_html&#x60; will be used. |  [optional] |
|**responseSubject** | **String** | Optional text to prepend to the subject line in vacation responses. In order to enable auto-replies, either the response subject or the response body must be nonempty. |  [optional] |
|**restrictToContacts** | **Boolean** | Flag that determines whether responses are sent to recipients who are not in the user&#39;s list of contacts. |  [optional] |
|**restrictToDomain** | **Boolean** | Flag that determines whether responses are sent to recipients who are outside of the user&#39;s domain. This feature is only available for Google Workspace users. |  [optional] |
|**startTime** | **String** | An optional start time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives after the start time. If both &#x60;startTime&#x60; and &#x60;endTime&#x60; are specified, &#x60;startTime&#x60; must precede &#x60;endTime&#x60;. |  [optional] |



