# LinodeApi.SupportTicketRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseId** | **Number** | The ID of the Managed Database this ticket is regarding, if relevant.  | [optional] 
**description** | **String** | The full details of the issue or question.  | 
**domainId** | **Number** | The ID of the Domain this ticket is regarding, if relevant.  | [optional] 
**firewallId** | **Number** | The ID of the Firewall this ticket is regarding, if relevant.  | [optional] 
**linodeId** | **Number** | The ID of the Linode this ticket is regarding, if relevant.  | [optional] 
**lkeclusterId** | **Number** | The ID of the Kubernetes cluster this ticket is regarding, if relevant.  | [optional] 
**longviewclientId** | **Number** | The ID of the Longview client this ticket is regarding, if relevant.  | [optional] 
**managedIssue** | **Boolean** | Designates if this ticket is related to a [Managed service](https://www.linode.com/products/managed/). If &#x60;true&#x60;, the following constraints will apply: * No ID attributes (i.e. &#x60;linode_id&#x60;, &#x60;domain_id&#x60;, etc.) should be provided with this request. * Your account must have a [Managed service enabled](/docs/api/managed/#managed-service-enable).  | [optional] 
**nodebalancerId** | **Number** | The ID of the NodeBalancer this ticket is regarding, if relevant.  | [optional] 
**region** | **String** | The [Region](/docs/api/regions/) ID for the associated VLAN this ticket is regarding.  Only allowed when submitting a VLAN ticket.  | [optional] 
**summary** | **String** | The summary or title for this SupportTicket.  | 
**vlan** | **String** | The label of the VLAN this ticket is regarding, if relevant. To view your VLANs, use the VLANs List ([GET /networking/vlans](/docs/api/networking/#vlans-list)) endpoint.  Requires a specified &#x60;region&#x60; to identify the VLAN.  | [optional] 
**volumeId** | **Number** | The ID of the Volume this ticket is regarding, if relevant.  | [optional] 


