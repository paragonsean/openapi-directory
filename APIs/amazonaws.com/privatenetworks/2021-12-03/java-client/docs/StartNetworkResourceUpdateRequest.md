

# StartNetworkResourceUpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitmentConfiguration** | [**ActivateNetworkSiteRequestCommitmentConfiguration**](ActivateNetworkSiteRequestCommitmentConfiguration.md) |  |  [optional] |
|**networkResourceArn** | **String** | The Amazon Resource Name (ARN) of the network resource. |  |
|**returnReason** | **String** | The reason for the return. Providing a reason for a return is optional. |  [optional] |
|**shippingAddress** | [**ActivateNetworkSiteRequestShippingAddress**](ActivateNetworkSiteRequestShippingAddress.md) |  |  [optional] |
|**updateType** | [**UpdateTypeEnum**](#UpdateTypeEnum) | &lt;p&gt;The update type.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;REPLACE&lt;/code&gt; - Submits a request to replace a defective radio unit. We provide a shipping label that you can use for the return process and we ship a replacement radio unit to you.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RETURN&lt;/code&gt; - Submits a request to return a radio unit that you no longer need. We provide a shipping label that you can use for the return process.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;COMMITMENT&lt;/code&gt; - Submits a request to change or renew the commitment period. If you choose this value, then you must set &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/private-networks/latest/APIReference/API_StartNetworkResourceUpdate.html#privatenetworks-StartNetworkResourceUpdate-request-commitmentConfiguration\&quot;&gt; &lt;code&gt;commitmentConfiguration&lt;/code&gt; &lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |



## Enum: UpdateTypeEnum

| Name | Value |
|---- | -----|
| REPLACE | &quot;REPLACE&quot; |
| RETURN | &quot;RETURN&quot; |
| COMMITMENT | &quot;COMMITMENT&quot; |



