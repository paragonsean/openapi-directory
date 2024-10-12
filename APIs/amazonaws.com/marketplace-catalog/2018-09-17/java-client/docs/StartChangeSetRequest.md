

# StartChangeSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalog** | **String** | The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;  |  |
|**changeSet** | [**List&lt;Change&gt;**](Change.md) | Array of &lt;code&gt;change&lt;/code&gt; object. |  |
|**changeSetName** | **String** | Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets.  |  [optional] |
|**clientRequestToken** | **String** | A unique token to identify the request to ensure idempotency. |  [optional] |
|**changeSetTags** | [**List&lt;Tag&gt;**](Tag.md) | A list of objects specifying each key name and value for the &lt;code&gt;ChangeSetTags&lt;/code&gt; property. |  [optional] |



