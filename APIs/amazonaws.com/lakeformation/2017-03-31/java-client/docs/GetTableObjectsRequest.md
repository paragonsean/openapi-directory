

# GetTableObjectsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The catalog containing the governed table. Defaults to the caller’s account. |  [optional] |
|**databaseName** | **String** | The database containing the governed table. |  |
|**tableName** | **String** | The governed table for which to retrieve objects. |  |
|**transactionId** | **String** | The transaction ID at which to read the governed table contents. If this transaction has aborted, an error is returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with &lt;code&gt;QueryAsOfTime&lt;/code&gt;. |  [optional] |
|**queryAsOfTime** | **OffsetDateTime** | The time as of when to read the governed table contents. If not set, the most recent transaction commit time is used. Cannot be specified along with &lt;code&gt;TransactionId&lt;/code&gt;. |  [optional] |
|**partitionPredicate** | **String** | &lt;p&gt;A predicate to filter the objects returned based on the partition keys defined in the governed table.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The comparison operators supported are: &#x3D;, &amp;gt;, &amp;lt;, &amp;gt;&#x3D;, &amp;lt;&#x3D;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The logical operators supported are: AND&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The data types supported are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss\&quot;), string and decimal.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**maxResults** | **Integer** | Specifies how many values to return in a page. |  [optional] |
|**nextToken** | **String** | A continuation token if this is not the first call to retrieve these objects. |  [optional] |



