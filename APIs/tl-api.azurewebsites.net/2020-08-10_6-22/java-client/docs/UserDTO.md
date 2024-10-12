

# UserDTO

The UserDTO Class. Contains relevant fields of User DTO by masking actual User entity's fields in application.             

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | Account number of the user.It can be any stakeholder of the application.even can be a gym.              |  [optional] |
|**externalEntityNumber** | **String** | Entity number that make a relationship with BOX API DB.              |  [optional] |
|**guardian** | **Integer** | Gaurdian of the this user if he/she is under 18 years old.              |  [optional] |
|**gymNumber** | **String** | If this user is a gym, then the gym number.              |  [optional] |
|**introduceBy** | **Integer** | If Someone introduced this user to the system, then that user&#39;s UserId.              |  [optional] |
|**name** | **String** | Name of the user.              |  [optional] |
|**number** | **String** | Unique number maintain by application to idenify user.              |  [optional] |
|**typeId** | **Integer** | Type of the user.              |  [optional] |
|**userId** | **Integer** | Indentity number(primary key) for user object. Generated in DB table when inserting a record.              |  [optional] |



