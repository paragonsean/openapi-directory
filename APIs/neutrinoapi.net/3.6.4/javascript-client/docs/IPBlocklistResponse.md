# NeutrinoApi.IPBlocklistResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocklists** | **[String]** | An array of strings indicating which blocklist categories this IP is listed on | 
**cidr** | **String** | The CIDR address for this listing (only set if the IP is listed) | 
**ip** | **String** | The IP address | 
**isBot** | **Boolean** | IP is hosting a malicious bot or is part of a botnet. This is a broad category which includes brute-force crackers | 
**isDshield** | **Boolean** | IP has been flagged as a significant attack source by DShield (dshield.org) | 
**isExploitBot** | **Boolean** | IP is hosting an exploit finding bot or is running exploit scanning software | 
**isHijacked** | **Boolean** | IP is part of a hijacked netblock or a netblock controlled by a criminal organization | 
**isListed** | **Boolean** | Is this IP on a blocklist | 
**isMalware** | **Boolean** | IP is involved in distributing or is running malware | 
**isProxy** | **Boolean** | IP has been detected as an anonymous web proxy or anonymous HTTP proxy | 
**isSpamBot** | **Boolean** | IP address is hosting a spam bot, comment spamming or any other spamming type software | 
**isSpider** | **Boolean** | IP is running a hostile web spider / web crawler | 
**isSpyware** | **Boolean** | IP is involved in distributing or is running spyware | 
**isTor** | **Boolean** | IP is a Tor node or running a Tor related service | 
**isVpn** | **Boolean** | IP belongs to a public VPN provider (only set if the &#39;vpn-lookup&#39; option is enabled) | 
**lastSeen** | **Number** | The unix time when this IP was last seen on any blocklist. IPs are automatically removed after 7 days therefor this value will never be older than 7 days | 
**listCount** | **Number** | The number of blocklists the IP is listed on | 
**sensors** | [**[BlocklistSensor]**](BlocklistSensor.md) | An array of objects containing details on which specific sensors detected the IP | 


