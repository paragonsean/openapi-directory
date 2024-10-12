

# TrafficStats

Email traffic statistics pertaining to a specific date.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryErrors** | [**List&lt;DeliveryError&gt;**](DeliveryError.md) | Delivery errors for the domain. This metric only pertains to traffic that passed [SPF](http://www.openspf.org/) or [DKIM](http://www.dkim.org/). |  [optional] |
|**dkimSuccessRatio** | **Double** | The ratio of mail that successfully authenticated with DKIM vs. all mail that attempted to authenticate with [DKIM](http://www.dkim.org/). Spoofed mail is excluded. |  [optional] |
|**dmarcSuccessRatio** | **Double** | The ratio of mail that passed [DMARC](https://dmarc.org/) alignment checks vs all mail received from the domain that successfully authenticated with either of [SPF](http://www.openspf.org/) or [DKIM](http://www.dkim.org/). |  [optional] |
|**domainReputation** | [**DomainReputationEnum**](#DomainReputationEnum) | Reputation of the domain. |  [optional] |
|**inboundEncryptionRatio** | **Double** | The ratio of incoming mail (to Gmail), that passed secure transport (TLS) vs all mail received from that domain. This metric only pertains to traffic that passed [SPF](http://www.openspf.org/) or [DKIM](http://www.dkim.org/). |  [optional] |
|**ipReputations** | [**List&lt;IpReputation&gt;**](IpReputation.md) | Reputation information pertaining to the IP addresses of the email servers for the domain. There is exactly one entry for each reputation category except REPUTATION_CATEGORY_UNSPECIFIED. |  [optional] |
|**name** | **String** | The resource name of the traffic statistics. Traffic statistic names have the form &#x60;domains/{domain}/trafficStats/{date}&#x60;, where domain_name is the fully qualified domain name (i.e., mymail.mydomain.com) of the domain this traffic statistics pertains to and date is the date in yyyymmdd format that these statistics corresponds to. For example: domains/mymail.mydomain.com/trafficStats/20160807 |  [optional] |
|**outboundEncryptionRatio** | **Double** | The ratio of outgoing mail (from Gmail) that was accepted over secure transport (TLS). |  [optional] |
|**spammyFeedbackLoops** | [**List&lt;FeedbackLoop&gt;**](FeedbackLoop.md) | Spammy [Feedback loop identifiers] (https://support.google.com/mail/answer/6254652) with their individual spam rates. This metric only pertains to traffic that is authenticated by [DKIM](http://www.dkim.org/). |  [optional] |
|**spfSuccessRatio** | **Double** | The ratio of mail that successfully authenticated with SPF vs. all mail that attempted to authenticate with [SPF](http://www.openspf.org/). Spoofed mail is excluded. |  [optional] |
|**userReportedSpamRatio** | **Double** | The ratio of user-report spam vs. email that was sent to the inbox. This is potentially inexact -- users may want to refer to the description of the interval fields userReportedSpamRatioLowerBound and userReportedSpamRatioUpperBound for more explicit accuracy guarantees. This metric only pertains to emails authenticated by [DKIM](http://www.dkim.org/). |  [optional] |
|**userReportedSpamRatioLowerBound** | **Double** | The lower bound of the confidence interval for the user reported spam ratio. If this field is set, then the value of userReportedSpamRatio is set to the midpoint of this interval and is thus inexact. However, the true ratio is guaranteed to be in between this lower bound and the corresponding upper bound 95% of the time. This metric only pertains to emails authenticated by [DKIM](http://www.dkim.org/). |  [optional] |
|**userReportedSpamRatioUpperBound** | **Double** | The upper bound of the confidence interval for the user reported spam ratio. If this field is set, then the value of userReportedSpamRatio is set to the midpoint of this interval and is thus inexact. However, the true ratio is guaranteed to be in between this upper bound and the corresponding lower bound 95% of the time. This metric only pertains to emails authenticated by [DKIM](http://www.dkim.org/). |  [optional] |



## Enum: DomainReputationEnum

| Name | Value |
|---- | -----|
| REPUTATION_CATEGORY_UNSPECIFIED | &quot;REPUTATION_CATEGORY_UNSPECIFIED&quot; |
| HIGH | &quot;HIGH&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LOW | &quot;LOW&quot; |
| BAD | &quot;BAD&quot; |



