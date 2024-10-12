

# MessageAttributeValue

<p>The user-specified message attribute value. For string data types, the <code>Value</code> attribute has the same restrictions on the content as the message body. For more information, see <code> <a>SendMessage</a>.</code> </p> <p> <code>Name</code>, <code>type</code>, <code>value</code> and the message body must not be empty or null. All parts of the message attribute, including <code>Name</code>, <code>Type</code>, and <code>Value</code>, are part of the message size restriction (256 KiB or 262,144 bytes).</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stringValue** | [**String**](String.md) |  |  [optional] |
|**binaryValue** | [**String**](String.md) |  |  [optional] |
|**stringListValues** | [**List**](List.md) |  |  [optional] |
|**binaryListValues** | [**List**](List.md) |  |  [optional] |
|**dataType** | [**String**](String.md) |  |  |



