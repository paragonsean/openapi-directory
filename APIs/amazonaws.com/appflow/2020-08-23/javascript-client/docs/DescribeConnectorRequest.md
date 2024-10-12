# AmazonAppflow.DescribeConnectorRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorType** | **String** | The connector type, such as CUSTOMCONNECTOR, Saleforce, Marketo. Please choose CUSTOMCONNECTOR for Lambda based custom connectors. | 
**connectorLabel** | **String** | The label of the connector. The label is unique for each &lt;code&gt;ConnectorRegistration&lt;/code&gt; in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/. | [optional] 



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




