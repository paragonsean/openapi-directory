

# UserActivitySession

This represents a user session performed on a specific device at a certain time over a period of time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activities** | [**List&lt;Activity&gt;**](Activity.md) | Represents a detailed view into each of the activity in this session. |  [optional] |
|**dataSource** | **String** | The data source of a hit. By default, hits sent from analytics.js are reported as \&quot;web\&quot; and hits sent from the mobile SDKs are reported as \&quot;app\&quot;. These values can be overridden in the Measurement Protocol. |  [optional] |
|**deviceCategory** | **String** | The type of device used: \&quot;mobile\&quot;, \&quot;tablet\&quot; etc. |  [optional] |
|**platform** | **String** | Platform on which the activity happened: \&quot;android\&quot;, \&quot;ios\&quot; etc. |  [optional] |
|**sessionDate** | **String** | Date of this session in ISO-8601 format. |  [optional] |
|**sessionId** | **String** | Unique ID of the session. |  [optional] |



