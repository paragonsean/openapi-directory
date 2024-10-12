

# UpdateItemInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableName** | [**String**](String.md) |  |  |
|**key** | [**Key**](Key.md) |  |  |
|**attributeUpdates** | [**Map&lt;String, AttributeValueUpdate&gt;**](AttributeValueUpdate.md) | Map of attribute name to the new value and action for the update. The attribute names specify the attributes to modify, and cannot contain any primary key attributes. |  |
|**expected** | [**Map&lt;String, ExpectedAttributeValue&gt;**](ExpectedAttributeValue.md) | Designates an attribute for a conditional modification. The &lt;code&gt;Expected&lt;/code&gt; parameter allows you to provide an attribute name, and whether or not Amazon DynamoDB should check to see if the attribute has a particular value before modifying it. |  [optional] |
|**returnValues** | **ReturnValue** |  |  [optional] |



