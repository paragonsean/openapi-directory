

# Employee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**employeeID** | **UUID** | The Xero identifier for an employee e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 |  [optional] |
|**externalLink** | [**ExternalLink**](ExternalLink.md) |  |  [optional] |
|**firstName** | **String** | First name of an employee (max length &#x3D; 255) |  [optional] |
|**lastName** | **String** | Last name of an employee (max length &#x3D; 255) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of an employee – see contact status types |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**updatedDateUTC** | **String** |  |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| GDPRREQUEST | &quot;GDPRREQUEST&quot; |
| DELETED | &quot;DELETED&quot; |



