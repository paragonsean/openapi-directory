

# Group

A group of users

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The creation date of the group |  [optional] |
|**id** | **String** | The unique identifier of the group |  [optional] |
|**name** | **String** | The display name of the group |  [optional] |
|**organization** | **String** | If the group is related to an organization, this field will contain the unique identifier of the organization  |  [optional] |
|**readOnly** | **Boolean** | &#x60;True&#x60; if the group is set in read-only  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the group: * &#x60;generic&#x60;: A group created by a Flat user * &#x60;classTeachers&#x60;: A group created automaticaly by Flat that contains   the teachers of a class * &#x60;classStudents&#x60;: A group created automaticaly by Flat that contains   the studnets of a class  |  [optional] |
|**usersCount** | **BigDecimal** | The number of users in this group |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GENERIC | &quot;generic&quot; |
| CLASS_TEACHERS | &quot;classTeachers&quot; |
| CLASS_STUDENTS | &quot;classStudents&quot; |



