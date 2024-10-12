# GraphHopperDirectionsApi.Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ResponseAddress**](ResponseAddress.md) |  | [optional] 
**arrDateTime** | **Date** | Arrival date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is &#x60;null&#x60;. | [optional] 
**arrTime** | **Number** | Arrival time at this activity in seconds. If type is &#x60;start&#x60;, this is not available (since it makes no sense to have &#x60;arr_time&#x60; at start). However, &#x60;end_time&#x60; is available and actually means \\\&quot;departure time\\\&quot; at start location. It is important to note that &#x60;arr_time&#x60; does not necessarily mean \\\&quot;start of underlying activity\\\&quot;, it solely means arrival time at activity location. If this activity has no time windows and if there are no further preparation times, &#x60;arr_time&#x60; is equal to activity start time. | [optional] 
**distance** | **Number** | cumulated distance from start to this activity in m | [optional] 
**drivingTime** | **Number** | cumulated driving time from start to this driver activity in seconds | [optional] 
**endDateTime** | **Date** | End date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is &#x60;null&#x60;. | [optional] 
**endTime** | **Number** | End time of and thus departure time at this activity. If type is &#x60;end&#x60;, this is not available (since it makes no sense to have an &#x60;end_time&#x60; at end) &#x60;end_time&#x60; at each activity is equal to the departure time at the activity location. | [optional] 
**id** | **String** | Id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to | [optional] 
**loadAfter** | **[Number]** | Array with size/capacity dimensions after this activity | [optional] 
**loadBefore** | **[Number]** | Array with size/capacity dimensions before this activity | [optional] 
**locationId** | **String** | Id that refers to address | [optional] 
**preparationTime** | **Number** | preparation time at this activity in seconds | [optional] 
**type** | **String** | type of activity | [optional] 
**waitingTime** | **Number** | Waiting time at this activity in seconds. A waiting time can occur if the activity has at least one time window. If &#x60;arr_time&#x60; &lt; &#x60;time_window.earliest&#x60; a waiting time of &#x60;time_window_earliest&#x60; - &#x60;arr_time&#x60; occurs. | [optional] 



## Enum: TypeEnum


* `start` (value: `"start"`)

* `end` (value: `"end"`)

* `service` (value: `"service"`)

* `pickupShipment` (value: `"pickupShipment"`)

* `deliverShipment` (value: `"deliverShipment"`)

* `pickup` (value: `"pickup"`)

* `delivery` (value: `"delivery"`)

* `break` (value: `"break"`)




