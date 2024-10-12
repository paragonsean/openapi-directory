

# MessageAttributeValue

<p>The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see <a href=\"https://docs.aws.amazon.com/sns/latest/api/API_Publish.html\">Publish</a>.</p> <p>Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see <a href=\"https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html\">Amazon SNS message attributes</a> and <a href=\"https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html\">Publishing to a mobile phone</a> in the <i>Amazon SNS Developer Guide.</i> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataType** | [**String**](String.md) |  |  |
|**stringValue** | [**String**](String.md) |  |  [optional] |
|**binaryValue** | [**String**](String.md) |  |  [optional] |



