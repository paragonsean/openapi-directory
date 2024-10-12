

# UserIdentity

Specify either the userName or autoUser property, but not both. On CloudServiceConfiguration pools, this user is logged in with the INTERACTIVE flag. On Windows VirtualMachineConfiguration pools, this user is logged in with the BATCH flag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoUser** | [**AutoUserSpecification**](AutoUserSpecification.md) |  |  [optional] |
|**username** | **String** | The userName and autoUser properties are mutually exclusive; you must specify one but not both. |  [optional] |



