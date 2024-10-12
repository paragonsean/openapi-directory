

# AssociateRepositoryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**repository** | [**AssociateRepositoryRequestRepository**](AssociateRepositoryRequestRepository.md) |  |  |
|**clientRequestToken** | **String** | Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate repository associations if there are failures and retries. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;i&gt;tag key&lt;/i&gt; (for example, &lt;code&gt;CostCenter&lt;/code&gt;, &lt;code&gt;Environment&lt;/code&gt;, &lt;code&gt;Project&lt;/code&gt;, or &lt;code&gt;Secret&lt;/code&gt;). Tag keys are case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An optional field known as a &lt;i&gt;tag value&lt;/i&gt; (for example, &lt;code&gt;111122223333&lt;/code&gt;, &lt;code&gt;Production&lt;/code&gt;, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**kmSKeyDetails** | [**AssociateRepositoryRequestKMSKeyDetails**](AssociateRepositoryRequestKMSKeyDetails.md) |  |  [optional] |



