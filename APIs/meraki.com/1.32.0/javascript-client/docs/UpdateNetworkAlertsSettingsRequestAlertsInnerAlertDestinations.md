# MerakiDashboardApi.UpdateNetworkAlertsSettingsRequestAlertsInnerAlertDestinations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allAdmins** | **Boolean** | If true, then all network admins will receive emails for this alert | [optional] 
**emails** | **[String]** | A list of emails that will receive information about the alert | [optional] 
**httpServerIds** | **[String]** | A list of HTTP server IDs to send a Webhook to for this alert | [optional] 
**snmp** | **Boolean** | If true, then an SNMP trap will be sent for this alert if there is an SNMP trap server configured for this network | [optional] 


