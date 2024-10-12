# CloudIdentityApi.UserInvitation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailsSentCount** | **String** | Number of invitation emails sent to the user. | [optional] 
**name** | **String** | Shall be of the form &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60;. | [optional] 
**state** | **String** | State of the &#x60;UserInvitation&#x60;. | [optional] 
**updateTime** | **String** | Time when the &#x60;UserInvitation&#x60; was last updated. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NOT_YET_SENT` (value: `"NOT_YET_SENT"`)

* `INVITED` (value: `"INVITED"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `DECLINED` (value: `"DECLINED"`)




