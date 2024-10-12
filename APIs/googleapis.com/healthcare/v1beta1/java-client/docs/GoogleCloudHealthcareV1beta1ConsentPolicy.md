

# GoogleCloudHealthcareV1beta1ConsentPolicy

Represents a user's consent in terms of the resources that can be accessed and under what conditions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationRule** | [**Expr**](Expr.md) |  |  [optional] |
|**resourceAttributes** | [**List&lt;Attribute&gt;**](Attribute.md) | The resources that this policy applies to. A resource is a match if it matches all the attributes listed here. If empty, this policy applies to all User data mappings for the given user. |  [optional] |



