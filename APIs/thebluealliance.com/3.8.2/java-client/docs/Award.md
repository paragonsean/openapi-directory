

# Award


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**awardType** | **Integer** | Type of award given. See https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/award_type.py#L6 |  |
|**eventKey** | **String** | The event_key of the event the award was won at. |  |
|**name** | **String** | The name of the award as provided by FIRST. May vary for the same award type. |  |
|**recipientList** | [**List&lt;AwardRecipient&gt;**](AwardRecipient.md) | A list of recipients of the award at the event. May have either a team_key or an awardee, both, or neither (in the case the award wasn&#39;t awarded at the event). |  |
|**year** | **Integer** | The year this award was won. |  |



