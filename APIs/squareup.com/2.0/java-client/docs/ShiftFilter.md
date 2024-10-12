

# ShiftFilter

Defines a filter used in a search for `Shift` records. `AND` logic is used by Square's servers to apply each filter property specified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**employeeIds** | **List&lt;String&gt;** | Fetch shifts for the specified employees. DEPRECATED at version 2020-08-26. Use &#x60;team_member_ids&#x60; instead. |  [optional] |
|**end** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**locationIds** | **List&lt;String&gt;** | Fetch shifts for the specified location. |  |
|**start** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**status** | **String** | Fetch a &#x60;Shift&#x60; instance by &#x60;Shift.status&#x60;. |  [optional] |
|**teamMemberIds** | **List&lt;String&gt;** | Fetch shifts for the specified team members. Replaced &#x60;employee_ids&#x60; at version \&quot;2020-08-26\&quot;. |  |
|**workday** | [**ShiftWorkday**](ShiftWorkday.md) |  |  [optional] |



