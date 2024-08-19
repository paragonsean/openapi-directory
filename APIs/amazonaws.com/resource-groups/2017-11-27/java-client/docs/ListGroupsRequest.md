

# ListGroupsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | [**List&lt;GroupFilter&gt;**](GroupFilter.md) | &lt;p&gt;Filters, formatted as &lt;a&gt;GroupFilter&lt;/a&gt; objects, that you want to apply to a &lt;code&gt;ListGroups&lt;/code&gt; operation.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-type&lt;/code&gt; - Filter the results to include only those of the specified resource types. Specify up to five resource types in the format &lt;code&gt;AWS::&lt;i&gt;ServiceCode&lt;/i&gt;::&lt;i&gt;ResourceType&lt;/i&gt; &lt;/code&gt;. For example, &lt;code&gt;AWS::EC2::Instance&lt;/code&gt;, or &lt;code&gt;AWS::S3::Bucket&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;configuration-type&lt;/code&gt; - Filter the results to include only those groups that have the specified configuration types attached. The current supported values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS::EC2::CapacityReservationPool&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS::EC2::HostManagement&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



