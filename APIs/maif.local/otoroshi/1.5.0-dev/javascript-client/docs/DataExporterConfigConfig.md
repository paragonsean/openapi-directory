# OtoroshiAdminApi.DataExporterConfigConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterUri** | **String** | URL of the elastic cluster | 
**headers** | **{String: String}** | Optional headers | 
**index** | **String** | Index for events. Default is otoroshi-events | 
**password** | **String** | Optional password | 
**type** | **String** | Type of events. Default is event | 
**user** | **String** | Optional user | 
**keyPass** | **String** | Optional keypass | [optional] 
**keyStore** | **String** | Optional path to keystore | [optional] 
**servers** | **[String]** | URLs of the kafka servers | 
**topic** | **String** | Topic | 
**trustore** | **String** | Optional path to trustore | [optional] 
**namespace** | **String** | Namespace | 
**tenant** | **String** | Tenant | 
**uri** | **[String]** | URI of the pulsar server | 
**path** | **String** | Path to file | 
**to** | **[String]** | Email adresses of recipents | [optional] 
**url** | **String** | Url of mailer | [optional] 
**apiKey** | **String** | Mailgun apiKey | [optional] 
**domain** | **String** | Mailgun domain | [optional] 
**eu** | **Boolean** | Whether the mailgun server is european | [optional] 
**apiKeyPrivate** | **String** | Mailjet private apiKey | [optional] 
**apiKeyPublic** | **String** | Sendgrid apiKey | [optional] 
**config** | **{String: String}** | Custom data exporter config | 
**ref** | **String** | Script Ref | 


