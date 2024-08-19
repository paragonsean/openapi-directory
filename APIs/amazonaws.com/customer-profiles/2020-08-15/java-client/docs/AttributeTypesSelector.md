

# AttributeTypesSelector

<p>Configuration information about the <code>AttributeTypesSelector </code>where the rule-based identity resolution uses to match profiles. You can choose how profiles are compared across attribute types and which attribute to use for matching from each type. There are three attribute types you can configure:</p> <ul> <li> <p>Email type</p> <ul> <li> <p>You can choose from <code>Email</code>, <code>BusinessEmail</code>, and <code>PersonalEmail</code> </p> </li> </ul> </li> <li> <p>Phone number type</p> <ul> <li> <p>You can choose from <code>Phone</code>, <code>HomePhone</code>, and <code>MobilePhone</code> </p> </li> </ul> </li> <li> <p>Address type</p> <ul> <li> <p>You can choose from <code>Address</code>, <code>BusinessAddress</code>, <code>MaillingAddress</code>, and <code>ShippingAddress</code> </p> </li> </ul> </li> </ul> <p>You can either choose <code>ONE_TO_ONE</code> or <code>MANY_TO_MANY</code> as the <code>AttributeMatchingModel</code>. When choosing <code>MANY_TO_MANY</code>, the system can match attribute across the sub-types of an attribute type. For example, if the value of the <code>Email</code> field of Profile A and the value of <code>BusinessEmail</code> field of Profile B matches, the two profiles are matched on the Email type. When choosing <code>ONE_TO_ONE</code> the system can only match if the sub-types are exact matches. For example, only when the value of the <code>Email</code> field of Profile A and the value of the <code>Email</code> field of Profile B matches, the two profiles are matched on the Email type.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeMatchingModel** | [**AttributeMatchingModel**](AttributeMatchingModel.md) |  |  |
|**address** | [**List**](List.md) |  |  [optional] |
|**phoneNumber** | [**List**](List.md) |  |  [optional] |
|**emailAddress** | [**List**](List.md) |  |  [optional] |



