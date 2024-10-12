

# InvoiceTimeShift

The invoice time shift in conjunction with `billingTiming` allows to setup different billing use cases such as: - Bill immediately when the service period _starts_ - Bill immediately after the service period _ends_ - Bill _interval of time_ before the service period _starts_ - Bill _interval of time_ after the service period _starts_ - Bill _interval of time_ before the service period _ends_ - Bill _interval of time_ after the service period _ends_ It allows to control the billing time. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dueTimeShift** | [**DueTimeShiftInstruction**](DueTimeShiftInstruction.md) |  |  [optional] |
|**issueTimeShift** | [**IssueTimeShiftInstruction**](IssueTimeShiftInstruction.md) |  |  [optional] |



