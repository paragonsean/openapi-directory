# AmazonRoute53.ChangeCidrCollectionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionVersion** | **Number** | &lt;p&gt;A sequential counter that Amazon Route 53 sets to 1 when you create a collection and increments it by 1 each time you update the collection.&lt;/p&gt; &lt;p&gt;We recommend that you use &lt;code&gt;ListCidrCollection&lt;/code&gt; to get the current value of &lt;code&gt;CollectionVersion&lt;/code&gt; for the collection that you want to update, and then include that value with the change request. This prevents Route 53 from overwriting an intervening update: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the value in the request matches the value of &lt;code&gt;CollectionVersion&lt;/code&gt; in the collection, Route 53 updates the collection.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value of &lt;code&gt;CollectionVersion&lt;/code&gt; in the collection is greater than the value in the request, the collection was changed after you got the version number. Route 53 does not update the collection, and it returns a &lt;code&gt;CidrCollectionVersionMismatch&lt;/code&gt; error. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**changes** | [**[CidrCollectionChange]**](CidrCollectionChange.md) |  Information about changes to a CIDR collection. | 


