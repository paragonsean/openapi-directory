

# Trigger

A condition to be satisfied for an action to be executed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**daysBeforeExpiry** | **Integer** | Days before expiry to attempt renewal. Value should be between 1 and validity_in_months multiplied by 27. If validity_in_months is 36, then value should be between 1 and 972 (36 * 27). |  [optional] |
|**lifetimePercentage** | **Integer** | Percentage of lifetime at which to trigger. Value should be between 1 and 99. |  [optional] |



