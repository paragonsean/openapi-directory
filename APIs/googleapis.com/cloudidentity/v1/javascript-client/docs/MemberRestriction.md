# CloudIdentityApi.MemberRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation** | [**RestrictionEvaluation**](RestrictionEvaluation.md) |  | [optional] 
**query** | **String** | Member Restriction as defined by CEL expression. Supported restrictions are: &#x60;member.customer_id&#x60; and &#x60;member.type&#x60;. Valid values for &#x60;member.type&#x60; are &#x60;1&#x60;, &#x60;2&#x60; and &#x60;3&#x60;. They correspond to USER, SERVICE_ACCOUNT, and GROUP respectively. The value for &#x60;member.customer_id&#x60; only supports &#x60;groupCustomerId()&#x60; currently which means the customer id of the group will be used for restriction. Supported operators are &#x60;&amp;&amp;&#x60;, &#x60;||&#x60; and &#x60;&#x3D;&#x3D;&#x60;, corresponding to AND, OR, and EQUAL. Examples: Allow only service accounts of given customer to be members. &#x60;member.type &#x3D;&#x3D; 2 &amp;&amp; member.customer_id &#x3D;&#x3D; groupCustomerId()&#x60; Allow only users or groups to be members. &#x60;member.type &#x3D;&#x3D; 1 || member.type &#x3D;&#x3D; 3&#x60; | [optional] 


