

# FilterCriteria

Message matching criteria.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludeChats** | **Boolean** | Whether the response should exclude chats. |  [optional] |
|**from** | **String** | The sender&#39;s display name or email address. |  [optional] |
|**hasAttachment** | **Boolean** | Whether the message has any attachment. |  [optional] |
|**negatedQuery** | **String** | Only return messages not matching the specified query. Supports the same query format as the Gmail search box. For example, &#x60;\&quot;from:someuser@example.com rfc822msgid: is:unread\&quot;&#x60;. |  [optional] |
|**query** | **String** | Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, &#x60;\&quot;from:someuser@example.com rfc822msgid: is:unread\&quot;&#x60;. |  [optional] |
|**size** | **Integer** | The size of the entire RFC822 message in bytes, including all headers and attachments. |  [optional] |
|**sizeComparison** | [**SizeComparisonEnum**](#SizeComparisonEnum) | How the message size in bytes should be in relation to the size field. |  [optional] |
|**subject** | **String** | Case-insensitive phrase found in the message&#39;s subject. Trailing and leading whitespace are be trimmed and adjacent spaces are collapsed. |  [optional] |
|**to** | **String** | The recipient&#39;s display name or email address. Includes recipients in the \&quot;to\&quot;, \&quot;cc\&quot;, and \&quot;bcc\&quot; header fields. You can use simply the local part of the email address. For example, \&quot;example\&quot; and \&quot;example@\&quot; both match \&quot;example@gmail.com\&quot;. This field is case-insensitive. |  [optional] |



## Enum: SizeComparisonEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;unspecified&quot; |
| SMALLER | &quot;smaller&quot; |
| LARGER | &quot;larger&quot; |



