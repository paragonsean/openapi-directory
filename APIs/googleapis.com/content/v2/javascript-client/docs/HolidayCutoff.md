# ContentApiForShopping.HolidayCutoff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadlineDate** | **String** | Date of the order deadline, in ISO 8601 format. E.g. \&quot;2016-11-29\&quot; for 29th November 2016. Required. | [optional] 
**deadlineHour** | **Number** | Hour of the day on the deadline date until which the order has to be placed to qualify for the delivery guarantee. Possible values are: 0 (midnight), 1, ..., 12 (noon), 13, ..., 23. Required. | [optional] 
**deadlineTimezone** | **String** | Timezone identifier for the deadline hour. A list of identifiers can be found in the AdWords API documentation. E.g. \&quot;Europe/Zurich\&quot;. Required. | [optional] 
**holidayId** | **String** | Unique identifier for the holiday. Required. | [optional] 
**visibleFromDate** | **String** | Date on which the deadline will become visible to consumers in ISO 8601 format. E.g. \&quot;2016-10-31\&quot; for 31st October 2016. Required. | [optional] 


