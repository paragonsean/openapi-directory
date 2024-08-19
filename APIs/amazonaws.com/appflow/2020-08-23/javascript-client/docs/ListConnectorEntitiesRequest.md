# AmazonAppflow.ListConnectorEntitiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorProfileName** | **String** |  The name of the connector profile. The name is unique for each &lt;code&gt;ConnectorProfile&lt;/code&gt; in the Amazon Web Services account, and is used to query the downstream connector.  | [optional] 
**connectorType** | **String** |  The type of connector, such as Salesforce, Amplitude, and so on.  | [optional] 
**entitiesPath** | **String** |  This optional parameter is specific to connector implementation. Some connectors support multiple levels or categories of entities. You can find out the list of roots for such providers by sending a request without the &lt;code&gt;entitiesPath&lt;/code&gt; parameter. If the connector supports entities at different roots, this initial request returns the list of roots. Otherwise, this request returns all entities supported by the provider.  | [optional] 
**apiVersion** | **String** | The version of the API that&#39;s used by the connector. | [optional] 
**maxResults** | **Number** | The maximum number of items that the operation returns in the response. | [optional] 
**nextToken** | **String** | A token that was provided by your prior &lt;code&gt;ListConnectorEntities&lt;/code&gt; operation if the response was too big for the page size. You specify this token to get the next page of results in paginated response. | [optional] 



## Enum: ConnectorTypeEnum


* `Salesforce` (value: `"Salesforce"`)

* `Singular` (value: `"Singular"`)

* `Slack` (value: `"Slack"`)

* `Redshift` (value: `"Redshift"`)

* `S3` (value: `"S3"`)

* `Marketo` (value: `"Marketo"`)

* `Googleanalytics` (value: `"Googleanalytics"`)

* `Zendesk` (value: `"Zendesk"`)

* `Servicenow` (value: `"Servicenow"`)

* `Datadog` (value: `"Datadog"`)

* `Trendmicro` (value: `"Trendmicro"`)

* `Snowflake` (value: `"Snowflake"`)

* `Dynatrace` (value: `"Dynatrace"`)

* `Infornexus` (value: `"Infornexus"`)

* `Amplitude` (value: `"Amplitude"`)

* `Veeva` (value: `"Veeva"`)

* `EventBridge` (value: `"EventBridge"`)

* `LookoutMetrics` (value: `"LookoutMetrics"`)

* `Upsolver` (value: `"Upsolver"`)

* `Honeycode` (value: `"Honeycode"`)

* `CustomerProfiles` (value: `"CustomerProfiles"`)

* `SAPOData` (value: `"SAPOData"`)

* `CustomConnector` (value: `"CustomConnector"`)

* `Pardot` (value: `"Pardot"`)




