# AmazonAppflow.CreateConnectorProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorProfileName** | **String** |  The name of the connector profile. The name is unique for each &lt;code&gt;ConnectorProfile&lt;/code&gt; in your Amazon Web Services account.  | 
**kmsArn** | **String** |  The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don&#39;t provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.  | [optional] 
**connectorType** | **String** |  The type of connector, such as Salesforce, Amplitude, and so on.  | 
**connectorLabel** | **String** | The label of the connector. The label is unique for each &lt;code&gt;ConnectorRegistration&lt;/code&gt; in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/. | [optional] 
**connectionMode** | **String** |  Indicates the connection mode and specifies whether it is public or private. Private flows use Amazon Web Services PrivateLink to route data over Amazon Web Services infrastructure without exposing it to the public internet.  | 
**connectorProfileConfig** | [**CreateConnectorProfileRequestConnectorProfileConfig**](CreateConnectorProfileRequestConnectorProfileConfig.md) |  | 
**clientToken** | **String** | &lt;p&gt;The &lt;code&gt;clientToken&lt;/code&gt; parameter is an idempotency token. It ensures that your &lt;code&gt;CreateConnectorProfile&lt;/code&gt; request completes only once. You choose the value to pass. For example, if you don&#39;t receive a response from your request, you can safely retry the request with the same &lt;code&gt;clientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you omit a &lt;code&gt;clientToken&lt;/code&gt; value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.&lt;/p&gt; &lt;p&gt;If you specify input parameters that differ from your first request, an error occurs. If you use a different value for &lt;code&gt;clientToken&lt;/code&gt;, Amazon AppFlow considers it a new call to &lt;code&gt;CreateConnectorProfile&lt;/code&gt;. The token is active for 8 hours.&lt;/p&gt; | [optional] 



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





## Enum: ConnectionModeEnum


* `Public` (value: `"Public"`)

* `Private` (value: `"Private"`)




