

# DomainPurchaseConsent

Domain purchase consent object, representing acceptance of applicable legal agreements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agreedAt** | **OffsetDateTime** | Timestamp when the agreements were accepted. |  [optional] |
|**agreedBy** | **String** | Client IP address. |  [optional] |
|**agreementKeys** | **List&lt;String&gt;** | List of applicable legal agreement keys. This list can be retrieved using ListLegalAgreements API under &lt;code&gt;TopLevelDomain&lt;/code&gt; resource. |  [optional] |



