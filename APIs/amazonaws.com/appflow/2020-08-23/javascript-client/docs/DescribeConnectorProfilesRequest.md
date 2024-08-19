# AmazonAppflow.DescribeConnectorProfilesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorProfileNames** | **[String]** |  The name of the connector profile. The name is unique for each &lt;code&gt;ConnectorProfile&lt;/code&gt; in the Amazon Web Services account.  | [optional] 
**connectorType** | **String** |  The type of connector, such as Salesforce, Amplitude, and so on.  | [optional] 
**connectorLabel** | **String** | The name of the connector. The name is unique for each &lt;code&gt;ConnectorRegistration&lt;/code&gt; in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/. | [optional] 
**maxResults** | **Number** |  Specifies the maximum number of items that should be returned in the result set. The default for &lt;code&gt;maxResults&lt;/code&gt; is 20 (for all paginated API operations).  | [optional] 
**nextToken** | **String** |  The pagination token for the next page of data.  | [optional] 



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




