

# Employee

An employee object that is used by the external API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | A read-only timestamp in RFC 3339 format. |  [optional] |
|**email** | **String** | The employee&#39;s email address |  [optional] |
|**firstName** | **String** | The employee&#39;s first name. |  [optional] |
|**id** | **String** | UUID for this object. |  [optional] |
|**isOwner** | **Boolean** | Whether this employee is the owner of the merchant. Each merchant has one owner employee, and that employee has full authority over the account. |  [optional] |
|**lastName** | **String** | The employee&#39;s last name. |  [optional] |
|**locationIds** | **List&lt;String&gt;** | A list of location IDs where this employee has access to. |  [optional] |
|**phoneNumber** | **String** | The employee&#39;s phone number in E.164 format, i.e. \&quot;+12125554250\&quot; |  [optional] |
|**status** | **String** | Specifies the status of the employees being fetched. |  [optional] |
|**updatedAt** | **String** | A read-only timestamp in RFC 3339 format. |  [optional] |



