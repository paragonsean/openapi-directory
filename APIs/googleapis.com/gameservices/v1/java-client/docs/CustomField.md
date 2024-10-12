

# CustomField

Custom fields. These can be used to create a counter with arbitrary field/value pairs. See: go/rpcsp-custom-fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name is the field name. |  [optional] |
|**value** | **String** | Value is the field value. It is important that in contrast to the CounterOptions.field, the value here is a constant that is not derived from the IAMContext. |  [optional] |



