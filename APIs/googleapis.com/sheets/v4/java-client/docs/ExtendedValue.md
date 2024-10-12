

# ExtendedValue

The kinds of value that a cell in a spreadsheet can have.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolValue** | **Boolean** | Represents a boolean value. |  [optional] |
|**errorValue** | [**ErrorValue**](ErrorValue.md) |  |  [optional] |
|**formulaValue** | **String** | Represents a formula. |  [optional] |
|**numberValue** | **Double** | Represents a double value. Note: Dates, Times and DateTimes are represented as doubles in SERIAL_NUMBER format. |  [optional] |
|**stringValue** | **String** | Represents a string value. Leading single quotes are not included. For example, if the user typed &#x60;&#39;123&#x60; into the UI, this would be represented as a &#x60;stringValue&#x60; of &#x60;\&quot;123\&quot;&#x60;. |  [optional] |



