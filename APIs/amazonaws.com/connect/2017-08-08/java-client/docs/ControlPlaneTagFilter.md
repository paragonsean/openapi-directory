

# ControlPlaneTagFilter

<p>An object that can be used to specify Tag conditions inside the <code>SearchFilter</code>. This accepts an <code>OR</code> of <code>AND</code> (List of List) input where: </p> <ul> <li> <p>Top level list specifies conditions that need to be applied with <code>OR</code> operator</p> </li> <li> <p>Inner list specifies conditions that need to be applied with <code>AND</code> operator.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orConditions** | [**List**](List.md) |  |  [optional] |
|**andConditions** | [**List**](List.md) |  |  [optional] |
|**tagCondition** | [**ControlPlaneTagFilterTagCondition**](ControlPlaneTagFilterTagCondition.md) |  |  [optional] |



