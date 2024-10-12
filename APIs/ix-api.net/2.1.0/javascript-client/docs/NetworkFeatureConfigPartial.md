# IxApi.NetworkFeatureConfigPartial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asSetV4** | **String** | AS-SET of the customer for IPv4 prefix filtering. This is used to generate filters on the router servers.  Only valid referenced prefixes within the AS-SET are allowed inbound to the route server. All other routes are filtered.  This field is *required* if the route server network feature only supports the &#x60;af_inet&#x60; address family. If multiple address families are supported, it is optional if the &#x60;as_set_v6&#x60; is provided.  Important: The format has to be: \&quot;AS-SET@IRR\&quot;. IRR is the database where the AS-SET is registred. Typically used IRR&#39;s are RADB, RIPE, NTTCOM, APNIC, ALTDB, LEVEL3, ARIN, AFRINIC, LACNIC  | [optional] 
**asSetV6** | **String** | AS-SET of the customer for IPv6. This is used to generate filters on the router servers. Only valid referenced prefixes within the AS-SET are allowed inbound to the route server. All other routes are filtered.  This field is *required* if the route server network feature only supports the &#x60;af_inet6&#x60; address family. If multiple address families are supported, it is optional if the &#x60;as_set_v4&#x60; is provided.  Important: The format has to be: \&quot;AS-SET@IRR\&quot;. IRR is the database where the AS-SET is registred. Typically used IRR&#39;s are RADB, RIPE, NTTCOM, APNIC, ALTDB, LEVEL3, ARIN, AFRINIC, LACNIC  | [optional] 
**asn** | **Number** | The ASN of the peer.  | [optional] 
**bgpSessionType** | **String** | The session type describes which of the both parties will open the connection. If set to passive, the customer router needs to open the connection. If its set to active, the route server will open the connection. The standard behavior on most exchanges is passive.  | [optional] 
**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. | [optional] 
**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  | [optional] 
**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  | [optional] 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**id** | **String** |  | [optional] 
**insertIxpAsn** | **Boolean** | Insert the ASN of the exchange into the AS path. This function is only used in special cases. In 99% of all cases, it should be false.  | [optional] [default to true]
**ip** | **String** | The BGP session will be established from this IP address. Only IPs assigned to the corresponding network service config can be used. | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | [optional] 
**maxPrefixV4** | **Number** | Announcing more than &#x60;max_prefix&#x60; IPv4 prefixes the bgp session will be droped.  | [optional] 
**maxPrefixV6** | **Number** | Announcing more than &#x60;max_prefix&#x60; IPv6 prefixes the bgp session will be droped.  | [optional] 
**networkFeature** | **String** |  | [optional] 
**networkServiceConfig** | **String** |  | [optional] 
**password** | **String** | The cleartext BGP session password | [optional] [default to &#39;&#39;]
**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  | [optional] [default to &#39;&#39;]
**roleAssignments** | **[String]** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  | [optional] 
**sessionMode** | **String** | Set the session mode with the routeserver.  | [optional] 
**state** | **String** |  | [optional] 
**status** | [**[Status]**](Status.md) |  | [optional] 
**type** | **String** |  | 



## Enum: BgpSessionTypeEnum


* `active` (value: `"active"`)

* `passive` (value: `"passive"`)





## Enum: SessionModeEnum


* `public` (value: `"public"`)

* `collector` (value: `"collector"`)





## Enum: StateEnum


* `requested` (value: `"requested"`)

* `allocated` (value: `"allocated"`)

* `testing` (value: `"testing"`)

* `production` (value: `"production"`)

* `production_change_pending` (value: `"production_change_pending"`)

* `decommission_requested` (value: `"decommission_requested"`)

* `decommissioned` (value: `"decommissioned"`)

* `archived` (value: `"archived"`)

* `error` (value: `"error"`)

* `operator` (value: `"operator"`)

* `scheduled` (value: `"scheduled"`)




