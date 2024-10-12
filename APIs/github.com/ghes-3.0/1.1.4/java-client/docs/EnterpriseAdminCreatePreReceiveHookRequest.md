

# EnterpriseAdminCreatePreReceiveHookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowDownstreamConfiguration** | **Boolean** | Whether enforcement can be overridden at the org or repo level. default: &#x60;false&#x60; |  [optional] |
|**enforcement** | **String** | The state of enforcement for this hook. default: &#x60;disabled&#x60; |  [optional] |
|**environment** | **Map&lt;String, Object&gt;** | The pre-receive environment where the script is executed. |  |
|**name** | **String** | The name of the hook. |  |
|**script** | **String** | The script that the hook runs. |  |
|**scriptRepository** | **Map&lt;String, Object&gt;** | The GitHub repository where the script is kept. |  |



