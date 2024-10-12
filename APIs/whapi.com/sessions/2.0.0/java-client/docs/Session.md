

# Session


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryDateTime** | **String** | The UTC time when the ticket expires. |  |
|**extended** | **Boolean** | The value you have selected previous to executing the request. If the value is Y, this enables your application to generate a ticket valid for 60 days without expiring due to inactivity. |  [optional] |
|**location** | **String** | This is the URL of the target service sent in the request. This is a combination of the endpoint and the ticket for future operations such as DELETE. |  [optional] |
|**temporaryPassword** | **Boolean** | Indicates that the account has a temporary password set and hence the user must be prompted to change their password. |  [optional] |
|**temporaryPasswordUrl** | **String** | Url for user to change password. A TGT must be added to the URL |  [optional] |
|**ticket** | **String** | The TGT ticket |  |



