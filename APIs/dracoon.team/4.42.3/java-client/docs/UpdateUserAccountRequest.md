

# UpdateUserAccountRequest

Request model for updating user account information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptEULA** | **Boolean** | Accept EULA  Present, if EULA is system global active.  cf. &#x60;GET system/config/settings/general&#x60; - &#x60;eulaEnabled&#x60;  If accepted can not be undone. |  [optional] |
|**email** | **String** | Email  |  [optional] |
|**firstName** | **String** | User first name |  [optional] |
|**gender** | **String** | &amp;#128679; Deprecated since v4.12.0  Gender  Do NOT use &#x60;gender&#x60;! It will be ignored. |  [optional] |
|**language** | **String** | &amp;#128640; Since v4.20.0  IETF language tag |  [optional] |
|**lastName** | **String** | User last name |  [optional] |
|**login** | **String** | &amp;#128679; Deprecated since v4.13.0  User login name |  [optional] |
|**phone** | **String** | Phone number |  [optional] |
|**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title |  [optional] |
|**userName** | **String** | &amp;#128640; Since v4.13.0  Username |  [optional] |



