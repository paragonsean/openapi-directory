

# SpecialHourPeriod

Represents a single time period when a location's operational hours differ from its normal business hours. A special hour period must represent a range of less than 24 hours. The `open_time` and `start_date` must predate the `close_time` and `end_date`. The `close_time` and `end_date` can extend to 11:59 a.m. on the day after the specified `start_date`. For example, the following inputs are valid: start_date=2015-11-23, open_time=08:00, close_time=18:00 start_date=2015-11-23, end_date=2015-11-23, open_time=08:00, close_time=18:00 start_date=2015-11-23, end_date=2015-11-24, open_time=13:00, close_time=11:59 The following inputs are not valid: start_date=2015-11-23, open_time=13:00, close_time=11:59 start_date=2015-11-23, end_date=2015-11-24, open_time=13:00, close_time=12:00 start_date=2015-11-23, end_date=2015-11-25, open_time=08:00, close_time=18:00

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closeTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**closed** | **Boolean** | Optional. If true, &#x60;end_date&#x60;, &#x60;open_time&#x60;, and &#x60;close_time&#x60; are ignored, and the date specified in &#x60;start_date&#x60; is treated as the location being closed for the entire day. |  [optional] |
|**endDate** | [**Date**](Date.md) |  |  [optional] |
|**openTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**startDate** | [**Date**](Date.md) |  |  [optional] |



