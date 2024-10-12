

# V1Employee

Represents one of a business's employees.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedLocationIds** | **List&lt;String&gt;** | The IDs of the locations the employee is allowed to clock in at. |  [optional] |
|**createdAt** | **String** | The time when the employee entity was created, in ISO 8601 format. |  [optional] |
|**email** | **String** | The employee&#39;s email address. |  [optional] |
|**externalId** | **String** | An ID the merchant can set to associate the employee with an entity in another system. |  [optional] |
|**firstName** | **String** | The employee&#39;s first name. |  |
|**id** | **String** | The employee&#39;s unique ID. |  [optional] |
|**lastName** | **String** | The employee&#39;s last name. |  |
|**roleIds** | **List&lt;String&gt;** | The ids of the employee&#39;s associated roles. Currently, you can specify only one or zero roles per employee. |  [optional] |
|**status** | **String** | Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard. |  [optional] |
|**updatedAt** | **String** | The time when the employee entity was most recently updated, in ISO 8601 format. |  [optional] |



