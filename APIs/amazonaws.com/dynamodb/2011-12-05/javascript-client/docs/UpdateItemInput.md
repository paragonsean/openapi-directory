# AmazonDynamoDb.UpdateItemInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tableName** | **String** |  | 
**key** | [**Key**](Key.md) |  | 
**attributeUpdates** | [**{String: AttributeValueUpdate}**](AttributeValueUpdate.md) | Map of attribute name to the new value and action for the update. The attribute names specify the attributes to modify, and cannot contain any primary key attributes. | 
**expected** | [**{String: ExpectedAttributeValue}**](ExpectedAttributeValue.md) | Designates an attribute for a conditional modification. The &lt;code&gt;Expected&lt;/code&gt; parameter allows you to provide an attribute name, and whether or not Amazon DynamoDB should check to see if the attribute has a particular value before modifying it. | [optional] 
**returnValues** | [**ReturnValue**](ReturnValue.md) |  | [optional] 


