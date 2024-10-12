# OpenapiJsClient.DomainVerificationDetailAllOfCertificateAuthorityAuthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAt** | **String** | The date the certificate request completed processing. | [optional] 
**queryPaths** | **[String]** | Details all the individual DNS paths that were scanned for CAA records for this domain, as detailed by RFC 6844. This element not only contains the parts determined from parsing the domain, but also any CNAME or DNAME targets specified by any of those individual parts. | [optional] 
**recommendations** | **[String]** | Returns a list of fix recommendations if the query was unsuccessful, or if the domain was dropped from the certificate request, so that a subsequent certificate request with the specified domain will successfully pass its CAA scan. | [optional] 
**status** | **String** | Returns the status of the CAA Lookup for the specified domain: * &#x60;PENDING&#x60; - The CAA lookup has not yet been attempted for the specified domain. * &#x60;REMOVED_DNS_ERROR&#x60; - Repeated errors occurred while scanning for CAA records, thereby resulting in a DNSSEC scan. DNS errors then prevented the system from determining if DNSSEC was enabled for the specified domain, and it had to be removed from the certificate request. * &#x60;REMOVED_DNSSEC_ENABLED&#x60; - Repeated errors occurred while scanning for CAA records, thereby resulting in a DNSSEC scan. DNSSEC was determined to be enabled for the specified domain, and it had to be removed from the certificate request. * &#x60;REMOVED_NOT_FOUND_CA&#x60; - CAA records were found during the CAA lookup for the speicified domain, but &#x60;godaddy.com&#x60; or &#x60;starfieldtech.com&#x60; was not listed as a value, thereby not allowing us to issue a certificate with this domain. The specified domain was removed from the certificate request. * &#x60;REMOVED_UNKNOWN_CRITICAL_TAG&#x60; - A CAA record was found during the CAA lookup with its Critical bit set, as outlined by RFC 6844, yet the Tag of the CAA record was not understood (as outlined by RFC 6844). The specified domain was removed from the certificate request. * &#x60;SUCCESS_CAA&#x60; - The CAA lookup was successful for the specified domain, and the domain can remain in the certificate request. * &#x60;SUCCESS_DNSSEC&#x60; - Repeated errors occurred while scanning for CAA records, thereby resulting in a DNSSEC scan. The system detemined that DNSSEC was not enabled for the specified domain, so the domain is allowed to remain in the certificate request.  | [optional] 



## Enum: [RecommendationsEnum]


* `ADD_CA_TO_CAA` (value: `"ADD_CA_TO_CAA"`)

* `CREATE_TARGET_DOMAIN_CAA` (value: `"CREATE_TARGET_DOMAIN_CAA"`)

* `DISABLE_DNSSEC` (value: `"DISABLE_DNSSEC"`)

* `FIX_CRITICAL_TAG` (value: `"FIX_CRITICAL_TAG"`)

* `VALIDATE_SOA` (value: `"VALIDATE_SOA"`)





## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `REMOVED_DNS_ERROR` (value: `"REMOVED_DNS_ERROR"`)

* `REMOVED_DNSSEC_ENABLED` (value: `"REMOVED_DNSSEC_ENABLED"`)

* `REMOVED_NOT_FOUND_CA` (value: `"REMOVED_NOT_FOUND_CA"`)

* `REMOVED_UNKNOWN_CRITICAL_TAG` (value: `"REMOVED_UNKNOWN_CRITICAL_TAG"`)

* `SUCCESS_CAA` (value: `"SUCCESS_CAA"`)

* `SUCCESS_DNSSEC` (value: `"SUCCESS_DNSSEC"`)




