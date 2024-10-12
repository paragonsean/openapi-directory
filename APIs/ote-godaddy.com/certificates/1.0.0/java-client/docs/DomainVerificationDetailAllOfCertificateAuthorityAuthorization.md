

# DomainVerificationDetailAllOfCertificateAuthorityAuthorization

Contains information about the last Certificate Authority Authorization (CAA) Lookup details for the specified domain.  In order for a domain to be eligible to be included in the certificate, the entire domain hierarchy must be scanned for DNS CAA records, as outlined by RFC 6844.  The absence of any CAA records found in the domain hierarchy indicates that the domain may be included in the certificate. Alternatively, if CAA records are found when scanning the domain hierarchy, the domain may be included in the certificate as long as `godaddy.com` or `starfieldtech.com` is found in the DNS record value. However, if CAA records are found, yet `godaddy.com` or `starfieldtech.com` is not found in any CAA record's value, then we must drop the domain from the certificate request.  In the case where there are repeated DNS errors when scanning the domain hierarchy for CAA records, thus ending in an unsuccessful scan, then the domain can still be included in the certificate provided the primary domain is not setup with DNSSEC. Conversely, if DNSSEC is found to be setup on the primary domain when scanning following repeated CAA failures, the domain must be dropped from the certificate request. Finally, if DNS errors persist to the point where a successful DNSSEC query could not be obtained, then the domain must be dropped from the certificate request. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedAt** | **String** | The date the certificate request completed processing. |  [optional] |
|**queryPaths** | **List&lt;String&gt;** | Details all the individual DNS paths that were scanned for CAA records for this domain, as detailed by RFC 6844. This element not only contains the parts determined from parsing the domain, but also any CNAME or DNAME targets specified by any of those individual parts. |  [optional] |
|**recommendations** | [**List&lt;RecommendationsEnum&gt;**](#List&lt;RecommendationsEnum&gt;) | Returns a list of fix recommendations if the query was unsuccessful, or if the domain was dropped from the certificate request, so that a subsequent certificate request with the specified domain will successfully pass its CAA scan. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Returns the status of the CAA Lookup for the specified domain: * &#x60;PENDING&#x60; - The CAA lookup has not yet been attempted for the specified domain. * &#x60;REMOVED_DNS_ERROR&#x60; - Repeated errors occurred while scanning for CAA records, thereby resulting in a DNSSEC scan. DNS errors then prevented the system from determining if DNSSEC was enabled for the specified domain, and it had to be removed from the certificate request. * &#x60;REMOVED_DNSSEC_ENABLED&#x60; - Repeated errors occurred while scanning for CAA records, thereby resulting in a DNSSEC scan. DNSSEC was determined to be enabled for the specified domain, and it had to be removed from the certificate request. * &#x60;REMOVED_NOT_FOUND_CA&#x60; - CAA records were found during the CAA lookup for the speicified domain, but &#x60;godaddy.com&#x60; or &#x60;starfieldtech.com&#x60; was not listed as a value, thereby not allowing us to issue a certificate with this domain. The specified domain was removed from the certificate request. * &#x60;REMOVED_UNKNOWN_CRITICAL_TAG&#x60; - A CAA record was found during the CAA lookup with its Critical bit set, as outlined by RFC 6844, yet the Tag of the CAA record was not understood (as outlined by RFC 6844). The specified domain was removed from the certificate request. * &#x60;SUCCESS_CAA&#x60; - The CAA lookup was successful for the specified domain, and the domain can remain in the certificate request. * &#x60;SUCCESS_DNSSEC&#x60; - Repeated errors occurred while scanning for CAA records, thereby resulting in a DNSSEC scan. The system detemined that DNSSEC was not enabled for the specified domain, so the domain is allowed to remain in the certificate request.  |  [optional] |



## Enum: List&lt;RecommendationsEnum&gt;

| Name | Value |
|---- | -----|
| ADD_CA_TO_CAA | &quot;ADD_CA_TO_CAA&quot; |
| CREATE_TARGET_DOMAIN_CAA | &quot;CREATE_TARGET_DOMAIN_CAA&quot; |
| DISABLE_DNSSEC | &quot;DISABLE_DNSSEC&quot; |
| FIX_CRITICAL_TAG | &quot;FIX_CRITICAL_TAG&quot; |
| VALIDATE_SOA | &quot;VALIDATE_SOA&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| REMOVED_DNS_ERROR | &quot;REMOVED_DNS_ERROR&quot; |
| REMOVED_DNSSEC_ENABLED | &quot;REMOVED_DNSSEC_ENABLED&quot; |
| REMOVED_NOT_FOUND_CA | &quot;REMOVED_NOT_FOUND_CA&quot; |
| REMOVED_UNKNOWN_CRITICAL_TAG | &quot;REMOVED_UNKNOWN_CRITICAL_TAG&quot; |
| SUCCESS_CAA | &quot;SUCCESS_CAA&quot; |
| SUCCESS_DNSSEC | &quot;SUCCESS_DNSSEC&quot; |



