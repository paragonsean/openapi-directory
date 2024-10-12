

# AuthorizedOrgsDesc

`AuthorizedOrgsDesc` contains data for an organization's authorization policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetType** | [**AssetTypeEnum**](#AssetTypeEnum) | The asset type of this authorized orgs desc. Valid values are &#x60;ASSET_TYPE_DEVICE&#x60;, and &#x60;ASSET_TYPE_CREDENTIAL_STRENGTH&#x60;. |  [optional] |
|**authorizationDirection** | [**AuthorizationDirectionEnum**](#AuthorizationDirectionEnum) | The direction of the authorization relationship between this organization and the organizations listed in the &#x60;orgs&#x60; field. The valid values for this field include the following: &#x60;AUTHORIZATION_DIRECTION_FROM&#x60;: Allows this organization to evaluate traffic in the organizations listed in the &#x60;orgs&#x60; field. &#x60;AUTHORIZATION_DIRECTION_TO&#x60;: Allows the organizations listed in the &#x60;orgs&#x60; field to evaluate the traffic in this organization. For the authorization relationship to take effect, all of the organizations must authorize and specify the appropriate relationship direction. For example, if organization A authorized organization B and C to evaluate its traffic, by specifying &#x60;AUTHORIZATION_DIRECTION_TO&#x60; as the authorization direction, organizations B and C must specify &#x60;AUTHORIZATION_DIRECTION_FROM&#x60; as the authorization direction in their &#x60;AuthorizedOrgsDesc&#x60; resource. |  [optional] |
|**authorizationType** | [**AuthorizationTypeEnum**](#AuthorizationTypeEnum) | A granular control type for authorization levels. Valid value is &#x60;AUTHORIZATION_TYPE_TRUST&#x60;. |  [optional] |
|**name** | **String** | Resource name for the &#x60;AuthorizedOrgsDesc&#x60;. Format: &#x60;accessPolicies/{access_policy}/authorizedOrgsDescs/{authorized_orgs_desc}&#x60;. The &#x60;authorized_orgs_desc&#x60; component must begin with a letter, followed by alphanumeric characters or &#x60;_&#x60;. After you create an &#x60;AuthorizedOrgsDesc&#x60;, you cannot change its &#x60;name&#x60;. |  [optional] |
|**orgs** | **List&lt;String&gt;** | The list of organization ids in this AuthorizedOrgsDesc. Format: &#x60;organizations/&#x60; Example: &#x60;organizations/123456&#x60; |  [optional] |



## Enum: AssetTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ASSET_TYPE_UNSPECIFIED&quot; |
| DEVICE | &quot;ASSET_TYPE_DEVICE&quot; |
| CREDENTIAL_STRENGTH | &quot;ASSET_TYPE_CREDENTIAL_STRENGTH&quot; |



## Enum: AuthorizationDirectionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTHORIZATION_DIRECTION_UNSPECIFIED&quot; |
| TO | &quot;AUTHORIZATION_DIRECTION_TO&quot; |
| FROM | &quot;AUTHORIZATION_DIRECTION_FROM&quot; |



## Enum: AuthorizationTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTHORIZATION_TYPE_UNSPECIFIED&quot; |
| TRUST | &quot;AUTHORIZATION_TYPE_TRUST&quot; |



