

# GoogleCloudApigeeV1SecurityActionConditionConfig

The following are a list of conditions. A valid SecurityAction must contain at least one condition. Within a condition, each element is ORed. Across conditions elements are ANDed. For example if a SecurityAction has the following: ip_address_ranges: [\"ip1\", \"ip2\"] and bot_reasons: [\"Flooder\", \"Robot Abuser\"] then this is interpreted as: enforce the action if the incoming request has ((ip_address_ranges = \"ip1\" OR ip_address_ranges = \"ip2\") AND (bot_reasons=\"Flooder\" OR bot_reasons=\"Robot Abuser\")). Conditions other than ip_address_ranges and bot_reasons cannot be ANDed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTokens** | **List&lt;String&gt;** | Optional. A list of access_tokens. Limit 1000 per action. |  [optional] |
|**apiKeys** | **List&lt;String&gt;** | Optional. A list of API keys. Limit 1000 per action. |  [optional] |
|**apiProducts** | **List&lt;String&gt;** | Optional. A list of API Products. Limit 1000 per action. |  [optional] |
|**botReasons** | **List&lt;String&gt;** | Optional. A list of Bot Reasons. Current options: Flooder, Brute Guessor, Static Content Scraper, OAuth Abuser, Robot Abuser, TorListRule, Advanced Anomaly Detection, Advanced API Scraper, Search Engine Crawlers, Public Clouds, Public Cloud AWS, Public Cloud Azure, and Public Cloud Google. |  [optional] |
|**developerApps** | **List&lt;String&gt;** | Optional. A list of developer apps. Limit 1000 per action. |  [optional] |
|**developers** | **List&lt;String&gt;** | Optional. A list of developers. Limit 1000 per action. |  [optional] |
|**ipAddressRanges** | **List&lt;String&gt;** | Optional. A list of IP addresses. This could be either IPv4 or IPv6. Limited to 100 per action. |  [optional] |
|**userAgents** | **List&lt;String&gt;** | Optional. A list of user agents to deny. We look for exact matches. Limit 50 per action. |  [optional] |



