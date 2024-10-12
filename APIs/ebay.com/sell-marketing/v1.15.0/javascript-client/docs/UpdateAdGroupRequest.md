# MarketingApi.UpdateAdGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupStatus** | **String** | An enumeration value representing the current status of the ad group.&lt;p&gt;If the status of the ad is currently &lt;code&gt;ACTIVE&lt;/code&gt;, you can change status to &lt;code&gt;PAUSED&lt;/code&gt; or &lt;code&gt;ARCHIVED&lt;/code&gt;. If ad group is currently in &lt;code&gt;PAUSED&lt;/code&gt; status, you can change the status back to &lt;code&gt;ACTIVE&lt;/code&gt;. Ads that are currently in &lt;code&gt;ARCHIVED&lt;/code&gt; status cannot be made &lt;code&gt;ACTIVE&lt;/code&gt; again.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;ACTIVE&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;PAUSED&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;ARCHIVED&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/pls:AdGroupStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**defaultBid** | [**Amount**](Amount.md) |  | [optional] 
**name** | **String** | The updated name for the specified ad group. | [optional] 


