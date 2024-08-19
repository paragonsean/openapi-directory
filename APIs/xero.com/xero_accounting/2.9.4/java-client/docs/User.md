

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | Email address of user |  [optional] |
|**firstName** | **String** | First name of user |  [optional] |
|**isSubscriber** | **Boolean** | Boolean to indicate if user is the subscriber |  [optional] |
|**lastName** | **String** | Last name of user |  [optional] |
|**organisationRole** | [**OrganisationRoleEnum**](#OrganisationRoleEnum) | User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc) |  [optional] |
|**updatedDateUTC** | **String** | Timestamp of last change to user |  [optional] [readonly] |
|**userID** | **UUID** | Xero identifier |  [optional] |



## Enum: OrganisationRoleEnum

| Name | Value |
|---- | -----|
| READONLY | &quot;READONLY&quot; |
| INVOICEONLY | &quot;INVOICEONLY&quot; |
| STANDARD | &quot;STANDARD&quot; |
| FINANCIALADVISER | &quot;FINANCIALADVISER&quot; |
| MANAGEDCLIENT | &quot;MANAGEDCLIENT&quot; |
| CASHBOOKCLIENT | &quot;CASHBOOKCLIENT&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



