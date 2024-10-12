# AmazonDynamoDb.PutItemInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tableName** | **String** |  | 
**item** | [**{String: AttributeValue}**](AttributeValue.md) | A map of the attributes for the item, and must include the primary key values that define the item. Other attribute name-value pairs can be provided for the item. | 
**expected** | [**{String: ExpectedAttributeValue}**](ExpectedAttributeValue.md) | Designates an attribute for a conditional modification. The &lt;code&gt;Expected&lt;/code&gt; parameter allows you to provide an attribute name, and whether or not Amazon DynamoDB should check to see if the attribute has a particular value before modifying it. | [optional] 
**returnValues** | [**ReturnValue**](ReturnValue.md) |  | [optional] 


