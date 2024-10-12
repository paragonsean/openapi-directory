

# PagesHttpsCertificate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  |
|**domains** | **List&lt;Object&gt;** | Array of the domain set and its alternate name (if it is configured) |  |
|**expiresAt** | **LocalDate** |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NEW | &quot;new&quot; |
| AUTHORIZATION_CREATED | &quot;authorization_created&quot; |
| AUTHORIZATION_PENDING | &quot;authorization_pending&quot; |
| AUTHORIZED | &quot;authorized&quot; |
| AUTHORIZATION_REVOKED | &quot;authorization_revoked&quot; |
| ISSUED | &quot;issued&quot; |
| UPLOADED | &quot;uploaded&quot; |
| APPROVED | &quot;approved&quot; |
| ERRORED | &quot;errored&quot; |
| BAD_AUTHZ | &quot;bad_authz&quot; |
| DESTROY_PENDING | &quot;destroy_pending&quot; |
| DNS_CHANGED | &quot;dns_changed&quot; |



