

# Avg

Average of the values of the requested property. * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped. * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards. * If the aggregated value set is empty, returns `NULL`. * Always returns the result as a double.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**property** | [**PropertyReference**](PropertyReference.md) |  |  [optional] |



