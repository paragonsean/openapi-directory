

# SenderAuthorization

the authorization used by the user who has performed the operation that led to this event. This captures the RBAC properties of the event. These usually include the 'action', 'role' and the 'scope'

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | the permissible actions. For instance: microsoft.support/supporttickets/write |  [optional] |
|**role** | **String** | the role of the user. For instance: Subscription Admin |  [optional] |
|**scope** | **String** | the scope. |  [optional] |



