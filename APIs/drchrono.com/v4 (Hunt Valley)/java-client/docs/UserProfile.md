

# UserProfile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**doctor** | **String** | For staff members, this is their primary physician&#39;s ID. For doctors, it is their own ID. |  [optional] [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**isDoctor** | **String** | Mutually exclusive with &#x60;is_staff&#x60; |  [optional] [readonly] |
|**isStaff** | **String** | Mutually exclusive with &#x60;is_doctor&#x60; |  [optional] [readonly] |
|**permissions** | **String** | Permissions the user has. |  [optional] [readonly] |
|**practiceGroup** | **String** | The ID of the practice group this user belongs to. This can be used to identify users in the same practice. |  [optional] [readonly] |
|**username** | **String** |  |  [optional] |



