# ApigeeApi.GoogleCloudApigeeV1SecurityActionConditionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokens** | **[String]** | Optional. A list of access_tokens. Limit 1000 per action. | [optional] 
**apiKeys** | **[String]** | Optional. A list of API keys. Limit 1000 per action. | [optional] 
**apiProducts** | **[String]** | Optional. A list of API Products. Limit 1000 per action. | [optional] 
**botReasons** | **[String]** | Optional. A list of Bot Reasons. Current options: Flooder, Brute Guessor, Static Content Scraper, OAuth Abuser, Robot Abuser, TorListRule, Advanced Anomaly Detection, Advanced API Scraper, Search Engine Crawlers, Public Clouds, Public Cloud AWS, Public Cloud Azure, and Public Cloud Google. | [optional] 
**developerApps** | **[String]** | Optional. A list of developer apps. Limit 1000 per action. | [optional] 
**developers** | **[String]** | Optional. A list of developers. Limit 1000 per action. | [optional] 
**ipAddressRanges** | **[String]** | Optional. A list of IP addresses. This could be either IPv4 or IPv6. Limited to 100 per action. | [optional] 
**userAgents** | **[String]** | Optional. A list of user agents to deny. We look for exact matches. Limit 50 per action. | [optional] 


