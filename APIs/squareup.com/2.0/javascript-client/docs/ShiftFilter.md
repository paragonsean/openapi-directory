# SquareConnectApi.ShiftFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employeeIds** | **[String]** | Fetch shifts for the specified employees. DEPRECATED at version 2020-08-26. Use &#x60;team_member_ids&#x60; instead. | [optional] 
**end** | [**TimeRange**](TimeRange.md) |  | [optional] 
**locationIds** | **[String]** | Fetch shifts for the specified location. | 
**start** | [**TimeRange**](TimeRange.md) |  | [optional] 
**status** | **String** | Fetch a &#x60;Shift&#x60; instance by &#x60;Shift.status&#x60;. | [optional] 
**teamMemberIds** | **[String]** | Fetch shifts for the specified team members. Replaced &#x60;employee_ids&#x60; at version \&quot;2020-08-26\&quot;. | 
**workday** | [**ShiftWorkday**](ShiftWorkday.md) |  | [optional] 


