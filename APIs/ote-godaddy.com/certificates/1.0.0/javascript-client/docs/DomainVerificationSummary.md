# OpenapiJsClient.DomainVerificationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | Timestamp indicating when the domain verification process was started | 
**dceToken** | **String** | DCE verification type token (if DCE verification type). | [optional] 
**domain** | **String** | Domain name | 
**domainEntityId** | **Number** | A unique identifier that can be leveraged for retrieving domain verification related information. Primarily used when troubleshooting a request | 
**modifiedAt** | **String** | Timestamp indicating when the domain verification process was last updated | 
**status** | **String** | Domain verification status:    * &#x60;AWAITING&#x60; - Verification pending customer input   * &#x60;INVALID&#x60; - SAN connected to a cancelled request   * &#x60;COMPLETED&#x60; - Verification completed   * &#x60;FAILED_VERIFICATION&#x60; - Verification failed   * &#x60;PENDING_POSSIBLE_FRAUD&#x60; - Flagged for a system level fraud review   * &#x60;VERIFIED_POSSIBLE_FRAUD&#x60; - Fraud detection reviewed but verified   * &#x60;DROPPED&#x60; - SAN dropped from request   * &#x60;REVOKED_CERT&#x60; - Certificate revoked   * &#x60;DROPPED_GOOGLE_SAFE_BROWSING&#x60; - SAN dropped from request due to Google Safe Browsing check   * &#x60;DROPPED_CERTIFICATE_AUTHORITY_AUTHORIZATION&#x60; - SAN dropped from request due to Certificate Authorization Authority DNS record check  | 
**type** | **String** | Domain verification type:    * &#x60;AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_ADMIN&#x60; - Domain verified using domain control verification email sent to admin@&lt;your.domain.com&gt;   * &#x60;AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_ADMINSTRATOR&#x60; - Domain verified using domain control verification email sent to administrator@&lt;your.domain.com&gt;   * &#x60;AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_HOST_MASTER&#x60; - Domain verified using domain control verification email sent to hostmaster@&lt;your.domain.com&gt;   * &#x60;AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_POST_MASTER&#x60; - Domain verified using domain control verification email sent to postmaster@&lt;your.domain.com&gt;   * &#x60;AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_WEB_MASTER&#x60; - Domain verified using domain control verification email sent to webmaster@&lt;your.domain.com&gt;   * &#x60;DOMAIN_ACCESS_EMAIL&#x60; - Domain verified using a domain access email   * &#x60;DOMAIN_ACCESS_LETTER&#x60; - Customer completed a domain access letter which was used for domain verification   * &#x60;DOMAIN_CONTROL_EMAIL&#x60; - Domain verified using HTML file or DNS zone file text value   * &#x60;DOMAIN_ZONE_CONTROL&#x60; - DNS zone file containing a pre-generated text value used for domain verification   * &#x60;MANUAL_DOMAIN_ACCESS_EMAIL&#x60; - DAE sent to an email address manually entered by a rep   * &#x60;PREVIOUS_DOMAIN_ACCESS_EMAIL&#x60; - Customers domain access email for a prior certificate request was used for domain verification   * &#x60;REGISTRATION_AUTHORITY_DOMAIN_ACCESS_LETTER&#x60; - Representative reviewed a customer provided domain access letter and verified domain   * &#x60;REGISTRATION_AUTHORITY_DOMAIN_ZONE_CONTROL&#x60; - Representative verified domain using a manual domain zone control check   * &#x60;REGISTRATION_AUTHORITY_OVERRIDE&#x60; - Representative verified domain using alternative methods   * &#x60;REGISTRATION_AUTHORITY_WEBSITE_CONTROL&#x60; - Representative verified domain using a manual website control check   * &#x60;CUSTOMER_OWNED&#x60; - Validated customer account information used for domain control verification   * &#x60;WEBSITE_CONTROL&#x60; - HTML file in root website directory containing pre-generated value used for domain control verification  | 
**usage** | **String** | Type of domain name used for domain verification | 



## Enum: StatusEnum


* `COMPLETED` (value: `"COMPLETED"`)

* `FAILED_VERIFICATION` (value: `"FAILED_VERIFICATION"`)

* `VERIFIED_POSSIBLE_FRAUD` (value: `"VERIFIED_POSSIBLE_FRAUD"`)

* `DROPPED` (value: `"DROPPED"`)

* `DROPPED_CERTIFICATE_AUTHORITY_AUTHORIZATION` (value: `"DROPPED_CERTIFICATE_AUTHORITY_AUTHORIZATION"`)

* `DROPPED_GOOGLE_SAFE_BROWSING` (value: `"DROPPED_GOOGLE_SAFE_BROWSING"`)

* `INVALID` (value: `"INVALID"`)

* `AWAITING` (value: `"AWAITING"`)

* `PENDING_POSSIBLE_FRAUD` (value: `"PENDING_POSSIBLE_FRAUD"`)

* `REVOKED_CERTIFICATE` (value: `"REVOKED_CERTIFICATE"`)





## Enum: TypeEnum


* `DOMAIN_CONTROL_EMAIL` (value: `"DOMAIN_CONTROL_EMAIL"`)

* `AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_ADMIN` (value: `"AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_ADMIN"`)

* `AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_ADMINSTRATOR` (value: `"AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_ADMINSTRATOR"`)

* `AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_HOST_MASTER` (value: `"AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_HOST_MASTER"`)

* `AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_POST_MASTER` (value: `"AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_POST_MASTER"`)

* `AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_WEB_MASTER` (value: `"AUTO_GENERATED_DOMAIN_ACCESS_EMAIL_WEB_MASTER"`)

* `DOMAIN_ACCESS_EMAIL` (value: `"DOMAIN_ACCESS_EMAIL"`)

* `DOMAIN_ACCESS_LETTER` (value: `"DOMAIN_ACCESS_LETTER"`)

* `DOMAIN_ZONE_CONTROL` (value: `"DOMAIN_ZONE_CONTROL"`)

* `MANUAL_DOMAIN_ACCESS_EMAIL` (value: `"MANUAL_DOMAIN_ACCESS_EMAIL"`)

* `PREVIOUS_DOMAIN_ACCESS_EMAIL` (value: `"PREVIOUS_DOMAIN_ACCESS_EMAIL"`)

* `REGISTRATION_AUTHORITY_DOMAIN_ACCESS_LETTER` (value: `"REGISTRATION_AUTHORITY_DOMAIN_ACCESS_LETTER"`)

* `REGISTRATION_AUTHORITY_DOMAIN_ZONE_CONTROL` (value: `"REGISTRATION_AUTHORITY_DOMAIN_ZONE_CONTROL"`)

* `REGISTRATION_AUTHORITY_OVERRIDE` (value: `"REGISTRATION_AUTHORITY_OVERRIDE"`)

* `REGISTRATION_AUTHORITY_WEBSITE_CONTROL` (value: `"REGISTRATION_AUTHORITY_WEBSITE_CONTROL"`)

* `CUSTOMER_OWNED` (value: `"CUSTOMER_OWNED"`)

* `WEBSITE_CONTROL` (value: `"WEBSITE_CONTROL"`)





## Enum: UsageEnum


* `COMMON_NAME` (value: `"COMMON_NAME"`)

* `SUBJECT_ALTERNATIVE_NAME` (value: `"SUBJECT_ALTERNATIVE_NAME"`)




