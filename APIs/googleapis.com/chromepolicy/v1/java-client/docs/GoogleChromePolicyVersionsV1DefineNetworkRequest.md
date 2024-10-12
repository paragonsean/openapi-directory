

# GoogleChromePolicyVersionsV1DefineNetworkRequest

Request object for creating a new network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. Name of the new created network. |  [optional] |
|**settings** | [**List&lt;GoogleChromePolicyVersionsV1NetworkSetting&gt;**](GoogleChromePolicyVersionsV1NetworkSetting.md) | Required. Detailed network settings. |  [optional] |
|**targetResource** | **String** | Required. The target resource on which this new network will be defined. The following resources are supported: * Organizational Unit (\&quot;orgunits/{orgunit_id}\&quot;) |  [optional] |



