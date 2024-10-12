

# DatafeedFetchSchedule

The required fields vary based on the frequency of fetching. For a monthly fetch schedule, day_of_month and hour are required. For a weekly fetch schedule, weekday and hour are required. For a daily fetch schedule, only hour is required.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfMonth** | **Integer** | The day of the month the feed file should be fetched (1-31). |  [optional] |
|**fetchUrl** | **String** | The URL where the feed file can be fetched. Google Merchant Center will support automatic scheduled uploads using the HTTP, HTTPS, FTP, or SFTP protocols, so the value will need to be a valid link using one of those four protocols. |  [optional] |
|**hour** | **Integer** | The hour of the day the feed file should be fetched (0-23). |  [optional] |
|**minuteOfHour** | **Integer** | The minute of the hour the feed file should be fetched (0-59). Read-only. |  [optional] |
|**password** | **String** | An optional password for fetch_url. |  [optional] |
|**paused** | **Boolean** | Whether the scheduled fetch is paused or not. |  [optional] |
|**timeZone** | **String** | Time zone used for schedule. UTC by default. For example, \&quot;America/Los_Angeles\&quot;. |  [optional] |
|**username** | **String** | An optional user name for fetch_url. |  [optional] |
|**weekday** | **String** | The day of the week the feed file should be fetched. Acceptable values are: - \&quot;&#x60;monday&#x60;\&quot; - \&quot;&#x60;tuesday&#x60;\&quot; - \&quot;&#x60;wednesday&#x60;\&quot; - \&quot;&#x60;thursday&#x60;\&quot; - \&quot;&#x60;friday&#x60;\&quot; - \&quot;&#x60;saturday&#x60;\&quot; - \&quot;&#x60;sunday&#x60;\&quot;  |  [optional] |



