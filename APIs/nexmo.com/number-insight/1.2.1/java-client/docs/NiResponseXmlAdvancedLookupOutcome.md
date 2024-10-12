

# NiResponseXmlAdvancedLookupOutcome

An object indicating whether all information about a phone number has been returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Shows if all information about a phone number has been returned. Possible values:  Code | Text -- | -- 0 | Success 1 | Partial success - some fields populated 2 | Failed  |  [optional] |
|**lookupOutcomeMessage** | **String** | Shows if all information about a phone number has been returned. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | new BigDecimal(&quot;0&quot;) |
| NUMBER_1 | new BigDecimal(&quot;1&quot;) |
| NUMBER_2 | new BigDecimal(&quot;2&quot;) |



