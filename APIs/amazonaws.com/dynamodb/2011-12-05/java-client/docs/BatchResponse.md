

# BatchResponse

The item attributes from a response in a specific table, along with the read resources consumed on the table during the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | **List&lt;Map&lt;String, AttributeValue&gt;&gt;** |  |  [optional] |
|**consumedCapacityUnits** | **Double** | The number of Capacity Units of the provisioned throughput of the table consumed during the operation. &lt;code&gt;GetItem&lt;/code&gt;, &lt;code&gt;BatchGetItem&lt;/code&gt;, &lt;code&gt;BatchWriteItem&lt;/code&gt;, &lt;code&gt;Query&lt;/code&gt;, and &lt;code&gt;Scan&lt;/code&gt; operations consume &lt;code&gt;ReadCapacityUnits&lt;/code&gt;, while &lt;code&gt;PutItem&lt;/code&gt;, &lt;code&gt;UpdateItem&lt;/code&gt;, and &lt;code&gt;DeleteItem&lt;/code&gt; operations consume &lt;code&gt;WriteCapacityUnits&lt;/code&gt;. |  [optional] |



