

# CreateUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consoleAccess** | **Boolean** | Enables access to the ActiveMQ Web Console for the ActiveMQ user. |  [optional] |
|**groups** | **List&lt;String&gt;** | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. |  [optional] |
|**password** | **String** | Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:&#x3D;). |  |
|**replicationUser** | **Boolean** | Defines if this user is intended for CRDR replication purposes. |  [optional] |



