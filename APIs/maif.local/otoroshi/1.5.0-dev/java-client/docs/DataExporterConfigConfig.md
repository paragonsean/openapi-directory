

# DataExporterConfigConfig

Data Exporter config

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterUri** | **String** | URL of the elastic cluster |  |
|**headers** | **Map&lt;String, String&gt;** | Optional headers |  |
|**index** | **String** | Index for events. Default is otoroshi-events |  |
|**password** | **String** | Optional password |  |
|**type** | **String** | Type of events. Default is event |  |
|**user** | **String** | Optional user |  |
|**keyPass** | **String** | Optional keypass |  [optional] |
|**keyStore** | **String** | Optional path to keystore |  [optional] |
|**servers** | **List&lt;String&gt;** | URLs of the kafka servers |  |
|**topic** | **String** | Topic |  |
|**trustore** | **String** | Optional path to trustore |  [optional] |
|**namespace** | **String** | Namespace |  |
|**tenant** | **String** | Tenant |  |
|**uri** | **List&lt;String&gt;** | URI of the pulsar server |  |
|**path** | **String** | Path to file |  |
|**to** | **List&lt;String&gt;** | Email adresses of recipents |  [optional] |
|**url** | **String** | Url of mailer |  [optional] |
|**apiKey** | **String** | Mailgun apiKey |  [optional] |
|**domain** | **String** | Mailgun domain |  [optional] |
|**eu** | **Boolean** | Whether the mailgun server is european |  [optional] |
|**apiKeyPrivate** | **String** | Mailjet private apiKey |  [optional] |
|**apiKeyPublic** | **String** | Sendgrid apiKey |  [optional] |
|**config** | **Map&lt;String, String&gt;** | Custom data exporter config |  |
|**ref** | **String** | Script Ref |  |



