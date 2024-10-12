

# ValueMatcher

Specifies the way to match a ProtobufWkt::Value. Primitive values and ListValue are supported. StructValue is not supported and is always not matched. [#next-free-field: 8]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolMatch** | **Boolean** | If specified, a match occurs if and only if the target value is a bool value and is equal to this field. |  [optional] |
|**doubleMatch** | [**DoubleMatcher**](DoubleMatcher.md) |  |  [optional] |
|**listMatch** | [**ListMatcher**](ListMatcher.md) |  |  [optional] |
|**nullMatch** | **Object** | NullMatch is an empty message to specify a null value. |  [optional] |
|**orMatch** | [**OrMatcher**](OrMatcher.md) |  |  [optional] |
|**presentMatch** | **Boolean** | If specified, value match will be performed based on whether the path is referring to a valid primitive value in the metadata. If the path is referring to a non-primitive value, the result is always not matched. |  [optional] |
|**stringMatch** | [**StringMatcher**](StringMatcher.md) |  |  [optional] |



