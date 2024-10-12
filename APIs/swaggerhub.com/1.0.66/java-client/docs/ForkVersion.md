

# ForkVersion


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name for the forked definition. Must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html). Can be the name of an existing definition, in which case the fork will become a new version in that definition, unless that version already exists. |  |
|**owner** | **String** | The account to fork into. Can be an organization or user name. Case-sensitive. The authenticated user must have permissions to create definitions in this account. |  |
|**_private** | **Boolean** | Whether the forked version should be public (&#x60;false&#x60;) or private (&#x60;true&#x60;). If the value is not set, the original version&#39;s setting will be used. |  [optional] |
|**project** | **String** | If forking into an organization, you can optionally specify an existing project to add the forked definition to. |  [optional] |
|**version** | **String** | Version identifier for the forked definition. Must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format). If forking into an existing definition, this version must not already exist. |  |



