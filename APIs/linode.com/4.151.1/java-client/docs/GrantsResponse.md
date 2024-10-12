

# GrantsResponse

A structure representing all grants a restricted User has on the Account. Not available for unrestricted users, as they have access to everything without grants. If retrieved from the `/profile/grants` endpoint, entities to which a User has no access will be omitted. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**database** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each Database that is owned by this Account.  |  [optional] |
|**domain** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each Domain that is owned by this Account.  |  [optional] |
|**global** | [**GrantsResponseGlobal**](GrantsResponseGlobal.md) |  |  [optional] |
|**image** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each Image that is owned by this Account.  |  [optional] |
|**linode** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each Linode that is owned by this Account.  |  [optional] |
|**longview** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each Longview Client that is owned by this Account.  |  [optional] |
|**nodebalancer** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each NodeBalancer that is owned by this Account.  |  [optional] |
|**stackscript** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each StackScript that is owned by this Account.  |  [optional] |
|**volume** | [**List&lt;Grant&gt;**](Grant.md) | The grants this User has for each Block Storage Volume that is owned by this Account.  |  [optional] |



