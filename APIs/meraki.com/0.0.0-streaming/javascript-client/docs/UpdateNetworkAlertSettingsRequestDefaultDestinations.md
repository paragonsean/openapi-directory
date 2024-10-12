# MerakiDashboardApi.UpdateNetworkAlertSettingsRequestDefaultDestinations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allAdmins** | **Boolean** | If true, then all network admins will receive emails. | [optional] 
**emails** | **[String]** | A list of emails that will recieve the alert(s). | [optional] 
**httpServerIds** | **[String]** | A list of HTTP server IDs to send a Webhook to | [optional] 
**snmp** | **Boolean** | If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network. | [optional] 


