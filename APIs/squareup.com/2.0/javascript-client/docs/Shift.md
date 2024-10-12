# SquareConnectApi.Shift

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breaks** | [**[Break]**](Break.md) | A list of all the paid or unpaid breaks that were taken during this shift. | [optional] 
**createdAt** | **String** | A read-only timestamp in RFC 3339 format; presented in UTC. | [optional] 
**employeeId** | **String** | The ID of the employee this shift belongs to. DEPRECATED at version 2020-08-26. Use &#x60;team_member_id&#x60; instead. | [optional] 
**endAt** | **String** | RFC 3339; shifted to the timezone + offset. Precision up to the minute is respected; seconds are truncated. | [optional] 
**id** | **String** | The UUID for this object. | [optional] 
**locationId** | **String** | The ID of the location this shift occurred at. The location should be based on where the employee clocked in. | [optional] 
**startAt** | **String** | RFC 3339; shifted to the location timezone + offset. Precision up to the minute is respected; seconds are truncated. | 
**status** | **String** | Describes the working state of the current &#x60;Shift&#x60;. | [optional] 
**teamMemberId** | **String** | The ID of the team member this shift belongs to. Replaced &#x60;employee_id&#x60; at version \&quot;2020-08-26\&quot;. | [optional] 
**timezone** | **String** | The read-only convenience value that is calculated from the location based on the &#x60;location_id&#x60;. Format: the IANA timezone database identifier for the location timezone. | [optional] 
**updatedAt** | **String** | A read-only timestamp in RFC 3339 format; presented in UTC. | [optional] 
**version** | **Number** | Used for resolving concurrency issues. The request fails if the version provided does not match the server version at the time of the request. If not provided, Square executes a blind write; potentially overwriting data from another write. | [optional] 
**wage** | [**ShiftWage**](ShiftWage.md) |  | [optional] 


