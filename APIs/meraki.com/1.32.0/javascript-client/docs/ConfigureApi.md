# MerakiDashboardApi.ConfigureApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addNetworkSwitchStack_0**](ConfigureApi.md#addNetworkSwitchStack_0) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/add | Add a switch to a stack
[**assignOrganizationLicensesSeats_0**](ConfigureApi.md#assignOrganizationLicensesSeats_0) | **POST** /organizations/{organizationId}/licenses/assignSeats | Assign SM seats to a network
[**bindNetwork_0**](ConfigureApi.md#bindNetwork_0) | **POST** /networks/{networkId}/bind | Bind a network to a template.
[**checkinNetworkSmDevices_0**](ConfigureApi.md#checkinNetworkSmDevices_0) | **POST** /networks/{networkId}/sm/devices/checkin | Force check-in a set of devices
[**claimIntoOrganizationInventory_0**](ConfigureApi.md#claimIntoOrganizationInventory_0) | **POST** /organizations/{organizationId}/inventory/claim | Claim a list of devices, licenses, and/or orders into an organization inventory
[**claimIntoOrganization_0**](ConfigureApi.md#claimIntoOrganization_0) | **POST** /organizations/{organizationId}/claim | Claim a list of devices, licenses, and/or orders into an organization
[**claimNetworkDevices_0**](ConfigureApi.md#claimNetworkDevices_0) | **POST** /networks/{networkId}/devices/claim | Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)
[**cloneOrganizationSwitchDevices_0**](ConfigureApi.md#cloneOrganizationSwitchDevices_0) | **POST** /organizations/{organizationId}/switch/devices/clone | Clone port-level and some switch-level configuration settings from a source switch to one or more target switches
[**cloneOrganization_0**](ConfigureApi.md#cloneOrganization_0) | **POST** /organizations/{organizationId}/clone | Create a new organization by cloning the addressed organization
[**combineOrganizationNetworks_0**](ConfigureApi.md#combineOrganizationNetworks_0) | **POST** /organizations/{organizationId}/networks/combine | Combine multiple networks into a single network
[**createDeviceApplianceVmxAuthenticationToken_0**](ConfigureApi.md#createDeviceApplianceVmxAuthenticationToken_0) | **POST** /devices/{serial}/appliance/vmx/authenticationToken | Generate a new vMX authentication token
[**createDeviceSwitchRoutingInterface_0**](ConfigureApi.md#createDeviceSwitchRoutingInterface_0) | **POST** /devices/{serial}/switch/routing/interfaces | Create a layer 3 interface for a switch
[**createDeviceSwitchRoutingStaticRoute_0**](ConfigureApi.md#createDeviceSwitchRoutingStaticRoute_0) | **POST** /devices/{serial}/switch/routing/staticRoutes | Create a layer 3 static route for a switch
[**createNetworkAppliancePrefixesDelegatedStatic_0**](ConfigureApi.md#createNetworkAppliancePrefixesDelegatedStatic_0) | **POST** /networks/{networkId}/appliance/prefixes/delegated/statics | Add a static delegated prefix from a network
[**createNetworkApplianceStaticRoute_0**](ConfigureApi.md#createNetworkApplianceStaticRoute_0) | **POST** /networks/{networkId}/appliance/staticRoutes | Add a static route for an MX or teleworker network
[**createNetworkApplianceTrafficShapingCustomPerformanceClass_0**](ConfigureApi.md#createNetworkApplianceTrafficShapingCustomPerformanceClass_0) | **POST** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | Add a custom performance class for an MX network
[**createNetworkApplianceVlan_0**](ConfigureApi.md#createNetworkApplianceVlan_0) | **POST** /networks/{networkId}/appliance/vlans | Add a VLAN
[**createNetworkCameraQualityRetentionProfile_0**](ConfigureApi.md#createNetworkCameraQualityRetentionProfile_0) | **POST** /networks/{networkId}/camera/qualityRetentionProfiles | Creates new quality retention profile for this network.
[**createNetworkCameraWirelessProfile_0**](ConfigureApi.md#createNetworkCameraWirelessProfile_0) | **POST** /networks/{networkId}/camera/wirelessProfiles | Creates a new camera wireless profile for this network.
[**createNetworkFirmwareUpgradesRollback_0**](ConfigureApi.md#createNetworkFirmwareUpgradesRollback_0) | **POST** /networks/{networkId}/firmwareUpgrades/rollbacks | Rollback a Firmware Upgrade For A Network
[**createNetworkFirmwareUpgradesStagedEvent_0**](ConfigureApi.md#createNetworkFirmwareUpgradesStagedEvent_0) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events | Create a Staged Upgrade Event for a network
[**createNetworkFirmwareUpgradesStagedGroup_0**](ConfigureApi.md#createNetworkFirmwareUpgradesStagedGroup_0) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network
[**createNetworkFloorPlan_0**](ConfigureApi.md#createNetworkFloorPlan_0) | **POST** /networks/{networkId}/floorPlans | Upload a floor plan
[**createNetworkGroupPolicy_0**](ConfigureApi.md#createNetworkGroupPolicy_0) | **POST** /networks/{networkId}/groupPolicies | Create a group policy
[**createNetworkMerakiAuthUser_0**](ConfigureApi.md#createNetworkMerakiAuthUser_0) | **POST** /networks/{networkId}/merakiAuthUsers | Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)
[**createNetworkMqttBroker_0**](ConfigureApi.md#createNetworkMqttBroker_0) | **POST** /networks/{networkId}/mqttBrokers | Add an MQTT broker
[**createNetworkPiiRequest_0**](ConfigureApi.md#createNetworkPiiRequest_0) | **POST** /networks/{networkId}/pii/requests | Submit a new delete or restrict processing PII request
[**createNetworkSensorAlertsProfile_0**](ConfigureApi.md#createNetworkSensorAlertsProfile_0) | **POST** /networks/{networkId}/sensor/alerts/profiles | Creates a sensor alert profile for a network.
[**createNetworkSmBypassActivationLockAttempt_0**](ConfigureApi.md#createNetworkSmBypassActivationLockAttempt_0) | **POST** /networks/{networkId}/sm/bypassActivationLockAttempts | Bypass activation lock attempt
[**createNetworkSmTargetGroup_0**](ConfigureApi.md#createNetworkSmTargetGroup_0) | **POST** /networks/{networkId}/sm/targetGroups | Add a target group
[**createNetworkSwitchAccessPolicy_0**](ConfigureApi.md#createNetworkSwitchAccessPolicy_0) | **POST** /networks/{networkId}/switch/accessPolicies | Create an access policy for a switch network
[**createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0**](ConfigureApi.md#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0) | **POST** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Add a server to be trusted by Dynamic ARP Inspection on this network
[**createNetworkSwitchLinkAggregation_0**](ConfigureApi.md#createNetworkSwitchLinkAggregation_0) | **POST** /networks/{networkId}/switch/linkAggregations | Create a link aggregation group
[**createNetworkSwitchPortSchedule_0**](ConfigureApi.md#createNetworkSwitchPortSchedule_0) | **POST** /networks/{networkId}/switch/portSchedules | Add a switch port schedule
[**createNetworkSwitchQosRule_0**](ConfigureApi.md#createNetworkSwitchQosRule_0) | **POST** /networks/{networkId}/switch/qosRules | Add a quality of service rule
[**createNetworkSwitchRoutingMulticastRendezvousPoint_0**](ConfigureApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint_0) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point
[**createNetworkSwitchStackRoutingInterface_0**](ConfigureApi.md#createNetworkSwitchStackRoutingInterface_0) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | Create a layer 3 interface for a switch stack
[**createNetworkSwitchStackRoutingStaticRoute_0**](ConfigureApi.md#createNetworkSwitchStackRoutingStaticRoute_0) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | Create a layer 3 static route for a switch stack
[**createNetworkSwitchStack_0**](ConfigureApi.md#createNetworkSwitchStack_0) | **POST** /networks/{networkId}/switch/stacks | Create a stack
[**createNetworkWebhooksHttpServer_0**](ConfigureApi.md#createNetworkWebhooksHttpServer_0) | **POST** /networks/{networkId}/webhooks/httpServers | Add an HTTP server to a network
[**createNetworkWebhooksPayloadTemplate_0**](ConfigureApi.md#createNetworkWebhooksPayloadTemplate_0) | **POST** /networks/{networkId}/webhooks/payloadTemplates | Create a webhook payload template for a network
[**createNetworkWebhooksWebhookTest_0**](ConfigureApi.md#createNetworkWebhooksWebhookTest_0) | **POST** /networks/{networkId}/webhooks/webhookTests | Send a test webhook for a network
[**createNetworkWirelessRfProfile_0**](ConfigureApi.md#createNetworkWirelessRfProfile_0) | **POST** /networks/{networkId}/wireless/rfProfiles | Creates new RF profile for this network
[**createNetworkWirelessSsidIdentityPsk_0**](ConfigureApi.md#createNetworkWirelessSsidIdentityPsk_0) | **POST** /networks/{networkId}/wireless/ssids/{number}/identityPsks | Create an Identity PSK
[**createOrganizationActionBatch_0**](ConfigureApi.md#createOrganizationActionBatch_0) | **POST** /organizations/{organizationId}/actionBatches | Create an action batch
[**createOrganizationAdaptivePolicyAcl_0**](ConfigureApi.md#createOrganizationAdaptivePolicyAcl_0) | **POST** /organizations/{organizationId}/adaptivePolicy/acls | Creates new adaptive policy ACL
[**createOrganizationAdaptivePolicyGroup_0**](ConfigureApi.md#createOrganizationAdaptivePolicyGroup_0) | **POST** /organizations/{organizationId}/adaptivePolicy/groups | Creates a new adaptive policy group
[**createOrganizationAdaptivePolicyPolicy_0**](ConfigureApi.md#createOrganizationAdaptivePolicyPolicy_0) | **POST** /organizations/{organizationId}/adaptivePolicy/policies | Add an Adaptive Policy
[**createOrganizationAdmin_0**](ConfigureApi.md#createOrganizationAdmin_0) | **POST** /organizations/{organizationId}/admins | Create a new dashboard administrator
[**createOrganizationAlertsProfile_0**](ConfigureApi.md#createOrganizationAlertsProfile_0) | **POST** /organizations/{organizationId}/alerts/profiles | Create an organization-wide alert configuration
[**createOrganizationBrandingPolicy_0**](ConfigureApi.md#createOrganizationBrandingPolicy_0) | **POST** /organizations/{organizationId}/brandingPolicies | Add a new branding policy to an organization
[**createOrganizationCameraCustomAnalyticsArtifact_0**](ConfigureApi.md#createOrganizationCameraCustomAnalyticsArtifact_0) | **POST** /organizations/{organizationId}/camera/customAnalytics/artifacts | Create custom analytics artifact
[**createOrganizationConfigTemplate_0**](ConfigureApi.md#createOrganizationConfigTemplate_0) | **POST** /organizations/{organizationId}/configTemplates | Create a new configuration template
[**createOrganizationEarlyAccessFeaturesOptIn_0**](ConfigureApi.md#createOrganizationEarlyAccessFeaturesOptIn_0) | **POST** /organizations/{organizationId}/earlyAccess/features/optIns | Create a new early access feature opt-in for an organization
[**createOrganizationInsightMonitoredMediaServer_0**](ConfigureApi.md#createOrganizationInsightMonitoredMediaServer_0) | **POST** /organizations/{organizationId}/insight/monitoredMediaServers | Add a media server to be monitored for this organization
[**createOrganizationInventoryOnboardingCloudMonitoringExportEvent_0**](ConfigureApi.md#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_0) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents | Imports event logs related to the onboarding app into elastisearch
[**createOrganizationInventoryOnboardingCloudMonitoringImport_0**](ConfigureApi.md#createOrganizationInventoryOnboardingCloudMonitoringImport_0) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.
[**createOrganizationInventoryOnboardingCloudMonitoringPrepare_0**](ConfigureApi.md#createOrganizationInventoryOnboardingCloudMonitoringPrepare_0) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare | Initiates or updates an import session
[**createOrganizationNetwork_0**](ConfigureApi.md#createOrganizationNetwork_0) | **POST** /organizations/{organizationId}/networks | Create a network
[**createOrganizationPolicyObject_0**](ConfigureApi.md#createOrganizationPolicyObject_0) | **POST** /organizations/{organizationId}/policyObjects | Creates a new Policy Object.
[**createOrganizationPolicyObjectsGroup_0**](ConfigureApi.md#createOrganizationPolicyObjectsGroup_0) | **POST** /organizations/{organizationId}/policyObjects/groups | Creates a new Policy Object Group.
[**createOrganizationSamlIdp_0**](ConfigureApi.md#createOrganizationSamlIdp_0) | **POST** /organizations/{organizationId}/saml/idps | Create a SAML IdP for your organization.
[**createOrganizationSamlRole_0**](ConfigureApi.md#createOrganizationSamlRole_0) | **POST** /organizations/{organizationId}/samlRoles | Create a SAML role
[**createOrganization_0**](ConfigureApi.md#createOrganization_0) | **POST** /organizations | Create a new organization
[**deferNetworkFirmwareUpgradesStagedEvents_0**](ConfigureApi.md#deferNetworkFirmwareUpgradesStagedEvents_0) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/defer | Postpone by 1 week all pending staged upgrade stages for a network
[**deleteDeviceSwitchRoutingInterface_0**](ConfigureApi.md#deleteDeviceSwitchRoutingInterface_0) | **DELETE** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Delete a layer 3 interface from the switch
[**deleteDeviceSwitchRoutingStaticRoute_0**](ConfigureApi.md#deleteDeviceSwitchRoutingStaticRoute_0) | **DELETE** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch
[**deleteNetworkAppliancePrefixesDelegatedStatic_0**](ConfigureApi.md#deleteNetworkAppliancePrefixesDelegatedStatic_0) | **DELETE** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Delete a static delegated prefix from a network
[**deleteNetworkApplianceStaticRoute_0**](ConfigureApi.md#deleteNetworkApplianceStaticRoute_0) | **DELETE** /networks/{networkId}/appliance/staticRoutes/{staticRouteId} | Delete a static route from an MX or teleworker network
[**deleteNetworkApplianceTrafficShapingCustomPerformanceClass_0**](ConfigureApi.md#deleteNetworkApplianceTrafficShapingCustomPerformanceClass_0) | **DELETE** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Delete a custom performance class from an MX network
[**deleteNetworkApplianceVlan_0**](ConfigureApi.md#deleteNetworkApplianceVlan_0) | **DELETE** /networks/{networkId}/appliance/vlans/{vlanId} | Delete a VLAN from a network
[**deleteNetworkCameraQualityRetentionProfile_0**](ConfigureApi.md#deleteNetworkCameraQualityRetentionProfile_0) | **DELETE** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Delete an existing quality retention profile for this network.
[**deleteNetworkCameraWirelessProfile_0**](ConfigureApi.md#deleteNetworkCameraWirelessProfile_0) | **DELETE** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Delete an existing camera wireless profile for this network.
[**deleteNetworkFirmwareUpgradesStagedGroup_0**](ConfigureApi.md#deleteNetworkFirmwareUpgradesStagedGroup_0) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group
[**deleteNetworkFloorPlan_0**](ConfigureApi.md#deleteNetworkFloorPlan_0) | **DELETE** /networks/{networkId}/floorPlans/{floorPlanId} | Destroy a floor plan
[**deleteNetworkGroupPolicy_0**](ConfigureApi.md#deleteNetworkGroupPolicy_0) | **DELETE** /networks/{networkId}/groupPolicies/{groupPolicyId} | Delete a group policy
[**deleteNetworkMerakiAuthUser_0**](ConfigureApi.md#deleteNetworkMerakiAuthUser_0) | **DELETE** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Deauthorize a user
[**deleteNetworkMqttBroker_0**](ConfigureApi.md#deleteNetworkMqttBroker_0) | **DELETE** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Delete an MQTT broker
[**deleteNetworkPiiRequest_0**](ConfigureApi.md#deleteNetworkPiiRequest_0) | **DELETE** /networks/{networkId}/pii/requests/{requestId} | Delete a restrict processing PII request
[**deleteNetworkSensorAlertsProfile_0**](ConfigureApi.md#deleteNetworkSensorAlertsProfile_0) | **DELETE** /networks/{networkId}/sensor/alerts/profiles/{id} | Deletes a sensor alert profile from a network.
[**deleteNetworkSmTargetGroup_0**](ConfigureApi.md#deleteNetworkSmTargetGroup_0) | **DELETE** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Delete a target group from a network
[**deleteNetworkSmUserAccessDevice_0**](ConfigureApi.md#deleteNetworkSmUserAccessDevice_0) | **DELETE** /networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId} | Delete a User Access Device
[**deleteNetworkSwitchAccessPolicy_0**](ConfigureApi.md#deleteNetworkSwitchAccessPolicy_0) | **DELETE** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Delete an access policy for a switch network
[**deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0**](ConfigureApi.md#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0) | **DELETE** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Remove a server from being trusted by Dynamic ARP Inspection on this network
[**deleteNetworkSwitchLinkAggregation_0**](ConfigureApi.md#deleteNetworkSwitchLinkAggregation_0) | **DELETE** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Split a link aggregation group into separate ports
[**deleteNetworkSwitchPortSchedule_0**](ConfigureApi.md#deleteNetworkSwitchPortSchedule_0) | **DELETE** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Delete a switch port schedule
[**deleteNetworkSwitchQosRule_0**](ConfigureApi.md#deleteNetworkSwitchQosRule_0) | **DELETE** /networks/{networkId}/switch/qosRules/{qosRuleId} | Delete a quality of service rule
[**deleteNetworkSwitchRoutingMulticastRendezvousPoint_0**](ConfigureApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint_0) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point
[**deleteNetworkSwitchStackRoutingInterface_0**](ConfigureApi.md#deleteNetworkSwitchStackRoutingInterface_0) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Delete a layer 3 interface from a switch stack
[**deleteNetworkSwitchStackRoutingStaticRoute_0**](ConfigureApi.md#deleteNetworkSwitchStackRoutingStaticRoute_0) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch stack
[**deleteNetworkSwitchStack_0**](ConfigureApi.md#deleteNetworkSwitchStack_0) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId} | Delete a stack
[**deleteNetworkWebhooksHttpServer_0**](ConfigureApi.md#deleteNetworkWebhooksHttpServer_0) | **DELETE** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Delete an HTTP server from a network
[**deleteNetworkWebhooksPayloadTemplate_0**](ConfigureApi.md#deleteNetworkWebhooksPayloadTemplate_0) | **DELETE** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Destroy a webhook payload template for a network
[**deleteNetworkWirelessRfProfile_0**](ConfigureApi.md#deleteNetworkWirelessRfProfile_0) | **DELETE** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Delete a RF Profile
[**deleteNetworkWirelessSsidIdentityPsk_0**](ConfigureApi.md#deleteNetworkWirelessSsidIdentityPsk_0) | **DELETE** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Delete an Identity PSK
[**deleteNetwork_0**](ConfigureApi.md#deleteNetwork_0) | **DELETE** /networks/{networkId} | Delete a network
[**deleteOrganizationActionBatch_0**](ConfigureApi.md#deleteOrganizationActionBatch_0) | **DELETE** /organizations/{organizationId}/actionBatches/{actionBatchId} | Delete an action batch
[**deleteOrganizationAdaptivePolicyAcl_0**](ConfigureApi.md#deleteOrganizationAdaptivePolicyAcl_0) | **DELETE** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Deletes the specified adaptive policy ACL
[**deleteOrganizationAdaptivePolicyGroup_0**](ConfigureApi.md#deleteOrganizationAdaptivePolicyGroup_0) | **DELETE** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Deletes the specified adaptive policy group and any associated policies and references
[**deleteOrganizationAdaptivePolicyPolicy_0**](ConfigureApi.md#deleteOrganizationAdaptivePolicyPolicy_0) | **DELETE** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Delete an Adaptive Policy
[**deleteOrganizationAdmin_0**](ConfigureApi.md#deleteOrganizationAdmin_0) | **DELETE** /organizations/{organizationId}/admins/{adminId} | Revoke all access for a dashboard administrator within this organization
[**deleteOrganizationAlertsProfile_0**](ConfigureApi.md#deleteOrganizationAlertsProfile_0) | **DELETE** /organizations/{organizationId}/alerts/profiles/{alertConfigId} | Removes an organization-wide alert config
[**deleteOrganizationBrandingPolicy_0**](ConfigureApi.md#deleteOrganizationBrandingPolicy_0) | **DELETE** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Delete a branding policy
[**deleteOrganizationCameraCustomAnalyticsArtifact_0**](ConfigureApi.md#deleteOrganizationCameraCustomAnalyticsArtifact_0) | **DELETE** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Delete Custom Analytics Artifact
[**deleteOrganizationConfigTemplate_0**](ConfigureApi.md#deleteOrganizationConfigTemplate_0) | **DELETE** /organizations/{organizationId}/configTemplates/{configTemplateId} | Remove a configuration template
[**deleteOrganizationEarlyAccessFeaturesOptIn_0**](ConfigureApi.md#deleteOrganizationEarlyAccessFeaturesOptIn_0) | **DELETE** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Delete an early access feature opt-in
[**deleteOrganizationInsightMonitoredMediaServer_0**](ConfigureApi.md#deleteOrganizationInsightMonitoredMediaServer_0) | **DELETE** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Delete a monitored media server from this organization
[**deleteOrganizationPolicyObject_0**](ConfigureApi.md#deleteOrganizationPolicyObject_0) | **DELETE** /organizations/{organizationId}/policyObjects/{policyObjectId} | Deletes a Policy Object.
[**deleteOrganizationPolicyObjectsGroup_0**](ConfigureApi.md#deleteOrganizationPolicyObjectsGroup_0) | **DELETE** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Deletes a Policy Object Group.
[**deleteOrganizationSamlIdp_0**](ConfigureApi.md#deleteOrganizationSamlIdp_0) | **DELETE** /organizations/{organizationId}/saml/idps/{idpId} | Remove a SAML IdP in your organization.
[**deleteOrganizationSamlRole_0**](ConfigureApi.md#deleteOrganizationSamlRole_0) | **DELETE** /organizations/{organizationId}/samlRoles/{samlRoleId} | Remove a SAML role
[**deleteOrganizationUser_0**](ConfigureApi.md#deleteOrganizationUser_0) | **DELETE** /organizations/{organizationId}/users/{userId} | Delete a user and all of its authentication methods.
[**deleteOrganization_0**](ConfigureApi.md#deleteOrganization_0) | **DELETE** /organizations/{organizationId} | Delete an organization
[**getDeviceApplianceUplinksSettings_0**](ConfigureApi.md#getDeviceApplianceUplinksSettings_0) | **GET** /devices/{serial}/appliance/uplinks/settings | Return the uplink settings for an MX appliance
[**getDeviceCameraCustomAnalytics_0**](ConfigureApi.md#getDeviceCameraCustomAnalytics_0) | **GET** /devices/{serial}/camera/customAnalytics | Return custom analytics settings for a camera
[**getDeviceCameraQualityAndRetention_0**](ConfigureApi.md#getDeviceCameraQualityAndRetention_0) | **GET** /devices/{serial}/camera/qualityAndRetention | Returns quality and retention settings for the given camera
[**getDeviceCameraSenseObjectDetectionModels_0**](ConfigureApi.md#getDeviceCameraSenseObjectDetectionModels_0) | **GET** /devices/{serial}/camera/sense/objectDetectionModels | Returns the MV Sense object detection model list for the given camera
[**getDeviceCameraSense_0**](ConfigureApi.md#getDeviceCameraSense_0) | **GET** /devices/{serial}/camera/sense | Returns sense settings for a given camera
[**getDeviceCameraVideoLink_0**](ConfigureApi.md#getDeviceCameraVideoLink_0) | **GET** /devices/{serial}/camera/videoLink | Returns video link to the specified camera
[**getDeviceCameraVideoSettings_0**](ConfigureApi.md#getDeviceCameraVideoSettings_0) | **GET** /devices/{serial}/camera/video/settings | Returns video settings for the given camera
[**getDeviceCameraWirelessProfiles_0**](ConfigureApi.md#getDeviceCameraWirelessProfiles_0) | **GET** /devices/{serial}/camera/wirelessProfiles | Returns wireless profile assigned to the given camera
[**getDeviceCellularGatewayLan_0**](ConfigureApi.md#getDeviceCellularGatewayLan_0) | **GET** /devices/{serial}/cellularGateway/lan | Show the LAN Settings of a MG
[**getDeviceCellularGatewayPortForwardingRules_0**](ConfigureApi.md#getDeviceCellularGatewayPortForwardingRules_0) | **GET** /devices/{serial}/cellularGateway/portForwardingRules | Returns the port forwarding rules for a single MG.
[**getDeviceCellularSims_0**](ConfigureApi.md#getDeviceCellularSims_0) | **GET** /devices/{serial}/cellular/sims | Return the SIM and APN configurations for a cellular device.
[**getDeviceManagementInterface_0**](ConfigureApi.md#getDeviceManagementInterface_0) | **GET** /devices/{serial}/managementInterface | Return the management interface settings for a device
[**getDeviceSensorRelationships_0**](ConfigureApi.md#getDeviceSensorRelationships_0) | **GET** /devices/{serial}/sensor/relationships | List the sensor roles for a given sensor or camera device.
[**getDeviceSwitchPort_0**](ConfigureApi.md#getDeviceSwitchPort_0) | **GET** /devices/{serial}/switch/ports/{portId} | Return a switch port
[**getDeviceSwitchPorts_0**](ConfigureApi.md#getDeviceSwitchPorts_0) | **GET** /devices/{serial}/switch/ports | List the switch ports for a switch
[**getDeviceSwitchRoutingInterfaceDhcp_0**](ConfigureApi.md#getDeviceSwitchRoutingInterfaceDhcp_0) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch
[**getDeviceSwitchRoutingInterface_0**](ConfigureApi.md#getDeviceSwitchRoutingInterface_0) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Return a layer 3 interface for a switch
[**getDeviceSwitchRoutingInterfaces_0**](ConfigureApi.md#getDeviceSwitchRoutingInterfaces_0) | **GET** /devices/{serial}/switch/routing/interfaces | List layer 3 interfaces for a switch
[**getDeviceSwitchRoutingStaticRoute_0**](ConfigureApi.md#getDeviceSwitchRoutingStaticRoute_0) | **GET** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch
[**getDeviceSwitchRoutingStaticRoutes_0**](ConfigureApi.md#getDeviceSwitchRoutingStaticRoutes_0) | **GET** /devices/{serial}/switch/routing/staticRoutes | List layer 3 static routes for a switch
[**getDeviceSwitchWarmSpare_0**](ConfigureApi.md#getDeviceSwitchWarmSpare_0) | **GET** /devices/{serial}/switch/warmSpare | Return warm spare configuration for a switch
[**getDeviceWirelessBluetoothSettings_0**](ConfigureApi.md#getDeviceWirelessBluetoothSettings_0) | **GET** /devices/{serial}/wireless/bluetooth/settings | Return the bluetooth settings for a wireless device
[**getDeviceWirelessRadioSettings_0**](ConfigureApi.md#getDeviceWirelessRadioSettings_0) | **GET** /devices/{serial}/wireless/radio/settings | Return the radio settings of a device
[**getDevice_0**](ConfigureApi.md#getDevice_0) | **GET** /devices/{serial} | Return a single device
[**getNetworkAlertsSettings_0**](ConfigureApi.md#getNetworkAlertsSettings_0) | **GET** /networks/{networkId}/alerts/settings | Return the alert configuration for this network
[**getNetworkApplianceConnectivityMonitoringDestinations_0**](ConfigureApi.md#getNetworkApplianceConnectivityMonitoringDestinations_0) | **GET** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MX network
[**getNetworkApplianceContentFilteringCategories_0**](ConfigureApi.md#getNetworkApplianceContentFilteringCategories_0) | **GET** /networks/{networkId}/appliance/contentFiltering/categories | List all available content filtering categories for an MX network
[**getNetworkApplianceContentFiltering_0**](ConfigureApi.md#getNetworkApplianceContentFiltering_0) | **GET** /networks/{networkId}/appliance/contentFiltering | Return the content filtering settings for an MX network
[**getNetworkApplianceFirewallCellularFirewallRules_0**](ConfigureApi.md#getNetworkApplianceFirewallCellularFirewallRules_0) | **GET** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Return the cellular firewall rules for an MX network
[**getNetworkApplianceFirewallFirewalledService_0**](ConfigureApi.md#getNetworkApplianceFirewallFirewalledService_0) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)
[**getNetworkApplianceFirewallFirewalledServices_0**](ConfigureApi.md#getNetworkApplianceFirewallFirewalledServices_0) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices | List the appliance services and their accessibility rules
[**getNetworkApplianceFirewallInboundCellularFirewallRules_0**](ConfigureApi.md#getNetworkApplianceFirewallInboundCellularFirewallRules_0) | **GET** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Return the inbound cellular firewall rules for an MX network
[**getNetworkApplianceFirewallInboundFirewallRules_0**](ConfigureApi.md#getNetworkApplianceFirewallInboundFirewallRules_0) | **GET** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Return the inbound firewall rules for an MX network
[**getNetworkApplianceFirewallL3FirewallRules_0**](ConfigureApi.md#getNetworkApplianceFirewallL3FirewallRules_0) | **GET** /networks/{networkId}/appliance/firewall/l3FirewallRules | Return the L3 firewall rules for an MX network
[**getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_0**](ConfigureApi.md#getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_0) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories | Return the L7 firewall application categories and their associated applications for an MX network
[**getNetworkApplianceFirewallL7FirewallRules_0**](ConfigureApi.md#getNetworkApplianceFirewallL7FirewallRules_0) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules | List the MX L7 firewall rules for an MX network
[**getNetworkApplianceFirewallOneToManyNatRules_0**](ConfigureApi.md#getNetworkApplianceFirewallOneToManyNatRules_0) | **GET** /networks/{networkId}/appliance/firewall/oneToManyNatRules | Return the 1:Many NAT mapping rules for an MX network
[**getNetworkApplianceFirewallOneToOneNatRules_0**](ConfigureApi.md#getNetworkApplianceFirewallOneToOneNatRules_0) | **GET** /networks/{networkId}/appliance/firewall/oneToOneNatRules | Return the 1:1 NAT mapping rules for an MX network
[**getNetworkApplianceFirewallPortForwardingRules_0**](ConfigureApi.md#getNetworkApplianceFirewallPortForwardingRules_0) | **GET** /networks/{networkId}/appliance/firewall/portForwardingRules | Return the port forwarding rules for an MX network
[**getNetworkApplianceFirewallSettings_0**](ConfigureApi.md#getNetworkApplianceFirewallSettings_0) | **GET** /networks/{networkId}/appliance/firewall/settings | Return the firewall settings for this network
[**getNetworkAppliancePort_0**](ConfigureApi.md#getNetworkAppliancePort_0) | **GET** /networks/{networkId}/appliance/ports/{portId} | Return per-port VLAN settings for a single MX port.
[**getNetworkAppliancePorts_0**](ConfigureApi.md#getNetworkAppliancePorts_0) | **GET** /networks/{networkId}/appliance/ports | List per-port VLAN settings for all ports of a MX.
[**getNetworkAppliancePrefixesDelegatedStatic_0**](ConfigureApi.md#getNetworkAppliancePrefixesDelegatedStatic_0) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Return a static delegated prefix from a network
[**getNetworkAppliancePrefixesDelegatedStatics_0**](ConfigureApi.md#getNetworkAppliancePrefixesDelegatedStatics_0) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics | List static delegated prefixes for a network
[**getNetworkApplianceSecurityIntrusion_0**](ConfigureApi.md#getNetworkApplianceSecurityIntrusion_0) | **GET** /networks/{networkId}/appliance/security/intrusion | Returns all supported intrusion settings for an MX network
[**getNetworkApplianceSecurityMalware_0**](ConfigureApi.md#getNetworkApplianceSecurityMalware_0) | **GET** /networks/{networkId}/appliance/security/malware | Returns all supported malware settings for an MX network
[**getNetworkApplianceSettings_0**](ConfigureApi.md#getNetworkApplianceSettings_0) | **GET** /networks/{networkId}/appliance/settings | Return the appliance settings for a network
[**getNetworkApplianceSingleLan_0**](ConfigureApi.md#getNetworkApplianceSingleLan_0) | **GET** /networks/{networkId}/appliance/singleLan | Return single LAN configuration
[**getNetworkApplianceSsid_0**](ConfigureApi.md#getNetworkApplianceSsid_0) | **GET** /networks/{networkId}/appliance/ssids/{number} | Return a single MX SSID
[**getNetworkApplianceSsids_0**](ConfigureApi.md#getNetworkApplianceSsids_0) | **GET** /networks/{networkId}/appliance/ssids | List the MX SSIDs in a network
[**getNetworkApplianceStaticRoute_0**](ConfigureApi.md#getNetworkApplianceStaticRoute_0) | **GET** /networks/{networkId}/appliance/staticRoutes/{staticRouteId} | Return a static route for an MX or teleworker network
[**getNetworkApplianceStaticRoutes_0**](ConfigureApi.md#getNetworkApplianceStaticRoutes_0) | **GET** /networks/{networkId}/appliance/staticRoutes | List the static routes for an MX or teleworker network
[**getNetworkApplianceTrafficShapingCustomPerformanceClass_0**](ConfigureApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClass_0) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Return a custom performance class for an MX network
[**getNetworkApplianceTrafficShapingCustomPerformanceClasses_0**](ConfigureApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClasses_0) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | List all custom performance classes for an MX network
[**getNetworkApplianceTrafficShapingRules_0**](ConfigureApi.md#getNetworkApplianceTrafficShapingRules_0) | **GET** /networks/{networkId}/appliance/trafficShaping/rules | Display the traffic shaping settings rules for an MX network
[**getNetworkApplianceTrafficShapingUplinkBandwidth_0**](ConfigureApi.md#getNetworkApplianceTrafficShapingUplinkBandwidth_0) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Returns the uplink bandwidth limits for your MX network
[**getNetworkApplianceTrafficShapingUplinkSelection_0**](ConfigureApi.md#getNetworkApplianceTrafficShapingUplinkSelection_0) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Show uplink selection settings for an MX network
[**getNetworkApplianceTrafficShaping_0**](ConfigureApi.md#getNetworkApplianceTrafficShaping_0) | **GET** /networks/{networkId}/appliance/trafficShaping | Display the traffic shaping settings for an MX network
[**getNetworkApplianceVlan_0**](ConfigureApi.md#getNetworkApplianceVlan_0) | **GET** /networks/{networkId}/appliance/vlans/{vlanId} | Return a VLAN
[**getNetworkApplianceVlansSettings_0**](ConfigureApi.md#getNetworkApplianceVlansSettings_0) | **GET** /networks/{networkId}/appliance/vlans/settings | Returns the enabled status of VLANs for the network
[**getNetworkApplianceVlans_0**](ConfigureApi.md#getNetworkApplianceVlans_0) | **GET** /networks/{networkId}/appliance/vlans | List the VLANs for an MX network
[**getNetworkApplianceVpnBgp_0**](ConfigureApi.md#getNetworkApplianceVpnBgp_0) | **GET** /networks/{networkId}/appliance/vpn/bgp | Return a Hub BGP Configuration
[**getNetworkApplianceVpnSiteToSiteVpn_0**](ConfigureApi.md#getNetworkApplianceVpnSiteToSiteVpn_0) | **GET** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Return the site-to-site VPN settings of a network
[**getNetworkApplianceWarmSpare_0**](ConfigureApi.md#getNetworkApplianceWarmSpare_0) | **GET** /networks/{networkId}/appliance/warmSpare | Return MX warm spare settings
[**getNetworkCameraQualityRetentionProfile_0**](ConfigureApi.md#getNetworkCameraQualityRetentionProfile_0) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Retrieve a single quality retention profile
[**getNetworkCameraQualityRetentionProfiles_0**](ConfigureApi.md#getNetworkCameraQualityRetentionProfiles_0) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles | List the quality retention profiles for this network
[**getNetworkCameraSchedules_0**](ConfigureApi.md#getNetworkCameraSchedules_0) | **GET** /networks/{networkId}/camera/schedules | Returns a list of all camera recording schedules.
[**getNetworkCameraWirelessProfile_0**](ConfigureApi.md#getNetworkCameraWirelessProfile_0) | **GET** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Retrieve a single camera wireless profile.
[**getNetworkCameraWirelessProfiles_0**](ConfigureApi.md#getNetworkCameraWirelessProfiles_0) | **GET** /networks/{networkId}/camera/wirelessProfiles | List the camera wireless profiles for this network.
[**getNetworkCellularGatewayConnectivityMonitoringDestinations_0**](ConfigureApi.md#getNetworkCellularGatewayConnectivityMonitoringDestinations_0) | **GET** /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MG network
[**getNetworkCellularGatewayDhcp_0**](ConfigureApi.md#getNetworkCellularGatewayDhcp_0) | **GET** /networks/{networkId}/cellularGateway/dhcp | List common DHCP settings of MGs
[**getNetworkCellularGatewaySubnetPool_0**](ConfigureApi.md#getNetworkCellularGatewaySubnetPool_0) | **GET** /networks/{networkId}/cellularGateway/subnetPool | Return the subnet pool and mask configured for MGs in the network.
[**getNetworkCellularGatewayUplink_0**](ConfigureApi.md#getNetworkCellularGatewayUplink_0) | **GET** /networks/{networkId}/cellularGateway/uplink | Returns the uplink settings for your MG network.
[**getNetworkClientPolicy_0**](ConfigureApi.md#getNetworkClientPolicy_0) | **GET** /networks/{networkId}/clients/{clientId}/policy | Return the policy assigned to a client on the network
[**getNetworkClientSplashAuthorizationStatus_0**](ConfigureApi.md#getNetworkClientSplashAuthorizationStatus_0) | **GET** /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus | Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash
[**getNetworkDevices_0**](ConfigureApi.md#getNetworkDevices_0) | **GET** /networks/{networkId}/devices | List the devices in a network
[**getNetworkFirmwareUpgradesStagedEvents_0**](ConfigureApi.md#getNetworkFirmwareUpgradesStagedEvents_0) | **GET** /networks/{networkId}/firmwareUpgrades/staged/events | Get the Staged Upgrade Event from a network
[**getNetworkFirmwareUpgradesStagedGroup_0**](ConfigureApi.md#getNetworkFirmwareUpgradesStagedGroup_0) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network
[**getNetworkFirmwareUpgradesStagedGroups_0**](ConfigureApi.md#getNetworkFirmwareUpgradesStagedGroups_0) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network
[**getNetworkFirmwareUpgradesStagedStages_0**](ConfigureApi.md#getNetworkFirmwareUpgradesStagedStages_0) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network
[**getNetworkFirmwareUpgrades_0**](ConfigureApi.md#getNetworkFirmwareUpgrades_0) | **GET** /networks/{networkId}/firmwareUpgrades | Get firmware upgrade information for a network
[**getNetworkFloorPlan_0**](ConfigureApi.md#getNetworkFloorPlan_0) | **GET** /networks/{networkId}/floorPlans/{floorPlanId} | Find a floor plan by ID
[**getNetworkFloorPlans_0**](ConfigureApi.md#getNetworkFloorPlans_0) | **GET** /networks/{networkId}/floorPlans | List the floor plans that belong to your network
[**getNetworkGroupPolicies_0**](ConfigureApi.md#getNetworkGroupPolicies_0) | **GET** /networks/{networkId}/groupPolicies | List the group policies in a network
[**getNetworkGroupPolicy_0**](ConfigureApi.md#getNetworkGroupPolicy_0) | **GET** /networks/{networkId}/groupPolicies/{groupPolicyId} | Display a group policy
[**getNetworkHealthAlerts_0**](ConfigureApi.md#getNetworkHealthAlerts_0) | **GET** /networks/{networkId}/health/alerts | Return all global alerts on this network
[**getNetworkMerakiAuthUser_0**](ConfigureApi.md#getNetworkMerakiAuthUser_0) | **GET** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Return the Meraki Auth splash guest, RADIUS, or client VPN user
[**getNetworkMerakiAuthUsers_0**](ConfigureApi.md#getNetworkMerakiAuthUsers_0) | **GET** /networks/{networkId}/merakiAuthUsers | List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)
[**getNetworkMqttBroker_0**](ConfigureApi.md#getNetworkMqttBroker_0) | **GET** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Return an MQTT broker
[**getNetworkMqttBrokers_0**](ConfigureApi.md#getNetworkMqttBrokers_0) | **GET** /networks/{networkId}/mqttBrokers | List the MQTT brokers for this network
[**getNetworkNetflow_0**](ConfigureApi.md#getNetworkNetflow_0) | **GET** /networks/{networkId}/netflow | Return the NetFlow traffic reporting settings for a network
[**getNetworkPiiPiiKeys_0**](ConfigureApi.md#getNetworkPiiPiiKeys_0) | **GET** /networks/{networkId}/pii/piiKeys | List the keys required to access Personally Identifiable Information (PII) for a given identifier
[**getNetworkPiiRequest_0**](ConfigureApi.md#getNetworkPiiRequest_0) | **GET** /networks/{networkId}/pii/requests/{requestId} | Return a PII request
[**getNetworkPiiRequests_0**](ConfigureApi.md#getNetworkPiiRequests_0) | **GET** /networks/{networkId}/pii/requests | List the PII requests for this network or organization
[**getNetworkPiiSmDevicesForKey_0**](ConfigureApi.md#getNetworkPiiSmDevicesForKey_0) | **GET** /networks/{networkId}/pii/smDevicesForKey | Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier
[**getNetworkPiiSmOwnersForKey_0**](ConfigureApi.md#getNetworkPiiSmOwnersForKey_0) | **GET** /networks/{networkId}/pii/smOwnersForKey | Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier
[**getNetworkPoliciesByClient_0**](ConfigureApi.md#getNetworkPoliciesByClient_0) | **GET** /networks/{networkId}/policies/byClient | Get policies for all clients with policies
[**getNetworkSensorAlertsProfile_0**](ConfigureApi.md#getNetworkSensorAlertsProfile_0) | **GET** /networks/{networkId}/sensor/alerts/profiles/{id} | Show details of a sensor alert profile for a network.
[**getNetworkSensorAlertsProfiles_0**](ConfigureApi.md#getNetworkSensorAlertsProfiles_0) | **GET** /networks/{networkId}/sensor/alerts/profiles | Lists all sensor alert profiles for a network.
[**getNetworkSensorRelationships_0**](ConfigureApi.md#getNetworkSensorRelationships_0) | **GET** /networks/{networkId}/sensor/relationships | List the sensor roles for devices in a given network
[**getNetworkSettings_0**](ConfigureApi.md#getNetworkSettings_0) | **GET** /networks/{networkId}/settings | Return the settings for a network
[**getNetworkSmBypassActivationLockAttempt_0**](ConfigureApi.md#getNetworkSmBypassActivationLockAttempt_0) | **GET** /networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId} | Bypass activation lock attempt status
[**getNetworkSmDeviceCerts_0**](ConfigureApi.md#getNetworkSmDeviceCerts_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/certs | List the certs on a device
[**getNetworkSmDeviceDeviceProfiles_0**](ConfigureApi.md#getNetworkSmDeviceDeviceProfiles_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/deviceProfiles | Get the installed profiles associated with a device
[**getNetworkSmDeviceNetworkAdapters_0**](ConfigureApi.md#getNetworkSmDeviceNetworkAdapters_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/networkAdapters | List the network adapters of a device
[**getNetworkSmDeviceRestrictions_0**](ConfigureApi.md#getNetworkSmDeviceRestrictions_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/restrictions | List the restrictions on a device
[**getNetworkSmDeviceSecurityCenters_0**](ConfigureApi.md#getNetworkSmDeviceSecurityCenters_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/securityCenters | List the security centers on a device
[**getNetworkSmDeviceSoftwares_0**](ConfigureApi.md#getNetworkSmDeviceSoftwares_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/softwares | Get a list of softwares associated with a device
[**getNetworkSmDeviceWlanLists_0**](ConfigureApi.md#getNetworkSmDeviceWlanLists_0) | **GET** /networks/{networkId}/sm/devices/{deviceId}/wlanLists | List the saved SSID names on a device
[**getNetworkSmDevices_0**](ConfigureApi.md#getNetworkSmDevices_0) | **GET** /networks/{networkId}/sm/devices | List the devices enrolled in an SM network with various specified fields and filters
[**getNetworkSmProfiles_0**](ConfigureApi.md#getNetworkSmProfiles_0) | **GET** /networks/{networkId}/sm/profiles | List all profiles in a network
[**getNetworkSmTargetGroup_0**](ConfigureApi.md#getNetworkSmTargetGroup_0) | **GET** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Return a target group
[**getNetworkSmTargetGroups_0**](ConfigureApi.md#getNetworkSmTargetGroups_0) | **GET** /networks/{networkId}/sm/targetGroups | List the target groups in this network
[**getNetworkSmTrustedAccessConfigs_0**](ConfigureApi.md#getNetworkSmTrustedAccessConfigs_0) | **GET** /networks/{networkId}/sm/trustedAccessConfigs | List Trusted Access Configs
[**getNetworkSmUserAccessDevices_0**](ConfigureApi.md#getNetworkSmUserAccessDevices_0) | **GET** /networks/{networkId}/sm/userAccessDevices | List User Access Devices and its Trusted Access Connections
[**getNetworkSmUserDeviceProfiles_0**](ConfigureApi.md#getNetworkSmUserDeviceProfiles_0) | **GET** /networks/{networkId}/sm/users/{userId}/deviceProfiles | Get the profiles associated with a user
[**getNetworkSmUserSoftwares_0**](ConfigureApi.md#getNetworkSmUserSoftwares_0) | **GET** /networks/{networkId}/sm/users/{userId}/softwares | Get a list of softwares associated with a user
[**getNetworkSmUsers_0**](ConfigureApi.md#getNetworkSmUsers_0) | **GET** /networks/{networkId}/sm/users | List the owners in an SM network with various specified fields and filters
[**getNetworkSnmp_0**](ConfigureApi.md#getNetworkSnmp_0) | **GET** /networks/{networkId}/snmp | Return the SNMP settings for a network
[**getNetworkSwitchAccessControlLists_0**](ConfigureApi.md#getNetworkSwitchAccessControlLists_0) | **GET** /networks/{networkId}/switch/accessControlLists | Return the access control lists for a MS network
[**getNetworkSwitchAccessPolicies_0**](ConfigureApi.md#getNetworkSwitchAccessPolicies_0) | **GET** /networks/{networkId}/switch/accessPolicies | List the access policies for a switch network
[**getNetworkSwitchAccessPolicy_0**](ConfigureApi.md#getNetworkSwitchAccessPolicy_0) | **GET** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Return a specific access policy for a switch network
[**getNetworkSwitchAlternateManagementInterface_0**](ConfigureApi.md#getNetworkSwitchAlternateManagementInterface_0) | **GET** /networks/{networkId}/switch/alternateManagementInterface | Return the switch alternate management interface for the network
[**getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_0**](ConfigureApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_0) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Return the list of servers trusted by Dynamic ARP Inspection on this network
[**getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_0**](ConfigureApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_0) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice | Return the devices that have a Dynamic ARP Inspection warning and their warnings
[**getNetworkSwitchDhcpServerPolicy_0**](ConfigureApi.md#getNetworkSwitchDhcpServerPolicy_0) | **GET** /networks/{networkId}/switch/dhcpServerPolicy | Return the DHCP server settings
[**getNetworkSwitchDhcpV4ServersSeen_0**](ConfigureApi.md#getNetworkSwitchDhcpV4ServersSeen_0) | **GET** /networks/{networkId}/switch/dhcp/v4/servers/seen | Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)
[**getNetworkSwitchDscpToCosMappings_0**](ConfigureApi.md#getNetworkSwitchDscpToCosMappings_0) | **GET** /networks/{networkId}/switch/dscpToCosMappings | Return the DSCP to CoS mappings
[**getNetworkSwitchLinkAggregations_0**](ConfigureApi.md#getNetworkSwitchLinkAggregations_0) | **GET** /networks/{networkId}/switch/linkAggregations | List link aggregation groups
[**getNetworkSwitchMtu_0**](ConfigureApi.md#getNetworkSwitchMtu_0) | **GET** /networks/{networkId}/switch/mtu | Return the MTU configuration
[**getNetworkSwitchPortSchedules_0**](ConfigureApi.md#getNetworkSwitchPortSchedules_0) | **GET** /networks/{networkId}/switch/portSchedules | List switch port schedules
[**getNetworkSwitchQosRule_0**](ConfigureApi.md#getNetworkSwitchQosRule_0) | **GET** /networks/{networkId}/switch/qosRules/{qosRuleId} | Return a quality of service rule
[**getNetworkSwitchQosRulesOrder_0**](ConfigureApi.md#getNetworkSwitchQosRulesOrder_0) | **GET** /networks/{networkId}/switch/qosRules/order | Return the quality of service rule IDs by order in which they will be processed by the switch
[**getNetworkSwitchQosRules_0**](ConfigureApi.md#getNetworkSwitchQosRules_0) | **GET** /networks/{networkId}/switch/qosRules | List quality of service rules
[**getNetworkSwitchRoutingMulticastRendezvousPoint_0**](ConfigureApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint_0) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point
[**getNetworkSwitchRoutingMulticastRendezvousPoints_0**](ConfigureApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints_0) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points
[**getNetworkSwitchRoutingMulticast_0**](ConfigureApi.md#getNetworkSwitchRoutingMulticast_0) | **GET** /networks/{networkId}/switch/routing/multicast | Return multicast settings for a network
[**getNetworkSwitchRoutingOspf_0**](ConfigureApi.md#getNetworkSwitchRoutingOspf_0) | **GET** /networks/{networkId}/switch/routing/ospf | Return layer 3 OSPF routing configuration
[**getNetworkSwitchSettings_0**](ConfigureApi.md#getNetworkSwitchSettings_0) | **GET** /networks/{networkId}/switch/settings | Returns the switch network settings
[**getNetworkSwitchStackRoutingInterfaceDhcp_0**](ConfigureApi.md#getNetworkSwitchStackRoutingInterfaceDhcp_0) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch stack
[**getNetworkSwitchStackRoutingInterface_0**](ConfigureApi.md#getNetworkSwitchStackRoutingInterface_0) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Return a layer 3 interface from a switch stack
[**getNetworkSwitchStackRoutingInterfaces_0**](ConfigureApi.md#getNetworkSwitchStackRoutingInterfaces_0) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | List layer 3 interfaces for a switch stack
[**getNetworkSwitchStackRoutingStaticRoute_0**](ConfigureApi.md#getNetworkSwitchStackRoutingStaticRoute_0) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch stack
[**getNetworkSwitchStackRoutingStaticRoutes_0**](ConfigureApi.md#getNetworkSwitchStackRoutingStaticRoutes_0) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | List layer 3 static routes for a switch stack
[**getNetworkSwitchStack_0**](ConfigureApi.md#getNetworkSwitchStack_0) | **GET** /networks/{networkId}/switch/stacks/{switchStackId} | Show a switch stack
[**getNetworkSwitchStacks_0**](ConfigureApi.md#getNetworkSwitchStacks_0) | **GET** /networks/{networkId}/switch/stacks | List the switch stacks in a network
[**getNetworkSwitchStormControl_0**](ConfigureApi.md#getNetworkSwitchStormControl_0) | **GET** /networks/{networkId}/switch/stormControl | Return the storm control configuration for a switch network
[**getNetworkSwitchStp_0**](ConfigureApi.md#getNetworkSwitchStp_0) | **GET** /networks/{networkId}/switch/stp | Returns STP settings
[**getNetworkSyslogServers_0**](ConfigureApi.md#getNetworkSyslogServers_0) | **GET** /networks/{networkId}/syslogServers | List the syslog servers for a network
[**getNetworkTrafficAnalysis_0**](ConfigureApi.md#getNetworkTrafficAnalysis_0) | **GET** /networks/{networkId}/trafficAnalysis | Return the traffic analysis settings for a network
[**getNetworkTrafficShapingApplicationCategories_0**](ConfigureApi.md#getNetworkTrafficShapingApplicationCategories_0) | **GET** /networks/{networkId}/trafficShaping/applicationCategories | Returns the application categories for traffic shaping rules.
[**getNetworkTrafficShapingDscpTaggingOptions_0**](ConfigureApi.md#getNetworkTrafficShapingDscpTaggingOptions_0) | **GET** /networks/{networkId}/trafficShaping/dscpTaggingOptions | Returns the available DSCP tagging options for your traffic shaping rules.
[**getNetworkWebhooksHttpServer_0**](ConfigureApi.md#getNetworkWebhooksHttpServer_0) | **GET** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Return an HTTP server for a network
[**getNetworkWebhooksHttpServers_0**](ConfigureApi.md#getNetworkWebhooksHttpServers_0) | **GET** /networks/{networkId}/webhooks/httpServers | List the HTTP servers for a network
[**getNetworkWebhooksPayloadTemplate_0**](ConfigureApi.md#getNetworkWebhooksPayloadTemplate_0) | **GET** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Get the webhook payload template for a network
[**getNetworkWebhooksPayloadTemplates_0**](ConfigureApi.md#getNetworkWebhooksPayloadTemplates_0) | **GET** /networks/{networkId}/webhooks/payloadTemplates | List the webhook payload templates for a network
[**getNetworkWebhooksWebhookTest_0**](ConfigureApi.md#getNetworkWebhooksWebhookTest_0) | **GET** /networks/{networkId}/webhooks/webhookTests/{webhookTestId} | Return the status of a webhook test for a network
[**getNetworkWirelessAlternateManagementInterface_0**](ConfigureApi.md#getNetworkWirelessAlternateManagementInterface_0) | **GET** /networks/{networkId}/wireless/alternateManagementInterface | Return alternate management interface and devices with IP assigned
[**getNetworkWirelessBilling_0**](ConfigureApi.md#getNetworkWirelessBilling_0) | **GET** /networks/{networkId}/wireless/billing | Return the billing settings of this network
[**getNetworkWirelessBluetoothSettings_0**](ConfigureApi.md#getNetworkWirelessBluetoothSettings_0) | **GET** /networks/{networkId}/wireless/bluetooth/settings | Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
[**getNetworkWirelessRfProfile_0**](ConfigureApi.md#getNetworkWirelessRfProfile_0) | **GET** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Return a RF profile
[**getNetworkWirelessRfProfiles_0**](ConfigureApi.md#getNetworkWirelessRfProfiles_0) | **GET** /networks/{networkId}/wireless/rfProfiles | List the non-basic RF profiles for this network
[**getNetworkWirelessSettings_0**](ConfigureApi.md#getNetworkWirelessSettings_0) | **GET** /networks/{networkId}/wireless/settings | Return the wireless settings for a network
[**getNetworkWirelessSsidBonjourForwarding_0**](ConfigureApi.md#getNetworkWirelessSsidBonjourForwarding_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | List the Bonjour forwarding setting and rules for the SSID
[**getNetworkWirelessSsidDeviceTypeGroupPolicies_0**](ConfigureApi.md#getNetworkWirelessSsidDeviceTypeGroupPolicies_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | List the device type group policies for the SSID
[**getNetworkWirelessSsidEapOverride_0**](ConfigureApi.md#getNetworkWirelessSsidEapOverride_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Return the EAP overridden parameters for an SSID
[**getNetworkWirelessSsidFirewallL3FirewallRules_0**](ConfigureApi.md#getNetworkWirelessSsidFirewallL3FirewallRules_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network
[**getNetworkWirelessSsidFirewallL7FirewallRules_0**](ConfigureApi.md#getNetworkWirelessSsidFirewallL7FirewallRules_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Return the L7 firewall rules for an SSID on an MR network
[**getNetworkWirelessSsidHotspot20_0**](ConfigureApi.md#getNetworkWirelessSsidHotspot20_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Return the Hotspot 2.0 settings for an SSID
[**getNetworkWirelessSsidIdentityPsk_0**](ConfigureApi.md#getNetworkWirelessSsidIdentityPsk_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Return an Identity PSK
[**getNetworkWirelessSsidIdentityPsks_0**](ConfigureApi.md#getNetworkWirelessSsidIdentityPsks_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks | List all Identity PSKs in a wireless network
[**getNetworkWirelessSsidSchedules_0**](ConfigureApi.md#getNetworkWirelessSsidSchedules_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/schedules | List the outage schedule for the SSID
[**getNetworkWirelessSsidSplashSettings_0**](ConfigureApi.md#getNetworkWirelessSsidSplashSettings_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Display the splash page settings for the given SSID
[**getNetworkWirelessSsidTrafficShapingRules_0**](ConfigureApi.md#getNetworkWirelessSsidTrafficShapingRules_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Display the traffic shaping settings for a SSID on an MR network
[**getNetworkWirelessSsidVpn_0**](ConfigureApi.md#getNetworkWirelessSsidVpn_0) | **GET** /networks/{networkId}/wireless/ssids/{number}/vpn | List the VPN settings for the SSID.
[**getNetworkWirelessSsid_0**](ConfigureApi.md#getNetworkWirelessSsid_0) | **GET** /networks/{networkId}/wireless/ssids/{number} | Return a single MR SSID
[**getNetworkWirelessSsids_0**](ConfigureApi.md#getNetworkWirelessSsids_0) | **GET** /networks/{networkId}/wireless/ssids | List the MR SSIDs in a network
[**getNetwork_0**](ConfigureApi.md#getNetwork_0) | **GET** /networks/{networkId} | Return a network
[**getOrganizationActionBatch_0**](ConfigureApi.md#getOrganizationActionBatch_0) | **GET** /organizations/{organizationId}/actionBatches/{actionBatchId} | Return an action batch
[**getOrganizationActionBatches_0**](ConfigureApi.md#getOrganizationActionBatches_0) | **GET** /organizations/{organizationId}/actionBatches | Return the list of action batches in the organization
[**getOrganizationAdaptivePolicyAcl_0**](ConfigureApi.md#getOrganizationAdaptivePolicyAcl_0) | **GET** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Returns the adaptive policy ACL information
[**getOrganizationAdaptivePolicyAcls_0**](ConfigureApi.md#getOrganizationAdaptivePolicyAcls_0) | **GET** /organizations/{organizationId}/adaptivePolicy/acls | List adaptive policy ACLs in a organization
[**getOrganizationAdaptivePolicyGroup_0**](ConfigureApi.md#getOrganizationAdaptivePolicyGroup_0) | **GET** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Returns an adaptive policy group
[**getOrganizationAdaptivePolicyGroups_0**](ConfigureApi.md#getOrganizationAdaptivePolicyGroups_0) | **GET** /organizations/{organizationId}/adaptivePolicy/groups | List adaptive policy groups in a organization
[**getOrganizationAdaptivePolicyPolicies_0**](ConfigureApi.md#getOrganizationAdaptivePolicyPolicies_0) | **GET** /organizations/{organizationId}/adaptivePolicy/policies | List adaptive policies in an organization
[**getOrganizationAdaptivePolicyPolicy_0**](ConfigureApi.md#getOrganizationAdaptivePolicyPolicy_0) | **GET** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Return an adaptive policy
[**getOrganizationAdaptivePolicySettings_0**](ConfigureApi.md#getOrganizationAdaptivePolicySettings_0) | **GET** /organizations/{organizationId}/adaptivePolicy/settings | Returns global adaptive policy settings in an organization
[**getOrganizationAdmins_0**](ConfigureApi.md#getOrganizationAdmins_0) | **GET** /organizations/{organizationId}/admins | List the dashboard administrators in this organization
[**getOrganizationAlertsProfiles_0**](ConfigureApi.md#getOrganizationAlertsProfiles_0) | **GET** /organizations/{organizationId}/alerts/profiles | List all organization-wide alert configurations
[**getOrganizationApplianceSecurityIntrusion_0**](ConfigureApi.md#getOrganizationApplianceSecurityIntrusion_0) | **GET** /organizations/{organizationId}/appliance/security/intrusion | Returns all supported intrusion settings for an organization
[**getOrganizationApplianceVpnThirdPartyVPNPeers_0**](ConfigureApi.md#getOrganizationApplianceVpnThirdPartyVPNPeers_0) | **GET** /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers | Return the third party VPN peers for an organization
[**getOrganizationApplianceVpnVpnFirewallRules_0**](ConfigureApi.md#getOrganizationApplianceVpnVpnFirewallRules_0) | **GET** /organizations/{organizationId}/appliance/vpn/vpnFirewallRules | Return the firewall rules for an organization&#39;s site-to-site VPN
[**getOrganizationBrandingPoliciesPriorities_0**](ConfigureApi.md#getOrganizationBrandingPoliciesPriorities_0) | **GET** /organizations/{organizationId}/brandingPolicies/priorities | Return the branding policy IDs of an organization in priority order
[**getOrganizationBrandingPolicies_0**](ConfigureApi.md#getOrganizationBrandingPolicies_0) | **GET** /organizations/{organizationId}/brandingPolicies | List the branding policies of an organization
[**getOrganizationBrandingPolicy_0**](ConfigureApi.md#getOrganizationBrandingPolicy_0) | **GET** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Return a branding policy
[**getOrganizationCameraCustomAnalyticsArtifact_0**](ConfigureApi.md#getOrganizationCameraCustomAnalyticsArtifact_0) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Get Custom Analytics Artifact
[**getOrganizationCameraCustomAnalyticsArtifacts_0**](ConfigureApi.md#getOrganizationCameraCustomAnalyticsArtifacts_0) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts | List Custom Analytics Artifacts
[**getOrganizationCameraOnboardingStatuses_0**](ConfigureApi.md#getOrganizationCameraOnboardingStatuses_0) | **GET** /organizations/{organizationId}/camera/onboarding/statuses | Fetch onboarding status of cameras
[**getOrganizationClientsSearch_0**](ConfigureApi.md#getOrganizationClientsSearch_0) | **GET** /organizations/{organizationId}/clients/search | Return the client details in an organization
[**getOrganizationConfigTemplateSwitchProfilePort_0**](ConfigureApi.md#getOrganizationConfigTemplateSwitchProfilePort_0) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Return a switch profile port
[**getOrganizationConfigTemplateSwitchProfilePorts_0**](ConfigureApi.md#getOrganizationConfigTemplateSwitchProfilePorts_0) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports | Return all the ports of a switch profile
[**getOrganizationConfigTemplateSwitchProfiles_0**](ConfigureApi.md#getOrganizationConfigTemplateSwitchProfiles_0) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles | List the switch profiles for your switch template configuration
[**getOrganizationConfigTemplate_0**](ConfigureApi.md#getOrganizationConfigTemplate_0) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId} | Return a single configuration template
[**getOrganizationConfigTemplates_0**](ConfigureApi.md#getOrganizationConfigTemplates_0) | **GET** /organizations/{organizationId}/configTemplates | List the configuration templates for this organization
[**getOrganizationDevices_0**](ConfigureApi.md#getOrganizationDevices_0) | **GET** /organizations/{organizationId}/devices | List the devices in an organization
[**getOrganizationEarlyAccessFeaturesOptIn_0**](ConfigureApi.md#getOrganizationEarlyAccessFeaturesOptIn_0) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Show an early access feature opt-in for an organization
[**getOrganizationEarlyAccessFeaturesOptIns_0**](ConfigureApi.md#getOrganizationEarlyAccessFeaturesOptIns_0) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns | List the early access feature opt-ins for an organization
[**getOrganizationEarlyAccessFeatures_0**](ConfigureApi.md#getOrganizationEarlyAccessFeatures_0) | **GET** /organizations/{organizationId}/earlyAccess/features | List the available early access features for organization
[**getOrganizationFirmwareUpgradesByDevice_0**](ConfigureApi.md#getOrganizationFirmwareUpgradesByDevice_0) | **GET** /organizations/{organizationId}/firmware/upgrades/byDevice | Get firmware upgrade status for the filtered devices
[**getOrganizationFirmwareUpgrades_0**](ConfigureApi.md#getOrganizationFirmwareUpgrades_0) | **GET** /organizations/{organizationId}/firmware/upgrades | Get firmware upgrade information for an organization
[**getOrganizationInsightApplications_0**](ConfigureApi.md#getOrganizationInsightApplications_0) | **GET** /organizations/{organizationId}/insight/applications | List all Insight tracked applications
[**getOrganizationInsightMonitoredMediaServer_0**](ConfigureApi.md#getOrganizationInsightMonitoredMediaServer_0) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Return a monitored media server for this organization
[**getOrganizationInsightMonitoredMediaServers_0**](ConfigureApi.md#getOrganizationInsightMonitoredMediaServers_0) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers | List the monitored media servers for this organization
[**getOrganizationInventoryDevice_0**](ConfigureApi.md#getOrganizationInventoryDevice_0) | **GET** /organizations/{organizationId}/inventory/devices/{serial} | Return a single device from the inventory of an organization
[**getOrganizationInventoryDevices_0**](ConfigureApi.md#getOrganizationInventoryDevices_0) | **GET** /organizations/{organizationId}/inventory/devices | Return the device inventory for an organization
[**getOrganizationInventoryOnboardingCloudMonitoringImports_0**](ConfigureApi.md#getOrganizationInventoryOnboardingCloudMonitoringImports_0) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Check the status of a committed Import operation
[**getOrganizationInventoryOnboardingCloudMonitoringNetworks_0**](ConfigureApi.md#getOrganizationInventoryOnboardingCloudMonitoringNetworks_0) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks | Returns list of networks eligible for adding cloud monitored device
[**getOrganizationLicense_0**](ConfigureApi.md#getOrganizationLicense_0) | **GET** /organizations/{organizationId}/licenses/{licenseId} | Display a license
[**getOrganizationLicenses_0**](ConfigureApi.md#getOrganizationLicenses_0) | **GET** /organizations/{organizationId}/licenses | List the licenses for an organization
[**getOrganizationLicensingCotermLicenses_0**](ConfigureApi.md#getOrganizationLicensingCotermLicenses_0) | **GET** /organizations/{organizationId}/licensing/coterm/licenses | List the licenses in a coterm organization
[**getOrganizationLoginSecurity_0**](ConfigureApi.md#getOrganizationLoginSecurity_0) | **GET** /organizations/{organizationId}/loginSecurity | Returns the login security settings for an organization.
[**getOrganizationNetworks_0**](ConfigureApi.md#getOrganizationNetworks_0) | **GET** /organizations/{organizationId}/networks | List the networks that the user has privileges on in an organization
[**getOrganizationPolicyObject_0**](ConfigureApi.md#getOrganizationPolicyObject_0) | **GET** /organizations/{organizationId}/policyObjects/{policyObjectId} | Shows details of a Policy Object.
[**getOrganizationPolicyObjectsGroup_0**](ConfigureApi.md#getOrganizationPolicyObjectsGroup_0) | **GET** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Shows details of a Policy Object Group.
[**getOrganizationPolicyObjectsGroups_0**](ConfigureApi.md#getOrganizationPolicyObjectsGroups_0) | **GET** /organizations/{organizationId}/policyObjects/groups | Lists Policy Object Groups belonging to the organization.
[**getOrganizationPolicyObjects_0**](ConfigureApi.md#getOrganizationPolicyObjects_0) | **GET** /organizations/{organizationId}/policyObjects | Lists Policy Objects belonging to the organization.
[**getOrganizationSamlIdp_0**](ConfigureApi.md#getOrganizationSamlIdp_0) | **GET** /organizations/{organizationId}/saml/idps/{idpId} | Get a SAML IdP from your organization.
[**getOrganizationSamlIdps_0**](ConfigureApi.md#getOrganizationSamlIdps_0) | **GET** /organizations/{organizationId}/saml/idps | List the SAML IdPs in your organization.
[**getOrganizationSamlRole_0**](ConfigureApi.md#getOrganizationSamlRole_0) | **GET** /organizations/{organizationId}/samlRoles/{samlRoleId} | Return a SAML role
[**getOrganizationSamlRoles_0**](ConfigureApi.md#getOrganizationSamlRoles_0) | **GET** /organizations/{organizationId}/samlRoles | List the SAML roles for this organization
[**getOrganizationSaml_0**](ConfigureApi.md#getOrganizationSaml_0) | **GET** /organizations/{organizationId}/saml | Returns the SAML SSO enabled settings for an organization.
[**getOrganizationSmApnsCert_0**](ConfigureApi.md#getOrganizationSmApnsCert_0) | **GET** /organizations/{organizationId}/sm/apnsCert | Get the organization&#39;s APNS certificate
[**getOrganizationSmVppAccount_0**](ConfigureApi.md#getOrganizationSmVppAccount_0) | **GET** /organizations/{organizationId}/sm/vppAccounts/{vppAccountId} | Get a hash containing the unparsed token of the VPP account with the given ID
[**getOrganizationSmVppAccounts_0**](ConfigureApi.md#getOrganizationSmVppAccounts_0) | **GET** /organizations/{organizationId}/sm/vppAccounts | List the VPP accounts in the organization
[**getOrganizationSnmp_0**](ConfigureApi.md#getOrganizationSnmp_0) | **GET** /organizations/{organizationId}/snmp | Return the SNMP settings for an organization
[**getOrganizationSwitchPortsBySwitch_0**](ConfigureApi.md#getOrganizationSwitchPortsBySwitch_0) | **GET** /organizations/{organizationId}/switch/ports/bySwitch | List the switchports in an organization by switch
[**getOrganizationWirelessDevicesEthernetStatuses_0**](ConfigureApi.md#getOrganizationWirelessDevicesEthernetStatuses_0) | **GET** /organizations/{organizationId}/wireless/devices/ethernet/statuses | Endpoint to see power status for wireless devices
[**getOrganization_0**](ConfigureApi.md#getOrganization_0) | **GET** /organizations/{organizationId} | Return an organization
[**getOrganizations_0**](ConfigureApi.md#getOrganizations_0) | **GET** /organizations | List the organizations that the user has privileges on
[**lockNetworkSmDevices_0**](ConfigureApi.md#lockNetworkSmDevices_0) | **POST** /networks/{networkId}/sm/devices/lock | Lock a set of devices
[**modifyNetworkSmDevicesTags_0**](ConfigureApi.md#modifyNetworkSmDevicesTags_0) | **POST** /networks/{networkId}/sm/devices/modifyTags | Add, delete, or update the tags of a set of devices
[**moveNetworkSmDevices_0**](ConfigureApi.md#moveNetworkSmDevices_0) | **POST** /networks/{networkId}/sm/devices/move | Move a set of devices to a new network
[**moveOrganizationLicensesSeats_0**](ConfigureApi.md#moveOrganizationLicensesSeats_0) | **POST** /organizations/{organizationId}/licenses/moveSeats | Move SM seats to another organization
[**moveOrganizationLicenses_0**](ConfigureApi.md#moveOrganizationLicenses_0) | **POST** /organizations/{organizationId}/licenses/move | Move licenses to another organization
[**moveOrganizationLicensingCotermLicenses_0**](ConfigureApi.md#moveOrganizationLicensingCotermLicenses_0) | **POST** /organizations/{organizationId}/licensing/coterm/licenses/move | Moves a license to a different organization (coterm only)
[**provisionNetworkClients_0**](ConfigureApi.md#provisionNetworkClients_0) | **POST** /networks/{networkId}/clients/provision | Provisions a client with a name and policy
[**refreshNetworkSmDeviceDetails_0**](ConfigureApi.md#refreshNetworkSmDeviceDetails_0) | **POST** /networks/{networkId}/sm/devices/{deviceId}/refreshDetails | Refresh the details of a device
[**releaseFromOrganizationInventory_0**](ConfigureApi.md#releaseFromOrganizationInventory_0) | **POST** /organizations/{organizationId}/inventory/release | Release a list of claimed devices from an organization.
[**removeNetworkDevices_0**](ConfigureApi.md#removeNetworkDevices_0) | **POST** /networks/{networkId}/devices/remove | Remove a single device
[**removeNetworkSwitchStack_0**](ConfigureApi.md#removeNetworkSwitchStack_0) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/remove | Remove a switch from a stack
[**renewOrganizationLicensesSeats_0**](ConfigureApi.md#renewOrganizationLicensesSeats_0) | **POST** /organizations/{organizationId}/licenses/renewSeats | Renew SM seats of a license
[**rollbacksNetworkFirmwareUpgradesStagedEvents_0**](ConfigureApi.md#rollbacksNetworkFirmwareUpgradesStagedEvents_0) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks | Rollback a Staged Upgrade Event for a network
[**splitNetwork_0**](ConfigureApi.md#splitNetwork_0) | **POST** /networks/{networkId}/split | Split a combined network into individual networks for each type of device
[**swapNetworkApplianceWarmSpare_0**](ConfigureApi.md#swapNetworkApplianceWarmSpare_0) | **POST** /networks/{networkId}/appliance/warmSpare/swap | Swap MX primary and warm spare appliances
[**unbindNetwork_0**](ConfigureApi.md#unbindNetwork_0) | **POST** /networks/{networkId}/unbind | Unbind a network from a template.
[**unenrollNetworkSmDevice_0**](ConfigureApi.md#unenrollNetworkSmDevice_0) | **POST** /networks/{networkId}/sm/devices/{deviceId}/unenroll | Unenroll a device
[**updateDeviceApplianceUplinksSettings_0**](ConfigureApi.md#updateDeviceApplianceUplinksSettings_0) | **PUT** /devices/{serial}/appliance/uplinks/settings | Update the uplink settings for an MX appliance
[**updateDeviceCameraCustomAnalytics_0**](ConfigureApi.md#updateDeviceCameraCustomAnalytics_0) | **PUT** /devices/{serial}/camera/customAnalytics | Update custom analytics settings for a camera
[**updateDeviceCameraQualityAndRetention_0**](ConfigureApi.md#updateDeviceCameraQualityAndRetention_0) | **PUT** /devices/{serial}/camera/qualityAndRetention | Update quality and retention settings for the given camera
[**updateDeviceCameraSense_0**](ConfigureApi.md#updateDeviceCameraSense_0) | **PUT** /devices/{serial}/camera/sense | Update sense settings for the given camera
[**updateDeviceCameraVideoSettings_0**](ConfigureApi.md#updateDeviceCameraVideoSettings_0) | **PUT** /devices/{serial}/camera/video/settings | Update video settings for the given camera
[**updateDeviceCameraWirelessProfiles_0**](ConfigureApi.md#updateDeviceCameraWirelessProfiles_0) | **PUT** /devices/{serial}/camera/wirelessProfiles | Assign wireless profiles to the given camera
[**updateDeviceCellularGatewayLan_0**](ConfigureApi.md#updateDeviceCellularGatewayLan_0) | **PUT** /devices/{serial}/cellularGateway/lan | Update the LAN Settings for a single MG.
[**updateDeviceCellularGatewayPortForwardingRules_0**](ConfigureApi.md#updateDeviceCellularGatewayPortForwardingRules_0) | **PUT** /devices/{serial}/cellularGateway/portForwardingRules | Updates the port forwarding rules for a single MG.
[**updateDeviceCellularSims_0**](ConfigureApi.md#updateDeviceCellularSims_0) | **PUT** /devices/{serial}/cellular/sims | Updates the SIM and APN configurations for a cellular device.
[**updateDeviceManagementInterface_0**](ConfigureApi.md#updateDeviceManagementInterface_0) | **PUT** /devices/{serial}/managementInterface | Update the management interface settings for a device
[**updateDeviceSensorRelationships_0**](ConfigureApi.md#updateDeviceSensorRelationships_0) | **PUT** /devices/{serial}/sensor/relationships | Assign one or more sensor roles to a given sensor or camera device.
[**updateDeviceSwitchPort_0**](ConfigureApi.md#updateDeviceSwitchPort_0) | **PUT** /devices/{serial}/switch/ports/{portId} | Update a switch port
[**updateDeviceSwitchRoutingInterfaceDhcp_0**](ConfigureApi.md#updateDeviceSwitchRoutingInterfaceDhcp_0) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch
[**updateDeviceSwitchRoutingInterface_0**](ConfigureApi.md#updateDeviceSwitchRoutingInterface_0) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch
[**updateDeviceSwitchRoutingStaticRoute_0**](ConfigureApi.md#updateDeviceSwitchRoutingStaticRoute_0) | **PUT** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch
[**updateDeviceSwitchWarmSpare_0**](ConfigureApi.md#updateDeviceSwitchWarmSpare_0) | **PUT** /devices/{serial}/switch/warmSpare | Update warm spare configuration for a switch
[**updateDeviceWirelessBluetoothSettings_0**](ConfigureApi.md#updateDeviceWirelessBluetoothSettings_0) | **PUT** /devices/{serial}/wireless/bluetooth/settings | Update the bluetooth settings for a wireless device
[**updateDeviceWirelessRadioSettings_0**](ConfigureApi.md#updateDeviceWirelessRadioSettings_0) | **PUT** /devices/{serial}/wireless/radio/settings | Update the radio settings of a device
[**updateDevice_0**](ConfigureApi.md#updateDevice_0) | **PUT** /devices/{serial} | Update the attributes of a device
[**updateNetworkAlertsSettings_0**](ConfigureApi.md#updateNetworkAlertsSettings_0) | **PUT** /networks/{networkId}/alerts/settings | Update the alert configuration for this network
[**updateNetworkApplianceConnectivityMonitoringDestinations_0**](ConfigureApi.md#updateNetworkApplianceConnectivityMonitoringDestinations_0) | **PUT** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MX network
[**updateNetworkApplianceContentFiltering_0**](ConfigureApi.md#updateNetworkApplianceContentFiltering_0) | **PUT** /networks/{networkId}/appliance/contentFiltering | Update the content filtering settings for an MX network
[**updateNetworkApplianceFirewallCellularFirewallRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallCellularFirewallRules_0) | **PUT** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Update the cellular firewall rules of an MX network
[**updateNetworkApplianceFirewallFirewalledService_0**](ConfigureApi.md#updateNetworkApplianceFirewallFirewalledService_0) | **PUT** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)
[**updateNetworkApplianceFirewallInboundCellularFirewallRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallInboundCellularFirewallRules_0) | **PUT** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Update the inbound cellular firewall rules of an MX network
[**updateNetworkApplianceFirewallInboundFirewallRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallInboundFirewallRules_0) | **PUT** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Update the inbound firewall rules of an MX network
[**updateNetworkApplianceFirewallL3FirewallRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallL3FirewallRules_0) | **PUT** /networks/{networkId}/appliance/firewall/l3FirewallRules | Update the L3 firewall rules of an MX network
[**updateNetworkApplianceFirewallL7FirewallRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallL7FirewallRules_0) | **PUT** /networks/{networkId}/appliance/firewall/l7FirewallRules | Update the MX L7 firewall rules for an MX network
[**updateNetworkApplianceFirewallOneToManyNatRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallOneToManyNatRules_0) | **PUT** /networks/{networkId}/appliance/firewall/oneToManyNatRules | Set the 1:Many NAT mapping rules for an MX network
[**updateNetworkApplianceFirewallOneToOneNatRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallOneToOneNatRules_0) | **PUT** /networks/{networkId}/appliance/firewall/oneToOneNatRules | Set the 1:1 NAT mapping rules for an MX network
[**updateNetworkApplianceFirewallPortForwardingRules_0**](ConfigureApi.md#updateNetworkApplianceFirewallPortForwardingRules_0) | **PUT** /networks/{networkId}/appliance/firewall/portForwardingRules | Update the port forwarding rules for an MX network
[**updateNetworkApplianceFirewallSettings_0**](ConfigureApi.md#updateNetworkApplianceFirewallSettings_0) | **PUT** /networks/{networkId}/appliance/firewall/settings | Update the firewall settings for this network
[**updateNetworkAppliancePort_0**](ConfigureApi.md#updateNetworkAppliancePort_0) | **PUT** /networks/{networkId}/appliance/ports/{portId} | Update the per-port VLAN settings for a single MX port.
[**updateNetworkAppliancePrefixesDelegatedStatic_0**](ConfigureApi.md#updateNetworkAppliancePrefixesDelegatedStatic_0) | **PUT** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Update a static delegated prefix from a network
[**updateNetworkApplianceSecurityIntrusion_0**](ConfigureApi.md#updateNetworkApplianceSecurityIntrusion_0) | **PUT** /networks/{networkId}/appliance/security/intrusion | Set the supported intrusion settings for an MX network
[**updateNetworkApplianceSecurityMalware_0**](ConfigureApi.md#updateNetworkApplianceSecurityMalware_0) | **PUT** /networks/{networkId}/appliance/security/malware | Set the supported malware settings for an MX network
[**updateNetworkApplianceSettings_0**](ConfigureApi.md#updateNetworkApplianceSettings_0) | **PUT** /networks/{networkId}/appliance/settings | Update the appliance settings for a network
[**updateNetworkApplianceSingleLan_0**](ConfigureApi.md#updateNetworkApplianceSingleLan_0) | **PUT** /networks/{networkId}/appliance/singleLan | Update single LAN configuration
[**updateNetworkApplianceSsid_0**](ConfigureApi.md#updateNetworkApplianceSsid_0) | **PUT** /networks/{networkId}/appliance/ssids/{number} | Update the attributes of an MX SSID
[**updateNetworkApplianceStaticRoute_0**](ConfigureApi.md#updateNetworkApplianceStaticRoute_0) | **PUT** /networks/{networkId}/appliance/staticRoutes/{staticRouteId} | Update a static route for an MX or teleworker network
[**updateNetworkApplianceTrafficShapingCustomPerformanceClass_0**](ConfigureApi.md#updateNetworkApplianceTrafficShapingCustomPerformanceClass_0) | **PUT** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Update a custom performance class for an MX network
[**updateNetworkApplianceTrafficShapingRules_0**](ConfigureApi.md#updateNetworkApplianceTrafficShapingRules_0) | **PUT** /networks/{networkId}/appliance/trafficShaping/rules | Update the traffic shaping settings rules for an MX network
[**updateNetworkApplianceTrafficShapingUplinkBandwidth_0**](ConfigureApi.md#updateNetworkApplianceTrafficShapingUplinkBandwidth_0) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Updates the uplink bandwidth settings for your MX network.
[**updateNetworkApplianceTrafficShapingUplinkSelection_0**](ConfigureApi.md#updateNetworkApplianceTrafficShapingUplinkSelection_0) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Update uplink selection settings for an MX network
[**updateNetworkApplianceTrafficShaping_0**](ConfigureApi.md#updateNetworkApplianceTrafficShaping_0) | **PUT** /networks/{networkId}/appliance/trafficShaping | Update the traffic shaping settings for an MX network
[**updateNetworkApplianceVlan_0**](ConfigureApi.md#updateNetworkApplianceVlan_0) | **PUT** /networks/{networkId}/appliance/vlans/{vlanId} | Update a VLAN
[**updateNetworkApplianceVlansSettings_0**](ConfigureApi.md#updateNetworkApplianceVlansSettings_0) | **PUT** /networks/{networkId}/appliance/vlans/settings | Enable/Disable VLANs for the given network
[**updateNetworkApplianceVpnBgp_0**](ConfigureApi.md#updateNetworkApplianceVpnBgp_0) | **PUT** /networks/{networkId}/appliance/vpn/bgp | Update a Hub BGP Configuration
[**updateNetworkApplianceVpnSiteToSiteVpn_0**](ConfigureApi.md#updateNetworkApplianceVpnSiteToSiteVpn_0) | **PUT** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Update the site-to-site VPN settings of a network
[**updateNetworkApplianceWarmSpare_0**](ConfigureApi.md#updateNetworkApplianceWarmSpare_0) | **PUT** /networks/{networkId}/appliance/warmSpare | Update MX warm spare settings
[**updateNetworkCameraQualityRetentionProfile_0**](ConfigureApi.md#updateNetworkCameraQualityRetentionProfile_0) | **PUT** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Update an existing quality retention profile for this network.
[**updateNetworkCameraWirelessProfile_0**](ConfigureApi.md#updateNetworkCameraWirelessProfile_0) | **PUT** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Update an existing camera wireless profile in this network.
[**updateNetworkCellularGatewayConnectivityMonitoringDestinations_0**](ConfigureApi.md#updateNetworkCellularGatewayConnectivityMonitoringDestinations_0) | **PUT** /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MG network
[**updateNetworkCellularGatewayDhcp_0**](ConfigureApi.md#updateNetworkCellularGatewayDhcp_0) | **PUT** /networks/{networkId}/cellularGateway/dhcp | Update common DHCP settings of MGs
[**updateNetworkCellularGatewaySubnetPool_0**](ConfigureApi.md#updateNetworkCellularGatewaySubnetPool_0) | **PUT** /networks/{networkId}/cellularGateway/subnetPool | Update the subnet pool and mask configuration for MGs in the network.
[**updateNetworkCellularGatewayUplink_0**](ConfigureApi.md#updateNetworkCellularGatewayUplink_0) | **PUT** /networks/{networkId}/cellularGateway/uplink | Updates the uplink settings for your MG network.
[**updateNetworkClientPolicy_0**](ConfigureApi.md#updateNetworkClientPolicy_0) | **PUT** /networks/{networkId}/clients/{clientId}/policy | Update the policy assigned to a client on the network
[**updateNetworkClientSplashAuthorizationStatus_0**](ConfigureApi.md#updateNetworkClientSplashAuthorizationStatus_0) | **PUT** /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus | Update a client&#39;s splash authorization
[**updateNetworkFirmwareUpgradesStagedEvents_0**](ConfigureApi.md#updateNetworkFirmwareUpgradesStagedEvents_0) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/events | Update the Staged Upgrade Event for a network
[**updateNetworkFirmwareUpgradesStagedGroup_0**](ConfigureApi.md#updateNetworkFirmwareUpgradesStagedGroup_0) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network
[**updateNetworkFirmwareUpgradesStagedStages_0**](ConfigureApi.md#updateNetworkFirmwareUpgradesStagedStages_0) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence.
[**updateNetworkFirmwareUpgrades_0**](ConfigureApi.md#updateNetworkFirmwareUpgrades_0) | **PUT** /networks/{networkId}/firmwareUpgrades | Update firmware upgrade information for a network
[**updateNetworkFloorPlan_0**](ConfigureApi.md#updateNetworkFloorPlan_0) | **PUT** /networks/{networkId}/floorPlans/{floorPlanId} | Update a floor plan&#39;s geolocation and other meta data
[**updateNetworkGroupPolicy_0**](ConfigureApi.md#updateNetworkGroupPolicy_0) | **PUT** /networks/{networkId}/groupPolicies/{groupPolicyId} | Update a group policy
[**updateNetworkMerakiAuthUser_0**](ConfigureApi.md#updateNetworkMerakiAuthUser_0) | **PUT** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)
[**updateNetworkMqttBroker_0**](ConfigureApi.md#updateNetworkMqttBroker_0) | **PUT** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Update an MQTT broker
[**updateNetworkNetflow_0**](ConfigureApi.md#updateNetworkNetflow_0) | **PUT** /networks/{networkId}/netflow | Update the NetFlow traffic reporting settings for a network
[**updateNetworkSensorAlertsProfile_0**](ConfigureApi.md#updateNetworkSensorAlertsProfile_0) | **PUT** /networks/{networkId}/sensor/alerts/profiles/{id} | Updates a sensor alert profile for a network.
[**updateNetworkSettings_0**](ConfigureApi.md#updateNetworkSettings_0) | **PUT** /networks/{networkId}/settings | Update the settings for a network
[**updateNetworkSmDevicesFields_0**](ConfigureApi.md#updateNetworkSmDevicesFields_0) | **PUT** /networks/{networkId}/sm/devices/fields | Modify the fields of a device
[**updateNetworkSmTargetGroup_0**](ConfigureApi.md#updateNetworkSmTargetGroup_0) | **PUT** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Update a target group
[**updateNetworkSnmp_0**](ConfigureApi.md#updateNetworkSnmp_0) | **PUT** /networks/{networkId}/snmp | Update the SNMP settings for a network
[**updateNetworkSwitchAccessControlLists_0**](ConfigureApi.md#updateNetworkSwitchAccessControlLists_0) | **PUT** /networks/{networkId}/switch/accessControlLists | Update the access control lists for a MS network
[**updateNetworkSwitchAccessPolicy_0**](ConfigureApi.md#updateNetworkSwitchAccessPolicy_0) | **PUT** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Update an access policy for a switch network
[**updateNetworkSwitchAlternateManagementInterface_0**](ConfigureApi.md#updateNetworkSwitchAlternateManagementInterface_0) | **PUT** /networks/{networkId}/switch/alternateManagementInterface | Update the switch alternate management interface for the network
[**updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0**](ConfigureApi.md#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Update a server that is trusted by Dynamic ARP Inspection on this network
[**updateNetworkSwitchDhcpServerPolicy_0**](ConfigureApi.md#updateNetworkSwitchDhcpServerPolicy_0) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy | Update the DHCP server settings
[**updateNetworkSwitchDscpToCosMappings_0**](ConfigureApi.md#updateNetworkSwitchDscpToCosMappings_0) | **PUT** /networks/{networkId}/switch/dscpToCosMappings | Update the DSCP to CoS mappings
[**updateNetworkSwitchLinkAggregation_0**](ConfigureApi.md#updateNetworkSwitchLinkAggregation_0) | **PUT** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Update a link aggregation group
[**updateNetworkSwitchMtu_0**](ConfigureApi.md#updateNetworkSwitchMtu_0) | **PUT** /networks/{networkId}/switch/mtu | Update the MTU configuration
[**updateNetworkSwitchPortSchedule_0**](ConfigureApi.md#updateNetworkSwitchPortSchedule_0) | **PUT** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Update a switch port schedule
[**updateNetworkSwitchQosRule_0**](ConfigureApi.md#updateNetworkSwitchQosRule_0) | **PUT** /networks/{networkId}/switch/qosRules/{qosRuleId} | Update a quality of service rule
[**updateNetworkSwitchQosRulesOrder_0**](ConfigureApi.md#updateNetworkSwitchQosRulesOrder_0) | **PUT** /networks/{networkId}/switch/qosRules/order | Update the order in which the rules should be processed by the switch
[**updateNetworkSwitchRoutingMulticastRendezvousPoint_0**](ConfigureApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint_0) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point
[**updateNetworkSwitchRoutingMulticast_0**](ConfigureApi.md#updateNetworkSwitchRoutingMulticast_0) | **PUT** /networks/{networkId}/switch/routing/multicast | Update multicast settings for a network
[**updateNetworkSwitchRoutingOspf_0**](ConfigureApi.md#updateNetworkSwitchRoutingOspf_0) | **PUT** /networks/{networkId}/switch/routing/ospf | Update layer 3 OSPF routing configuration
[**updateNetworkSwitchSettings_0**](ConfigureApi.md#updateNetworkSwitchSettings_0) | **PUT** /networks/{networkId}/switch/settings | Update switch network settings
[**updateNetworkSwitchStackRoutingInterfaceDhcp_0**](ConfigureApi.md#updateNetworkSwitchStackRoutingInterfaceDhcp_0) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch stack
[**updateNetworkSwitchStackRoutingInterface_0**](ConfigureApi.md#updateNetworkSwitchStackRoutingInterface_0) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch stack
[**updateNetworkSwitchStackRoutingStaticRoute_0**](ConfigureApi.md#updateNetworkSwitchStackRoutingStaticRoute_0) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch stack
[**updateNetworkSwitchStormControl_0**](ConfigureApi.md#updateNetworkSwitchStormControl_0) | **PUT** /networks/{networkId}/switch/stormControl | Update the storm control configuration for a switch network
[**updateNetworkSwitchStp_0**](ConfigureApi.md#updateNetworkSwitchStp_0) | **PUT** /networks/{networkId}/switch/stp | Updates STP settings
[**updateNetworkSyslogServers_0**](ConfigureApi.md#updateNetworkSyslogServers_0) | **PUT** /networks/{networkId}/syslogServers | Update the syslog servers for a network
[**updateNetworkTrafficAnalysis_0**](ConfigureApi.md#updateNetworkTrafficAnalysis_0) | **PUT** /networks/{networkId}/trafficAnalysis | Update the traffic analysis settings for a network
[**updateNetworkWebhooksHttpServer_0**](ConfigureApi.md#updateNetworkWebhooksHttpServer_0) | **PUT** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Update an HTTP server
[**updateNetworkWebhooksPayloadTemplate_0**](ConfigureApi.md#updateNetworkWebhooksPayloadTemplate_0) | **PUT** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Update a webhook payload template for a network
[**updateNetworkWirelessAlternateManagementInterface_0**](ConfigureApi.md#updateNetworkWirelessAlternateManagementInterface_0) | **PUT** /networks/{networkId}/wireless/alternateManagementInterface | Update alternate management interface and device static IP
[**updateNetworkWirelessBilling_0**](ConfigureApi.md#updateNetworkWirelessBilling_0) | **PUT** /networks/{networkId}/wireless/billing | Update the billing settings
[**updateNetworkWirelessBluetoothSettings_0**](ConfigureApi.md#updateNetworkWirelessBluetoothSettings_0) | **PUT** /networks/{networkId}/wireless/bluetooth/settings | Update the Bluetooth settings for a network
[**updateNetworkWirelessRfProfile_0**](ConfigureApi.md#updateNetworkWirelessRfProfile_0) | **PUT** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Updates specified RF profile for this network
[**updateNetworkWirelessSettings_0**](ConfigureApi.md#updateNetworkWirelessSettings_0) | **PUT** /networks/{networkId}/wireless/settings | Update the wireless settings for a network
[**updateNetworkWirelessSsidBonjourForwarding_0**](ConfigureApi.md#updateNetworkWirelessSsidBonjourForwarding_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | Update the bonjour forwarding setting and rules for the SSID
[**updateNetworkWirelessSsidDeviceTypeGroupPolicies_0**](ConfigureApi.md#updateNetworkWirelessSsidDeviceTypeGroupPolicies_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | Update the device type group policies for the SSID
[**updateNetworkWirelessSsidEapOverride_0**](ConfigureApi.md#updateNetworkWirelessSsidEapOverride_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Update the EAP overridden parameters for an SSID.
[**updateNetworkWirelessSsidFirewallL3FirewallRules_0**](ConfigureApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network
[**updateNetworkWirelessSsidFirewallL7FirewallRules_0**](ConfigureApi.md#updateNetworkWirelessSsidFirewallL7FirewallRules_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Update the L7 firewall rules of an SSID on an MR network
[**updateNetworkWirelessSsidHotspot20_0**](ConfigureApi.md#updateNetworkWirelessSsidHotspot20_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Update the Hotspot 2.0 settings of an SSID
[**updateNetworkWirelessSsidIdentityPsk_0**](ConfigureApi.md#updateNetworkWirelessSsidIdentityPsk_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Update an Identity PSK
[**updateNetworkWirelessSsidSchedules_0**](ConfigureApi.md#updateNetworkWirelessSsidSchedules_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/schedules | Update the outage schedule for the SSID
[**updateNetworkWirelessSsidSplashSettings_0**](ConfigureApi.md#updateNetworkWirelessSsidSplashSettings_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Modify the splash page settings for the given SSID
[**updateNetworkWirelessSsidTrafficShapingRules_0**](ConfigureApi.md#updateNetworkWirelessSsidTrafficShapingRules_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Update the traffic shaping settings for an SSID on an MR network
[**updateNetworkWirelessSsidVpn_0**](ConfigureApi.md#updateNetworkWirelessSsidVpn_0) | **PUT** /networks/{networkId}/wireless/ssids/{number}/vpn | Update the VPN settings for the SSID
[**updateNetworkWirelessSsid_0**](ConfigureApi.md#updateNetworkWirelessSsid_0) | **PUT** /networks/{networkId}/wireless/ssids/{number} | Update the attributes of an MR SSID
[**updateNetwork_0**](ConfigureApi.md#updateNetwork_0) | **PUT** /networks/{networkId} | Update a network
[**updateOrganizationActionBatch_0**](ConfigureApi.md#updateOrganizationActionBatch_0) | **PUT** /organizations/{organizationId}/actionBatches/{actionBatchId} | Update an action batch
[**updateOrganizationAdaptivePolicyAcl_0**](ConfigureApi.md#updateOrganizationAdaptivePolicyAcl_0) | **PUT** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Updates an adaptive policy ACL
[**updateOrganizationAdaptivePolicyGroup_0**](ConfigureApi.md#updateOrganizationAdaptivePolicyGroup_0) | **PUT** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Updates an adaptive policy group
[**updateOrganizationAdaptivePolicyPolicy_0**](ConfigureApi.md#updateOrganizationAdaptivePolicyPolicy_0) | **PUT** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Update an Adaptive Policy
[**updateOrganizationAdaptivePolicySettings_0**](ConfigureApi.md#updateOrganizationAdaptivePolicySettings_0) | **PUT** /organizations/{organizationId}/adaptivePolicy/settings | Update global adaptive policy settings
[**updateOrganizationAdmin_0**](ConfigureApi.md#updateOrganizationAdmin_0) | **PUT** /organizations/{organizationId}/admins/{adminId} | Update an administrator
[**updateOrganizationAlertsProfile_0**](ConfigureApi.md#updateOrganizationAlertsProfile_0) | **PUT** /organizations/{organizationId}/alerts/profiles/{alertConfigId} | Update an organization-wide alert config
[**updateOrganizationApplianceSecurityIntrusion_0**](ConfigureApi.md#updateOrganizationApplianceSecurityIntrusion_0) | **PUT** /organizations/{organizationId}/appliance/security/intrusion | Sets supported intrusion settings for an organization
[**updateOrganizationApplianceVpnThirdPartyVPNPeers_0**](ConfigureApi.md#updateOrganizationApplianceVpnThirdPartyVPNPeers_0) | **PUT** /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers | Update the third party VPN peers for an organization
[**updateOrganizationApplianceVpnVpnFirewallRules_0**](ConfigureApi.md#updateOrganizationApplianceVpnVpnFirewallRules_0) | **PUT** /organizations/{organizationId}/appliance/vpn/vpnFirewallRules | Update the firewall rules of an organization&#39;s site-to-site VPN
[**updateOrganizationBrandingPoliciesPriorities_0**](ConfigureApi.md#updateOrganizationBrandingPoliciesPriorities_0) | **PUT** /organizations/{organizationId}/brandingPolicies/priorities | Update the priority ordering of an organization&#39;s branding policies.
[**updateOrganizationBrandingPolicy_0**](ConfigureApi.md#updateOrganizationBrandingPolicy_0) | **PUT** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Update a branding policy
[**updateOrganizationCameraOnboardingStatuses_0**](ConfigureApi.md#updateOrganizationCameraOnboardingStatuses_0) | **PUT** /organizations/{organizationId}/camera/onboarding/statuses | Notify that credential handoff to camera has completed
[**updateOrganizationConfigTemplateSwitchProfilePort_0**](ConfigureApi.md#updateOrganizationConfigTemplateSwitchProfilePort_0) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Update a switch profile port
[**updateOrganizationConfigTemplate_0**](ConfigureApi.md#updateOrganizationConfigTemplate_0) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId} | Update a configuration template
[**updateOrganizationEarlyAccessFeaturesOptIn_0**](ConfigureApi.md#updateOrganizationEarlyAccessFeaturesOptIn_0) | **PUT** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Update an early access feature opt-in for an organization
[**updateOrganizationInsightMonitoredMediaServer_0**](ConfigureApi.md#updateOrganizationInsightMonitoredMediaServer_0) | **PUT** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Update a monitored media server for this organization
[**updateOrganizationLicense_0**](ConfigureApi.md#updateOrganizationLicense_0) | **PUT** /organizations/{organizationId}/licenses/{licenseId} | Update a license
[**updateOrganizationLoginSecurity_0**](ConfigureApi.md#updateOrganizationLoginSecurity_0) | **PUT** /organizations/{organizationId}/loginSecurity | Update the login security settings for an organization
[**updateOrganizationPolicyObject_0**](ConfigureApi.md#updateOrganizationPolicyObject_0) | **PUT** /organizations/{organizationId}/policyObjects/{policyObjectId} | Updates a Policy Object.
[**updateOrganizationPolicyObjectsGroup_0**](ConfigureApi.md#updateOrganizationPolicyObjectsGroup_0) | **PUT** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Updates a Policy Object Group.
[**updateOrganizationSamlIdp_0**](ConfigureApi.md#updateOrganizationSamlIdp_0) | **PUT** /organizations/{organizationId}/saml/idps/{idpId} | Update a SAML IdP in your organization
[**updateOrganizationSamlRole_0**](ConfigureApi.md#updateOrganizationSamlRole_0) | **PUT** /organizations/{organizationId}/samlRoles/{samlRoleId} | Update a SAML role
[**updateOrganizationSaml_0**](ConfigureApi.md#updateOrganizationSaml_0) | **PUT** /organizations/{organizationId}/saml | Updates the SAML SSO enabled settings for an organization.
[**updateOrganizationSnmp_0**](ConfigureApi.md#updateOrganizationSnmp_0) | **PUT** /organizations/{organizationId}/snmp | Update the SNMP settings for an organization
[**updateOrganization_0**](ConfigureApi.md#updateOrganization_0) | **PUT** /organizations/{organizationId} | Update an organization
[**vmxNetworkDevicesClaim_0**](ConfigureApi.md#vmxNetworkDevicesClaim_0) | **POST** /networks/{networkId}/devices/claim/vmx | Claim a vMX into a network
[**wipeNetworkSmDevices_0**](ConfigureApi.md#wipeNetworkSmDevices_0) | **POST** /networks/{networkId}/sm/devices/wipe | Wipe a device



## addNetworkSwitchStack_0

> Object addNetworkSwitchStack_0(networkId, switchStackId, addNetworkSwitchStackRequest)

Add a switch to a stack

Add a switch to a stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let addNetworkSwitchStackRequest = new MerakiDashboardApi.AddNetworkSwitchStackRequest(); // AddNetworkSwitchStackRequest | 
apiInstance.addNetworkSwitchStack_0(networkId, switchStackId, addNetworkSwitchStackRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **addNetworkSwitchStackRequest** | [**AddNetworkSwitchStackRequest**](AddNetworkSwitchStackRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assignOrganizationLicensesSeats_0

> AssignOrganizationLicensesSeats200Response assignOrganizationLicensesSeats_0(organizationId, assignOrganizationLicensesSeatsRequest)

Assign SM seats to a network

Assign SM seats to a network. This will increase the managed SM device limit of the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let assignOrganizationLicensesSeatsRequest = new MerakiDashboardApi.AssignOrganizationLicensesSeatsRequest(); // AssignOrganizationLicensesSeatsRequest | 
apiInstance.assignOrganizationLicensesSeats_0(organizationId, assignOrganizationLicensesSeatsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **assignOrganizationLicensesSeatsRequest** | [**AssignOrganizationLicensesSeatsRequest**](AssignOrganizationLicensesSeatsRequest.md)|  | 

### Return type

[**AssignOrganizationLicensesSeats200Response**](AssignOrganizationLicensesSeats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bindNetwork_0

> Object bindNetwork_0(networkId, bindNetworkRequest)

Bind a network to a template.

Bind a network to a template.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let bindNetworkRequest = new MerakiDashboardApi.BindNetworkRequest(); // BindNetworkRequest | 
apiInstance.bindNetwork_0(networkId, bindNetworkRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **bindNetworkRequest** | [**BindNetworkRequest**](BindNetworkRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkinNetworkSmDevices_0

> CheckinNetworkSmDevices200Response checkinNetworkSmDevices_0(networkId, opts)

Force check-in a set of devices

Force check-in a set of devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'checkinNetworkSmDevicesRequest': new MerakiDashboardApi.CheckinNetworkSmDevicesRequest() // CheckinNetworkSmDevicesRequest | 
};
apiInstance.checkinNetworkSmDevices_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **checkinNetworkSmDevicesRequest** | [**CheckinNetworkSmDevicesRequest**](CheckinNetworkSmDevicesRequest.md)|  | [optional] 

### Return type

[**CheckinNetworkSmDevices200Response**](CheckinNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## claimIntoOrganizationInventory_0

> Object claimIntoOrganizationInventory_0(organizationId, opts)

Claim a list of devices, licenses, and/or orders into an organization inventory

Claim a list of devices, licenses, and/or orders into an organization inventory. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory. Use /organizations/{organizationId}/inventory/release to release devices from an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'claimIntoOrganizationInventoryRequest': new MerakiDashboardApi.ClaimIntoOrganizationInventoryRequest() // ClaimIntoOrganizationInventoryRequest | 
};
apiInstance.claimIntoOrganizationInventory_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **claimIntoOrganizationInventoryRequest** | [**ClaimIntoOrganizationInventoryRequest**](ClaimIntoOrganizationInventoryRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## claimIntoOrganization_0

> Object claimIntoOrganization_0(organizationId, opts)

Claim a list of devices, licenses, and/or orders into an organization

Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'claimIntoOrganizationRequest': new MerakiDashboardApi.ClaimIntoOrganizationRequest() // ClaimIntoOrganizationRequest | 
};
apiInstance.claimIntoOrganization_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **claimIntoOrganizationRequest** | [**ClaimIntoOrganizationRequest**](ClaimIntoOrganizationRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## claimNetworkDevices_0

> claimNetworkDevices_0(networkId, claimNetworkDevicesRequest)

Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let claimNetworkDevicesRequest = new MerakiDashboardApi.ClaimNetworkDevicesRequest(); // ClaimNetworkDevicesRequest | 
apiInstance.claimNetworkDevices_0(networkId, claimNetworkDevicesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **claimNetworkDevicesRequest** | [**ClaimNetworkDevicesRequest**](ClaimNetworkDevicesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## cloneOrganizationSwitchDevices_0

> Object cloneOrganizationSwitchDevices_0(organizationId, cloneOrganizationSwitchDevicesRequest)

Clone port-level and some switch-level configuration settings from a source switch to one or more target switches

Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let cloneOrganizationSwitchDevicesRequest = new MerakiDashboardApi.CloneOrganizationSwitchDevicesRequest(); // CloneOrganizationSwitchDevicesRequest | 
apiInstance.cloneOrganizationSwitchDevices_0(organizationId, cloneOrganizationSwitchDevicesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **cloneOrganizationSwitchDevicesRequest** | [**CloneOrganizationSwitchDevicesRequest**](CloneOrganizationSwitchDevicesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloneOrganization_0

> GetOrganizations200ResponseInner cloneOrganization_0(organizationId, cloneOrganizationRequest)

Create a new organization by cloning the addressed organization

Create a new organization by cloning the addressed organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let cloneOrganizationRequest = new MerakiDashboardApi.CloneOrganizationRequest(); // CloneOrganizationRequest | 
apiInstance.cloneOrganization_0(organizationId, cloneOrganizationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **cloneOrganizationRequest** | [**CloneOrganizationRequest**](CloneOrganizationRequest.md)|  | 

### Return type

[**GetOrganizations200ResponseInner**](GetOrganizations200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## combineOrganizationNetworks_0

> CombineOrganizationNetworks200Response combineOrganizationNetworks_0(organizationId, combineOrganizationNetworksRequest)

Combine multiple networks into a single network

Combine multiple networks into a single network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let combineOrganizationNetworksRequest = new MerakiDashboardApi.CombineOrganizationNetworksRequest(); // CombineOrganizationNetworksRequest | 
apiInstance.combineOrganizationNetworks_0(organizationId, combineOrganizationNetworksRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **combineOrganizationNetworksRequest** | [**CombineOrganizationNetworksRequest**](CombineOrganizationNetworksRequest.md)|  | 

### Return type

[**CombineOrganizationNetworks200Response**](CombineOrganizationNetworks200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeviceApplianceVmxAuthenticationToken_0

> CreateDeviceApplianceVmxAuthenticationToken201Response createDeviceApplianceVmxAuthenticationToken_0(serial)

Generate a new vMX authentication token

Generate a new vMX authentication token

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.createDeviceApplianceVmxAuthenticationToken_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**CreateDeviceApplianceVmxAuthenticationToken201Response**](CreateDeviceApplianceVmxAuthenticationToken201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDeviceSwitchRoutingInterface_0

> GetDeviceSwitchRoutingInterfaces200ResponseInner createDeviceSwitchRoutingInterface_0(serial, opts)

Create a layer 3 interface for a switch

Create a layer 3 interface for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'createDeviceSwitchRoutingInterfaceRequest': new MerakiDashboardApi.CreateDeviceSwitchRoutingInterfaceRequest() // CreateDeviceSwitchRoutingInterfaceRequest | 
};
apiInstance.createDeviceSwitchRoutingInterface_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **createDeviceSwitchRoutingInterfaceRequest** | [**CreateDeviceSwitchRoutingInterfaceRequest**](CreateDeviceSwitchRoutingInterfaceRequest.md)|  | [optional] 

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeviceSwitchRoutingStaticRoute_0

> Object createDeviceSwitchRoutingStaticRoute_0(serial, createDeviceSwitchRoutingStaticRouteRequest)

Create a layer 3 static route for a switch

Create a layer 3 static route for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let createDeviceSwitchRoutingStaticRouteRequest = new MerakiDashboardApi.CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
apiInstance.createDeviceSwitchRoutingStaticRoute_0(serial, createDeviceSwitchRoutingStaticRouteRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **createDeviceSwitchRoutingStaticRouteRequest** | [**CreateDeviceSwitchRoutingStaticRouteRequest**](CreateDeviceSwitchRoutingStaticRouteRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkAppliancePrefixesDelegatedStatic_0

> Object createNetworkAppliancePrefixesDelegatedStatic_0(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest)

Add a static delegated prefix from a network

Add a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkAppliancePrefixesDelegatedStaticRequest = new MerakiDashboardApi.CreateNetworkAppliancePrefixesDelegatedStaticRequest(); // CreateNetworkAppliancePrefixesDelegatedStaticRequest | 
apiInstance.createNetworkAppliancePrefixesDelegatedStatic_0(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkAppliancePrefixesDelegatedStaticRequest** | [**CreateNetworkAppliancePrefixesDelegatedStaticRequest**](CreateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkApplianceStaticRoute_0

> Object createNetworkApplianceStaticRoute_0(networkId, createNetworkApplianceStaticRouteRequest)

Add a static route for an MX or teleworker network

Add a static route for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkApplianceStaticRouteRequest = new MerakiDashboardApi.CreateNetworkApplianceStaticRouteRequest(); // CreateNetworkApplianceStaticRouteRequest | 
apiInstance.createNetworkApplianceStaticRoute_0(networkId, createNetworkApplianceStaticRouteRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkApplianceStaticRouteRequest** | [**CreateNetworkApplianceStaticRouteRequest**](CreateNetworkApplianceStaticRouteRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkApplianceTrafficShapingCustomPerformanceClass_0

> Object createNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

Add a custom performance class for an MX network

Add a custom performance class for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new MerakiDashboardApi.CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
apiInstance.createNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkApplianceVlan_0

> CreateNetworkApplianceVlan201Response createNetworkApplianceVlan_0(networkId, createNetworkApplianceVlanRequest)

Add a VLAN

Add a VLAN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkApplianceVlanRequest = new MerakiDashboardApi.CreateNetworkApplianceVlanRequest(); // CreateNetworkApplianceVlanRequest | 
apiInstance.createNetworkApplianceVlan_0(networkId, createNetworkApplianceVlanRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkApplianceVlanRequest** | [**CreateNetworkApplianceVlanRequest**](CreateNetworkApplianceVlanRequest.md)|  | 

### Return type

[**CreateNetworkApplianceVlan201Response**](CreateNetworkApplianceVlan201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkCameraQualityRetentionProfile_0

> Object createNetworkCameraQualityRetentionProfile_0(networkId, createNetworkCameraQualityRetentionProfileRequest)

Creates new quality retention profile for this network.

Creates new quality retention profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkCameraQualityRetentionProfileRequest = new MerakiDashboardApi.CreateNetworkCameraQualityRetentionProfileRequest(); // CreateNetworkCameraQualityRetentionProfileRequest | 
apiInstance.createNetworkCameraQualityRetentionProfile_0(networkId, createNetworkCameraQualityRetentionProfileRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkCameraQualityRetentionProfileRequest** | [**CreateNetworkCameraQualityRetentionProfileRequest**](CreateNetworkCameraQualityRetentionProfileRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkCameraWirelessProfile_0

> Object createNetworkCameraWirelessProfile_0(networkId, createNetworkCameraWirelessProfileRequest)

Creates a new camera wireless profile for this network.

Creates a new camera wireless profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkCameraWirelessProfileRequest = new MerakiDashboardApi.CreateNetworkCameraWirelessProfileRequest(); // CreateNetworkCameraWirelessProfileRequest | 
apiInstance.createNetworkCameraWirelessProfile_0(networkId, createNetworkCameraWirelessProfileRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkCameraWirelessProfileRequest** | [**CreateNetworkCameraWirelessProfileRequest**](CreateNetworkCameraWirelessProfileRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkFirmwareUpgradesRollback_0

> CreateNetworkFirmwareUpgradesRollback200Response createNetworkFirmwareUpgradesRollback_0(networkId, createNetworkFirmwareUpgradesRollbackRequest)

Rollback a Firmware Upgrade For A Network

Rollback a Firmware Upgrade For A Network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesRollbackRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesRollbackRequest(); // CreateNetworkFirmwareUpgradesRollbackRequest | 
apiInstance.createNetworkFirmwareUpgradesRollback_0(networkId, createNetworkFirmwareUpgradesRollbackRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkFirmwareUpgradesRollbackRequest** | [**CreateNetworkFirmwareUpgradesRollbackRequest**](CreateNetworkFirmwareUpgradesRollbackRequest.md)|  | 

### Return type

[**CreateNetworkFirmwareUpgradesRollback200Response**](CreateNetworkFirmwareUpgradesRollback200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkFirmwareUpgradesStagedEvent_0

> GetNetworkFirmwareUpgradesStagedEvents200Response createNetworkFirmwareUpgradesStagedEvent_0(networkId, createNetworkFirmwareUpgradesStagedEventRequest)

Create a Staged Upgrade Event for a network

Create a Staged Upgrade Event for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedEventRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedEventRequest(); // CreateNetworkFirmwareUpgradesStagedEventRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedEvent_0(networkId, createNetworkFirmwareUpgradesStagedEventRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkFirmwareUpgradesStagedEventRequest** | [**CreateNetworkFirmwareUpgradesStagedEventRequest**](CreateNetworkFirmwareUpgradesStagedEventRequest.md)|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkFirmwareUpgradesStagedGroup_0

> Object createNetworkFirmwareUpgradesStagedGroup_0(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

Create a Staged Upgrade Group for a network

Create a Staged Upgrade Group for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedGroup_0(networkId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkFloorPlan_0

> Object createNetworkFloorPlan_0(networkId, createNetworkFloorPlanRequest)

Upload a floor plan

Upload a floor plan

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkFloorPlanRequest = new MerakiDashboardApi.CreateNetworkFloorPlanRequest(); // CreateNetworkFloorPlanRequest | 
apiInstance.createNetworkFloorPlan_0(networkId, createNetworkFloorPlanRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkFloorPlanRequest** | [**CreateNetworkFloorPlanRequest**](CreateNetworkFloorPlanRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkGroupPolicy_0

> Object createNetworkGroupPolicy_0(networkId, createNetworkGroupPolicyRequest)

Create a group policy

Create a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkGroupPolicyRequest = new MerakiDashboardApi.CreateNetworkGroupPolicyRequest(); // CreateNetworkGroupPolicyRequest | 
apiInstance.createNetworkGroupPolicy_0(networkId, createNetworkGroupPolicyRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkGroupPolicyRequest** | [**CreateNetworkGroupPolicyRequest**](CreateNetworkGroupPolicyRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkMerakiAuthUser_0

> GetNetworkMerakiAuthUsers200ResponseInner createNetworkMerakiAuthUser_0(networkId, createNetworkMerakiAuthUserRequest)

Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkMerakiAuthUserRequest = new MerakiDashboardApi.CreateNetworkMerakiAuthUserRequest(); // CreateNetworkMerakiAuthUserRequest | 
apiInstance.createNetworkMerakiAuthUser_0(networkId, createNetworkMerakiAuthUserRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkMerakiAuthUserRequest** | [**CreateNetworkMerakiAuthUserRequest**](CreateNetworkMerakiAuthUserRequest.md)|  | 

### Return type

[**GetNetworkMerakiAuthUsers200ResponseInner**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkMqttBroker_0

> Object createNetworkMqttBroker_0(networkId, createNetworkMqttBrokerRequest)

Add an MQTT broker

Add an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkMqttBrokerRequest = new MerakiDashboardApi.CreateNetworkMqttBrokerRequest(); // CreateNetworkMqttBrokerRequest | 
apiInstance.createNetworkMqttBroker_0(networkId, createNetworkMqttBrokerRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkMqttBrokerRequest** | [**CreateNetworkMqttBrokerRequest**](CreateNetworkMqttBrokerRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkPiiRequest_0

> Object createNetworkPiiRequest_0(networkId, opts)

Submit a new delete or restrict processing PII request

Submit a new delete or restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'createNetworkPiiRequestRequest': new MerakiDashboardApi.CreateNetworkPiiRequestRequest() // CreateNetworkPiiRequestRequest | 
};
apiInstance.createNetworkPiiRequest_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkPiiRequestRequest** | [**CreateNetworkPiiRequestRequest**](CreateNetworkPiiRequestRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSensorAlertsProfile_0

> GetNetworkSensorAlertsProfiles200ResponseInner createNetworkSensorAlertsProfile_0(networkId, createNetworkSensorAlertsProfileRequest)

Creates a sensor alert profile for a network.

Creates a sensor alert profile for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSensorAlertsProfileRequest = new MerakiDashboardApi.CreateNetworkSensorAlertsProfileRequest(); // CreateNetworkSensorAlertsProfileRequest | 
apiInstance.createNetworkSensorAlertsProfile_0(networkId, createNetworkSensorAlertsProfileRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSensorAlertsProfileRequest** | [**CreateNetworkSensorAlertsProfileRequest**](CreateNetworkSensorAlertsProfileRequest.md)|  | 

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSmBypassActivationLockAttempt_0

> Object createNetworkSmBypassActivationLockAttempt_0(networkId, createNetworkSmBypassActivationLockAttemptRequest)

Bypass activation lock attempt

Bypass activation lock attempt

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSmBypassActivationLockAttemptRequest = new MerakiDashboardApi.CreateNetworkSmBypassActivationLockAttemptRequest(); // CreateNetworkSmBypassActivationLockAttemptRequest | 
apiInstance.createNetworkSmBypassActivationLockAttempt_0(networkId, createNetworkSmBypassActivationLockAttemptRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSmBypassActivationLockAttemptRequest** | [**CreateNetworkSmBypassActivationLockAttemptRequest**](CreateNetworkSmBypassActivationLockAttemptRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSmTargetGroup_0

> Object createNetworkSmTargetGroup_0(networkId, opts)

Add a target group

Add a target group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'createNetworkSmTargetGroupRequest': new MerakiDashboardApi.CreateNetworkSmTargetGroupRequest() // CreateNetworkSmTargetGroupRequest | 
};
apiInstance.createNetworkSmTargetGroup_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSmTargetGroupRequest** | [**CreateNetworkSmTargetGroupRequest**](CreateNetworkSmTargetGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchAccessPolicy_0

> GetNetworkSwitchAccessPolicies200ResponseInner createNetworkSwitchAccessPolicy_0(networkId, createNetworkSwitchAccessPolicyRequest)

Create an access policy for a switch network

Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchAccessPolicyRequest = new MerakiDashboardApi.CreateNetworkSwitchAccessPolicyRequest(); // CreateNetworkSwitchAccessPolicyRequest | 
apiInstance.createNetworkSwitchAccessPolicy_0(networkId, createNetworkSwitchAccessPolicyRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchAccessPolicyRequest** | [**CreateNetworkSwitchAccessPolicyRequest**](CreateNetworkSwitchAccessPolicyRequest.md)|  | 

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0

> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

Add a server to be trusted by Dynamic ARP Inspection on this network

Add a server to be trusted by Dynamic ARP Inspection on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new MerakiDashboardApi.CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
apiInstance.createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest** | [**CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest**](CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.md)|  | 

### Return type

[**GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchLinkAggregation_0

> Object createNetworkSwitchLinkAggregation_0(networkId, opts)

Create a link aggregation group

Create a link aggregation group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'createNetworkSwitchLinkAggregationRequest': new MerakiDashboardApi.CreateNetworkSwitchLinkAggregationRequest() // CreateNetworkSwitchLinkAggregationRequest | 
};
apiInstance.createNetworkSwitchLinkAggregation_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchLinkAggregationRequest** | [**CreateNetworkSwitchLinkAggregationRequest**](CreateNetworkSwitchLinkAggregationRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchPortSchedule_0

> Object createNetworkSwitchPortSchedule_0(networkId, createNetworkSwitchPortScheduleRequest)

Add a switch port schedule

Add a switch port schedule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchPortScheduleRequest = new MerakiDashboardApi.CreateNetworkSwitchPortScheduleRequest(); // CreateNetworkSwitchPortScheduleRequest | 
apiInstance.createNetworkSwitchPortSchedule_0(networkId, createNetworkSwitchPortScheduleRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchPortScheduleRequest** | [**CreateNetworkSwitchPortScheduleRequest**](CreateNetworkSwitchPortScheduleRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchQosRule_0

> Object createNetworkSwitchQosRule_0(networkId, createNetworkSwitchQosRuleRequest)

Add a quality of service rule

Add a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchQosRuleRequest = new MerakiDashboardApi.CreateNetworkSwitchQosRuleRequest(); // CreateNetworkSwitchQosRuleRequest | 
apiInstance.createNetworkSwitchQosRule_0(networkId, createNetworkSwitchQosRuleRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchQosRuleRequest** | [**CreateNetworkSwitchQosRuleRequest**](CreateNetworkSwitchQosRuleRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchRoutingMulticastRendezvousPoint_0

> Object createNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

Create a multicast rendezvous point

Create a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchRoutingMulticastRendezvousPointRequest = new MerakiDashboardApi.CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**CreateNetworkSwitchRoutingMulticastRendezvousPointRequest**](CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchStackRoutingInterface_0

> Object createNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest)

Create a layer 3 interface for a switch stack

Create a layer 3 interface for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let createNetworkSwitchStackRoutingInterfaceRequest = new MerakiDashboardApi.CreateNetworkSwitchStackRoutingInterfaceRequest(); // CreateNetworkSwitchStackRoutingInterfaceRequest | 
apiInstance.createNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **createNetworkSwitchStackRoutingInterfaceRequest** | [**CreateNetworkSwitchStackRoutingInterfaceRequest**](CreateNetworkSwitchStackRoutingInterfaceRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchStackRoutingStaticRoute_0

> Object createNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest)

Create a layer 3 static route for a switch stack

Create a layer 3 static route for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let createDeviceSwitchRoutingStaticRouteRequest = new MerakiDashboardApi.CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
apiInstance.createNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **createDeviceSwitchRoutingStaticRouteRequest** | [**CreateDeviceSwitchRoutingStaticRouteRequest**](CreateDeviceSwitchRoutingStaticRouteRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkSwitchStack_0

> Object createNetworkSwitchStack_0(networkId, createNetworkSwitchStackRequest)

Create a stack

Create a stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchStackRequest = new MerakiDashboardApi.CreateNetworkSwitchStackRequest(); // CreateNetworkSwitchStackRequest | 
apiInstance.createNetworkSwitchStack_0(networkId, createNetworkSwitchStackRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkSwitchStackRequest** | [**CreateNetworkSwitchStackRequest**](CreateNetworkSwitchStackRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkWebhooksHttpServer_0

> GetNetworkWebhooksHttpServers200ResponseInner createNetworkWebhooksHttpServer_0(networkId, createNetworkWebhooksHttpServerRequest)

Add an HTTP server to a network

Add an HTTP server to a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkWebhooksHttpServerRequest = new MerakiDashboardApi.CreateNetworkWebhooksHttpServerRequest(); // CreateNetworkWebhooksHttpServerRequest | 
apiInstance.createNetworkWebhooksHttpServer_0(networkId, createNetworkWebhooksHttpServerRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkWebhooksHttpServerRequest** | [**CreateNetworkWebhooksHttpServerRequest**](CreateNetworkWebhooksHttpServerRequest.md)|  | 

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkWebhooksPayloadTemplate_0

> GetNetworkWebhooksPayloadTemplates200ResponseInner createNetworkWebhooksPayloadTemplate_0(networkId, createNetworkWebhooksPayloadTemplateRequest)

Create a webhook payload template for a network

Create a webhook payload template for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkWebhooksPayloadTemplateRequest = new MerakiDashboardApi.CreateNetworkWebhooksPayloadTemplateRequest(); // CreateNetworkWebhooksPayloadTemplateRequest | 
apiInstance.createNetworkWebhooksPayloadTemplate_0(networkId, createNetworkWebhooksPayloadTemplateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkWebhooksPayloadTemplateRequest** | [**CreateNetworkWebhooksPayloadTemplateRequest**](CreateNetworkWebhooksPayloadTemplateRequest.md)|  | 

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkWebhooksWebhookTest_0

> CreateNetworkWebhooksWebhookTest201Response createNetworkWebhooksWebhookTest_0(networkId, createNetworkWebhooksWebhookTestRequest)

Send a test webhook for a network

Send a test webhook for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkWebhooksWebhookTestRequest = new MerakiDashboardApi.CreateNetworkWebhooksWebhookTestRequest(); // CreateNetworkWebhooksWebhookTestRequest | 
apiInstance.createNetworkWebhooksWebhookTest_0(networkId, createNetworkWebhooksWebhookTestRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkWebhooksWebhookTestRequest** | [**CreateNetworkWebhooksWebhookTestRequest**](CreateNetworkWebhooksWebhookTestRequest.md)|  | 

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkWirelessRfProfile_0

> CreateNetworkWirelessRfProfile201Response createNetworkWirelessRfProfile_0(networkId, createNetworkWirelessRfProfileRequest)

Creates new RF profile for this network

Creates new RF profile for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let createNetworkWirelessRfProfileRequest = new MerakiDashboardApi.CreateNetworkWirelessRfProfileRequest(); // CreateNetworkWirelessRfProfileRequest | 
apiInstance.createNetworkWirelessRfProfile_0(networkId, createNetworkWirelessRfProfileRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkWirelessRfProfileRequest** | [**CreateNetworkWirelessRfProfileRequest**](CreateNetworkWirelessRfProfileRequest.md)|  | 

### Return type

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkWirelessSsidIdentityPsk_0

> Object createNetworkWirelessSsidIdentityPsk_0(networkId, number, createNetworkWirelessSsidIdentityPskRequest)

Create an Identity PSK

Create an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let createNetworkWirelessSsidIdentityPskRequest = new MerakiDashboardApi.CreateNetworkWirelessSsidIdentityPskRequest(); // CreateNetworkWirelessSsidIdentityPskRequest | 
apiInstance.createNetworkWirelessSsidIdentityPsk_0(networkId, number, createNetworkWirelessSsidIdentityPskRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **createNetworkWirelessSsidIdentityPskRequest** | [**CreateNetworkWirelessSsidIdentityPskRequest**](CreateNetworkWirelessSsidIdentityPskRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationActionBatch_0

> CreateOrganizationActionBatch201Response createOrganizationActionBatch_0(organizationId, createOrganizationActionBatchRequest)

Create an action batch

Create an action batch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationActionBatchRequest = new MerakiDashboardApi.CreateOrganizationActionBatchRequest(); // CreateOrganizationActionBatchRequest | 
apiInstance.createOrganizationActionBatch_0(organizationId, createOrganizationActionBatchRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationActionBatchRequest** | [**CreateOrganizationActionBatchRequest**](CreateOrganizationActionBatchRequest.md)|  | 

### Return type

[**CreateOrganizationActionBatch201Response**](CreateOrganizationActionBatch201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdaptivePolicyAcl_0

> Object createOrganizationAdaptivePolicyAcl_0(organizationId, createOrganizationAdaptivePolicyAclRequest)

Creates new adaptive policy ACL

Creates new adaptive policy ACL

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyAclRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyAclRequest(); // CreateOrganizationAdaptivePolicyAclRequest | 
apiInstance.createOrganizationAdaptivePolicyAcl_0(organizationId, createOrganizationAdaptivePolicyAclRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationAdaptivePolicyAclRequest** | [**CreateOrganizationAdaptivePolicyAclRequest**](CreateOrganizationAdaptivePolicyAclRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdaptivePolicyGroup_0

> Object createOrganizationAdaptivePolicyGroup_0(organizationId, createOrganizationAdaptivePolicyGroupRequest)

Creates a new adaptive policy group

Creates a new adaptive policy group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyGroupRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyGroupRequest(); // CreateOrganizationAdaptivePolicyGroupRequest | 
apiInstance.createOrganizationAdaptivePolicyGroup_0(organizationId, createOrganizationAdaptivePolicyGroupRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationAdaptivePolicyGroupRequest** | [**CreateOrganizationAdaptivePolicyGroupRequest**](CreateOrganizationAdaptivePolicyGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdaptivePolicyPolicy_0

> Object createOrganizationAdaptivePolicyPolicy_0(organizationId, createOrganizationAdaptivePolicyPolicyRequest)

Add an Adaptive Policy

Add an Adaptive Policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyPolicyRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyPolicyRequest(); // CreateOrganizationAdaptivePolicyPolicyRequest | 
apiInstance.createOrganizationAdaptivePolicyPolicy_0(organizationId, createOrganizationAdaptivePolicyPolicyRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationAdaptivePolicyPolicyRequest** | [**CreateOrganizationAdaptivePolicyPolicyRequest**](CreateOrganizationAdaptivePolicyPolicyRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdmin_0

> Object createOrganizationAdmin_0(organizationId, createOrganizationAdminRequest)

Create a new dashboard administrator

Create a new dashboard administrator

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdminRequest = new MerakiDashboardApi.CreateOrganizationAdminRequest(); // CreateOrganizationAdminRequest | 
apiInstance.createOrganizationAdmin_0(organizationId, createOrganizationAdminRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationAdminRequest** | [**CreateOrganizationAdminRequest**](CreateOrganizationAdminRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAlertsProfile_0

> Object createOrganizationAlertsProfile_0(organizationId, createOrganizationAlertsProfileRequest)

Create an organization-wide alert configuration

Create an organization-wide alert configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAlertsProfileRequest = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequest(); // CreateOrganizationAlertsProfileRequest | 
apiInstance.createOrganizationAlertsProfile_0(organizationId, createOrganizationAlertsProfileRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationAlertsProfileRequest** | [**CreateOrganizationAlertsProfileRequest**](CreateOrganizationAlertsProfileRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationBrandingPolicy_0

> CreateOrganizationBrandingPolicy201Response createOrganizationBrandingPolicy_0(organizationId, opts)

Add a new branding policy to an organization

Add a new branding policy to an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'createOrganizationBrandingPolicyRequest': new MerakiDashboardApi.CreateOrganizationBrandingPolicyRequest() // CreateOrganizationBrandingPolicyRequest | 
};
apiInstance.createOrganizationBrandingPolicy_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationBrandingPolicyRequest** | [**CreateOrganizationBrandingPolicyRequest**](CreateOrganizationBrandingPolicyRequest.md)|  | [optional] 

### Return type

[**CreateOrganizationBrandingPolicy201Response**](CreateOrganizationBrandingPolicy201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationCameraCustomAnalyticsArtifact_0

> Object createOrganizationCameraCustomAnalyticsArtifact_0(organizationId, opts)

Create custom analytics artifact

Create custom analytics artifact. Returns an artifact upload URL with expiry time. Upload the artifact file with a put request to the returned upload URL before its expiry.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'createOrganizationCameraCustomAnalyticsArtifactRequest': new MerakiDashboardApi.CreateOrganizationCameraCustomAnalyticsArtifactRequest() // CreateOrganizationCameraCustomAnalyticsArtifactRequest | 
};
apiInstance.createOrganizationCameraCustomAnalyticsArtifact_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationCameraCustomAnalyticsArtifactRequest** | [**CreateOrganizationCameraCustomAnalyticsArtifactRequest**](CreateOrganizationCameraCustomAnalyticsArtifactRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationConfigTemplate_0

> Object createOrganizationConfigTemplate_0(organizationId, createOrganizationConfigTemplateRequest)

Create a new configuration template

Create a new configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationConfigTemplateRequest = new MerakiDashboardApi.CreateOrganizationConfigTemplateRequest(); // CreateOrganizationConfigTemplateRequest | 
apiInstance.createOrganizationConfigTemplate_0(organizationId, createOrganizationConfigTemplateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationConfigTemplateRequest** | [**CreateOrganizationConfigTemplateRequest**](CreateOrganizationConfigTemplateRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationEarlyAccessFeaturesOptIn_0

> Object createOrganizationEarlyAccessFeaturesOptIn_0(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest)

Create a new early access feature opt-in for an organization

Create a new early access feature opt-in for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationEarlyAccessFeaturesOptInRequest = new MerakiDashboardApi.CreateOrganizationEarlyAccessFeaturesOptInRequest(); // CreateOrganizationEarlyAccessFeaturesOptInRequest | 
apiInstance.createOrganizationEarlyAccessFeaturesOptIn_0(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationEarlyAccessFeaturesOptInRequest** | [**CreateOrganizationEarlyAccessFeaturesOptInRequest**](CreateOrganizationEarlyAccessFeaturesOptInRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationInsightMonitoredMediaServer_0

> Object createOrganizationInsightMonitoredMediaServer_0(organizationId, createOrganizationInsightMonitoredMediaServerRequest)

Add a media server to be monitored for this organization

Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInsightMonitoredMediaServerRequest = new MerakiDashboardApi.CreateOrganizationInsightMonitoredMediaServerRequest(); // CreateOrganizationInsightMonitoredMediaServerRequest | 
apiInstance.createOrganizationInsightMonitoredMediaServer_0(organizationId, createOrganizationInsightMonitoredMediaServerRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationInsightMonitoredMediaServerRequest** | [**CreateOrganizationInsightMonitoredMediaServerRequest**](CreateOrganizationInsightMonitoredMediaServerRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationInventoryOnboardingCloudMonitoringExportEvent_0

> Object createOrganizationInventoryOnboardingCloudMonitoringExportEvent_0(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest)

Imports event logs related to the onboarding app into elastisearch

Imports event logs related to the onboarding app into elastisearch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_0(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationInventoryOnboardingCloudMonitoringImport_0

> [CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner] createOrganizationInventoryOnboardingCloudMonitoringImport_0(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest)

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringImportRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringImport_0(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationInventoryOnboardingCloudMonitoringImportRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.md)|  | 

### Return type

[**[CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner]**](CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationInventoryOnboardingCloudMonitoringPrepare_0

> [CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner] createOrganizationInventoryOnboardingCloudMonitoringPrepare_0(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest)

Initiates or updates an import session

Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringPrepare_0(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.md)|  | 

### Return type

[**[CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner]**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationNetwork_0

> GetNetwork200Response createOrganizationNetwork_0(organizationId, createOrganizationNetworkRequest)

Create a network

Create a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationNetworkRequest = new MerakiDashboardApi.CreateOrganizationNetworkRequest(); // CreateOrganizationNetworkRequest | 
apiInstance.createOrganizationNetwork_0(organizationId, createOrganizationNetworkRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationNetworkRequest** | [**CreateOrganizationNetworkRequest**](CreateOrganizationNetworkRequest.md)|  | 

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationPolicyObject_0

> Object createOrganizationPolicyObject_0(organizationId, createOrganizationPolicyObjectRequest)

Creates a new Policy Object.

Creates a new Policy Object.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationPolicyObjectRequest = new MerakiDashboardApi.CreateOrganizationPolicyObjectRequest(); // CreateOrganizationPolicyObjectRequest | 
apiInstance.createOrganizationPolicyObject_0(organizationId, createOrganizationPolicyObjectRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationPolicyObjectRequest** | [**CreateOrganizationPolicyObjectRequest**](CreateOrganizationPolicyObjectRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationPolicyObjectsGroup_0

> Object createOrganizationPolicyObjectsGroup_0(organizationId, createOrganizationPolicyObjectsGroupRequest)

Creates a new Policy Object Group.

Creates a new Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationPolicyObjectsGroupRequest = new MerakiDashboardApi.CreateOrganizationPolicyObjectsGroupRequest(); // CreateOrganizationPolicyObjectsGroupRequest | 
apiInstance.createOrganizationPolicyObjectsGroup_0(organizationId, createOrganizationPolicyObjectsGroupRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationPolicyObjectsGroupRequest** | [**CreateOrganizationPolicyObjectsGroupRequest**](CreateOrganizationPolicyObjectsGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationSamlIdp_0

> [GetOrganizationSamlIdps200ResponseInner] createOrganizationSamlIdp_0(organizationId, createOrganizationSamlIdpRequest)

Create a SAML IdP for your organization.

Create a SAML IdP for your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationSamlIdpRequest = new MerakiDashboardApi.CreateOrganizationSamlIdpRequest(); // CreateOrganizationSamlIdpRequest | 
apiInstance.createOrganizationSamlIdp_0(organizationId, createOrganizationSamlIdpRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationSamlIdpRequest** | [**CreateOrganizationSamlIdpRequest**](CreateOrganizationSamlIdpRequest.md)|  | 

### Return type

[**[GetOrganizationSamlIdps200ResponseInner]**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationSamlRole_0

> Object createOrganizationSamlRole_0(organizationId, createOrganizationSamlRoleRequest)

Create a SAML role

Create a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationSamlRoleRequest = new MerakiDashboardApi.CreateOrganizationSamlRoleRequest(); // CreateOrganizationSamlRoleRequest | 
apiInstance.createOrganizationSamlRole_0(organizationId, createOrganizationSamlRoleRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **createOrganizationSamlRoleRequest** | [**CreateOrganizationSamlRoleRequest**](CreateOrganizationSamlRoleRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganization_0

> GetOrganizations200ResponseInner createOrganization_0(createOrganizationRequest)

Create a new organization

Create a new organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let createOrganizationRequest = new MerakiDashboardApi.CreateOrganizationRequest(); // CreateOrganizationRequest | 
apiInstance.createOrganization_0(createOrganizationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createOrganizationRequest** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

### Return type

[**GetOrganizations200ResponseInner**](GetOrganizations200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deferNetworkFirmwareUpgradesStagedEvents_0

> GetNetworkFirmwareUpgradesStagedEvents200Response deferNetworkFirmwareUpgradesStagedEvents_0(networkId)

Postpone by 1 week all pending staged upgrade stages for a network

Postpone by 1 week all pending staged upgrade stages for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.deferNetworkFirmwareUpgradesStagedEvents_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDeviceSwitchRoutingInterface_0

> deleteDeviceSwitchRoutingInterface_0(serial, interfaceId)

Delete a layer 3 interface from the switch

Delete a layer 3 interface from the switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
apiInstance.deleteDeviceSwitchRoutingInterface_0(serial, interfaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **interfaceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDeviceSwitchRoutingStaticRoute_0

> deleteDeviceSwitchRoutingStaticRoute_0(serial, staticRouteId)

Delete a layer 3 static route for a switch

Delete a layer 3 static route for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.deleteDeviceSwitchRoutingStaticRoute_0(serial, staticRouteId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkAppliancePrefixesDelegatedStatic_0

> deleteNetworkAppliancePrefixesDelegatedStatic_0(networkId, staticDelegatedPrefixId)

Delete a static delegated prefix from a network

Delete a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
apiInstance.deleteNetworkAppliancePrefixesDelegatedStatic_0(networkId, staticDelegatedPrefixId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **staticDelegatedPrefixId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkApplianceStaticRoute_0

> deleteNetworkApplianceStaticRoute_0(networkId, staticRouteId)

Delete a static route from an MX or teleworker network

Delete a static route from an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.deleteNetworkApplianceStaticRoute_0(networkId, staticRouteId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkApplianceTrafficShapingCustomPerformanceClass_0

> deleteNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, customPerformanceClassId)

Delete a custom performance class from an MX network

Delete a custom performance class from an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let customPerformanceClassId = "customPerformanceClassId_example"; // String | 
apiInstance.deleteNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, customPerformanceClassId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **customPerformanceClassId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkApplianceVlan_0

> deleteNetworkApplianceVlan_0(networkId, vlanId)

Delete a VLAN from a network

Delete a VLAN from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let vlanId = "vlanId_example"; // String | 
apiInstance.deleteNetworkApplianceVlan_0(networkId, vlanId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **vlanId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkCameraQualityRetentionProfile_0

> deleteNetworkCameraQualityRetentionProfile_0(networkId, qualityRetentionProfileId)

Delete an existing quality retention profile for this network.

Delete an existing quality retention profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
apiInstance.deleteNetworkCameraQualityRetentionProfile_0(networkId, qualityRetentionProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **qualityRetentionProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkCameraWirelessProfile_0

> deleteNetworkCameraWirelessProfile_0(networkId, wirelessProfileId)

Delete an existing camera wireless profile for this network.

Delete an existing camera wireless profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let wirelessProfileId = "wirelessProfileId_example"; // String | 
apiInstance.deleteNetworkCameraWirelessProfile_0(networkId, wirelessProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **wirelessProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkFirmwareUpgradesStagedGroup_0

> deleteNetworkFirmwareUpgradesStagedGroup_0(networkId, groupId)

Delete a Staged Upgrade Group

Delete a Staged Upgrade Group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.deleteNetworkFirmwareUpgradesStagedGroup_0(networkId, groupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkFloorPlan_0

> deleteNetworkFloorPlan_0(networkId, floorPlanId)

Destroy a floor plan

Destroy a floor plan

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let floorPlanId = "floorPlanId_example"; // String | 
apiInstance.deleteNetworkFloorPlan_0(networkId, floorPlanId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **floorPlanId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroupPolicy_0

> deleteNetworkGroupPolicy_0(networkId, groupPolicyId)

Delete a group policy

Delete a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let groupPolicyId = "groupPolicyId_example"; // String | 
apiInstance.deleteNetworkGroupPolicy_0(networkId, groupPolicyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **groupPolicyId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkMerakiAuthUser_0

> deleteNetworkMerakiAuthUser_0(networkId, merakiAuthUserId)

Deauthorize a user

Deauthorize a user. To reauthorize a user after deauthorizing them, POST to this endpoint. (Currently, 802.1X RADIUS, splash guest, and client VPN users can be deauthorized.)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let merakiAuthUserId = "merakiAuthUserId_example"; // String | 
apiInstance.deleteNetworkMerakiAuthUser_0(networkId, merakiAuthUserId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **merakiAuthUserId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkMqttBroker_0

> deleteNetworkMqttBroker_0(networkId, mqttBrokerId)

Delete an MQTT broker

Delete an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let mqttBrokerId = "mqttBrokerId_example"; // String | 
apiInstance.deleteNetworkMqttBroker_0(networkId, mqttBrokerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **mqttBrokerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkPiiRequest_0

> deleteNetworkPiiRequest_0(networkId, requestId)

Delete a restrict processing PII request

Delete a restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let requestId = "requestId_example"; // String | 
apiInstance.deleteNetworkPiiRequest_0(networkId, requestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **requestId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSensorAlertsProfile_0

> deleteNetworkSensorAlertsProfile_0(networkId, id)

Deletes a sensor alert profile from a network.

Deletes a sensor alert profile from a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteNetworkSensorAlertsProfile_0(networkId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSmTargetGroup_0

> deleteNetworkSmTargetGroup_0(networkId, targetGroupId)

Delete a target group from a network

Delete a target group from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let targetGroupId = "targetGroupId_example"; // String | 
apiInstance.deleteNetworkSmTargetGroup_0(networkId, targetGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **targetGroupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSmUserAccessDevice_0

> deleteNetworkSmUserAccessDevice_0(networkId, userAccessDeviceId)

Delete a User Access Device

Delete a User Access Device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let userAccessDeviceId = "userAccessDeviceId_example"; // String | 
apiInstance.deleteNetworkSmUserAccessDevice_0(networkId, userAccessDeviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **userAccessDeviceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchAccessPolicy_0

> deleteNetworkSwitchAccessPolicy_0(networkId, accessPolicyNumber)

Delete an access policy for a switch network

Delete an access policy for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let accessPolicyNumber = "accessPolicyNumber_example"; // String | 
apiInstance.deleteNetworkSwitchAccessPolicy_0(networkId, accessPolicyNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **accessPolicyNumber** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0

> deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0(networkId, trustedServerId)

Remove a server from being trusted by Dynamic ARP Inspection on this network

Remove a server from being trusted by Dynamic ARP Inspection on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let trustedServerId = "trustedServerId_example"; // String | 
apiInstance.deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0(networkId, trustedServerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **trustedServerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchLinkAggregation_0

> deleteNetworkSwitchLinkAggregation_0(networkId, linkAggregationId)

Split a link aggregation group into separate ports

Split a link aggregation group into separate ports

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let linkAggregationId = "linkAggregationId_example"; // String | 
apiInstance.deleteNetworkSwitchLinkAggregation_0(networkId, linkAggregationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **linkAggregationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchPortSchedule_0

> deleteNetworkSwitchPortSchedule_0(networkId, portScheduleId)

Delete a switch port schedule

Delete a switch port schedule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let portScheduleId = "portScheduleId_example"; // String | 
apiInstance.deleteNetworkSwitchPortSchedule_0(networkId, portScheduleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **portScheduleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchQosRule_0

> deleteNetworkSwitchQosRule_0(networkId, qosRuleId)

Delete a quality of service rule

Delete a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let qosRuleId = "qosRuleId_example"; // String | 
apiInstance.deleteNetworkSwitchQosRule_0(networkId, qosRuleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **qosRuleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchRoutingMulticastRendezvousPoint_0

> deleteNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, rendezvousPointId)

Delete a multicast rendezvous point

Delete a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, rendezvousPointId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rendezvousPointId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchStackRoutingInterface_0

> deleteNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, interfaceId)

Delete a layer 3 interface from a switch stack

Delete a layer 3 interface from a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
apiInstance.deleteNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, interfaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **interfaceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchStackRoutingStaticRoute_0

> deleteNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, staticRouteId)

Delete a layer 3 static route for a switch stack

Delete a layer 3 static route for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.deleteNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, staticRouteId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkSwitchStack_0

> deleteNetworkSwitchStack_0(networkId, switchStackId)

Delete a stack

Delete a stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
apiInstance.deleteNetworkSwitchStack_0(networkId, switchStackId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkWebhooksHttpServer_0

> deleteNetworkWebhooksHttpServer_0(networkId, httpServerId)

Delete an HTTP server from a network

Delete an HTTP server from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let httpServerId = "httpServerId_example"; // String | 
apiInstance.deleteNetworkWebhooksHttpServer_0(networkId, httpServerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **httpServerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkWebhooksPayloadTemplate_0

> deleteNetworkWebhooksPayloadTemplate_0(networkId, payloadTemplateId)

Destroy a webhook payload template for a network

Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let payloadTemplateId = "payloadTemplateId_example"; // String | 
apiInstance.deleteNetworkWebhooksPayloadTemplate_0(networkId, payloadTemplateId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **payloadTemplateId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkWirelessRfProfile_0

> deleteNetworkWirelessRfProfile_0(networkId, rfProfileId)

Delete a RF Profile

Delete a RF Profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
apiInstance.deleteNetworkWirelessRfProfile_0(networkId, rfProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rfProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkWirelessSsidIdentityPsk_0

> deleteNetworkWirelessSsidIdentityPsk_0(networkId, number, identityPskId)

Delete an Identity PSK

Delete an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let identityPskId = "identityPskId_example"; // String | 
apiInstance.deleteNetworkWirelessSsidIdentityPsk_0(networkId, number, identityPskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **identityPskId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetwork_0

> deleteNetwork_0(networkId)

Delete a network

Delete a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.deleteNetwork_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationActionBatch_0

> deleteOrganizationActionBatch_0(organizationId, actionBatchId)

Delete an action batch

Delete an action batch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let actionBatchId = "actionBatchId_example"; // String | 
apiInstance.deleteOrganizationActionBatch_0(organizationId, actionBatchId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **actionBatchId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdaptivePolicyAcl_0

> deleteOrganizationAdaptivePolicyAcl_0(organizationId, aclId)

Deletes the specified adaptive policy ACL

Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyAcl_0(organizationId, aclId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **aclId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdaptivePolicyGroup_0

> deleteOrganizationAdaptivePolicyGroup_0(organizationId, id)

Deletes the specified adaptive policy group and any associated policies and references

Deletes the specified adaptive policy group and any associated policies and references

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyGroup_0(organizationId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdaptivePolicyPolicy_0

> deleteOrganizationAdaptivePolicyPolicy_0(organizationId, id)

Delete an Adaptive Policy

Delete an Adaptive Policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyPolicy_0(organizationId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdmin_0

> deleteOrganizationAdmin_0(organizationId, adminId)

Revoke all access for a dashboard administrator within this organization

Revoke all access for a dashboard administrator within this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let adminId = "adminId_example"; // String | 
apiInstance.deleteOrganizationAdmin_0(organizationId, adminId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **adminId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAlertsProfile_0

> deleteOrganizationAlertsProfile_0(organizationId, alertConfigId)

Removes an organization-wide alert config

Removes an organization-wide alert config

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let alertConfigId = "alertConfigId_example"; // String | 
apiInstance.deleteOrganizationAlertsProfile_0(organizationId, alertConfigId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **alertConfigId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationBrandingPolicy_0

> deleteOrganizationBrandingPolicy_0(organizationId, brandingPolicyId)

Delete a branding policy

Delete a branding policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let brandingPolicyId = "brandingPolicyId_example"; // String | 
apiInstance.deleteOrganizationBrandingPolicy_0(organizationId, brandingPolicyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **brandingPolicyId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationCameraCustomAnalyticsArtifact_0

> deleteOrganizationCameraCustomAnalyticsArtifact_0(organizationId, artifactId)

Delete Custom Analytics Artifact

Delete Custom Analytics Artifact

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let artifactId = "artifactId_example"; // String | 
apiInstance.deleteOrganizationCameraCustomAnalyticsArtifact_0(organizationId, artifactId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **artifactId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationConfigTemplate_0

> deleteOrganizationConfigTemplate_0(organizationId, configTemplateId)

Remove a configuration template

Remove a configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
apiInstance.deleteOrganizationConfigTemplate_0(organizationId, configTemplateId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationEarlyAccessFeaturesOptIn_0

> deleteOrganizationEarlyAccessFeaturesOptIn_0(organizationId, optInId)

Delete an early access feature opt-in

Delete an early access feature opt-in

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let optInId = "optInId_example"; // String | 
apiInstance.deleteOrganizationEarlyAccessFeaturesOptIn_0(organizationId, optInId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **optInId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationInsightMonitoredMediaServer_0

> deleteOrganizationInsightMonitoredMediaServer_0(organizationId, monitoredMediaServerId)

Delete a monitored media server from this organization

Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
apiInstance.deleteOrganizationInsightMonitoredMediaServer_0(organizationId, monitoredMediaServerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **monitoredMediaServerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationPolicyObject_0

> deleteOrganizationPolicyObject_0(organizationId, policyObjectId)

Deletes a Policy Object.

Deletes a Policy Object.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectId = "policyObjectId_example"; // String | 
apiInstance.deleteOrganizationPolicyObject_0(organizationId, policyObjectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **policyObjectId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationPolicyObjectsGroup_0

> deleteOrganizationPolicyObjectsGroup_0(organizationId, policyObjectGroupId)

Deletes a Policy Object Group.

Deletes a Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectGroupId = "policyObjectGroupId_example"; // String | 
apiInstance.deleteOrganizationPolicyObjectsGroup_0(organizationId, policyObjectGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **policyObjectGroupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationSamlIdp_0

> deleteOrganizationSamlIdp_0(organizationId, idpId)

Remove a SAML IdP in your organization.

Remove a SAML IdP in your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let idpId = "idpId_example"; // String | 
apiInstance.deleteOrganizationSamlIdp_0(organizationId, idpId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **idpId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationSamlRole_0

> deleteOrganizationSamlRole_0(organizationId, samlRoleId)

Remove a SAML role

Remove a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
apiInstance.deleteOrganizationSamlRole_0(organizationId, samlRoleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **samlRoleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationUser_0

> deleteOrganizationUser_0(organizationId, userId)

Delete a user and all of its authentication methods.

Delete a user and all of its authentication methods.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.deleteOrganizationUser_0(organizationId, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganization_0

> deleteOrganization_0(organizationId)

Delete an organization

Delete an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.deleteOrganization_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeviceApplianceUplinksSettings_0

> GetDeviceApplianceUplinksSettings200Response getDeviceApplianceUplinksSettings_0(serial)

Return the uplink settings for an MX appliance

Return the uplink settings for an MX appliance

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceApplianceUplinksSettings_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraCustomAnalytics_0

> Object getDeviceCameraCustomAnalytics_0(serial)

Return custom analytics settings for a camera

Return custom analytics settings for a camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraCustomAnalytics_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraQualityAndRetention_0

> Object getDeviceCameraQualityAndRetention_0(serial)

Returns quality and retention settings for the given camera

Returns quality and retention settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraQualityAndRetention_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraSenseObjectDetectionModels_0

> [Object] getDeviceCameraSenseObjectDetectionModels_0(serial)

Returns the MV Sense object detection model list for the given camera

Returns the MV Sense object detection model list for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraSenseObjectDetectionModels_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraSense_0

> Object getDeviceCameraSense_0(serial)

Returns sense settings for a given camera

Returns sense settings for a given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraSense_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraVideoLink_0

> Object getDeviceCameraVideoLink_0(serial, opts)

Returns video link to the specified camera

Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'timestamp': new Date("2013-10-20T19:20:30+01:00") // Date | [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
};
apiInstance.getDeviceCameraVideoLink_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **timestamp** | **Date**| [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraVideoSettings_0

> Object getDeviceCameraVideoSettings_0(serial)

Returns video settings for the given camera

Returns video settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraVideoSettings_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraWirelessProfiles_0

> Object getDeviceCameraWirelessProfiles_0(serial)

Returns wireless profile assigned to the given camera

Returns wireless profile assigned to the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraWirelessProfiles_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCellularGatewayLan_0

> Object getDeviceCellularGatewayLan_0(serial)

Show the LAN Settings of a MG

Show the LAN Settings of a MG

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularGatewayLan_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCellularGatewayPortForwardingRules_0

> Object getDeviceCellularGatewayPortForwardingRules_0(serial)

Returns the port forwarding rules for a single MG.

Returns the port forwarding rules for a single MG.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularGatewayPortForwardingRules_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCellularSims_0

> Object getDeviceCellularSims_0(serial)

Return the SIM and APN configurations for a cellular device.

Return the SIM and APN configurations for a cellular device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularSims_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceManagementInterface_0

> Object getDeviceManagementInterface_0(serial)

Return the management interface settings for a device

Return the management interface settings for a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceManagementInterface_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSensorRelationships_0

> [GetDeviceSensorRelationships200ResponseInner] getDeviceSensorRelationships_0(serial)

List the sensor roles for a given sensor or camera device.

List the sensor roles for a given sensor or camera device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSensorRelationships_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**[GetDeviceSensorRelationships200ResponseInner]**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchPort_0

> GetDeviceSwitchPorts200ResponseInner getDeviceSwitchPort_0(serial, portId)

Return a switch port

Return a switch port

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let portId = "portId_example"; // String | 
apiInstance.getDeviceSwitchPort_0(serial, portId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **portId** | **String**|  | 

### Return type

[**GetDeviceSwitchPorts200ResponseInner**](GetDeviceSwitchPorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchPorts_0

> [GetDeviceSwitchPorts200ResponseInner] getDeviceSwitchPorts_0(serial)

List the switch ports for a switch

List the switch ports for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSwitchPorts_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**[GetDeviceSwitchPorts200ResponseInner]**](GetDeviceSwitchPorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchRoutingInterfaceDhcp_0

> Object getDeviceSwitchRoutingInterfaceDhcp_0(serial, interfaceId)

Return a layer 3 interface DHCP configuration for a switch

Return a layer 3 interface DHCP configuration for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
apiInstance.getDeviceSwitchRoutingInterfaceDhcp_0(serial, interfaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **interfaceId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchRoutingInterface_0

> GetDeviceSwitchRoutingInterfaces200ResponseInner getDeviceSwitchRoutingInterface_0(serial, interfaceId)

Return a layer 3 interface for a switch

Return a layer 3 interface for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
apiInstance.getDeviceSwitchRoutingInterface_0(serial, interfaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **interfaceId** | **String**|  | 

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchRoutingInterfaces_0

> [GetDeviceSwitchRoutingInterfaces200ResponseInner] getDeviceSwitchRoutingInterfaces_0(serial)

List layer 3 interfaces for a switch

List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSwitchRoutingInterfaces_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**[GetDeviceSwitchRoutingInterfaces200ResponseInner]**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchRoutingStaticRoute_0

> GetDeviceSwitchRoutingStaticRoute200Response getDeviceSwitchRoutingStaticRoute_0(serial, staticRouteId)

Return a layer 3 static route for a switch

Return a layer 3 static route for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.getDeviceSwitchRoutingStaticRoute_0(serial, staticRouteId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

[**GetDeviceSwitchRoutingStaticRoute200Response**](GetDeviceSwitchRoutingStaticRoute200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchRoutingStaticRoutes_0

> [Object] getDeviceSwitchRoutingStaticRoutes_0(serial)

List layer 3 static routes for a switch

List layer 3 static routes for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSwitchRoutingStaticRoutes_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceSwitchWarmSpare_0

> Object getDeviceSwitchWarmSpare_0(serial)

Return warm spare configuration for a switch

Return warm spare configuration for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSwitchWarmSpare_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceWirelessBluetoothSettings_0

> GetDeviceWirelessBluetoothSettings200Response getDeviceWirelessBluetoothSettings_0(serial)

Return the bluetooth settings for a wireless device

Return the bluetooth settings for a wireless device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceWirelessBluetoothSettings_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceWirelessRadioSettings_0

> Object getDeviceWirelessRadioSettings_0(serial)

Return the radio settings of a device

Return the radio settings of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceWirelessRadioSettings_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDevice_0

> Object getDevice_0(serial)

Return a single device

Return a single device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
apiInstance.getDevice_0(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAlertsSettings_0

> Object getNetworkAlertsSettings_0(networkId)

Return the alert configuration for this network

Return the alert configuration for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkAlertsSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceConnectivityMonitoringDestinations_0

> Object getNetworkApplianceConnectivityMonitoringDestinations_0(networkId)

Return the connectivity testing destinations for an MX network

Return the connectivity testing destinations for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceConnectivityMonitoringDestinations_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceContentFilteringCategories_0

> Object getNetworkApplianceContentFilteringCategories_0(networkId)

List all available content filtering categories for an MX network

List all available content filtering categories for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceContentFilteringCategories_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceContentFiltering_0

> Object getNetworkApplianceContentFiltering_0(networkId)

Return the content filtering settings for an MX network

Return the content filtering settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceContentFiltering_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallCellularFirewallRules_0

> Object getNetworkApplianceFirewallCellularFirewallRules_0(networkId)

Return the cellular firewall rules for an MX network

Return the cellular firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallCellularFirewallRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallFirewalledService_0

> Object getNetworkApplianceFirewallFirewalledService_0(networkId, service)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let service = "service_example"; // String | 
apiInstance.getNetworkApplianceFirewallFirewalledService_0(networkId, service, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **service** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallFirewalledServices_0

> [Object] getNetworkApplianceFirewallFirewalledServices_0(networkId)

List the appliance services and their accessibility rules

List the appliance services and their accessibility rules

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallFirewalledServices_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallInboundCellularFirewallRules_0

> [Object] getNetworkApplianceFirewallInboundCellularFirewallRules_0(networkId)

Return the inbound cellular firewall rules for an MX network

Return the inbound cellular firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallInboundCellularFirewallRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallInboundFirewallRules_0

> Object getNetworkApplianceFirewallInboundFirewallRules_0(networkId)

Return the inbound firewall rules for an MX network

Return the inbound firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallInboundFirewallRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallL3FirewallRules_0

> Object getNetworkApplianceFirewallL3FirewallRules_0(networkId)

Return the L3 firewall rules for an MX network

Return the L3 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL3FirewallRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_0

> Object getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_0(networkId)

Return the L7 firewall application categories and their associated applications for an MX network

Return the L7 firewall application categories and their associated applications for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallL7FirewallRules_0

> Object getNetworkApplianceFirewallL7FirewallRules_0(networkId)

List the MX L7 firewall rules for an MX network

List the MX L7 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL7FirewallRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallOneToManyNatRules_0

> Object getNetworkApplianceFirewallOneToManyNatRules_0(networkId)

Return the 1:Many NAT mapping rules for an MX network

Return the 1:Many NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallOneToManyNatRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallOneToOneNatRules_0

> Object getNetworkApplianceFirewallOneToOneNatRules_0(networkId)

Return the 1:1 NAT mapping rules for an MX network

Return the 1:1 NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallOneToOneNatRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallPortForwardingRules_0

> Object getNetworkApplianceFirewallPortForwardingRules_0(networkId)

Return the port forwarding rules for an MX network

Return the port forwarding rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallPortForwardingRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallSettings_0

> Object getNetworkApplianceFirewallSettings_0(networkId)

Return the firewall settings for this network

Return the firewall settings for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePort_0

> GetNetworkAppliancePorts200ResponseInner getNetworkAppliancePort_0(networkId, portId)

Return per-port VLAN settings for a single MX port.

Return per-port VLAN settings for a single MX port.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let portId = "portId_example"; // String | 
apiInstance.getNetworkAppliancePort_0(networkId, portId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **portId** | **String**|  | 

### Return type

[**GetNetworkAppliancePorts200ResponseInner**](GetNetworkAppliancePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePorts_0

> [GetNetworkAppliancePorts200ResponseInner] getNetworkAppliancePorts_0(networkId)

List per-port VLAN settings for all ports of a MX.

List per-port VLAN settings for all ports of a MX.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkAppliancePorts_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkAppliancePorts200ResponseInner]**](GetNetworkAppliancePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePrefixesDelegatedStatic_0

> GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner getNetworkAppliancePrefixesDelegatedStatic_0(networkId, staticDelegatedPrefixId)

Return a static delegated prefix from a network

Return a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
apiInstance.getNetworkAppliancePrefixesDelegatedStatic_0(networkId, staticDelegatedPrefixId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **staticDelegatedPrefixId** | **String**|  | 

### Return type

[**GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePrefixesDelegatedStatics_0

> [GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner] getNetworkAppliancePrefixesDelegatedStatics_0(networkId)

List static delegated prefixes for a network

List static delegated prefixes for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkAppliancePrefixesDelegatedStatics_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner]**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceSecurityIntrusion_0

> Object getNetworkApplianceSecurityIntrusion_0(networkId)

Returns all supported intrusion settings for an MX network

Returns all supported intrusion settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceSecurityIntrusion_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceSecurityMalware_0

> Object getNetworkApplianceSecurityMalware_0(networkId)

Returns all supported malware settings for an MX network

Returns all supported malware settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceSecurityMalware_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceSettings_0

> GetNetworkApplianceSettings200Response getNetworkApplianceSettings_0(networkId)

Return the appliance settings for a network

Return the appliance settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkApplianceSettings200Response**](GetNetworkApplianceSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceSingleLan_0

> GetNetworkApplianceSingleLan200Response getNetworkApplianceSingleLan_0(networkId)

Return single LAN configuration

Return single LAN configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceSingleLan_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceSsid_0

> GetNetworkApplianceSsids200ResponseInner getNetworkApplianceSsid_0(networkId, number)

Return a single MX SSID

Return a single MX SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkApplianceSsid_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**GetNetworkApplianceSsids200ResponseInner**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceSsids_0

> [GetNetworkApplianceSsids200ResponseInner] getNetworkApplianceSsids_0(networkId)

List the MX SSIDs in a network

List the MX SSIDs in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceSsids_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkApplianceSsids200ResponseInner]**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceStaticRoute_0

> Object getNetworkApplianceStaticRoute_0(networkId, staticRouteId)

Return a static route for an MX or teleworker network

Return a static route for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.getNetworkApplianceStaticRoute_0(networkId, staticRouteId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceStaticRoutes_0

> [Object] getNetworkApplianceStaticRoutes_0(networkId)

List the static routes for an MX or teleworker network

List the static routes for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceStaticRoutes_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShapingCustomPerformanceClass_0

> Object getNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, customPerformanceClassId)

Return a custom performance class for an MX network

Return a custom performance class for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let customPerformanceClassId = "customPerformanceClassId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, customPerformanceClassId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **customPerformanceClassId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShapingCustomPerformanceClasses_0

> [Object] getNetworkApplianceTrafficShapingCustomPerformanceClasses_0(networkId)

List all custom performance classes for an MX network

List all custom performance classes for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClasses_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShapingRules_0

> Object getNetworkApplianceTrafficShapingRules_0(networkId)

Display the traffic shaping settings rules for an MX network

Display the traffic shaping settings rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShapingUplinkBandwidth_0

> GetNetworkApplianceTrafficShapingUplinkBandwidth200Response getNetworkApplianceTrafficShapingUplinkBandwidth_0(networkId)

Returns the uplink bandwidth limits for your MX network

Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingUplinkBandwidth_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkApplianceTrafficShapingUplinkBandwidth200Response**](GetNetworkApplianceTrafficShapingUplinkBandwidth200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShapingUplinkSelection_0

> GetNetworkApplianceTrafficShapingUplinkSelection200Response getNetworkApplianceTrafficShapingUplinkSelection_0(networkId)

Show uplink selection settings for an MX network

Show uplink selection settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingUplinkSelection_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShaping_0

> Object getNetworkApplianceTrafficShaping_0(networkId)

Display the traffic shaping settings for an MX network

Display the traffic shaping settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShaping_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceVlan_0

> GetNetworkApplianceVlans200ResponseInner getNetworkApplianceVlan_0(networkId, vlanId)

Return a VLAN

Return a VLAN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let vlanId = "vlanId_example"; // String | 
apiInstance.getNetworkApplianceVlan_0(networkId, vlanId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **vlanId** | **String**|  | 

### Return type

[**GetNetworkApplianceVlans200ResponseInner**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceVlansSettings_0

> Object getNetworkApplianceVlansSettings_0(networkId)

Returns the enabled status of VLANs for the network

Returns the enabled status of VLANs for the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceVlansSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceVlans_0

> [GetNetworkApplianceVlans200ResponseInner] getNetworkApplianceVlans_0(networkId)

List the VLANs for an MX network

List the VLANs for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceVlans_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkApplianceVlans200ResponseInner]**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceVpnBgp_0

> Object getNetworkApplianceVpnBgp_0(networkId)

Return a Hub BGP Configuration

Return a Hub BGP Configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceVpnBgp_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceVpnSiteToSiteVpn_0

> GetNetworkApplianceVpnSiteToSiteVpn200Response getNetworkApplianceVpnSiteToSiteVpn_0(networkId)

Return the site-to-site VPN settings of a network

Return the site-to-site VPN settings of a network. Only valid for MX networks.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceVpnSiteToSiteVpn_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceWarmSpare_0

> Object getNetworkApplianceWarmSpare_0(networkId)

Return MX warm spare settings

Return MX warm spare settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceWarmSpare_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraQualityRetentionProfile_0

> Object getNetworkCameraQualityRetentionProfile_0(networkId, qualityRetentionProfileId)

Retrieve a single quality retention profile

Retrieve a single quality retention profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
apiInstance.getNetworkCameraQualityRetentionProfile_0(networkId, qualityRetentionProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **qualityRetentionProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraQualityRetentionProfiles_0

> [Object] getNetworkCameraQualityRetentionProfiles_0(networkId)

List the quality retention profiles for this network

List the quality retention profiles for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCameraQualityRetentionProfiles_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraSchedules_0

> [Object] getNetworkCameraSchedules_0(networkId)

Returns a list of all camera recording schedules.

Returns a list of all camera recording schedules.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCameraSchedules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraWirelessProfile_0

> Object getNetworkCameraWirelessProfile_0(networkId, wirelessProfileId)

Retrieve a single camera wireless profile.

Retrieve a single camera wireless profile.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let wirelessProfileId = "wirelessProfileId_example"; // String | 
apiInstance.getNetworkCameraWirelessProfile_0(networkId, wirelessProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **wirelessProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraWirelessProfiles_0

> [Object] getNetworkCameraWirelessProfiles_0(networkId)

List the camera wireless profiles for this network.

List the camera wireless profiles for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCameraWirelessProfiles_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCellularGatewayConnectivityMonitoringDestinations_0

> Object getNetworkCellularGatewayConnectivityMonitoringDestinations_0(networkId)

Return the connectivity testing destinations for an MG network

Return the connectivity testing destinations for an MG network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCellularGatewayConnectivityMonitoringDestinations_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCellularGatewayDhcp_0

> GetNetworkCellularGatewayDhcp200Response getNetworkCellularGatewayDhcp_0(networkId)

List common DHCP settings of MGs

List common DHCP settings of MGs

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCellularGatewayDhcp_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkCellularGatewayDhcp200Response**](GetNetworkCellularGatewayDhcp200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCellularGatewaySubnetPool_0

> Object getNetworkCellularGatewaySubnetPool_0(networkId)

Return the subnet pool and mask configured for MGs in the network.

Return the subnet pool and mask configured for MGs in the network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCellularGatewaySubnetPool_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCellularGatewayUplink_0

> Object getNetworkCellularGatewayUplink_0(networkId)

Returns the uplink settings for your MG network.

Returns the uplink settings for your MG network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCellularGatewayUplink_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkClientPolicy_0

> Object getNetworkClientPolicy_0(networkId, clientId)

Return the policy assigned to a client on the network

Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
apiInstance.getNetworkClientPolicy_0(networkId, clientId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkClientSplashAuthorizationStatus_0

> Object getNetworkClientSplashAuthorizationStatus_0(networkId, clientId)

Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash

Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
apiInstance.getNetworkClientSplashAuthorizationStatus_0(networkId, clientId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkDevices_0

> [Object] getNetworkDevices_0(networkId)

List the devices in a network

List the devices in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkDevices_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedEvents_0

> GetNetworkFirmwareUpgradesStagedEvents200Response getNetworkFirmwareUpgradesStagedEvents_0(networkId)

Get the Staged Upgrade Event from a network

Get the Staged Upgrade Event from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedEvents_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedGroup_0

> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup_0(networkId, groupId)

Get a Staged Upgrade Group from a network

Get a Staged Upgrade Group from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroup_0(networkId, groupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **groupId** | **String**|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedGroups200ResponseInner**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedGroups_0

> [GetNetworkFirmwareUpgradesStagedGroups200ResponseInner] getNetworkFirmwareUpgradesStagedGroups_0(networkId)

List of Staged Upgrade Groups in a network

List of Staged Upgrade Groups in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroups_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkFirmwareUpgradesStagedGroups200ResponseInner]**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedStages_0

> [GetNetworkFirmwareUpgradesStagedStages200ResponseInner] getNetworkFirmwareUpgradesStagedStages_0(networkId)

Order of Staged Upgrade Groups in a network

Order of Staged Upgrade Groups in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedStages_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkFirmwareUpgradesStagedStages200ResponseInner]**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgrades_0

> GetNetworkFirmwareUpgrades200Response getNetworkFirmwareUpgrades_0(networkId)

Get firmware upgrade information for a network

Get firmware upgrade information for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgrades_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFloorPlan_0

> Object getNetworkFloorPlan_0(networkId, floorPlanId)

Find a floor plan by ID

Find a floor plan by ID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let floorPlanId = "floorPlanId_example"; // String | 
apiInstance.getNetworkFloorPlan_0(networkId, floorPlanId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **floorPlanId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFloorPlans_0

> [Object] getNetworkFloorPlans_0(networkId)

List the floor plans that belong to your network

List the floor plans that belong to your network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFloorPlans_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroupPolicies_0

> [Object] getNetworkGroupPolicies_0(networkId)

List the group policies in a network

List the group policies in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkGroupPolicies_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroupPolicy_0

> Object getNetworkGroupPolicy_0(networkId, groupPolicyId)

Display a group policy

Display a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let groupPolicyId = "groupPolicyId_example"; // String | 
apiInstance.getNetworkGroupPolicy_0(networkId, groupPolicyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **groupPolicyId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkHealthAlerts_0

> [GetNetworkHealthAlerts200ResponseInner] getNetworkHealthAlerts_0(networkId)

Return all global alerts on this network

Return all global alerts on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkHealthAlerts_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkHealthAlerts200ResponseInner]**](GetNetworkHealthAlerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkMerakiAuthUser_0

> GetNetworkMerakiAuthUsers200ResponseInner getNetworkMerakiAuthUser_0(networkId, merakiAuthUserId)

Return the Meraki Auth splash guest, RADIUS, or client VPN user

Return the Meraki Auth splash guest, RADIUS, or client VPN user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let merakiAuthUserId = "merakiAuthUserId_example"; // String | 
apiInstance.getNetworkMerakiAuthUser_0(networkId, merakiAuthUserId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **merakiAuthUserId** | **String**|  | 

### Return type

[**GetNetworkMerakiAuthUsers200ResponseInner**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkMerakiAuthUsers_0

> [GetNetworkMerakiAuthUsers200ResponseInner] getNetworkMerakiAuthUsers_0(networkId)

List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkMerakiAuthUsers_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkMerakiAuthUsers200ResponseInner]**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkMqttBroker_0

> Object getNetworkMqttBroker_0(networkId, mqttBrokerId)

Return an MQTT broker

Return an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let mqttBrokerId = "mqttBrokerId_example"; // String | 
apiInstance.getNetworkMqttBroker_0(networkId, mqttBrokerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **mqttBrokerId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkMqttBrokers_0

> [Object] getNetworkMqttBrokers_0(networkId)

List the MQTT brokers for this network

List the MQTT brokers for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkMqttBrokers_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkNetflow_0

> Object getNetworkNetflow_0(networkId)

Return the NetFlow traffic reporting settings for a network

Return the NetFlow traffic reporting settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkNetflow_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkPiiPiiKeys_0

> Object getNetworkPiiPiiKeys_0(networkId, opts)

List the keys required to access Personally Identifiable Information (PII) for a given identifier

List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \&quot;0\&quot; containing the applicable keys.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/piiKeys &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'username': "username_example", // String | The username of a Systems Manager user
  'email': "email_example", // String | The email of a network user account or a Systems Manager device
  'mac': "mac_example", // String | The MAC of a network client device or a Systems Manager device
  'serial': "serial_example", // String | The serial of a Systems Manager device
  'imei': "imei_example", // String | The IMEI of a Systems Manager device
  'bluetoothMac': "bluetoothMac_example" // String | The MAC of a Bluetooth client
};
apiInstance.getNetworkPiiPiiKeys_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **username** | **String**| The username of a Systems Manager user | [optional] 
 **email** | **String**| The email of a network user account or a Systems Manager device | [optional] 
 **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] 
 **serial** | **String**| The serial of a Systems Manager device | [optional] 
 **imei** | **String**| The IMEI of a Systems Manager device | [optional] 
 **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkPiiRequest_0

> Object getNetworkPiiRequest_0(networkId, requestId)

Return a PII request

Return a PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let requestId = "requestId_example"; // String | 
apiInstance.getNetworkPiiRequest_0(networkId, requestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **requestId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkPiiRequests_0

> [Object] getNetworkPiiRequests_0(networkId)

List the PII requests for this network or organization

List the PII requests for this network or organization  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkPiiRequests_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkPiiSmDevicesForKey_0

> Object getNetworkPiiSmDevicesForKey_0(networkId, opts)

Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier

Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smDevicesForKey &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'username': "username_example", // String | The username of a Systems Manager user
  'email': "email_example", // String | The email of a network user account or a Systems Manager device
  'mac': "mac_example", // String | The MAC of a network client device or a Systems Manager device
  'serial': "serial_example", // String | The serial of a Systems Manager device
  'imei': "imei_example", // String | The IMEI of a Systems Manager device
  'bluetoothMac': "bluetoothMac_example" // String | The MAC of a Bluetooth client
};
apiInstance.getNetworkPiiSmDevicesForKey_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **username** | **String**| The username of a Systems Manager user | [optional] 
 **email** | **String**| The email of a network user account or a Systems Manager device | [optional] 
 **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] 
 **serial** | **String**| The serial of a Systems Manager device | [optional] 
 **imei** | **String**| The IMEI of a Systems Manager device | [optional] 
 **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkPiiSmOwnersForKey_0

> Object getNetworkPiiSmOwnersForKey_0(networkId, opts)

Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier

Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smOwnersForKey &#x60;&#x60;&#x60;

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'username': "username_example", // String | The username of a Systems Manager user
  'email': "email_example", // String | The email of a network user account or a Systems Manager device
  'mac': "mac_example", // String | The MAC of a network client device or a Systems Manager device
  'serial': "serial_example", // String | The serial of a Systems Manager device
  'imei': "imei_example", // String | The IMEI of a Systems Manager device
  'bluetoothMac': "bluetoothMac_example" // String | The MAC of a Bluetooth client
};
apiInstance.getNetworkPiiSmOwnersForKey_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **username** | **String**| The username of a Systems Manager user | [optional] 
 **email** | **String**| The email of a network user account or a Systems Manager device | [optional] 
 **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] 
 **serial** | **String**| The serial of a Systems Manager device | [optional] 
 **imei** | **String**| The IMEI of a Systems Manager device | [optional] 
 **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkPoliciesByClient_0

> [GetNetworkPoliciesByClient200ResponseInner] getNetworkPoliciesByClient_0(networkId, opts)

Get policies for all clients with policies

Get policies for all clients with policies

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  'timespan': 3.4 // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
};
apiInstance.getNetworkPoliciesByClient_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] 

### Return type

[**[GetNetworkPoliciesByClient200ResponseInner]**](GetNetworkPoliciesByClient200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorAlertsProfile_0

> GetNetworkSensorAlertsProfiles200ResponseInner getNetworkSensorAlertsProfile_0(networkId, id)

Show details of a sensor alert profile for a network.

Show details of a sensor alert profile for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getNetworkSensorAlertsProfile_0(networkId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorAlertsProfiles_0

> [GetNetworkSensorAlertsProfiles200ResponseInner] getNetworkSensorAlertsProfiles_0(networkId)

Lists all sensor alert profiles for a network.

Lists all sensor alert profiles for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSensorAlertsProfiles_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkSensorAlertsProfiles200ResponseInner]**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorRelationships_0

> [GetNetworkSensorRelationships200ResponseInner] getNetworkSensorRelationships_0(networkId)

List the sensor roles for devices in a given network

List the sensor roles for devices in a given network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSensorRelationships_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkSensorRelationships200ResponseInner]**](GetNetworkSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSettings_0

> GetNetworkSettings200Response getNetworkSettings_0(networkId)

Return the settings for a network

Return the settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSettings200Response**](GetNetworkSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmBypassActivationLockAttempt_0

> Object getNetworkSmBypassActivationLockAttempt_0(networkId, attemptId)

Bypass activation lock attempt status

Bypass activation lock attempt status

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let attemptId = "attemptId_example"; // String | 
apiInstance.getNetworkSmBypassActivationLockAttempt_0(networkId, attemptId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **attemptId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceCerts_0

> [GetNetworkSmDeviceCerts200ResponseInner] getNetworkSmDeviceCerts_0(networkId, deviceId)

List the certs on a device

List the certs on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceCerts_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceCerts200ResponseInner]**](GetNetworkSmDeviceCerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceDeviceProfiles_0

> [GetNetworkSmDeviceDeviceProfiles200ResponseInner] getNetworkSmDeviceDeviceProfiles_0(networkId, deviceId)

Get the installed profiles associated with a device

Get the installed profiles associated with a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceDeviceProfiles_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceDeviceProfiles200ResponseInner]**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceNetworkAdapters_0

> [GetNetworkSmDeviceNetworkAdapters200ResponseInner] getNetworkSmDeviceNetworkAdapters_0(networkId, deviceId)

List the network adapters of a device

List the network adapters of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceNetworkAdapters_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceNetworkAdapters200ResponseInner]**](GetNetworkSmDeviceNetworkAdapters200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceRestrictions_0

> [Object] getNetworkSmDeviceRestrictions_0(networkId, deviceId)

List the restrictions on a device

List the restrictions on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceRestrictions_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceSecurityCenters_0

> [GetNetworkSmDeviceSecurityCenters200ResponseInner] getNetworkSmDeviceSecurityCenters_0(networkId, deviceId)

List the security centers on a device

List the security centers on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceSecurityCenters_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceSecurityCenters200ResponseInner]**](GetNetworkSmDeviceSecurityCenters200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceSoftwares_0

> [GetNetworkSmDeviceSoftwares200ResponseInner] getNetworkSmDeviceSoftwares_0(networkId, deviceId)

Get a list of softwares associated with a device

Get a list of softwares associated with a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceSoftwares_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceSoftwares200ResponseInner]**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceWlanLists_0

> [GetNetworkSmDeviceWlanLists200ResponseInner] getNetworkSmDeviceWlanLists_0(networkId, deviceId)

List the saved SSID names on a device

List the saved SSID names on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceWlanLists_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceWlanLists200ResponseInner]**](GetNetworkSmDeviceWlanLists200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDevices_0

> [GetNetworkSmDevices200ResponseInner] getNetworkSmDevices_0(networkId, opts)

List the devices enrolled in an SM network with various specified fields and filters

List the devices enrolled in an SM network with various specified fields and filters

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'fields': ["null"], // [String] | Additional fields that will be displayed for each device.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, and url.
  'wifiMacs': ["null"], // [String] | Filter devices by wifi mac(s).
  'serials': ["null"], // [String] | Filter devices by serial(s).
  'ids': ["null"], // [String] | Filter devices by id(s).
  'scope': ["null"], // [String] | Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags.
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmDevices_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **fields** | [**[String]**](String.md)| Additional fields that will be displayed for each device.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, and url. | [optional] 
 **wifiMacs** | [**[String]**](String.md)| Filter devices by wifi mac(s). | [optional] 
 **serials** | [**[String]**](String.md)| Filter devices by serial(s). | [optional] 
 **ids** | [**[String]**](String.md)| Filter devices by id(s). | [optional] 
 **scope** | [**[String]**](String.md)| Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags. | [optional] 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetworkSmDevices200ResponseInner]**](GetNetworkSmDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmProfiles_0

> [GetNetworkSmProfiles200ResponseInner] getNetworkSmProfiles_0(networkId)

List all profiles in a network

List all profiles in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSmProfiles_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkSmProfiles200ResponseInner]**](GetNetworkSmProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmTargetGroup_0

> Object getNetworkSmTargetGroup_0(networkId, targetGroupId, opts)

Return a target group

Return a target group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let targetGroupId = "targetGroupId_example"; // String | 
let opts = {
  'withDetails': true // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
};
apiInstance.getNetworkSmTargetGroup_0(networkId, targetGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **targetGroupId** | **String**|  | 
 **withDetails** | **Boolean**| Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmTargetGroups_0

> [Object] getNetworkSmTargetGroups_0(networkId, opts)

List the target groups in this network

List the target groups in this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'withDetails': true // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
};
apiInstance.getNetworkSmTargetGroups_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **withDetails** | **Boolean**| Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmTrustedAccessConfigs_0

> [GetNetworkSmTrustedAccessConfigs200ResponseInner] getNetworkSmTrustedAccessConfigs_0(networkId, opts)

List Trusted Access Configs

List Trusted Access Configs

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmTrustedAccessConfigs_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetworkSmTrustedAccessConfigs200ResponseInner]**](GetNetworkSmTrustedAccessConfigs200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserAccessDevices_0

> [GetNetworkSmUserAccessDevices200ResponseInner] getNetworkSmUserAccessDevices_0(networkId, opts)

List User Access Devices and its Trusted Access Connections

List User Access Devices and its Trusted Access Connections

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmUserAccessDevices_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetworkSmUserAccessDevices200ResponseInner]**](GetNetworkSmUserAccessDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserDeviceProfiles_0

> [GetNetworkSmDeviceDeviceProfiles200ResponseInner] getNetworkSmUserDeviceProfiles_0(networkId, userId)

Get the profiles associated with a user

Get the profiles associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserDeviceProfiles_0(networkId, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **userId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceDeviceProfiles200ResponseInner]**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserSoftwares_0

> [GetNetworkSmDeviceSoftwares200ResponseInner] getNetworkSmUserSoftwares_0(networkId, userId)

Get a list of softwares associated with a user

Get a list of softwares associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserSoftwares_0(networkId, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **userId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceSoftwares200ResponseInner]**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUsers_0

> [GetNetworkSmUsers200ResponseInner] getNetworkSmUsers_0(networkId, opts)

List the owners in an SM network with various specified fields and filters

List the owners in an SM network with various specified fields and filters

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'ids': ["null"], // [String] | Filter users by id(s).
  'usernames': ["null"], // [String] | Filter users by username(s).
  'emails': ["null"], // [String] | Filter users by email(s).
  'scope': ["null"] // [String] | Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.
};
apiInstance.getNetworkSmUsers_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **ids** | [**[String]**](String.md)| Filter users by id(s). | [optional] 
 **usernames** | [**[String]**](String.md)| Filter users by username(s). | [optional] 
 **emails** | [**[String]**](String.md)| Filter users by email(s). | [optional] 
 **scope** | [**[String]**](String.md)| Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags. | [optional] 

### Return type

[**[GetNetworkSmUsers200ResponseInner]**](GetNetworkSmUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSnmp_0

> Object getNetworkSnmp_0(networkId)

Return the SNMP settings for a network

Return the SNMP settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSnmp_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchAccessControlLists_0

> GetNetworkSwitchAccessControlLists200Response getNetworkSwitchAccessControlLists_0(networkId)

Return the access control lists for a MS network

Return the access control lists for a MS network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchAccessControlLists_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchAccessPolicies_0

> [GetNetworkSwitchAccessPolicies200ResponseInner] getNetworkSwitchAccessPolicies_0(networkId)

List the access policies for a switch network

List the access policies for a switch network. Only returns access policies with &#39;my RADIUS server&#39; as authentication method

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchAccessPolicies_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkSwitchAccessPolicies200ResponseInner]**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchAccessPolicy_0

> GetNetworkSwitchAccessPolicies200ResponseInner getNetworkSwitchAccessPolicy_0(networkId, accessPolicyNumber)

Return a specific access policy for a switch network

Return a specific access policy for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let accessPolicyNumber = "accessPolicyNumber_example"; // String | 
apiInstance.getNetworkSwitchAccessPolicy_0(networkId, accessPolicyNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **accessPolicyNumber** | **String**|  | 

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchAlternateManagementInterface_0

> Object getNetworkSwitchAlternateManagementInterface_0(networkId)

Return the switch alternate management interface for the network

Return the switch alternate management interface for the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchAlternateManagementInterface_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_0

> [GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner] getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_0(networkId, opts)

Return the list of servers trusted by Dynamic ARP Inspection on this network

Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner]**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_0

> [GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner] getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_0(networkId, opts)

Return the devices that have a Dynamic ARP Inspection warning and their warnings

Return the devices that have a Dynamic ARP Inspection warning and their warnings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner]**](GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchDhcpServerPolicy_0

> Object getNetworkSwitchDhcpServerPolicy_0(networkId)

Return the DHCP server settings

Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchDhcpServerPolicy_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchDhcpV4ServersSeen_0

> [GetNetworkSwitchDhcpV4ServersSeen200ResponseInner] getNetworkSwitchDhcpV4ServersSeen_0(networkId, opts)

Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSwitchDhcpV4ServersSeen_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetworkSwitchDhcpV4ServersSeen200ResponseInner]**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchDscpToCosMappings_0

> Object getNetworkSwitchDscpToCosMappings_0(networkId)

Return the DSCP to CoS mappings

Return the DSCP to CoS mappings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchDscpToCosMappings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchLinkAggregations_0

> [Object] getNetworkSwitchLinkAggregations_0(networkId)

List link aggregation groups

List link aggregation groups

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchLinkAggregations_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchMtu_0

> GetNetworkSwitchMtu200Response getNetworkSwitchMtu_0(networkId)

Return the MTU configuration

Return the MTU configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchMtu_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSwitchMtu200Response**](GetNetworkSwitchMtu200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchPortSchedules_0

> [Object] getNetworkSwitchPortSchedules_0(networkId)

List switch port schedules

List switch port schedules

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchPortSchedules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchQosRule_0

> Object getNetworkSwitchQosRule_0(networkId, qosRuleId)

Return a quality of service rule

Return a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let qosRuleId = "qosRuleId_example"; // String | 
apiInstance.getNetworkSwitchQosRule_0(networkId, qosRuleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **qosRuleId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchQosRulesOrder_0

> Object getNetworkSwitchQosRulesOrder_0(networkId)

Return the quality of service rule IDs by order in which they will be processed by the switch

Return the quality of service rule IDs by order in which they will be processed by the switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchQosRulesOrder_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchQosRules_0

> [Object] getNetworkSwitchQosRules_0(networkId)

List quality of service rules

List quality of service rules

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchQosRules_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchRoutingMulticastRendezvousPoint_0

> Object getNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, rendezvousPointId)

Return a multicast rendezvous point

Return a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, rendezvousPointId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rendezvousPointId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchRoutingMulticastRendezvousPoints_0

> [[Object]] getNetworkSwitchRoutingMulticastRendezvousPoints_0(networkId)

List multicast rendezvous points

List multicast rendezvous points

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[[Object]]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchRoutingMulticast_0

> Object getNetworkSwitchRoutingMulticast_0(networkId)

Return multicast settings for a network

Return multicast settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticast_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchRoutingOspf_0

> Object getNetworkSwitchRoutingOspf_0(networkId)

Return layer 3 OSPF routing configuration

Return layer 3 OSPF routing configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingOspf_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchSettings_0

> GetNetworkSwitchSettings200Response getNetworkSwitchSettings_0(networkId)

Returns the switch network settings

Returns the switch network settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSwitchSettings200Response**](GetNetworkSwitchSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStackRoutingInterfaceDhcp_0

> Object getNetworkSwitchStackRoutingInterfaceDhcp_0(networkId, switchStackId, interfaceId)

Return a layer 3 interface DHCP configuration for a switch stack

Return a layer 3 interface DHCP configuration for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
apiInstance.getNetworkSwitchStackRoutingInterfaceDhcp_0(networkId, switchStackId, interfaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **interfaceId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStackRoutingInterface_0

> Object getNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, interfaceId)

Return a layer 3 interface from a switch stack

Return a layer 3 interface from a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
apiInstance.getNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, interfaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **interfaceId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStackRoutingInterfaces_0

> [Object] getNetworkSwitchStackRoutingInterfaces_0(networkId, switchStackId)

List layer 3 interfaces for a switch stack

List layer 3 interfaces for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
apiInstance.getNetworkSwitchStackRoutingInterfaces_0(networkId, switchStackId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStackRoutingStaticRoute_0

> Object getNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, staticRouteId)

Return a layer 3 static route for a switch stack

Return a layer 3 static route for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.getNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, staticRouteId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStackRoutingStaticRoutes_0

> [Object] getNetworkSwitchStackRoutingStaticRoutes_0(networkId, switchStackId)

List layer 3 static routes for a switch stack

List layer 3 static routes for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
apiInstance.getNetworkSwitchStackRoutingStaticRoutes_0(networkId, switchStackId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStack_0

> GetNetworkSwitchStack200Response getNetworkSwitchStack_0(networkId, switchStackId)

Show a switch stack

Show a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
apiInstance.getNetworkSwitchStack_0(networkId, switchStackId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 

### Return type

[**GetNetworkSwitchStack200Response**](GetNetworkSwitchStack200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStacks_0

> [Object] getNetworkSwitchStacks_0(networkId)

List the switch stacks in a network

List the switch stacks in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchStacks_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStormControl_0

> GetNetworkSwitchStormControl200Response getNetworkSwitchStormControl_0(networkId)

Return the storm control configuration for a switch network

Return the storm control configuration for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchStormControl_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSwitchStormControl200Response**](GetNetworkSwitchStormControl200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchStp_0

> Object getNetworkSwitchStp_0(networkId)

Returns STP settings

Returns STP settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchStp_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSyslogServers_0

> GetNetworkSyslogServers200Response getNetworkSyslogServers_0(networkId)

List the syslog servers for a network

List the syslog servers for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSyslogServers_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkTrafficAnalysis_0

> Object getNetworkTrafficAnalysis_0(networkId)

Return the traffic analysis settings for a network

Return the traffic analysis settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkTrafficAnalysis_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkTrafficShapingApplicationCategories_0

> Object getNetworkTrafficShapingApplicationCategories_0(networkId)

Returns the application categories for traffic shaping rules.

Returns the application categories for traffic shaping rules.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkTrafficShapingApplicationCategories_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkTrafficShapingDscpTaggingOptions_0

> [Object] getNetworkTrafficShapingDscpTaggingOptions_0(networkId)

Returns the available DSCP tagging options for your traffic shaping rules.

Returns the available DSCP tagging options for your traffic shaping rules.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkTrafficShapingDscpTaggingOptions_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksHttpServer_0

> GetNetworkWebhooksHttpServers200ResponseInner getNetworkWebhooksHttpServer_0(networkId, httpServerId)

Return an HTTP server for a network

Return an HTTP server for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let httpServerId = "httpServerId_example"; // String | 
apiInstance.getNetworkWebhooksHttpServer_0(networkId, httpServerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **httpServerId** | **String**|  | 

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksHttpServers_0

> [GetNetworkWebhooksHttpServers200ResponseInner] getNetworkWebhooksHttpServers_0(networkId)

List the HTTP servers for a network

List the HTTP servers for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWebhooksHttpServers_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkWebhooksHttpServers200ResponseInner]**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksPayloadTemplate_0

> GetNetworkWebhooksPayloadTemplates200ResponseInner getNetworkWebhooksPayloadTemplate_0(networkId, payloadTemplateId)

Get the webhook payload template for a network

Get the webhook payload template for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let payloadTemplateId = "payloadTemplateId_example"; // String | 
apiInstance.getNetworkWebhooksPayloadTemplate_0(networkId, payloadTemplateId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **payloadTemplateId** | **String**|  | 

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksPayloadTemplates_0

> [GetNetworkWebhooksPayloadTemplates200ResponseInner] getNetworkWebhooksPayloadTemplates_0(networkId)

List the webhook payload templates for a network

List the webhook payload templates for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWebhooksPayloadTemplates_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkWebhooksPayloadTemplates200ResponseInner]**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksWebhookTest_0

> CreateNetworkWebhooksWebhookTest201Response getNetworkWebhooksWebhookTest_0(networkId, webhookTestId)

Return the status of a webhook test for a network

Return the status of a webhook test for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let webhookTestId = "webhookTestId_example"; // String | 
apiInstance.getNetworkWebhooksWebhookTest_0(networkId, webhookTestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **webhookTestId** | **String**|  | 

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessAlternateManagementInterface_0

> Object getNetworkWirelessAlternateManagementInterface_0(networkId)

Return alternate management interface and devices with IP assigned

Return alternate management interface and devices with IP assigned

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessAlternateManagementInterface_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessBilling_0

> Object getNetworkWirelessBilling_0(networkId)

Return the billing settings of this network

Return the billing settings of this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessBilling_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessBluetoothSettings_0

> GetNetworkWirelessBluetoothSettings200Response getNetworkWirelessBluetoothSettings_0(networkId)

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessBluetoothSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessRfProfile_0

> Object getNetworkWirelessRfProfile_0(networkId, rfProfileId)

Return a RF profile

Return a RF profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
apiInstance.getNetworkWirelessRfProfile_0(networkId, rfProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rfProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessRfProfiles_0

> [Object] getNetworkWirelessRfProfiles_0(networkId, opts)

List the non-basic RF profiles for this network

List the non-basic RF profiles for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'includeTemplateProfiles': true // Boolean | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
};
apiInstance.getNetworkWirelessRfProfiles_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **includeTemplateProfiles** | **Boolean**| If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSettings_0

> GetNetworkWirelessSettings200Response getNetworkWirelessSettings_0(networkId)

Return the wireless settings for a network

Return the wireless settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessSettings_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkWirelessSettings200Response**](GetNetworkWirelessSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidBonjourForwarding_0

> Object getNetworkWirelessSsidBonjourForwarding_0(networkId, number)

List the Bonjour forwarding setting and rules for the SSID

List the Bonjour forwarding setting and rules for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidBonjourForwarding_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidDeviceTypeGroupPolicies_0

> Object getNetworkWirelessSsidDeviceTypeGroupPolicies_0(networkId, number)

List the device type group policies for the SSID

List the device type group policies for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidDeviceTypeGroupPolicies_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidEapOverride_0

> GetNetworkWirelessSsidEapOverride200Response getNetworkWirelessSsidEapOverride_0(networkId, number)

Return the EAP overridden parameters for an SSID

Return the EAP overridden parameters for an SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidEapOverride_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**GetNetworkWirelessSsidEapOverride200Response**](GetNetworkWirelessSsidEapOverride200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidFirewallL3FirewallRules_0

> Object getNetworkWirelessSsidFirewallL3FirewallRules_0(networkId, number)

Return the L3 firewall rules for an SSID on an MR network

Return the L3 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidFirewallL7FirewallRules_0

> Object getNetworkWirelessSsidFirewallL7FirewallRules_0(networkId, number)

Return the L7 firewall rules for an SSID on an MR network

Return the L7 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL7FirewallRules_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidHotspot20_0

> Object getNetworkWirelessSsidHotspot20_0(networkId, number)

Return the Hotspot 2.0 settings for an SSID

Return the Hotspot 2.0 settings for an SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidHotspot20_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidIdentityPsk_0

> GetNetworkWirelessSsidIdentityPsks200ResponseInner getNetworkWirelessSsidIdentityPsk_0(networkId, number, identityPskId)

Return an Identity PSK

Return an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let identityPskId = "identityPskId_example"; // String | 
apiInstance.getNetworkWirelessSsidIdentityPsk_0(networkId, number, identityPskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **identityPskId** | **String**|  | 

### Return type

[**GetNetworkWirelessSsidIdentityPsks200ResponseInner**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidIdentityPsks_0

> [GetNetworkWirelessSsidIdentityPsks200ResponseInner] getNetworkWirelessSsidIdentityPsks_0(networkId, number)

List all Identity PSKs in a wireless network

List all Identity PSKs in a wireless network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidIdentityPsks_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**[GetNetworkWirelessSsidIdentityPsks200ResponseInner]**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidSchedules_0

> Object getNetworkWirelessSsidSchedules_0(networkId, number)

List the outage schedule for the SSID

List the outage schedule for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidSchedules_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidSplashSettings_0

> GetNetworkWirelessSsidSplashSettings200Response getNetworkWirelessSsidSplashSettings_0(networkId, number)

Display the splash page settings for the given SSID

Display the splash page settings for the given SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidSplashSettings_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidTrafficShapingRules_0

> Object getNetworkWirelessSsidTrafficShapingRules_0(networkId, number)

Display the traffic shaping settings for a SSID on an MR network

Display the traffic shaping settings for a SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidTrafficShapingRules_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidVpn_0

> Object getNetworkWirelessSsidVpn_0(networkId, number)

List the VPN settings for the SSID.

List the VPN settings for the SSID.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidVpn_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsid_0

> Object getNetworkWirelessSsid_0(networkId, number)

Return a single MR SSID

Return a single MR SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsid_0(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsids_0

> [Object] getNetworkWirelessSsids_0(networkId)

List the MR SSIDs in a network

List the MR SSIDs in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessSsids_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetwork_0

> GetNetwork200Response getNetwork_0(networkId)

Return a network

Return a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetwork_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationActionBatch_0

> CreateOrganizationActionBatch201Response getOrganizationActionBatch_0(organizationId, actionBatchId)

Return an action batch

Return an action batch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let actionBatchId = "actionBatchId_example"; // String | 
apiInstance.getOrganizationActionBatch_0(organizationId, actionBatchId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **actionBatchId** | **String**|  | 

### Return type

[**CreateOrganizationActionBatch201Response**](CreateOrganizationActionBatch201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationActionBatches_0

> [Object] getOrganizationActionBatches_0(organizationId, opts)

Return the list of action batches in the organization

Return the list of action batches in the organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'status': "status_example" // String | Filter batches by status. Valid types are pending, completed, and failed.
};
apiInstance.getOrganizationActionBatches_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **status** | **String**| Filter batches by status. Valid types are pending, completed, and failed. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyAcl_0

> Object getOrganizationAdaptivePolicyAcl_0(organizationId, aclId)

Returns the adaptive policy ACL information

Returns the adaptive policy ACL information

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyAcl_0(organizationId, aclId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **aclId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyAcls_0

> [Object] getOrganizationAdaptivePolicyAcls_0(organizationId)

List adaptive policy ACLs in a organization

List adaptive policy ACLs in a organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyAcls_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyGroup_0

> Object getOrganizationAdaptivePolicyGroup_0(organizationId, id)

Returns an adaptive policy group

Returns an adaptive policy group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyGroup_0(organizationId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyGroups_0

> [Object] getOrganizationAdaptivePolicyGroups_0(organizationId)

List adaptive policy groups in a organization

List adaptive policy groups in a organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyGroups_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyPolicies_0

> [Object] getOrganizationAdaptivePolicyPolicies_0(organizationId)

List adaptive policies in an organization

List adaptive policies in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyPolicies_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyPolicy_0

> Object getOrganizationAdaptivePolicyPolicy_0(organizationId, id)

Return an adaptive policy

Return an adaptive policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyPolicy_0(organizationId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicySettings_0

> Object getOrganizationAdaptivePolicySettings_0(organizationId)

Returns global adaptive policy settings in an organization

Returns global adaptive policy settings in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicySettings_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdmins_0

> [Object] getOrganizationAdmins_0(organizationId)

List the dashboard administrators in this organization

List the dashboard administrators in this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdmins_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAlertsProfiles_0

> [Object] getOrganizationAlertsProfiles_0(organizationId)

List all organization-wide alert configurations

List all organization-wide alert configurations

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAlertsProfiles_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationApplianceSecurityIntrusion_0

> Object getOrganizationApplianceSecurityIntrusion_0(organizationId)

Returns all supported intrusion settings for an organization

Returns all supported intrusion settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationApplianceSecurityIntrusion_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationApplianceVpnThirdPartyVPNPeers_0

> GetOrganizationApplianceVpnThirdPartyVPNPeers200Response getOrganizationApplianceVpnThirdPartyVPNPeers_0(organizationId)

Return the third party VPN peers for an organization

Return the third party VPN peers for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationApplianceVpnThirdPartyVPNPeers_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizationApplianceVpnThirdPartyVPNPeers200Response**](GetOrganizationApplianceVpnThirdPartyVPNPeers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationApplianceVpnVpnFirewallRules_0

> Object getOrganizationApplianceVpnVpnFirewallRules_0(organizationId)

Return the firewall rules for an organization&#39;s site-to-site VPN

Return the firewall rules for an organization&#39;s site-to-site VPN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationApplianceVpnVpnFirewallRules_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationBrandingPoliciesPriorities_0

> GetOrganizationBrandingPoliciesPriorities200Response getOrganizationBrandingPoliciesPriorities_0(organizationId)

Return the branding policy IDs of an organization in priority order

Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationBrandingPoliciesPriorities_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationBrandingPolicies_0

> [GetOrganizationBrandingPolicies200ResponseInner] getOrganizationBrandingPolicies_0(organizationId)

List the branding policies of an organization

List the branding policies of an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationBrandingPolicies_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**[GetOrganizationBrandingPolicies200ResponseInner]**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationBrandingPolicy_0

> GetOrganizationBrandingPolicies200ResponseInner getOrganizationBrandingPolicy_0(organizationId, brandingPolicyId)

Return a branding policy

Return a branding policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let brandingPolicyId = "brandingPolicyId_example"; // String | 
apiInstance.getOrganizationBrandingPolicy_0(organizationId, brandingPolicyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **brandingPolicyId** | **String**|  | 

### Return type

[**GetOrganizationBrandingPolicies200ResponseInner**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationCameraCustomAnalyticsArtifact_0

> Object getOrganizationCameraCustomAnalyticsArtifact_0(organizationId, artifactId)

Get Custom Analytics Artifact

Get Custom Analytics Artifact

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let artifactId = "artifactId_example"; // String | 
apiInstance.getOrganizationCameraCustomAnalyticsArtifact_0(organizationId, artifactId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **artifactId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationCameraCustomAnalyticsArtifacts_0

> [Object] getOrganizationCameraCustomAnalyticsArtifacts_0(organizationId)

List Custom Analytics Artifacts

List Custom Analytics Artifacts

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationCameraCustomAnalyticsArtifacts_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationCameraOnboardingStatuses_0

> [Object] getOrganizationCameraOnboardingStatuses_0(organizationId, opts)

Fetch onboarding status of cameras

Fetch onboarding status of cameras

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'serials': ["null"], // [String] | A list of serial numbers. The returned cameras will be filtered to only include these serials.
  'networkIds': ["null"] // [String] | A list of network IDs. The returned cameras will be filtered to only include these networks.
};
apiInstance.getOrganizationCameraOnboardingStatuses_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **serials** | [**[String]**](String.md)| A list of serial numbers. The returned cameras will be filtered to only include these serials. | [optional] 
 **networkIds** | [**[String]**](String.md)| A list of network IDs. The returned cameras will be filtered to only include these networks. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationClientsSearch_0

> Object getOrganizationClientsSearch_0(organizationId, mac, opts)

Return the client details in an organization

Return the client details in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let mac = "mac_example"; // String | The MAC address of the client. Required.
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationClientsSearch_0(organizationId, mac, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **mac** | **String**| The MAC address of the client. Required. | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 5. Default is 5. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplateSwitchProfilePort_0

> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner getOrganizationConfigTemplateSwitchProfilePort_0(organizationId, configTemplateId, profileId, portId)

Return a switch profile port

Return a switch profile port

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let profileId = "profileId_example"; // String | 
let portId = "portId_example"; // String | 
apiInstance.getOrganizationConfigTemplateSwitchProfilePort_0(organizationId, configTemplateId, profileId, portId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 
 **profileId** | **String**|  | 
 **portId** | **String**|  | 

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplateSwitchProfilePorts_0

> [GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner] getOrganizationConfigTemplateSwitchProfilePorts_0(organizationId, configTemplateId, profileId)

Return all the ports of a switch profile

Return all the ports of a switch profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let profileId = "profileId_example"; // String | 
apiInstance.getOrganizationConfigTemplateSwitchProfilePorts_0(organizationId, configTemplateId, profileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 
 **profileId** | **String**|  | 

### Return type

[**[GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner]**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplateSwitchProfiles_0

> GetOrganizationConfigTemplateSwitchProfiles200Response getOrganizationConfigTemplateSwitchProfiles_0(organizationId, configTemplateId)

List the switch profiles for your switch template configuration

List the switch profiles for your switch template configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
apiInstance.getOrganizationConfigTemplateSwitchProfiles_0(organizationId, configTemplateId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 

### Return type

[**GetOrganizationConfigTemplateSwitchProfiles200Response**](GetOrganizationConfigTemplateSwitchProfiles200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplate_0

> Object getOrganizationConfigTemplate_0(organizationId, configTemplateId)

Return a single configuration template

Return a single configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
apiInstance.getOrganizationConfigTemplate_0(organizationId, configTemplateId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplates_0

> [Object] getOrganizationConfigTemplates_0(organizationId)

List the configuration templates for this organization

List the configuration templates for this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationConfigTemplates_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationDevices_0

> [GetOrganizationDevices200ResponseInner] getOrganizationDevices_0(organizationId, opts)

List the devices in an organization

List the devices in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'configurationUpdatedAfter': "configurationUpdatedAfter_example", // String | Filter results by whether or not the device's configuration has been updated after the given timestamp
  'networkIds': ["null"], // [String] | Optional parameter to filter devices by network.
  'productTypes': ["null"], // [String] | Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
  'tags': ["null"], // [String] | Optional parameter to filter devices by tags.
  'tagsFilterType': "tagsFilterType_example", // String | Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
  'name': "name_example", // String | Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
  'mac': "mac_example", // String | Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
  'serial': "serial_example", // String | Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
  'model': "model_example", // String | Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
  'macs': ["null"], // [String] | Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
  'serials': ["null"], // [String] | Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
  'sensorMetrics': ["null"], // [String] | Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
  'sensorAlertProfileIds': ["null"], // [String] | Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
  'models': ["null"] // [String] | Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
};
apiInstance.getOrganizationDevices_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **configurationUpdatedAfter** | **String**| Filter results by whether or not the device&#39;s configuration has been updated after the given timestamp | [optional] 
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter devices by network. | [optional] 
 **productTypes** | [**[String]**](String.md)| Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. | [optional] 
 **tags** | [**[String]**](String.md)| Optional parameter to filter devices by tags. | [optional] 
 **tagsFilterType** | **String**| Optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] 
 **name** | **String**| Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match. | [optional] 
 **mac** | **String**| Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match. | [optional] 
 **serial** | **String**| Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match. | [optional] 
 **model** | **String**| Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match. | [optional] 
 **macs** | [**[String]**](String.md)| Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match. | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match. | [optional] 
 **sensorMetrics** | [**[String]**](String.md)| Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices. | [optional] 
 **sensorAlertProfileIds** | [**[String]**](String.md)| Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices. | [optional] 
 **models** | [**[String]**](String.md)| Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match. | [optional] 

### Return type

[**[GetOrganizationDevices200ResponseInner]**](GetOrganizationDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationEarlyAccessFeaturesOptIn_0

> Object getOrganizationEarlyAccessFeaturesOptIn_0(organizationId, optInId)

Show an early access feature opt-in for an organization

Show an early access feature opt-in for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let optInId = "optInId_example"; // String | 
apiInstance.getOrganizationEarlyAccessFeaturesOptIn_0(organizationId, optInId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **optInId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationEarlyAccessFeaturesOptIns_0

> [Object] getOrganizationEarlyAccessFeaturesOptIns_0(organizationId)

List the early access feature opt-ins for an organization

List the early access feature opt-ins for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationEarlyAccessFeaturesOptIns_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationEarlyAccessFeatures_0

> [Object] getOrganizationEarlyAccessFeatures_0(organizationId)

List the available early access features for organization

List the available early access features for organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationEarlyAccessFeatures_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationFirmwareUpgradesByDevice_0

> [GetOrganizationFirmwareUpgradesByDevice200ResponseInner] getOrganizationFirmwareUpgradesByDevice_0(organizationId, opts)

Get firmware upgrade status for the filtered devices

Get firmware upgrade status for the filtered devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | Optional parameter to filter by network
  'serials': ["null"], // [String] | Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
  'macs': ["null"], // [String] | Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
  'firmwareUpgradeIds': ["null"], // [String] | Optional parameter to filter by firmware upgrade ids.
  'firmwareUpgradeBatchIds': ["null"] // [String] | Optional parameter to filter by firmware upgrade batch ids.
};
apiInstance.getOrganizationFirmwareUpgradesByDevice_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter by network | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match. | [optional] 
 **macs** | [**[String]**](String.md)| Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match. | [optional] 
 **firmwareUpgradeIds** | [**[String]**](String.md)| Optional parameter to filter by firmware upgrade ids. | [optional] 
 **firmwareUpgradeBatchIds** | [**[String]**](String.md)| Optional parameter to filter by firmware upgrade batch ids. | [optional] 

### Return type

[**[GetOrganizationFirmwareUpgradesByDevice200ResponseInner]**](GetOrganizationFirmwareUpgradesByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationFirmwareUpgrades_0

> [GetOrganizationFirmwareUpgrades200ResponseInner] getOrganizationFirmwareUpgrades_0(organizationId, opts)

Get firmware upgrade information for an organization

Get firmware upgrade information for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'status': ["null"], // [String] | The status of an upgrade 
  'productType': ["null"] // [String] | The product type in a given upgrade ID
};
apiInstance.getOrganizationFirmwareUpgrades_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **status** | [**[String]**](String.md)| The status of an upgrade  | [optional] 
 **productType** | [**[String]**](String.md)| The product type in a given upgrade ID | [optional] 

### Return type

[**[GetOrganizationFirmwareUpgrades200ResponseInner]**](GetOrganizationFirmwareUpgrades200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInsightApplications_0

> [GetOrganizationInsightApplications200ResponseInner] getOrganizationInsightApplications_0(organizationId)

List all Insight tracked applications

List all Insight tracked applications

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationInsightApplications_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**[GetOrganizationInsightApplications200ResponseInner]**](GetOrganizationInsightApplications200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInsightMonitoredMediaServer_0

> Object getOrganizationInsightMonitoredMediaServer_0(organizationId, monitoredMediaServerId)

Return a monitored media server for this organization

Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
apiInstance.getOrganizationInsightMonitoredMediaServer_0(organizationId, monitoredMediaServerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **monitoredMediaServerId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInsightMonitoredMediaServers_0

> [GetOrganizationInsightMonitoredMediaServers200ResponseInner] getOrganizationInsightMonitoredMediaServers_0(organizationId)

List the monitored media servers for this organization

List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationInsightMonitoredMediaServers_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**[GetOrganizationInsightMonitoredMediaServers200ResponseInner]**](GetOrganizationInsightMonitoredMediaServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInventoryDevice_0

> GetOrganizationInventoryDevices200ResponseInner getOrganizationInventoryDevice_0(organizationId, serial)

Return a single device from the inventory of an organization

Return a single device from the inventory of an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let serial = "serial_example"; // String | 
apiInstance.getOrganizationInventoryDevice_0(organizationId, serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **serial** | **String**|  | 

### Return type

[**GetOrganizationInventoryDevices200ResponseInner**](GetOrganizationInventoryDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInventoryDevices_0

> [GetOrganizationInventoryDevices200ResponseInner] getOrganizationInventoryDevices_0(organizationId, opts)

Return the device inventory for an organization

Return the device inventory for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'usedState': "usedState_example", // String | Filter results by used or unused inventory. Accepted values are 'used' or 'unused'.
  'search': "search_example", // String | Search for devices in inventory based on serial number, mac address, or model.
  'macs': ["null"], // [String] | Search for devices in inventory based on mac addresses.
  'networkIds': ["null"], // [String] | Search for devices in inventory based on network ids.
  'serials': ["null"], // [String] | Search for devices in inventory based on serials.
  'models': ["null"], // [String] | Search for devices in inventory based on model.
  'orderNumbers': ["null"], // [String] | Search for devices in inventory based on order numbers.
  'tags': ["null"], // [String] | Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
  'tagsFilterType': "tagsFilterType_example", // String | To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'.
  'productTypes': ["null"] // [String] | Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
};
apiInstance.getOrganizationInventoryDevices_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **usedState** | **String**| Filter results by used or unused inventory. Accepted values are &#39;used&#39; or &#39;unused&#39;. | [optional] 
 **search** | **String**| Search for devices in inventory based on serial number, mac address, or model. | [optional] 
 **macs** | [**[String]**](String.md)| Search for devices in inventory based on mac addresses. | [optional] 
 **networkIds** | [**[String]**](String.md)| Search for devices in inventory based on network ids. | [optional] 
 **serials** | [**[String]**](String.md)| Search for devices in inventory based on serials. | [optional] 
 **models** | [**[String]**](String.md)| Search for devices in inventory based on model. | [optional] 
 **orderNumbers** | [**[String]**](String.md)| Search for devices in inventory based on order numbers. | [optional] 
 **tags** | [**[String]**](String.md)| Filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). | [optional] 
 **tagsFilterType** | **String**| To use with &#39;tags&#39; parameter, to filter devices which contain ANY or ALL given tags. Accepted values are &#39;withAnyTags&#39; or &#39;withAllTags&#39;, default is &#39;withAnyTags&#39;. | [optional] 
 **productTypes** | [**[String]**](String.md)| Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless. | [optional] 

### Return type

[**[GetOrganizationInventoryDevices200ResponseInner]**](GetOrganizationInventoryDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInventoryOnboardingCloudMonitoringImports_0

> [GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner] getOrganizationInventoryOnboardingCloudMonitoringImports_0(organizationId, importIds)

Check the status of a committed Import operation

Check the status of a committed Import operation

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let importIds = ["null"]; // [String] | import ids from an imports
apiInstance.getOrganizationInventoryOnboardingCloudMonitoringImports_0(organizationId, importIds, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **importIds** | [**[String]**](String.md)| import ids from an imports | 

### Return type

[**[GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner]**](GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInventoryOnboardingCloudMonitoringNetworks_0

> [GetNetwork200Response] getOrganizationInventoryOnboardingCloudMonitoringNetworks_0(organizationId, deviceType, opts)

Returns list of networks eligible for adding cloud monitored device

Returns list of networks eligible for adding cloud monitored device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let deviceType = "deviceType_example"; // String | Device Type switch or wireless controller
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationInventoryOnboardingCloudMonitoringNetworks_0(organizationId, deviceType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **deviceType** | **String**| Device Type switch or wireless controller | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetwork200Response]**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationLicense_0

> GetOrganizationLicenses200ResponseInner getOrganizationLicense_0(organizationId, licenseId)

Display a license

Display a license

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let licenseId = "licenseId_example"; // String | 
apiInstance.getOrganizationLicense_0(organizationId, licenseId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **licenseId** | **String**|  | 

### Return type

[**GetOrganizationLicenses200ResponseInner**](GetOrganizationLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationLicenses_0

> [GetOrganizationLicenses200ResponseInner] getOrganizationLicenses_0(organizationId, opts)

List the licenses for an organization

List the licenses for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'deviceSerial': "deviceSerial_example", // String | Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
  'networkId': "networkId_example", // String | Filter the licenses to those assigned in a particular network
  'state': "state_example" // String | Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'
};
apiInstance.getOrganizationLicenses_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **deviceSerial** | **String**| Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device. | [optional] 
 **networkId** | **String**| Filter the licenses to those assigned in a particular network | [optional] 
 **state** | **String**| Filter the licenses to those in a particular state. Can be one of &#39;active&#39;, &#39;expired&#39;, &#39;expiring&#39;, &#39;recentlyQueued&#39;, &#39;unused&#39; or &#39;unusedActive&#39; | [optional] 

### Return type

[**[GetOrganizationLicenses200ResponseInner]**](GetOrganizationLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationLicensingCotermLicenses_0

> [GetOrganizationLicensingCotermLicenses200ResponseInner] getOrganizationLicensingCotermLicenses_0(organizationId, opts)

List the licenses in a coterm organization

List the licenses in a coterm organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'invalidated': true, // Boolean | Filter for licenses that are invalidated
  'expired': true // Boolean | Filter for licenses that are expired
};
apiInstance.getOrganizationLicensingCotermLicenses_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **invalidated** | **Boolean**| Filter for licenses that are invalidated | [optional] 
 **expired** | **Boolean**| Filter for licenses that are expired | [optional] 

### Return type

[**[GetOrganizationLicensingCotermLicenses200ResponseInner]**](GetOrganizationLicensingCotermLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationLoginSecurity_0

> GetOrganizationLoginSecurity200Response getOrganizationLoginSecurity_0(organizationId)

Returns the login security settings for an organization.

Returns the login security settings for an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationLoginSecurity_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizationLoginSecurity200Response**](GetOrganizationLoginSecurity200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationNetworks_0

> [GetNetwork200Response] getOrganizationNetworks_0(organizationId, opts)

List the networks that the user has privileges on in an organization

List the networks that the user has privileges on in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'configTemplateId': "configTemplateId_example", // String | An optional parameter that is the ID of a config template. Will return all networks bound to that template.
  'isBoundToConfigTemplate': true, // Boolean | An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
  'tags': ["null"], // [String] | An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
  'tagsFilterType': "tagsFilterType_example", // String | An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationNetworks_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**| An optional parameter that is the ID of a config template. Will return all networks bound to that template. | [optional] 
 **isBoundToConfigTemplate** | **Boolean**| An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false. | [optional] 
 **tags** | [**[String]**](String.md)| An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). | [optional] 
 **tagsFilterType** | **String**| An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetwork200Response]**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationPolicyObject_0

> Object getOrganizationPolicyObject_0(organizationId, policyObjectId)

Shows details of a Policy Object.

Shows details of a Policy Object.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectId = "policyObjectId_example"; // String | 
apiInstance.getOrganizationPolicyObject_0(organizationId, policyObjectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **policyObjectId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationPolicyObjectsGroup_0

> Object getOrganizationPolicyObjectsGroup_0(organizationId, policyObjectGroupId)

Shows details of a Policy Object Group.

Shows details of a Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectGroupId = "policyObjectGroupId_example"; // String | 
apiInstance.getOrganizationPolicyObjectsGroup_0(organizationId, policyObjectGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **policyObjectGroupId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationPolicyObjectsGroups_0

> [Object] getOrganizationPolicyObjectsGroups_0(organizationId, opts)

Lists Policy Object Groups belonging to the organization.

Lists Policy Object Groups belonging to the organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationPolicyObjectsGroups_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationPolicyObjects_0

> [Object] getOrganizationPolicyObjects_0(organizationId, opts)

Lists Policy Objects belonging to the organization.

Lists Policy Objects belonging to the organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationPolicyObjects_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSamlIdp_0

> GetOrganizationSamlIdps200ResponseInner getOrganizationSamlIdp_0(organizationId, idpId)

Get a SAML IdP from your organization.

Get a SAML IdP from your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let idpId = "idpId_example"; // String | 
apiInstance.getOrganizationSamlIdp_0(organizationId, idpId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **idpId** | **String**|  | 

### Return type

[**GetOrganizationSamlIdps200ResponseInner**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSamlIdps_0

> [GetOrganizationSamlIdps200ResponseInner] getOrganizationSamlIdps_0(organizationId)

List the SAML IdPs in your organization.

List the SAML IdPs in your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSamlIdps_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**[GetOrganizationSamlIdps200ResponseInner]**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSamlRole_0

> Object getOrganizationSamlRole_0(organizationId, samlRoleId)

Return a SAML role

Return a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
apiInstance.getOrganizationSamlRole_0(organizationId, samlRoleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **samlRoleId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSamlRoles_0

> [Object] getOrganizationSamlRoles_0(organizationId)

List the SAML roles for this organization

List the SAML roles for this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSamlRoles_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSaml_0

> GetOrganizationSaml200Response getOrganizationSaml_0(organizationId)

Returns the SAML SSO enabled settings for an organization.

Returns the SAML SSO enabled settings for an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSaml_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizationSaml200Response**](GetOrganizationSaml200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSmApnsCert_0

> GetOrganizationSmApnsCert200Response getOrganizationSmApnsCert_0(organizationId)

Get the organization&#39;s APNS certificate

Get the organization&#39;s APNS certificate

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSmApnsCert_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizationSmApnsCert200Response**](GetOrganizationSmApnsCert200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSmVppAccount_0

> GetOrganizationSmVppAccounts200ResponseInner getOrganizationSmVppAccount_0(organizationId, vppAccountId)

Get a hash containing the unparsed token of the VPP account with the given ID

Get a hash containing the unparsed token of the VPP account with the given ID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let vppAccountId = "vppAccountId_example"; // String | 
apiInstance.getOrganizationSmVppAccount_0(organizationId, vppAccountId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **vppAccountId** | **String**|  | 

### Return type

[**GetOrganizationSmVppAccounts200ResponseInner**](GetOrganizationSmVppAccounts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSmVppAccounts_0

> [GetOrganizationSmVppAccounts200ResponseInner] getOrganizationSmVppAccounts_0(organizationId)

List the VPP accounts in the organization

List the VPP accounts in the organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSmVppAccounts_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**[GetOrganizationSmVppAccounts200ResponseInner]**](GetOrganizationSmVppAccounts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSnmp_0

> Object getOrganizationSnmp_0(organizationId)

Return the SNMP settings for an organization

Return the SNMP settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSnmp_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSwitchPortsBySwitch_0

> [GetOrganizationSwitchPortsBySwitch200ResponseInner] getOrganizationSwitchPortsBySwitch_0(organizationId, opts)

List the switchports in an organization by switch

List the switchports in an organization by switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | Optional parameter to filter switchports by network.
  'portProfileIds': ["null"], // [String] | Optional parameter to filter switchports belonging to the specified switchport profiles.
  'name': "name_example", // String | Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
  'mac': "mac_example", // String | Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
  'macs': ["null"], // [String] | Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
  'serial': "serial_example", // String | Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
  'serials': ["null"], // [String] | Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
  'configurationUpdatedAfter': "configurationUpdatedAfter_example" // String | Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
};
apiInstance.getOrganizationSwitchPortsBySwitch_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter switchports by network. | [optional] 
 **portProfileIds** | [**[String]**](String.md)| Optional parameter to filter switchports belonging to the specified switchport profiles. | [optional] 
 **name** | **String**| Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match. | [optional] 
 **mac** | **String**| Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match. | [optional] 
 **macs** | [**[String]**](String.md)| Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match. | [optional] 
 **serial** | **String**| Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match. | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match. | [optional] 
 **configurationUpdatedAfter** | **String**| Optional parameter to filter results by switches where the configuration has been updated after the given timestamp. | [optional] 

### Return type

[**[GetOrganizationSwitchPortsBySwitch200ResponseInner]**](GetOrganizationSwitchPortsBySwitch200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationWirelessDevicesEthernetStatuses_0

> [GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner] getOrganizationWirelessDevicesEthernetStatuses_0(organizationId, opts)

Endpoint to see power status for wireless devices

Endpoint to see power status for wireless devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"] // [String] | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
};
apiInstance.getOrganizationWirelessDevicesEthernetStatuses_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **networkIds** | [**[String]**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] 

### Return type

[**[GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner]**](GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganization_0

> GetOrganizations200ResponseInner getOrganization_0(organizationId)

Return an organization

Return an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganization_0(organizationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizations200ResponseInner**](GetOrganizations200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizations_0

> [GetOrganizations200ResponseInner] getOrganizations_0()

List the organizations that the user has privileges on

List the organizations that the user has privileges on

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
apiInstance.getOrganizations_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[GetOrganizations200ResponseInner]**](GetOrganizations200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lockNetworkSmDevices_0

> CheckinNetworkSmDevices200Response lockNetworkSmDevices_0(networkId, opts)

Lock a set of devices

Lock a set of devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'lockNetworkSmDevicesRequest': new MerakiDashboardApi.LockNetworkSmDevicesRequest() // LockNetworkSmDevicesRequest | 
};
apiInstance.lockNetworkSmDevices_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **lockNetworkSmDevicesRequest** | [**LockNetworkSmDevicesRequest**](LockNetworkSmDevicesRequest.md)|  | [optional] 

### Return type

[**CheckinNetworkSmDevices200Response**](CheckinNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modifyNetworkSmDevicesTags_0

> [ModifyNetworkSmDevicesTags200ResponseInner] modifyNetworkSmDevicesTags_0(networkId, modifyNetworkSmDevicesTagsRequest)

Add, delete, or update the tags of a set of devices

Add, delete, or update the tags of a set of devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let modifyNetworkSmDevicesTagsRequest = new MerakiDashboardApi.ModifyNetworkSmDevicesTagsRequest(); // ModifyNetworkSmDevicesTagsRequest | 
apiInstance.modifyNetworkSmDevicesTags_0(networkId, modifyNetworkSmDevicesTagsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **modifyNetworkSmDevicesTagsRequest** | [**ModifyNetworkSmDevicesTagsRequest**](ModifyNetworkSmDevicesTagsRequest.md)|  | 

### Return type

[**[ModifyNetworkSmDevicesTags200ResponseInner]**](ModifyNetworkSmDevicesTags200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## moveNetworkSmDevices_0

> MoveNetworkSmDevices200Response moveNetworkSmDevices_0(networkId, moveNetworkSmDevicesRequest)

Move a set of devices to a new network

Move a set of devices to a new network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let moveNetworkSmDevicesRequest = new MerakiDashboardApi.MoveNetworkSmDevicesRequest(); // MoveNetworkSmDevicesRequest | 
apiInstance.moveNetworkSmDevices_0(networkId, moveNetworkSmDevicesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **moveNetworkSmDevicesRequest** | [**MoveNetworkSmDevicesRequest**](MoveNetworkSmDevicesRequest.md)|  | 

### Return type

[**MoveNetworkSmDevices200Response**](MoveNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## moveOrganizationLicensesSeats_0

> MoveOrganizationLicensesSeats200Response moveOrganizationLicensesSeats_0(organizationId, moveOrganizationLicensesSeatsRequest)

Move SM seats to another organization

Move SM seats to another organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let moveOrganizationLicensesSeatsRequest = new MerakiDashboardApi.MoveOrganizationLicensesSeatsRequest(); // MoveOrganizationLicensesSeatsRequest | 
apiInstance.moveOrganizationLicensesSeats_0(organizationId, moveOrganizationLicensesSeatsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **moveOrganizationLicensesSeatsRequest** | [**MoveOrganizationLicensesSeatsRequest**](MoveOrganizationLicensesSeatsRequest.md)|  | 

### Return type

[**MoveOrganizationLicensesSeats200Response**](MoveOrganizationLicensesSeats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## moveOrganizationLicenses_0

> MoveOrganizationLicenses200Response moveOrganizationLicenses_0(organizationId, moveOrganizationLicensesRequest)

Move licenses to another organization

Move licenses to another organization. This will also move any devices that the licenses are assigned to

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let moveOrganizationLicensesRequest = new MerakiDashboardApi.MoveOrganizationLicensesRequest(); // MoveOrganizationLicensesRequest | 
apiInstance.moveOrganizationLicenses_0(organizationId, moveOrganizationLicensesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **moveOrganizationLicensesRequest** | [**MoveOrganizationLicensesRequest**](MoveOrganizationLicensesRequest.md)|  | 

### Return type

[**MoveOrganizationLicenses200Response**](MoveOrganizationLicenses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## moveOrganizationLicensingCotermLicenses_0

> MoveOrganizationLicensingCotermLicenses200Response moveOrganizationLicensingCotermLicenses_0(organizationId, moveOrganizationLicensingCotermLicensesRequest)

Moves a license to a different organization (coterm only)

Moves a license to a different organization (coterm only)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let moveOrganizationLicensingCotermLicensesRequest = new MerakiDashboardApi.MoveOrganizationLicensingCotermLicensesRequest(); // MoveOrganizationLicensingCotermLicensesRequest | 
apiInstance.moveOrganizationLicensingCotermLicenses_0(organizationId, moveOrganizationLicensingCotermLicensesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **moveOrganizationLicensingCotermLicensesRequest** | [**MoveOrganizationLicensingCotermLicensesRequest**](MoveOrganizationLicensingCotermLicensesRequest.md)|  | 

### Return type

[**MoveOrganizationLicensingCotermLicenses200Response**](MoveOrganizationLicensingCotermLicenses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## provisionNetworkClients_0

> Object provisionNetworkClients_0(networkId, provisionNetworkClientsRequest)

Provisions a client with a name and policy

Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let provisionNetworkClientsRequest = new MerakiDashboardApi.ProvisionNetworkClientsRequest(); // ProvisionNetworkClientsRequest | 
apiInstance.provisionNetworkClients_0(networkId, provisionNetworkClientsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **provisionNetworkClientsRequest** | [**ProvisionNetworkClientsRequest**](ProvisionNetworkClientsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refreshNetworkSmDeviceDetails_0

> refreshNetworkSmDeviceDetails_0(networkId, deviceId)

Refresh the details of a device

Refresh the details of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.refreshNetworkSmDeviceDetails_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## releaseFromOrganizationInventory_0

> Object releaseFromOrganizationInventory_0(organizationId, opts)

Release a list of claimed devices from an organization.

Release a list of claimed devices from an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'releaseFromOrganizationInventoryRequest': new MerakiDashboardApi.ReleaseFromOrganizationInventoryRequest() // ReleaseFromOrganizationInventoryRequest | 
};
apiInstance.releaseFromOrganizationInventory_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **releaseFromOrganizationInventoryRequest** | [**ReleaseFromOrganizationInventoryRequest**](ReleaseFromOrganizationInventoryRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeNetworkDevices_0

> removeNetworkDevices_0(networkId, removeNetworkDevicesRequest)

Remove a single device

Remove a single device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let removeNetworkDevicesRequest = new MerakiDashboardApi.RemoveNetworkDevicesRequest(); // RemoveNetworkDevicesRequest | 
apiInstance.removeNetworkDevices_0(networkId, removeNetworkDevicesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **removeNetworkDevicesRequest** | [**RemoveNetworkDevicesRequest**](RemoveNetworkDevicesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## removeNetworkSwitchStack_0

> Object removeNetworkSwitchStack_0(networkId, switchStackId, removeNetworkSwitchStackRequest)

Remove a switch from a stack

Remove a switch from a stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let removeNetworkSwitchStackRequest = new MerakiDashboardApi.RemoveNetworkSwitchStackRequest(); // RemoveNetworkSwitchStackRequest | 
apiInstance.removeNetworkSwitchStack_0(networkId, switchStackId, removeNetworkSwitchStackRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **removeNetworkSwitchStackRequest** | [**RemoveNetworkSwitchStackRequest**](RemoveNetworkSwitchStackRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## renewOrganizationLicensesSeats_0

> AssignOrganizationLicensesSeats200Response renewOrganizationLicensesSeats_0(organizationId, renewOrganizationLicensesSeatsRequest)

Renew SM seats of a license

Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let renewOrganizationLicensesSeatsRequest = new MerakiDashboardApi.RenewOrganizationLicensesSeatsRequest(); // RenewOrganizationLicensesSeatsRequest | 
apiInstance.renewOrganizationLicensesSeats_0(organizationId, renewOrganizationLicensesSeatsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **renewOrganizationLicensesSeatsRequest** | [**RenewOrganizationLicensesSeatsRequest**](RenewOrganizationLicensesSeatsRequest.md)|  | 

### Return type

[**AssignOrganizationLicensesSeats200Response**](AssignOrganizationLicensesSeats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rollbacksNetworkFirmwareUpgradesStagedEvents_0

> GetNetworkFirmwareUpgradesStagedEvents200Response rollbacksNetworkFirmwareUpgradesStagedEvents_0(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest)

Rollback a Staged Upgrade Event for a network

Rollback a Staged Upgrade Event for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rollbacksNetworkFirmwareUpgradesStagedEventsRequest = new MerakiDashboardApi.RollbacksNetworkFirmwareUpgradesStagedEventsRequest(); // RollbacksNetworkFirmwareUpgradesStagedEventsRequest | 
apiInstance.rollbacksNetworkFirmwareUpgradesStagedEvents_0(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rollbacksNetworkFirmwareUpgradesStagedEventsRequest** | [**RollbacksNetworkFirmwareUpgradesStagedEventsRequest**](RollbacksNetworkFirmwareUpgradesStagedEventsRequest.md)|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## splitNetwork_0

> SplitNetwork200Response splitNetwork_0(networkId)

Split a combined network into individual networks for each type of device

Split a combined network into individual networks for each type of device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.splitNetwork_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**SplitNetwork200Response**](SplitNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## swapNetworkApplianceWarmSpare_0

> Object swapNetworkApplianceWarmSpare_0(networkId)

Swap MX primary and warm spare appliances

Swap MX primary and warm spare appliances

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
apiInstance.swapNetworkApplianceWarmSpare_0(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unbindNetwork_0

> GetNetwork200Response unbindNetwork_0(networkId, opts)

Unbind a network from a template.

Unbind a network from a template.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'unbindNetworkRequest': new MerakiDashboardApi.UnbindNetworkRequest() // UnbindNetworkRequest | 
};
apiInstance.unbindNetwork_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **unbindNetworkRequest** | [**UnbindNetworkRequest**](UnbindNetworkRequest.md)|  | [optional] 

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unenrollNetworkSmDevice_0

> Object unenrollNetworkSmDevice_0(networkId, deviceId)

Unenroll a device

Unenroll a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.unenrollNetworkSmDevice_0(networkId, deviceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceApplianceUplinksSettings_0

> GetDeviceApplianceUplinksSettings200Response updateDeviceApplianceUplinksSettings_0(serial, updateDeviceApplianceUplinksSettingsRequest)

Update the uplink settings for an MX appliance

Update the uplink settings for an MX appliance

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let updateDeviceApplianceUplinksSettingsRequest = new MerakiDashboardApi.UpdateDeviceApplianceUplinksSettingsRequest(); // UpdateDeviceApplianceUplinksSettingsRequest | 
apiInstance.updateDeviceApplianceUplinksSettings_0(serial, updateDeviceApplianceUplinksSettingsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceApplianceUplinksSettingsRequest** | [**UpdateDeviceApplianceUplinksSettingsRequest**](UpdateDeviceApplianceUplinksSettingsRequest.md)|  | 

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCameraCustomAnalytics_0

> Object updateDeviceCameraCustomAnalytics_0(serial, opts)

Update custom analytics settings for a camera

Update custom analytics settings for a camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraCustomAnalyticsRequest': new MerakiDashboardApi.UpdateDeviceCameraCustomAnalyticsRequest() // UpdateDeviceCameraCustomAnalyticsRequest | 
};
apiInstance.updateDeviceCameraCustomAnalytics_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCameraCustomAnalyticsRequest** | [**UpdateDeviceCameraCustomAnalyticsRequest**](UpdateDeviceCameraCustomAnalyticsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCameraQualityAndRetention_0

> Object updateDeviceCameraQualityAndRetention_0(serial, opts)

Update quality and retention settings for the given camera

Update quality and retention settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraQualityAndRetentionRequest': new MerakiDashboardApi.UpdateDeviceCameraQualityAndRetentionRequest() // UpdateDeviceCameraQualityAndRetentionRequest | 
};
apiInstance.updateDeviceCameraQualityAndRetention_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCameraQualityAndRetentionRequest** | [**UpdateDeviceCameraQualityAndRetentionRequest**](UpdateDeviceCameraQualityAndRetentionRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCameraSense_0

> Object updateDeviceCameraSense_0(serial, opts)

Update sense settings for the given camera

Update sense settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraSenseRequest': new MerakiDashboardApi.UpdateDeviceCameraSenseRequest() // UpdateDeviceCameraSenseRequest | 
};
apiInstance.updateDeviceCameraSense_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCameraSenseRequest** | [**UpdateDeviceCameraSenseRequest**](UpdateDeviceCameraSenseRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCameraVideoSettings_0

> Object updateDeviceCameraVideoSettings_0(serial, opts)

Update video settings for the given camera

Update video settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraVideoSettingsRequest': new MerakiDashboardApi.UpdateDeviceCameraVideoSettingsRequest() // UpdateDeviceCameraVideoSettingsRequest | 
};
apiInstance.updateDeviceCameraVideoSettings_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCameraVideoSettingsRequest** | [**UpdateDeviceCameraVideoSettingsRequest**](UpdateDeviceCameraVideoSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCameraWirelessProfiles_0

> Object updateDeviceCameraWirelessProfiles_0(serial, updateDeviceCameraWirelessProfilesRequest)

Assign wireless profiles to the given camera

Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let updateDeviceCameraWirelessProfilesRequest = new MerakiDashboardApi.UpdateDeviceCameraWirelessProfilesRequest(); // UpdateDeviceCameraWirelessProfilesRequest | 
apiInstance.updateDeviceCameraWirelessProfiles_0(serial, updateDeviceCameraWirelessProfilesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCameraWirelessProfilesRequest** | [**UpdateDeviceCameraWirelessProfilesRequest**](UpdateDeviceCameraWirelessProfilesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCellularGatewayLan_0

> Object updateDeviceCellularGatewayLan_0(serial, opts)

Update the LAN Settings for a single MG.

Update the LAN Settings for a single MG.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularGatewayLanRequest': new MerakiDashboardApi.UpdateDeviceCellularGatewayLanRequest() // UpdateDeviceCellularGatewayLanRequest | 
};
apiInstance.updateDeviceCellularGatewayLan_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCellularGatewayLanRequest** | [**UpdateDeviceCellularGatewayLanRequest**](UpdateDeviceCellularGatewayLanRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCellularGatewayPortForwardingRules_0

> Object updateDeviceCellularGatewayPortForwardingRules_0(serial, opts)

Updates the port forwarding rules for a single MG.

Updates the port forwarding rules for a single MG.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularGatewayPortForwardingRulesRequest': new MerakiDashboardApi.UpdateDeviceCellularGatewayPortForwardingRulesRequest() // UpdateDeviceCellularGatewayPortForwardingRulesRequest | 
};
apiInstance.updateDeviceCellularGatewayPortForwardingRules_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCellularGatewayPortForwardingRulesRequest** | [**UpdateDeviceCellularGatewayPortForwardingRulesRequest**](UpdateDeviceCellularGatewayPortForwardingRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceCellularSims_0

> Object updateDeviceCellularSims_0(serial, opts)

Updates the SIM and APN configurations for a cellular device.

Updates the SIM and APN configurations for a cellular device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularSimsRequest': new MerakiDashboardApi.UpdateDeviceCellularSimsRequest() // UpdateDeviceCellularSimsRequest | 
};
apiInstance.updateDeviceCellularSims_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceCellularSimsRequest** | [**UpdateDeviceCellularSimsRequest**](UpdateDeviceCellularSimsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceManagementInterface_0

> Object updateDeviceManagementInterface_0(serial, opts)

Update the management interface settings for a device

Update the management interface settings for a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceManagementInterfaceRequest': new MerakiDashboardApi.UpdateDeviceManagementInterfaceRequest() // UpdateDeviceManagementInterfaceRequest | 
};
apiInstance.updateDeviceManagementInterface_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceManagementInterfaceRequest** | [**UpdateDeviceManagementInterfaceRequest**](UpdateDeviceManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceSensorRelationships_0

> GetDeviceSensorRelationships200ResponseInner updateDeviceSensorRelationships_0(serial, opts)

Assign one or more sensor roles to a given sensor or camera device.

Assign one or more sensor roles to a given sensor or camera device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceSensorRelationshipsRequest': new MerakiDashboardApi.UpdateDeviceSensorRelationshipsRequest() // UpdateDeviceSensorRelationshipsRequest | 
};
apiInstance.updateDeviceSensorRelationships_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceSensorRelationshipsRequest** | [**UpdateDeviceSensorRelationshipsRequest**](UpdateDeviceSensorRelationshipsRequest.md)|  | [optional] 

### Return type

[**GetDeviceSensorRelationships200ResponseInner**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceSwitchPort_0

> GetDeviceSwitchPorts200ResponseInner updateDeviceSwitchPort_0(serial, portId, opts)

Update a switch port

Update a switch port

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let portId = "portId_example"; // String | 
let opts = {
  'updateDeviceSwitchPortRequest': new MerakiDashboardApi.UpdateDeviceSwitchPortRequest() // UpdateDeviceSwitchPortRequest | 
};
apiInstance.updateDeviceSwitchPort_0(serial, portId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **portId** | **String**|  | 
 **updateDeviceSwitchPortRequest** | [**UpdateDeviceSwitchPortRequest**](UpdateDeviceSwitchPortRequest.md)|  | [optional] 

### Return type

[**GetDeviceSwitchPorts200ResponseInner**](GetDeviceSwitchPorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceSwitchRoutingInterfaceDhcp_0

> Object updateDeviceSwitchRoutingInterfaceDhcp_0(serial, interfaceId, opts)

Update a layer 3 interface DHCP configuration for a switch

Update a layer 3 interface DHCP configuration for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
let opts = {
  'updateDeviceSwitchRoutingInterfaceDhcpRequest': new MerakiDashboardApi.UpdateDeviceSwitchRoutingInterfaceDhcpRequest() // UpdateDeviceSwitchRoutingInterfaceDhcpRequest | 
};
apiInstance.updateDeviceSwitchRoutingInterfaceDhcp_0(serial, interfaceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **interfaceId** | **String**|  | 
 **updateDeviceSwitchRoutingInterfaceDhcpRequest** | [**UpdateDeviceSwitchRoutingInterfaceDhcpRequest**](UpdateDeviceSwitchRoutingInterfaceDhcpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceSwitchRoutingInterface_0

> GetDeviceSwitchRoutingInterfaces200ResponseInner updateDeviceSwitchRoutingInterface_0(serial, interfaceId, opts)

Update a layer 3 interface for a switch

Update a layer 3 interface for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
let opts = {
  'createDeviceSwitchRoutingInterfaceRequest': new MerakiDashboardApi.CreateDeviceSwitchRoutingInterfaceRequest() // CreateDeviceSwitchRoutingInterfaceRequest | 
};
apiInstance.updateDeviceSwitchRoutingInterface_0(serial, interfaceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **interfaceId** | **String**|  | 
 **createDeviceSwitchRoutingInterfaceRequest** | [**CreateDeviceSwitchRoutingInterfaceRequest**](CreateDeviceSwitchRoutingInterfaceRequest.md)|  | [optional] 

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceSwitchRoutingStaticRoute_0

> Object updateDeviceSwitchRoutingStaticRoute_0(serial, staticRouteId, opts)

Update a layer 3 static route for a switch

Update a layer 3 static route for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
let opts = {
  'updateDeviceSwitchRoutingStaticRouteRequest': new MerakiDashboardApi.UpdateDeviceSwitchRoutingStaticRouteRequest() // UpdateDeviceSwitchRoutingStaticRouteRequest | 
};
apiInstance.updateDeviceSwitchRoutingStaticRoute_0(serial, staticRouteId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **staticRouteId** | **String**|  | 
 **updateDeviceSwitchRoutingStaticRouteRequest** | [**UpdateDeviceSwitchRoutingStaticRouteRequest**](UpdateDeviceSwitchRoutingStaticRouteRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceSwitchWarmSpare_0

> Object updateDeviceSwitchWarmSpare_0(serial, updateDeviceSwitchWarmSpareRequest)

Update warm spare configuration for a switch

Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let updateDeviceSwitchWarmSpareRequest = new MerakiDashboardApi.UpdateDeviceSwitchWarmSpareRequest(); // UpdateDeviceSwitchWarmSpareRequest | 
apiInstance.updateDeviceSwitchWarmSpare_0(serial, updateDeviceSwitchWarmSpareRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceSwitchWarmSpareRequest** | [**UpdateDeviceSwitchWarmSpareRequest**](UpdateDeviceSwitchWarmSpareRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceWirelessBluetoothSettings_0

> GetDeviceWirelessBluetoothSettings200Response updateDeviceWirelessBluetoothSettings_0(serial, opts)

Update the bluetooth settings for a wireless device

Update the bluetooth settings for a wireless device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceWirelessBluetoothSettingsRequest': new MerakiDashboardApi.UpdateDeviceWirelessBluetoothSettingsRequest() // UpdateDeviceWirelessBluetoothSettingsRequest | 
};
apiInstance.updateDeviceWirelessBluetoothSettings_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceWirelessBluetoothSettingsRequest** | [**UpdateDeviceWirelessBluetoothSettingsRequest**](UpdateDeviceWirelessBluetoothSettingsRequest.md)|  | [optional] 

### Return type

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceWirelessRadioSettings_0

> Object updateDeviceWirelessRadioSettings_0(serial, opts)

Update the radio settings of a device

Update the radio settings of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceWirelessRadioSettingsRequest': new MerakiDashboardApi.UpdateDeviceWirelessRadioSettingsRequest() // UpdateDeviceWirelessRadioSettingsRequest | 
};
apiInstance.updateDeviceWirelessRadioSettings_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceWirelessRadioSettingsRequest** | [**UpdateDeviceWirelessRadioSettingsRequest**](UpdateDeviceWirelessRadioSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDevice_0

> Object updateDevice_0(serial, opts)

Update the attributes of a device

Update the attributes of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceRequest': new MerakiDashboardApi.UpdateDeviceRequest() // UpdateDeviceRequest | 
};
apiInstance.updateDevice_0(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceRequest** | [**UpdateDeviceRequest**](UpdateDeviceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkAlertsSettings_0

> Object updateNetworkAlertsSettings_0(networkId, opts)

Update the alert configuration for this network

Update the alert configuration for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkAlertsSettingsRequest': new MerakiDashboardApi.UpdateNetworkAlertsSettingsRequest() // UpdateNetworkAlertsSettingsRequest | 
};
apiInstance.updateNetworkAlertsSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkAlertsSettingsRequest** | [**UpdateNetworkAlertsSettingsRequest**](UpdateNetworkAlertsSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceConnectivityMonitoringDestinations_0

> Object updateNetworkApplianceConnectivityMonitoringDestinations_0(networkId, opts)

Update the connectivity testing destinations for an MX network

Update the connectivity testing destinations for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceConnectivityMonitoringDestinationsRequest': new MerakiDashboardApi.UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest() // UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest | 
};
apiInstance.updateNetworkApplianceConnectivityMonitoringDestinations_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest**](UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceContentFiltering_0

> Object updateNetworkApplianceContentFiltering_0(networkId, opts)

Update the content filtering settings for an MX network

Update the content filtering settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceContentFilteringRequest': new MerakiDashboardApi.UpdateNetworkApplianceContentFilteringRequest() // UpdateNetworkApplianceContentFilteringRequest | 
};
apiInstance.updateNetworkApplianceContentFiltering_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceContentFilteringRequest** | [**UpdateNetworkApplianceContentFilteringRequest**](UpdateNetworkApplianceContentFilteringRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallCellularFirewallRules_0

> Object updateNetworkApplianceFirewallCellularFirewallRules_0(networkId, opts)

Update the cellular firewall rules of an MX network

Update the cellular firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest() // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallCellularFirewallRules_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallCellularFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallCellularFirewallRulesRequest**](UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallFirewalledService_0

> Object updateNetworkApplianceFirewallFirewalledService_0(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let service = "service_example"; // String | 
let updateNetworkApplianceFirewallFirewalledServiceRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallFirewalledServiceRequest(); // UpdateNetworkApplianceFirewallFirewalledServiceRequest | 
apiInstance.updateNetworkApplianceFirewallFirewalledService_0(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **service** | **String**|  | 
 **updateNetworkApplianceFirewallFirewalledServiceRequest** | [**UpdateNetworkApplianceFirewallFirewalledServiceRequest**](UpdateNetworkApplianceFirewallFirewalledServiceRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallInboundCellularFirewallRules_0

> [Object] updateNetworkApplianceFirewallInboundCellularFirewallRules_0(networkId, opts)

Update the inbound cellular firewall rules of an MX network

Update the inbound cellular firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest() // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallInboundCellularFirewallRules_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallCellularFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallCellularFirewallRulesRequest**](UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.md)|  | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallInboundFirewallRules_0

> Object updateNetworkApplianceFirewallInboundFirewallRules_0(networkId, opts)

Update the inbound firewall rules of an MX network

Update the inbound firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallInboundFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest() // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallInboundFirewallRules_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallL3FirewallRules_0

> Object updateNetworkApplianceFirewallL3FirewallRules_0(networkId, opts)

Update the L3 firewall rules of an MX network

Update the L3 firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallInboundFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest() // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallL3FirewallRules_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallL7FirewallRules_0

> Object updateNetworkApplianceFirewallL7FirewallRules_0(networkId, opts)

Update the MX L7 firewall rules for an MX network

Update the MX L7 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallL7FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallL7FirewallRulesRequest() // UpdateNetworkApplianceFirewallL7FirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallL7FirewallRules_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallL7FirewallRulesRequest** | [**UpdateNetworkApplianceFirewallL7FirewallRulesRequest**](UpdateNetworkApplianceFirewallL7FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallOneToManyNatRules_0

> Object updateNetworkApplianceFirewallOneToManyNatRules_0(networkId, updateNetworkApplianceFirewallOneToManyNatRulesRequest)

Set the 1:Many NAT mapping rules for an MX network

Set the 1:Many NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceFirewallOneToManyNatRulesRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallOneToManyNatRulesRequest(); // UpdateNetworkApplianceFirewallOneToManyNatRulesRequest | 
apiInstance.updateNetworkApplianceFirewallOneToManyNatRules_0(networkId, updateNetworkApplianceFirewallOneToManyNatRulesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallOneToManyNatRulesRequest** | [**UpdateNetworkApplianceFirewallOneToManyNatRulesRequest**](UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallOneToOneNatRules_0

> Object updateNetworkApplianceFirewallOneToOneNatRules_0(networkId, updateNetworkApplianceFirewallOneToOneNatRulesRequest)

Set the 1:1 NAT mapping rules for an MX network

Set the 1:1 NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceFirewallOneToOneNatRulesRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallOneToOneNatRulesRequest(); // UpdateNetworkApplianceFirewallOneToOneNatRulesRequest | 
apiInstance.updateNetworkApplianceFirewallOneToOneNatRules_0(networkId, updateNetworkApplianceFirewallOneToOneNatRulesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallOneToOneNatRulesRequest** | [**UpdateNetworkApplianceFirewallOneToOneNatRulesRequest**](UpdateNetworkApplianceFirewallOneToOneNatRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallPortForwardingRules_0

> Object updateNetworkApplianceFirewallPortForwardingRules_0(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest)

Update the port forwarding rules for an MX network

Update the port forwarding rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceFirewallPortForwardingRulesRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallPortForwardingRulesRequest(); // UpdateNetworkApplianceFirewallPortForwardingRulesRequest | 
apiInstance.updateNetworkApplianceFirewallPortForwardingRules_0(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallPortForwardingRulesRequest** | [**UpdateNetworkApplianceFirewallPortForwardingRulesRequest**](UpdateNetworkApplianceFirewallPortForwardingRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallSettings_0

> Object updateNetworkApplianceFirewallSettings_0(networkId, opts)

Update the firewall settings for this network

Update the firewall settings for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallSettingsRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallSettingsRequest() // UpdateNetworkApplianceFirewallSettingsRequest | 
};
apiInstance.updateNetworkApplianceFirewallSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceFirewallSettingsRequest** | [**UpdateNetworkApplianceFirewallSettingsRequest**](UpdateNetworkApplianceFirewallSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkAppliancePort_0

> GetNetworkAppliancePorts200ResponseInner updateNetworkAppliancePort_0(networkId, portId, opts)

Update the per-port VLAN settings for a single MX port.

Update the per-port VLAN settings for a single MX port.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let portId = "portId_example"; // String | 
let opts = {
  'updateNetworkAppliancePortRequest': new MerakiDashboardApi.UpdateNetworkAppliancePortRequest() // UpdateNetworkAppliancePortRequest | 
};
apiInstance.updateNetworkAppliancePort_0(networkId, portId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **portId** | **String**|  | 
 **updateNetworkAppliancePortRequest** | [**UpdateNetworkAppliancePortRequest**](UpdateNetworkAppliancePortRequest.md)|  | [optional] 

### Return type

[**GetNetworkAppliancePorts200ResponseInner**](GetNetworkAppliancePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkAppliancePrefixesDelegatedStatic_0

> Object updateNetworkAppliancePrefixesDelegatedStatic_0(networkId, staticDelegatedPrefixId, opts)

Update a static delegated prefix from a network

Update a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
let opts = {
  'updateNetworkAppliancePrefixesDelegatedStaticRequest': new MerakiDashboardApi.UpdateNetworkAppliancePrefixesDelegatedStaticRequest() // UpdateNetworkAppliancePrefixesDelegatedStaticRequest | 
};
apiInstance.updateNetworkAppliancePrefixesDelegatedStatic_0(networkId, staticDelegatedPrefixId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **staticDelegatedPrefixId** | **String**|  | 
 **updateNetworkAppliancePrefixesDelegatedStaticRequest** | [**UpdateNetworkAppliancePrefixesDelegatedStaticRequest**](UpdateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceSecurityIntrusion_0

> Object updateNetworkApplianceSecurityIntrusion_0(networkId, opts)

Set the supported intrusion settings for an MX network

Set the supported intrusion settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceSecurityIntrusionRequest': new MerakiDashboardApi.UpdateNetworkApplianceSecurityIntrusionRequest() // UpdateNetworkApplianceSecurityIntrusionRequest | 
};
apiInstance.updateNetworkApplianceSecurityIntrusion_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceSecurityIntrusionRequest** | [**UpdateNetworkApplianceSecurityIntrusionRequest**](UpdateNetworkApplianceSecurityIntrusionRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceSecurityMalware_0

> Object updateNetworkApplianceSecurityMalware_0(networkId, updateNetworkApplianceSecurityMalwareRequest)

Set the supported malware settings for an MX network

Set the supported malware settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceSecurityMalwareRequest = new MerakiDashboardApi.UpdateNetworkApplianceSecurityMalwareRequest(); // UpdateNetworkApplianceSecurityMalwareRequest | 
apiInstance.updateNetworkApplianceSecurityMalware_0(networkId, updateNetworkApplianceSecurityMalwareRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceSecurityMalwareRequest** | [**UpdateNetworkApplianceSecurityMalwareRequest**](UpdateNetworkApplianceSecurityMalwareRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceSettings_0

> GetNetworkApplianceSettings200Response updateNetworkApplianceSettings_0(networkId, opts)

Update the appliance settings for a network

Update the appliance settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceSettingsRequest': new MerakiDashboardApi.UpdateNetworkApplianceSettingsRequest() // UpdateNetworkApplianceSettingsRequest | 
};
apiInstance.updateNetworkApplianceSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceSettingsRequest** | [**UpdateNetworkApplianceSettingsRequest**](UpdateNetworkApplianceSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkApplianceSettings200Response**](GetNetworkApplianceSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceSingleLan_0

> GetNetworkApplianceSingleLan200Response updateNetworkApplianceSingleLan_0(networkId, opts)

Update single LAN configuration

Update single LAN configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceSingleLanRequest': new MerakiDashboardApi.UpdateNetworkApplianceSingleLanRequest() // UpdateNetworkApplianceSingleLanRequest | 
};
apiInstance.updateNetworkApplianceSingleLan_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceSingleLanRequest** | [**UpdateNetworkApplianceSingleLanRequest**](UpdateNetworkApplianceSingleLanRequest.md)|  | [optional] 

### Return type

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceSsid_0

> GetNetworkApplianceSsids200ResponseInner updateNetworkApplianceSsid_0(networkId, number, opts)

Update the attributes of an MX SSID

Update the attributes of an MX SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkApplianceSsidRequest': new MerakiDashboardApi.UpdateNetworkApplianceSsidRequest() // UpdateNetworkApplianceSsidRequest | 
};
apiInstance.updateNetworkApplianceSsid_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkApplianceSsidRequest** | [**UpdateNetworkApplianceSsidRequest**](UpdateNetworkApplianceSsidRequest.md)|  | [optional] 

### Return type

[**GetNetworkApplianceSsids200ResponseInner**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceStaticRoute_0

> Object updateNetworkApplianceStaticRoute_0(networkId, staticRouteId, opts)

Update a static route for an MX or teleworker network

Update a static route for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
let opts = {
  'updateNetworkApplianceStaticRouteRequest': new MerakiDashboardApi.UpdateNetworkApplianceStaticRouteRequest() // UpdateNetworkApplianceStaticRouteRequest | 
};
apiInstance.updateNetworkApplianceStaticRoute_0(networkId, staticRouteId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **staticRouteId** | **String**|  | 
 **updateNetworkApplianceStaticRouteRequest** | [**UpdateNetworkApplianceStaticRouteRequest**](UpdateNetworkApplianceStaticRouteRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceTrafficShapingCustomPerformanceClass_0

> Object updateNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, customPerformanceClassId, opts)

Update a custom performance class for an MX network

Update a custom performance class for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let customPerformanceClassId = "customPerformanceClassId_example"; // String | 
let opts = {
  'updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest': new MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest() // UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
};
apiInstance.updateNetworkApplianceTrafficShapingCustomPerformanceClass_0(networkId, customPerformanceClassId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **customPerformanceClassId** | **String**|  | 
 **updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceTrafficShapingRules_0

> Object updateNetworkApplianceTrafficShapingRules_0(networkId, opts)

Update the traffic shaping settings rules for an MX network

Update the traffic shaping settings rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceTrafficShapingRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingRulesRequest() // UpdateNetworkApplianceTrafficShapingRulesRequest | 
};
apiInstance.updateNetworkApplianceTrafficShapingRules_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceTrafficShapingRulesRequest** | [**UpdateNetworkApplianceTrafficShapingRulesRequest**](UpdateNetworkApplianceTrafficShapingRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceTrafficShapingUplinkBandwidth_0

> Object updateNetworkApplianceTrafficShapingUplinkBandwidth_0(networkId, opts)

Updates the uplink bandwidth settings for your MX network.

Updates the uplink bandwidth settings for your MX network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceTrafficShapingUplinkBandwidthRequest': new MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest() // UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest | 
};
apiInstance.updateNetworkApplianceTrafficShapingUplinkBandwidth_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceTrafficShapingUplinkBandwidthRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest**](UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceTrafficShapingUplinkSelection_0

> GetNetworkApplianceTrafficShapingUplinkSelection200Response updateNetworkApplianceTrafficShapingUplinkSelection_0(networkId, opts)

Update uplink selection settings for an MX network

Update uplink selection settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceTrafficShapingUplinkSelectionRequest': new MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest() // UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest | 
};
apiInstance.updateNetworkApplianceTrafficShapingUplinkSelection_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceTrafficShapingUplinkSelectionRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.md)|  | [optional] 

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceTrafficShaping_0

> Object updateNetworkApplianceTrafficShaping_0(networkId, opts)

Update the traffic shaping settings for an MX network

Update the traffic shaping settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceTrafficShapingRequest': new MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingRequest() // UpdateNetworkApplianceTrafficShapingRequest | 
};
apiInstance.updateNetworkApplianceTrafficShaping_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceTrafficShapingRequest** | [**UpdateNetworkApplianceTrafficShapingRequest**](UpdateNetworkApplianceTrafficShapingRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceVlan_0

> GetNetworkApplianceVlans200ResponseInner updateNetworkApplianceVlan_0(networkId, vlanId, opts)

Update a VLAN

Update a VLAN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let vlanId = "vlanId_example"; // String | 
let opts = {
  'updateNetworkApplianceVlanRequest': new MerakiDashboardApi.UpdateNetworkApplianceVlanRequest() // UpdateNetworkApplianceVlanRequest | 
};
apiInstance.updateNetworkApplianceVlan_0(networkId, vlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **vlanId** | **String**|  | 
 **updateNetworkApplianceVlanRequest** | [**UpdateNetworkApplianceVlanRequest**](UpdateNetworkApplianceVlanRequest.md)|  | [optional] 

### Return type

[**GetNetworkApplianceVlans200ResponseInner**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceVlansSettings_0

> Object updateNetworkApplianceVlansSettings_0(networkId, opts)

Enable/Disable VLANs for the given network

Enable/Disable VLANs for the given network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceVlansSettingsRequest': new MerakiDashboardApi.UpdateNetworkApplianceVlansSettingsRequest() // UpdateNetworkApplianceVlansSettingsRequest | 
};
apiInstance.updateNetworkApplianceVlansSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceVlansSettingsRequest** | [**UpdateNetworkApplianceVlansSettingsRequest**](UpdateNetworkApplianceVlansSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceVpnBgp_0

> Object updateNetworkApplianceVpnBgp_0(networkId, updateNetworkApplianceVpnBgpRequest)

Update a Hub BGP Configuration

Update a Hub BGP Configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceVpnBgpRequest = new MerakiDashboardApi.UpdateNetworkApplianceVpnBgpRequest(); // UpdateNetworkApplianceVpnBgpRequest | 
apiInstance.updateNetworkApplianceVpnBgp_0(networkId, updateNetworkApplianceVpnBgpRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceVpnBgpRequest** | [**UpdateNetworkApplianceVpnBgpRequest**](UpdateNetworkApplianceVpnBgpRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceVpnSiteToSiteVpn_0

> GetNetworkApplianceVpnSiteToSiteVpn200Response updateNetworkApplianceVpnSiteToSiteVpn_0(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest)

Update the site-to-site VPN settings of a network

Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceVpnSiteToSiteVpnRequest = new MerakiDashboardApi.UpdateNetworkApplianceVpnSiteToSiteVpnRequest(); // UpdateNetworkApplianceVpnSiteToSiteVpnRequest | 
apiInstance.updateNetworkApplianceVpnSiteToSiteVpn_0(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceVpnSiteToSiteVpnRequest** | [**UpdateNetworkApplianceVpnSiteToSiteVpnRequest**](UpdateNetworkApplianceVpnSiteToSiteVpnRequest.md)|  | 

### Return type

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceWarmSpare_0

> Object updateNetworkApplianceWarmSpare_0(networkId, updateNetworkApplianceWarmSpareRequest)

Update MX warm spare settings

Update MX warm spare settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceWarmSpareRequest = new MerakiDashboardApi.UpdateNetworkApplianceWarmSpareRequest(); // UpdateNetworkApplianceWarmSpareRequest | 
apiInstance.updateNetworkApplianceWarmSpare_0(networkId, updateNetworkApplianceWarmSpareRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkApplianceWarmSpareRequest** | [**UpdateNetworkApplianceWarmSpareRequest**](UpdateNetworkApplianceWarmSpareRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCameraQualityRetentionProfile_0

> Object updateNetworkCameraQualityRetentionProfile_0(networkId, qualityRetentionProfileId, opts)

Update an existing quality retention profile for this network.

Update an existing quality retention profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
let opts = {
  'updateNetworkCameraQualityRetentionProfileRequest': new MerakiDashboardApi.UpdateNetworkCameraQualityRetentionProfileRequest() // UpdateNetworkCameraQualityRetentionProfileRequest | 
};
apiInstance.updateNetworkCameraQualityRetentionProfile_0(networkId, qualityRetentionProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **qualityRetentionProfileId** | **String**|  | 
 **updateNetworkCameraQualityRetentionProfileRequest** | [**UpdateNetworkCameraQualityRetentionProfileRequest**](UpdateNetworkCameraQualityRetentionProfileRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCameraWirelessProfile_0

> Object updateNetworkCameraWirelessProfile_0(networkId, wirelessProfileId, opts)

Update an existing camera wireless profile in this network.

Update an existing camera wireless profile in this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let wirelessProfileId = "wirelessProfileId_example"; // String | 
let opts = {
  'updateNetworkCameraWirelessProfileRequest': new MerakiDashboardApi.UpdateNetworkCameraWirelessProfileRequest() // UpdateNetworkCameraWirelessProfileRequest | 
};
apiInstance.updateNetworkCameraWirelessProfile_0(networkId, wirelessProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **wirelessProfileId** | **String**|  | 
 **updateNetworkCameraWirelessProfileRequest** | [**UpdateNetworkCameraWirelessProfileRequest**](UpdateNetworkCameraWirelessProfileRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCellularGatewayConnectivityMonitoringDestinations_0

> Object updateNetworkCellularGatewayConnectivityMonitoringDestinations_0(networkId, opts)

Update the connectivity testing destinations for an MG network

Update the connectivity testing destinations for an MG network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest': new MerakiDashboardApi.UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest() // UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest | 
};
apiInstance.updateNetworkCellularGatewayConnectivityMonitoringDestinations_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest**](UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCellularGatewayDhcp_0

> GetNetworkCellularGatewayDhcp200Response updateNetworkCellularGatewayDhcp_0(networkId, opts)

Update common DHCP settings of MGs

Update common DHCP settings of MGs

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkCellularGatewayDhcpRequest': new MerakiDashboardApi.UpdateNetworkCellularGatewayDhcpRequest() // UpdateNetworkCellularGatewayDhcpRequest | 
};
apiInstance.updateNetworkCellularGatewayDhcp_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkCellularGatewayDhcpRequest** | [**UpdateNetworkCellularGatewayDhcpRequest**](UpdateNetworkCellularGatewayDhcpRequest.md)|  | [optional] 

### Return type

[**GetNetworkCellularGatewayDhcp200Response**](GetNetworkCellularGatewayDhcp200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCellularGatewaySubnetPool_0

> Object updateNetworkCellularGatewaySubnetPool_0(networkId, opts)

Update the subnet pool and mask configuration for MGs in the network.

Update the subnet pool and mask configuration for MGs in the network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkCellularGatewaySubnetPoolRequest': new MerakiDashboardApi.UpdateNetworkCellularGatewaySubnetPoolRequest() // UpdateNetworkCellularGatewaySubnetPoolRequest | 
};
apiInstance.updateNetworkCellularGatewaySubnetPool_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkCellularGatewaySubnetPoolRequest** | [**UpdateNetworkCellularGatewaySubnetPoolRequest**](UpdateNetworkCellularGatewaySubnetPoolRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCellularGatewayUplink_0

> Object updateNetworkCellularGatewayUplink_0(networkId, opts)

Updates the uplink settings for your MG network.

Updates the uplink settings for your MG network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkCellularGatewayUplinkRequest': new MerakiDashboardApi.UpdateNetworkCellularGatewayUplinkRequest() // UpdateNetworkCellularGatewayUplinkRequest | 
};
apiInstance.updateNetworkCellularGatewayUplink_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkCellularGatewayUplinkRequest** | [**UpdateNetworkCellularGatewayUplinkRequest**](UpdateNetworkCellularGatewayUplinkRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkClientPolicy_0

> Object updateNetworkClientPolicy_0(networkId, clientId, updateNetworkClientPolicyRequest)

Update the policy assigned to a client on the network

Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let updateNetworkClientPolicyRequest = new MerakiDashboardApi.UpdateNetworkClientPolicyRequest(); // UpdateNetworkClientPolicyRequest | 
apiInstance.updateNetworkClientPolicy_0(networkId, clientId, updateNetworkClientPolicyRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 
 **updateNetworkClientPolicyRequest** | [**UpdateNetworkClientPolicyRequest**](UpdateNetworkClientPolicyRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkClientSplashAuthorizationStatus_0

> Object updateNetworkClientSplashAuthorizationStatus_0(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest)

Update a client&#39;s splash authorization

Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let updateNetworkClientSplashAuthorizationStatusRequest = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequest(); // UpdateNetworkClientSplashAuthorizationStatusRequest | 
apiInstance.updateNetworkClientSplashAuthorizationStatus_0(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 
 **updateNetworkClientSplashAuthorizationStatusRequest** | [**UpdateNetworkClientSplashAuthorizationStatusRequest**](UpdateNetworkClientSplashAuthorizationStatusRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedEvents_0

> GetNetworkFirmwareUpgradesStagedEvents200Response updateNetworkFirmwareUpgradesStagedEvents_0(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest)

Update the Staged Upgrade Event for a network

Update the Staged Upgrade Event for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkFirmwareUpgradesStagedEventsRequest = new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesStagedEventsRequest(); // UpdateNetworkFirmwareUpgradesStagedEventsRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedEvents_0(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkFirmwareUpgradesStagedEventsRequest** | [**UpdateNetworkFirmwareUpgradesStagedEventsRequest**](UpdateNetworkFirmwareUpgradesStagedEventsRequest.md)|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedGroup_0

> Object updateNetworkFirmwareUpgradesStagedGroup_0(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

Update a Staged Upgrade Group for a network

Update a Staged Upgrade Group for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedGroup_0(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **groupId** | **String**|  | 
 **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedStages_0

> [GetNetworkFirmwareUpgradesStagedStages200ResponseInner] updateNetworkFirmwareUpgradesStagedStages_0(networkId, opts)

Assign Staged Upgrade Group order in the sequence.

Assign Staged Upgrade Group order in the sequence.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkFirmwareUpgradesStagedStagesRequest': new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesStagedStagesRequest() // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
};
apiInstance.updateNetworkFirmwareUpgradesStagedStages_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkFirmwareUpgradesStagedStagesRequest** | [**UpdateNetworkFirmwareUpgradesStagedStagesRequest**](UpdateNetworkFirmwareUpgradesStagedStagesRequest.md)|  | [optional] 

### Return type

[**[GetNetworkFirmwareUpgradesStagedStages200ResponseInner]**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgrades_0

> GetNetworkFirmwareUpgrades200Response updateNetworkFirmwareUpgrades_0(networkId, opts)

Update firmware upgrade information for a network

Update firmware upgrade information for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkFirmwareUpgradesRequest': new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesRequest() // UpdateNetworkFirmwareUpgradesRequest | 
};
apiInstance.updateNetworkFirmwareUpgrades_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkFirmwareUpgradesRequest** | [**UpdateNetworkFirmwareUpgradesRequest**](UpdateNetworkFirmwareUpgradesRequest.md)|  | [optional] 

### Return type

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFloorPlan_0

> Object updateNetworkFloorPlan_0(networkId, floorPlanId, opts)

Update a floor plan&#39;s geolocation and other meta data

Update a floor plan&#39;s geolocation and other meta data

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let floorPlanId = "floorPlanId_example"; // String | 
let opts = {
  'updateNetworkFloorPlanRequest': new MerakiDashboardApi.UpdateNetworkFloorPlanRequest() // UpdateNetworkFloorPlanRequest | 
};
apiInstance.updateNetworkFloorPlan_0(networkId, floorPlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **floorPlanId** | **String**|  | 
 **updateNetworkFloorPlanRequest** | [**UpdateNetworkFloorPlanRequest**](UpdateNetworkFloorPlanRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkGroupPolicy_0

> Object updateNetworkGroupPolicy_0(networkId, groupPolicyId, opts)

Update a group policy

Update a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let groupPolicyId = "groupPolicyId_example"; // String | 
let opts = {
  'updateNetworkGroupPolicyRequest': new MerakiDashboardApi.UpdateNetworkGroupPolicyRequest() // UpdateNetworkGroupPolicyRequest | 
};
apiInstance.updateNetworkGroupPolicy_0(networkId, groupPolicyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **groupPolicyId** | **String**|  | 
 **updateNetworkGroupPolicyRequest** | [**UpdateNetworkGroupPolicyRequest**](UpdateNetworkGroupPolicyRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkMerakiAuthUser_0

> GetNetworkMerakiAuthUsers200ResponseInner updateNetworkMerakiAuthUser_0(networkId, merakiAuthUserId, opts)

Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let merakiAuthUserId = "merakiAuthUserId_example"; // String | 
let opts = {
  'updateNetworkMerakiAuthUserRequest': new MerakiDashboardApi.UpdateNetworkMerakiAuthUserRequest() // UpdateNetworkMerakiAuthUserRequest | 
};
apiInstance.updateNetworkMerakiAuthUser_0(networkId, merakiAuthUserId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **merakiAuthUserId** | **String**|  | 
 **updateNetworkMerakiAuthUserRequest** | [**UpdateNetworkMerakiAuthUserRequest**](UpdateNetworkMerakiAuthUserRequest.md)|  | [optional] 

### Return type

[**GetNetworkMerakiAuthUsers200ResponseInner**](GetNetworkMerakiAuthUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkMqttBroker_0

> Object updateNetworkMqttBroker_0(networkId, mqttBrokerId, opts)

Update an MQTT broker

Update an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let mqttBrokerId = "mqttBrokerId_example"; // String | 
let opts = {
  'updateNetworkMqttBrokerRequest': new MerakiDashboardApi.UpdateNetworkMqttBrokerRequest() // UpdateNetworkMqttBrokerRequest | 
};
apiInstance.updateNetworkMqttBroker_0(networkId, mqttBrokerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **mqttBrokerId** | **String**|  | 
 **updateNetworkMqttBrokerRequest** | [**UpdateNetworkMqttBrokerRequest**](UpdateNetworkMqttBrokerRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkNetflow_0

> Object updateNetworkNetflow_0(networkId, opts)

Update the NetFlow traffic reporting settings for a network

Update the NetFlow traffic reporting settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkNetflowRequest': new MerakiDashboardApi.UpdateNetworkNetflowRequest() // UpdateNetworkNetflowRequest | 
};
apiInstance.updateNetworkNetflow_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkNetflowRequest** | [**UpdateNetworkNetflowRequest**](UpdateNetworkNetflowRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSensorAlertsProfile_0

> GetNetworkSensorAlertsProfiles200ResponseInner updateNetworkSensorAlertsProfile_0(networkId, id, opts)

Updates a sensor alert profile for a network.

Updates a sensor alert profile for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateNetworkSensorAlertsProfileRequest': new MerakiDashboardApi.UpdateNetworkSensorAlertsProfileRequest() // UpdateNetworkSensorAlertsProfileRequest | 
};
apiInstance.updateNetworkSensorAlertsProfile_0(networkId, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **id** | **String**|  | 
 **updateNetworkSensorAlertsProfileRequest** | [**UpdateNetworkSensorAlertsProfileRequest**](UpdateNetworkSensorAlertsProfileRequest.md)|  | [optional] 

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSettings_0

> GetNetworkSettings200Response updateNetworkSettings_0(networkId, opts)

Update the settings for a network

Update the settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSettingsRequest': new MerakiDashboardApi.UpdateNetworkSettingsRequest() // UpdateNetworkSettingsRequest | 
};
apiInstance.updateNetworkSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSettingsRequest** | [**UpdateNetworkSettingsRequest**](UpdateNetworkSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkSettings200Response**](GetNetworkSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSmDevicesFields_0

> [UpdateNetworkSmDevicesFields200ResponseInner] updateNetworkSmDevicesFields_0(networkId, updateNetworkSmDevicesFieldsRequest)

Modify the fields of a device

Modify the fields of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSmDevicesFieldsRequest = new MerakiDashboardApi.UpdateNetworkSmDevicesFieldsRequest(); // UpdateNetworkSmDevicesFieldsRequest | 
apiInstance.updateNetworkSmDevicesFields_0(networkId, updateNetworkSmDevicesFieldsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSmDevicesFieldsRequest** | [**UpdateNetworkSmDevicesFieldsRequest**](UpdateNetworkSmDevicesFieldsRequest.md)|  | 

### Return type

[**[UpdateNetworkSmDevicesFields200ResponseInner]**](UpdateNetworkSmDevicesFields200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSmTargetGroup_0

> Object updateNetworkSmTargetGroup_0(networkId, targetGroupId, opts)

Update a target group

Update a target group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let targetGroupId = "targetGroupId_example"; // String | 
let opts = {
  'createNetworkSmTargetGroupRequest': new MerakiDashboardApi.CreateNetworkSmTargetGroupRequest() // CreateNetworkSmTargetGroupRequest | 
};
apiInstance.updateNetworkSmTargetGroup_0(networkId, targetGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **targetGroupId** | **String**|  | 
 **createNetworkSmTargetGroupRequest** | [**CreateNetworkSmTargetGroupRequest**](CreateNetworkSmTargetGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSnmp_0

> Object updateNetworkSnmp_0(networkId, opts)

Update the SNMP settings for a network

Update the SNMP settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSnmpRequest': new MerakiDashboardApi.UpdateNetworkSnmpRequest() // UpdateNetworkSnmpRequest | 
};
apiInstance.updateNetworkSnmp_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSnmpRequest** | [**UpdateNetworkSnmpRequest**](UpdateNetworkSnmpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchAccessControlLists_0

> GetNetworkSwitchAccessControlLists200Response updateNetworkSwitchAccessControlLists_0(networkId, updateNetworkSwitchAccessControlListsRequest)

Update the access control lists for a MS network

Update the access control lists for a MS network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSwitchAccessControlListsRequest = new MerakiDashboardApi.UpdateNetworkSwitchAccessControlListsRequest(); // UpdateNetworkSwitchAccessControlListsRequest | 
apiInstance.updateNetworkSwitchAccessControlLists_0(networkId, updateNetworkSwitchAccessControlListsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchAccessControlListsRequest** | [**UpdateNetworkSwitchAccessControlListsRequest**](UpdateNetworkSwitchAccessControlListsRequest.md)|  | 

### Return type

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchAccessPolicy_0

> GetNetworkSwitchAccessPolicies200ResponseInner updateNetworkSwitchAccessPolicy_0(networkId, accessPolicyNumber, opts)

Update an access policy for a switch network

Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let accessPolicyNumber = "accessPolicyNumber_example"; // String | 
let opts = {
  'updateNetworkSwitchAccessPolicyRequest': new MerakiDashboardApi.UpdateNetworkSwitchAccessPolicyRequest() // UpdateNetworkSwitchAccessPolicyRequest | 
};
apiInstance.updateNetworkSwitchAccessPolicy_0(networkId, accessPolicyNumber, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **accessPolicyNumber** | **String**|  | 
 **updateNetworkSwitchAccessPolicyRequest** | [**UpdateNetworkSwitchAccessPolicyRequest**](UpdateNetworkSwitchAccessPolicyRequest.md)|  | [optional] 

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchAlternateManagementInterface_0

> Object updateNetworkSwitchAlternateManagementInterface_0(networkId, opts)

Update the switch alternate management interface for the network

Update the switch alternate management interface for the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchAlternateManagementInterfaceRequest': new MerakiDashboardApi.UpdateNetworkSwitchAlternateManagementInterfaceRequest() // UpdateNetworkSwitchAlternateManagementInterfaceRequest | 
};
apiInstance.updateNetworkSwitchAlternateManagementInterface_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchAlternateManagementInterfaceRequest** | [**UpdateNetworkSwitchAlternateManagementInterfaceRequest**](UpdateNetworkSwitchAlternateManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0

> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0(networkId, trustedServerId, opts)

Update a server that is trusted by Dynamic ARP Inspection on this network

Update a server that is trusted by Dynamic ARP Inspection on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let trustedServerId = "trustedServerId_example"; // String | 
let opts = {
  'updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest': new MerakiDashboardApi.UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest() // UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
};
apiInstance.updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_0(networkId, trustedServerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **trustedServerId** | **String**|  | 
 **updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest** | [**UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest**](UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.md)|  | [optional] 

### Return type

[**GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchDhcpServerPolicy_0

> Object updateNetworkSwitchDhcpServerPolicy_0(networkId, opts)

Update the DHCP server settings

Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchDhcpServerPolicyRequest': new MerakiDashboardApi.UpdateNetworkSwitchDhcpServerPolicyRequest() // UpdateNetworkSwitchDhcpServerPolicyRequest | 
};
apiInstance.updateNetworkSwitchDhcpServerPolicy_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchDhcpServerPolicyRequest** | [**UpdateNetworkSwitchDhcpServerPolicyRequest**](UpdateNetworkSwitchDhcpServerPolicyRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchDscpToCosMappings_0

> Object updateNetworkSwitchDscpToCosMappings_0(networkId, updateNetworkSwitchDscpToCosMappingsRequest)

Update the DSCP to CoS mappings

Update the DSCP to CoS mappings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSwitchDscpToCosMappingsRequest = new MerakiDashboardApi.UpdateNetworkSwitchDscpToCosMappingsRequest(); // UpdateNetworkSwitchDscpToCosMappingsRequest | 
apiInstance.updateNetworkSwitchDscpToCosMappings_0(networkId, updateNetworkSwitchDscpToCosMappingsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchDscpToCosMappingsRequest** | [**UpdateNetworkSwitchDscpToCosMappingsRequest**](UpdateNetworkSwitchDscpToCosMappingsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchLinkAggregation_0

> Object updateNetworkSwitchLinkAggregation_0(networkId, linkAggregationId, opts)

Update a link aggregation group

Update a link aggregation group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let linkAggregationId = "linkAggregationId_example"; // String | 
let opts = {
  'updateNetworkSwitchLinkAggregationRequest': new MerakiDashboardApi.UpdateNetworkSwitchLinkAggregationRequest() // UpdateNetworkSwitchLinkAggregationRequest | 
};
apiInstance.updateNetworkSwitchLinkAggregation_0(networkId, linkAggregationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **linkAggregationId** | **String**|  | 
 **updateNetworkSwitchLinkAggregationRequest** | [**UpdateNetworkSwitchLinkAggregationRequest**](UpdateNetworkSwitchLinkAggregationRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchMtu_0

> Object updateNetworkSwitchMtu_0(networkId, opts)

Update the MTU configuration

Update the MTU configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchMtuRequest': new MerakiDashboardApi.UpdateNetworkSwitchMtuRequest() // UpdateNetworkSwitchMtuRequest | 
};
apiInstance.updateNetworkSwitchMtu_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchMtuRequest** | [**UpdateNetworkSwitchMtuRequest**](UpdateNetworkSwitchMtuRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchPortSchedule_0

> Object updateNetworkSwitchPortSchedule_0(networkId, portScheduleId, opts)

Update a switch port schedule

Update a switch port schedule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let portScheduleId = "portScheduleId_example"; // String | 
let opts = {
  'updateNetworkSwitchPortScheduleRequest': new MerakiDashboardApi.UpdateNetworkSwitchPortScheduleRequest() // UpdateNetworkSwitchPortScheduleRequest | 
};
apiInstance.updateNetworkSwitchPortSchedule_0(networkId, portScheduleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **portScheduleId** | **String**|  | 
 **updateNetworkSwitchPortScheduleRequest** | [**UpdateNetworkSwitchPortScheduleRequest**](UpdateNetworkSwitchPortScheduleRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchQosRule_0

> Object updateNetworkSwitchQosRule_0(networkId, qosRuleId, opts)

Update a quality of service rule

Update a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let qosRuleId = "qosRuleId_example"; // String | 
let opts = {
  'updateNetworkSwitchQosRuleRequest': new MerakiDashboardApi.UpdateNetworkSwitchQosRuleRequest() // UpdateNetworkSwitchQosRuleRequest | 
};
apiInstance.updateNetworkSwitchQosRule_0(networkId, qosRuleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **qosRuleId** | **String**|  | 
 **updateNetworkSwitchQosRuleRequest** | [**UpdateNetworkSwitchQosRuleRequest**](UpdateNetworkSwitchQosRuleRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchQosRulesOrder_0

> Object updateNetworkSwitchQosRulesOrder_0(networkId, updateNetworkSwitchQosRulesOrderRequest)

Update the order in which the rules should be processed by the switch

Update the order in which the rules should be processed by the switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSwitchQosRulesOrderRequest = new MerakiDashboardApi.UpdateNetworkSwitchQosRulesOrderRequest(); // UpdateNetworkSwitchQosRulesOrderRequest | 
apiInstance.updateNetworkSwitchQosRulesOrder_0(networkId, updateNetworkSwitchQosRulesOrderRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchQosRulesOrderRequest** | [**UpdateNetworkSwitchQosRulesOrderRequest**](UpdateNetworkSwitchQosRulesOrderRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchRoutingMulticastRendezvousPoint_0

> Object updateNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

Update a multicast rendezvous point

Update a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
let updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new MerakiDashboardApi.UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint_0(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rendezvousPointId** | **String**|  | 
 **updateNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest**](UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchRoutingMulticast_0

> Object updateNetworkSwitchRoutingMulticast_0(networkId, opts)

Update multicast settings for a network

Update multicast settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchRoutingMulticastRequest': new MerakiDashboardApi.UpdateNetworkSwitchRoutingMulticastRequest() // UpdateNetworkSwitchRoutingMulticastRequest | 
};
apiInstance.updateNetworkSwitchRoutingMulticast_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchRoutingMulticastRequest** | [**UpdateNetworkSwitchRoutingMulticastRequest**](UpdateNetworkSwitchRoutingMulticastRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchRoutingOspf_0

> Object updateNetworkSwitchRoutingOspf_0(networkId, opts)

Update layer 3 OSPF routing configuration

Update layer 3 OSPF routing configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchRoutingOspfRequest': new MerakiDashboardApi.UpdateNetworkSwitchRoutingOspfRequest() // UpdateNetworkSwitchRoutingOspfRequest | 
};
apiInstance.updateNetworkSwitchRoutingOspf_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchRoutingOspfRequest** | [**UpdateNetworkSwitchRoutingOspfRequest**](UpdateNetworkSwitchRoutingOspfRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchSettings_0

> GetNetworkSwitchSettings200Response updateNetworkSwitchSettings_0(networkId, opts)

Update switch network settings

Update switch network settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchSettingsRequest': new MerakiDashboardApi.UpdateNetworkSwitchSettingsRequest() // UpdateNetworkSwitchSettingsRequest | 
};
apiInstance.updateNetworkSwitchSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchSettingsRequest** | [**UpdateNetworkSwitchSettingsRequest**](UpdateNetworkSwitchSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkSwitchSettings200Response**](GetNetworkSwitchSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchStackRoutingInterfaceDhcp_0

> Object updateNetworkSwitchStackRoutingInterfaceDhcp_0(networkId, switchStackId, interfaceId, opts)

Update a layer 3 interface DHCP configuration for a switch stack

Update a layer 3 interface DHCP configuration for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
let opts = {
  'updateNetworkSwitchStackRoutingInterfaceDhcpRequest': new MerakiDashboardApi.UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest() // UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest | 
};
apiInstance.updateNetworkSwitchStackRoutingInterfaceDhcp_0(networkId, switchStackId, interfaceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **interfaceId** | **String**|  | 
 **updateNetworkSwitchStackRoutingInterfaceDhcpRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest**](UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchStackRoutingInterface_0

> Object updateNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, interfaceId, opts)

Update a layer 3 interface for a switch stack

Update a layer 3 interface for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let interfaceId = "interfaceId_example"; // String | 
let opts = {
  'updateNetworkSwitchStackRoutingInterfaceRequest': new MerakiDashboardApi.UpdateNetworkSwitchStackRoutingInterfaceRequest() // UpdateNetworkSwitchStackRoutingInterfaceRequest | 
};
apiInstance.updateNetworkSwitchStackRoutingInterface_0(networkId, switchStackId, interfaceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **interfaceId** | **String**|  | 
 **updateNetworkSwitchStackRoutingInterfaceRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceRequest**](UpdateNetworkSwitchStackRoutingInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchStackRoutingStaticRoute_0

> Object updateNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, staticRouteId, opts)

Update a layer 3 static route for a switch stack

Update a layer 3 static route for a switch stack

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let switchStackId = "switchStackId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
let opts = {
  'updateDeviceSwitchRoutingStaticRouteRequest': new MerakiDashboardApi.UpdateDeviceSwitchRoutingStaticRouteRequest() // UpdateDeviceSwitchRoutingStaticRouteRequest | 
};
apiInstance.updateNetworkSwitchStackRoutingStaticRoute_0(networkId, switchStackId, staticRouteId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **switchStackId** | **String**|  | 
 **staticRouteId** | **String**|  | 
 **updateDeviceSwitchRoutingStaticRouteRequest** | [**UpdateDeviceSwitchRoutingStaticRouteRequest**](UpdateDeviceSwitchRoutingStaticRouteRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchStormControl_0

> Object updateNetworkSwitchStormControl_0(networkId, opts)

Update the storm control configuration for a switch network

Update the storm control configuration for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchStormControlRequest': new MerakiDashboardApi.UpdateNetworkSwitchStormControlRequest() // UpdateNetworkSwitchStormControlRequest | 
};
apiInstance.updateNetworkSwitchStormControl_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchStormControlRequest** | [**UpdateNetworkSwitchStormControlRequest**](UpdateNetworkSwitchStormControlRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchStp_0

> Object updateNetworkSwitchStp_0(networkId, opts)

Updates STP settings

Updates STP settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchStpRequest': new MerakiDashboardApi.UpdateNetworkSwitchStpRequest() // UpdateNetworkSwitchStpRequest | 
};
apiInstance.updateNetworkSwitchStp_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSwitchStpRequest** | [**UpdateNetworkSwitchStpRequest**](UpdateNetworkSwitchStpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSyslogServers_0

> GetNetworkSyslogServers200Response updateNetworkSyslogServers_0(networkId, updateNetworkSyslogServersRequest)

Update the syslog servers for a network

Update the syslog servers for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSyslogServersRequest = new MerakiDashboardApi.UpdateNetworkSyslogServersRequest(); // UpdateNetworkSyslogServersRequest | 
apiInstance.updateNetworkSyslogServers_0(networkId, updateNetworkSyslogServersRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkSyslogServersRequest** | [**UpdateNetworkSyslogServersRequest**](UpdateNetworkSyslogServersRequest.md)|  | 

### Return type

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkTrafficAnalysis_0

> Object updateNetworkTrafficAnalysis_0(networkId, opts)

Update the traffic analysis settings for a network

Update the traffic analysis settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkTrafficAnalysisRequest': new MerakiDashboardApi.UpdateNetworkTrafficAnalysisRequest() // UpdateNetworkTrafficAnalysisRequest | 
};
apiInstance.updateNetworkTrafficAnalysis_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkTrafficAnalysisRequest** | [**UpdateNetworkTrafficAnalysisRequest**](UpdateNetworkTrafficAnalysisRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWebhooksHttpServer_0

> GetNetworkWebhooksHttpServers200ResponseInner updateNetworkWebhooksHttpServer_0(networkId, httpServerId, opts)

Update an HTTP server

Update an HTTP server. To change a URL, create a new HTTP server.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let httpServerId = "httpServerId_example"; // String | 
let opts = {
  'updateNetworkWebhooksHttpServerRequest': new MerakiDashboardApi.UpdateNetworkWebhooksHttpServerRequest() // UpdateNetworkWebhooksHttpServerRequest | 
};
apiInstance.updateNetworkWebhooksHttpServer_0(networkId, httpServerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **httpServerId** | **String**|  | 
 **updateNetworkWebhooksHttpServerRequest** | [**UpdateNetworkWebhooksHttpServerRequest**](UpdateNetworkWebhooksHttpServerRequest.md)|  | [optional] 

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWebhooksPayloadTemplate_0

> GetNetworkWebhooksPayloadTemplates200ResponseInner updateNetworkWebhooksPayloadTemplate_0(networkId, payloadTemplateId, opts)

Update a webhook payload template for a network

Update a webhook payload template for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let payloadTemplateId = "payloadTemplateId_example"; // String | 
let opts = {
  'updateNetworkWebhooksPayloadTemplateRequest': new MerakiDashboardApi.UpdateNetworkWebhooksPayloadTemplateRequest() // UpdateNetworkWebhooksPayloadTemplateRequest | 
};
apiInstance.updateNetworkWebhooksPayloadTemplate_0(networkId, payloadTemplateId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **payloadTemplateId** | **String**|  | 
 **updateNetworkWebhooksPayloadTemplateRequest** | [**UpdateNetworkWebhooksPayloadTemplateRequest**](UpdateNetworkWebhooksPayloadTemplateRequest.md)|  | [optional] 

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessAlternateManagementInterface_0

> Object updateNetworkWirelessAlternateManagementInterface_0(networkId, opts)

Update alternate management interface and device static IP

Update alternate management interface and device static IP

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessAlternateManagementInterfaceRequest': new MerakiDashboardApi.UpdateNetworkWirelessAlternateManagementInterfaceRequest() // UpdateNetworkWirelessAlternateManagementInterfaceRequest | 
};
apiInstance.updateNetworkWirelessAlternateManagementInterface_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessAlternateManagementInterfaceRequest** | [**UpdateNetworkWirelessAlternateManagementInterfaceRequest**](UpdateNetworkWirelessAlternateManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessBilling_0

> Object updateNetworkWirelessBilling_0(networkId, opts)

Update the billing settings

Update the billing settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessBillingRequest': new MerakiDashboardApi.UpdateNetworkWirelessBillingRequest() // UpdateNetworkWirelessBillingRequest | 
};
apiInstance.updateNetworkWirelessBilling_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessBillingRequest** | [**UpdateNetworkWirelessBillingRequest**](UpdateNetworkWirelessBillingRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessBluetoothSettings_0

> GetNetworkWirelessBluetoothSettings200Response updateNetworkWirelessBluetoothSettings_0(networkId, opts)

Update the Bluetooth settings for a network

Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessBluetoothSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessBluetoothSettingsRequest() // UpdateNetworkWirelessBluetoothSettingsRequest | 
};
apiInstance.updateNetworkWirelessBluetoothSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessBluetoothSettingsRequest** | [**UpdateNetworkWirelessBluetoothSettingsRequest**](UpdateNetworkWirelessBluetoothSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessRfProfile_0

> CreateNetworkWirelessRfProfile201Response updateNetworkWirelessRfProfile_0(networkId, rfProfileId, opts)

Updates specified RF profile for this network

Updates specified RF profile for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
let opts = {
  'updateNetworkWirelessRfProfileRequest': new MerakiDashboardApi.UpdateNetworkWirelessRfProfileRequest() // UpdateNetworkWirelessRfProfileRequest | 
};
apiInstance.updateNetworkWirelessRfProfile_0(networkId, rfProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rfProfileId** | **String**|  | 
 **updateNetworkWirelessRfProfileRequest** | [**UpdateNetworkWirelessRfProfileRequest**](UpdateNetworkWirelessRfProfileRequest.md)|  | [optional] 

### Return type

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSettings_0

> GetNetworkWirelessSettings200Response updateNetworkWirelessSettings_0(networkId, opts)

Update the wireless settings for a network

Update the wireless settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessSettingsRequest() // UpdateNetworkWirelessSettingsRequest | 
};
apiInstance.updateNetworkWirelessSettings_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessSettingsRequest** | [**UpdateNetworkWirelessSettingsRequest**](UpdateNetworkWirelessSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessSettings200Response**](GetNetworkWirelessSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidBonjourForwarding_0

> Object updateNetworkWirelessSsidBonjourForwarding_0(networkId, number, opts)

Update the bonjour forwarding setting and rules for the SSID

Update the bonjour forwarding setting and rules for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidBonjourForwardingRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidBonjourForwardingRequest() // UpdateNetworkWirelessSsidBonjourForwardingRequest | 
};
apiInstance.updateNetworkWirelessSsidBonjourForwarding_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidBonjourForwardingRequest** | [**UpdateNetworkWirelessSsidBonjourForwardingRequest**](UpdateNetworkWirelessSsidBonjourForwardingRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidDeviceTypeGroupPolicies_0

> Object updateNetworkWirelessSsidDeviceTypeGroupPolicies_0(networkId, number, opts)

Update the device type group policies for the SSID

Update the device type group policies for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest() // UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest | 
};
apiInstance.updateNetworkWirelessSsidDeviceTypeGroupPolicies_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest** | [**UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest**](UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidEapOverride_0

> GetNetworkWirelessSsidEapOverride200Response updateNetworkWirelessSsidEapOverride_0(networkId, number, opts)

Update the EAP overridden parameters for an SSID.

Update the EAP overridden parameters for an SSID.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidEapOverrideRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidEapOverrideRequest() // UpdateNetworkWirelessSsidEapOverrideRequest | 
};
apiInstance.updateNetworkWirelessSsidEapOverride_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidEapOverrideRequest** | [**UpdateNetworkWirelessSsidEapOverrideRequest**](UpdateNetworkWirelessSsidEapOverrideRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessSsidEapOverride200Response**](GetNetworkWirelessSsidEapOverride200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL3FirewallRules_0

> Object updateNetworkWirelessSsidFirewallL3FirewallRules_0(networkId, number, opts)

Update the L3 firewall rules of an SSID on an MR network

Update the L3 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL3FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidFirewallL3FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL7FirewallRules_0

> Object updateNetworkWirelessSsidFirewallL7FirewallRules_0(networkId, number, opts)

Update the L7 firewall rules of an SSID on an MR network

Update the L7 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL7FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL7FirewallRules_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidFirewallL7FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidHotspot20_0

> Object updateNetworkWirelessSsidHotspot20_0(networkId, number, opts)

Update the Hotspot 2.0 settings of an SSID

Update the Hotspot 2.0 settings of an SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidHotspot20Request': new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request() // UpdateNetworkWirelessSsidHotspot20Request | 
};
apiInstance.updateNetworkWirelessSsidHotspot20_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidHotspot20Request** | [**UpdateNetworkWirelessSsidHotspot20Request**](UpdateNetworkWirelessSsidHotspot20Request.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidIdentityPsk_0

> Object updateNetworkWirelessSsidIdentityPsk_0(networkId, number, identityPskId, opts)

Update an Identity PSK

Update an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let identityPskId = "identityPskId_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidIdentityPskRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidIdentityPskRequest() // UpdateNetworkWirelessSsidIdentityPskRequest | 
};
apiInstance.updateNetworkWirelessSsidIdentityPsk_0(networkId, number, identityPskId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **identityPskId** | **String**|  | 
 **updateNetworkWirelessSsidIdentityPskRequest** | [**UpdateNetworkWirelessSsidIdentityPskRequest**](UpdateNetworkWirelessSsidIdentityPskRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidSchedules_0

> Object updateNetworkWirelessSsidSchedules_0(networkId, number, opts)

Update the outage schedule for the SSID

Update the outage schedule for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidSchedulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidSchedulesRequest() // UpdateNetworkWirelessSsidSchedulesRequest | 
};
apiInstance.updateNetworkWirelessSsidSchedules_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidSchedulesRequest** | [**UpdateNetworkWirelessSsidSchedulesRequest**](UpdateNetworkWirelessSsidSchedulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidSplashSettings_0

> GetNetworkWirelessSsidSplashSettings200Response updateNetworkWirelessSsidSplashSettings_0(networkId, number, opts)

Modify the splash page settings for the given SSID

Modify the splash page settings for the given SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidSplashSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidSplashSettingsRequest() // UpdateNetworkWirelessSsidSplashSettingsRequest | 
};
apiInstance.updateNetworkWirelessSsidSplashSettings_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidSplashSettingsRequest** | [**UpdateNetworkWirelessSsidSplashSettingsRequest**](UpdateNetworkWirelessSsidSplashSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidTrafficShapingRules_0

> Object updateNetworkWirelessSsidTrafficShapingRules_0(networkId, number, opts)

Update the traffic shaping settings for an SSID on an MR network

Update the traffic shaping settings for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidTrafficShapingRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidTrafficShapingRulesRequest() // UpdateNetworkWirelessSsidTrafficShapingRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidTrafficShapingRules_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidTrafficShapingRulesRequest** | [**UpdateNetworkWirelessSsidTrafficShapingRulesRequest**](UpdateNetworkWirelessSsidTrafficShapingRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidVpn_0

> Object updateNetworkWirelessSsidVpn_0(networkId, number, opts)

Update the VPN settings for the SSID

Update the VPN settings for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidVpnRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidVpnRequest() // UpdateNetworkWirelessSsidVpnRequest | 
};
apiInstance.updateNetworkWirelessSsidVpn_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidVpnRequest** | [**UpdateNetworkWirelessSsidVpnRequest**](UpdateNetworkWirelessSsidVpnRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsid_0

> Object updateNetworkWirelessSsid_0(networkId, number, opts)

Update the attributes of an MR SSID

Update the attributes of an MR SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest() // UpdateNetworkWirelessSsidRequest | 
};
apiInstance.updateNetworkWirelessSsid_0(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidRequest** | [**UpdateNetworkWirelessSsidRequest**](UpdateNetworkWirelessSsidRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetwork_0

> GetNetwork200Response updateNetwork_0(networkId, opts)

Update a network

Update a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkRequest': new MerakiDashboardApi.UpdateNetworkRequest() // UpdateNetworkRequest | 
};
apiInstance.updateNetwork_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkRequest** | [**UpdateNetworkRequest**](UpdateNetworkRequest.md)|  | [optional] 

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationActionBatch_0

> Object updateOrganizationActionBatch_0(organizationId, actionBatchId, opts)

Update an action batch

Update an action batch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let actionBatchId = "actionBatchId_example"; // String | 
let opts = {
  'updateOrganizationActionBatchRequest': new MerakiDashboardApi.UpdateOrganizationActionBatchRequest() // UpdateOrganizationActionBatchRequest | 
};
apiInstance.updateOrganizationActionBatch_0(organizationId, actionBatchId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **actionBatchId** | **String**|  | 
 **updateOrganizationActionBatchRequest** | [**UpdateOrganizationActionBatchRequest**](UpdateOrganizationActionBatchRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicyAcl_0

> Object updateOrganizationAdaptivePolicyAcl_0(organizationId, aclId, opts)

Updates an adaptive policy ACL

Updates an adaptive policy ACL

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyAclRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyAclRequest() // UpdateOrganizationAdaptivePolicyAclRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyAcl_0(organizationId, aclId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **aclId** | **String**|  | 
 **updateOrganizationAdaptivePolicyAclRequest** | [**UpdateOrganizationAdaptivePolicyAclRequest**](UpdateOrganizationAdaptivePolicyAclRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicyGroup_0

> Object updateOrganizationAdaptivePolicyGroup_0(organizationId, id, opts)

Updates an adaptive policy group

Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyGroupRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyGroupRequest() // UpdateOrganizationAdaptivePolicyGroupRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyGroup_0(organizationId, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **id** | **String**|  | 
 **updateOrganizationAdaptivePolicyGroupRequest** | [**UpdateOrganizationAdaptivePolicyGroupRequest**](UpdateOrganizationAdaptivePolicyGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicyPolicy_0

> Object updateOrganizationAdaptivePolicyPolicy_0(organizationId, id, opts)

Update an Adaptive Policy

Update an Adaptive Policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyPolicyRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyPolicyRequest() // UpdateOrganizationAdaptivePolicyPolicyRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyPolicy_0(organizationId, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **id** | **String**|  | 
 **updateOrganizationAdaptivePolicyPolicyRequest** | [**UpdateOrganizationAdaptivePolicyPolicyRequest**](UpdateOrganizationAdaptivePolicyPolicyRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicySettings_0

> Object updateOrganizationAdaptivePolicySettings_0(organizationId, opts)

Update global adaptive policy settings

Update global adaptive policy settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicySettingsRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicySettingsRequest() // UpdateOrganizationAdaptivePolicySettingsRequest | 
};
apiInstance.updateOrganizationAdaptivePolicySettings_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationAdaptivePolicySettingsRequest** | [**UpdateOrganizationAdaptivePolicySettingsRequest**](UpdateOrganizationAdaptivePolicySettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdmin_0

> Object updateOrganizationAdmin_0(organizationId, adminId, opts)

Update an administrator

Update an administrator

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let adminId = "adminId_example"; // String | 
let opts = {
  'updateOrganizationAdminRequest': new MerakiDashboardApi.UpdateOrganizationAdminRequest() // UpdateOrganizationAdminRequest | 
};
apiInstance.updateOrganizationAdmin_0(organizationId, adminId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **adminId** | **String**|  | 
 **updateOrganizationAdminRequest** | [**UpdateOrganizationAdminRequest**](UpdateOrganizationAdminRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAlertsProfile_0

> Object updateOrganizationAlertsProfile_0(organizationId, alertConfigId, opts)

Update an organization-wide alert config

Update an organization-wide alert config

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let alertConfigId = "alertConfigId_example"; // String | 
let opts = {
  'updateOrganizationAlertsProfileRequest': new MerakiDashboardApi.UpdateOrganizationAlertsProfileRequest() // UpdateOrganizationAlertsProfileRequest | 
};
apiInstance.updateOrganizationAlertsProfile_0(organizationId, alertConfigId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **alertConfigId** | **String**|  | 
 **updateOrganizationAlertsProfileRequest** | [**UpdateOrganizationAlertsProfileRequest**](UpdateOrganizationAlertsProfileRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationApplianceSecurityIntrusion_0

> Object updateOrganizationApplianceSecurityIntrusion_0(organizationId, updateOrganizationApplianceSecurityIntrusionRequest)

Sets supported intrusion settings for an organization

Sets supported intrusion settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let updateOrganizationApplianceSecurityIntrusionRequest = new MerakiDashboardApi.UpdateOrganizationApplianceSecurityIntrusionRequest(); // UpdateOrganizationApplianceSecurityIntrusionRequest | 
apiInstance.updateOrganizationApplianceSecurityIntrusion_0(organizationId, updateOrganizationApplianceSecurityIntrusionRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationApplianceSecurityIntrusionRequest** | [**UpdateOrganizationApplianceSecurityIntrusionRequest**](UpdateOrganizationApplianceSecurityIntrusionRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationApplianceVpnThirdPartyVPNPeers_0

> GetOrganizationApplianceVpnThirdPartyVPNPeers200Response updateOrganizationApplianceVpnThirdPartyVPNPeers_0(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest)

Update the third party VPN peers for an organization

Update the third party VPN peers for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let updateOrganizationApplianceVpnThirdPartyVPNPeersRequest = new MerakiDashboardApi.UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest(); // UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest | 
apiInstance.updateOrganizationApplianceVpnThirdPartyVPNPeers_0(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationApplianceVpnThirdPartyVPNPeersRequest** | [**UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest**](UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest.md)|  | 

### Return type

[**GetOrganizationApplianceVpnThirdPartyVPNPeers200Response**](GetOrganizationApplianceVpnThirdPartyVPNPeers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationApplianceVpnVpnFirewallRules_0

> Object updateOrganizationApplianceVpnVpnFirewallRules_0(organizationId, opts)

Update the firewall rules of an organization&#39;s site-to-site VPN

Update the firewall rules of an organization&#39;s site-to-site VPN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationApplianceVpnVpnFirewallRulesRequest': new MerakiDashboardApi.UpdateOrganizationApplianceVpnVpnFirewallRulesRequest() // UpdateOrganizationApplianceVpnVpnFirewallRulesRequest | 
};
apiInstance.updateOrganizationApplianceVpnVpnFirewallRules_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationApplianceVpnVpnFirewallRulesRequest** | [**UpdateOrganizationApplianceVpnVpnFirewallRulesRequest**](UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationBrandingPoliciesPriorities_0

> GetOrganizationBrandingPoliciesPriorities200Response updateOrganizationBrandingPoliciesPriorities_0(organizationId, opts)

Update the priority ordering of an organization&#39;s branding policies.

Update the priority ordering of an organization&#39;s branding policies.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationBrandingPoliciesPrioritiesRequest': new MerakiDashboardApi.UpdateOrganizationBrandingPoliciesPrioritiesRequest() // UpdateOrganizationBrandingPoliciesPrioritiesRequest | 
};
apiInstance.updateOrganizationBrandingPoliciesPriorities_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationBrandingPoliciesPrioritiesRequest** | [**UpdateOrganizationBrandingPoliciesPrioritiesRequest**](UpdateOrganizationBrandingPoliciesPrioritiesRequest.md)|  | [optional] 

### Return type

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationBrandingPolicy_0

> GetOrganizationBrandingPolicies200ResponseInner updateOrganizationBrandingPolicy_0(organizationId, brandingPolicyId, opts)

Update a branding policy

Update a branding policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let brandingPolicyId = "brandingPolicyId_example"; // String | 
let opts = {
  'updateOrganizationBrandingPolicyRequest': new MerakiDashboardApi.UpdateOrganizationBrandingPolicyRequest() // UpdateOrganizationBrandingPolicyRequest | 
};
apiInstance.updateOrganizationBrandingPolicy_0(organizationId, brandingPolicyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **brandingPolicyId** | **String**|  | 
 **updateOrganizationBrandingPolicyRequest** | [**UpdateOrganizationBrandingPolicyRequest**](UpdateOrganizationBrandingPolicyRequest.md)|  | [optional] 

### Return type

[**GetOrganizationBrandingPolicies200ResponseInner**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationCameraOnboardingStatuses_0

> Object updateOrganizationCameraOnboardingStatuses_0(organizationId, opts)

Notify that credential handoff to camera has completed

Notify that credential handoff to camera has completed

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationCameraOnboardingStatusesRequest': new MerakiDashboardApi.UpdateOrganizationCameraOnboardingStatusesRequest() // UpdateOrganizationCameraOnboardingStatusesRequest | 
};
apiInstance.updateOrganizationCameraOnboardingStatuses_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationCameraOnboardingStatusesRequest** | [**UpdateOrganizationCameraOnboardingStatusesRequest**](UpdateOrganizationCameraOnboardingStatusesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationConfigTemplateSwitchProfilePort_0

> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner updateOrganizationConfigTemplateSwitchProfilePort_0(organizationId, configTemplateId, profileId, portId, opts)

Update a switch profile port

Update a switch profile port

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let profileId = "profileId_example"; // String | 
let portId = "portId_example"; // String | 
let opts = {
  'updateOrganizationConfigTemplateSwitchProfilePortRequest': new MerakiDashboardApi.UpdateOrganizationConfigTemplateSwitchProfilePortRequest() // UpdateOrganizationConfigTemplateSwitchProfilePortRequest | 
};
apiInstance.updateOrganizationConfigTemplateSwitchProfilePort_0(organizationId, configTemplateId, profileId, portId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 
 **profileId** | **String**|  | 
 **portId** | **String**|  | 
 **updateOrganizationConfigTemplateSwitchProfilePortRequest** | [**UpdateOrganizationConfigTemplateSwitchProfilePortRequest**](UpdateOrganizationConfigTemplateSwitchProfilePortRequest.md)|  | [optional] 

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationConfigTemplate_0

> Object updateOrganizationConfigTemplate_0(organizationId, configTemplateId, opts)

Update a configuration template

Update a configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let opts = {
  'updateOrganizationConfigTemplateRequest': new MerakiDashboardApi.UpdateOrganizationConfigTemplateRequest() // UpdateOrganizationConfigTemplateRequest | 
};
apiInstance.updateOrganizationConfigTemplate_0(organizationId, configTemplateId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **configTemplateId** | **String**|  | 
 **updateOrganizationConfigTemplateRequest** | [**UpdateOrganizationConfigTemplateRequest**](UpdateOrganizationConfigTemplateRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationEarlyAccessFeaturesOptIn_0

> Object updateOrganizationEarlyAccessFeaturesOptIn_0(organizationId, optInId, opts)

Update an early access feature opt-in for an organization

Update an early access feature opt-in for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let optInId = "optInId_example"; // String | 
let opts = {
  'updateOrganizationEarlyAccessFeaturesOptInRequest': new MerakiDashboardApi.UpdateOrganizationEarlyAccessFeaturesOptInRequest() // UpdateOrganizationEarlyAccessFeaturesOptInRequest | 
};
apiInstance.updateOrganizationEarlyAccessFeaturesOptIn_0(organizationId, optInId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **optInId** | **String**|  | 
 **updateOrganizationEarlyAccessFeaturesOptInRequest** | [**UpdateOrganizationEarlyAccessFeaturesOptInRequest**](UpdateOrganizationEarlyAccessFeaturesOptInRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationInsightMonitoredMediaServer_0

> Object updateOrganizationInsightMonitoredMediaServer_0(organizationId, monitoredMediaServerId, opts)

Update a monitored media server for this organization

Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
let opts = {
  'updateOrganizationInsightMonitoredMediaServerRequest': new MerakiDashboardApi.UpdateOrganizationInsightMonitoredMediaServerRequest() // UpdateOrganizationInsightMonitoredMediaServerRequest | 
};
apiInstance.updateOrganizationInsightMonitoredMediaServer_0(organizationId, monitoredMediaServerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **monitoredMediaServerId** | **String**|  | 
 **updateOrganizationInsightMonitoredMediaServerRequest** | [**UpdateOrganizationInsightMonitoredMediaServerRequest**](UpdateOrganizationInsightMonitoredMediaServerRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationLicense_0

> GetOrganizationLicenses200ResponseInner updateOrganizationLicense_0(organizationId, licenseId, opts)

Update a license

Update a license

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let licenseId = "licenseId_example"; // String | 
let opts = {
  'updateOrganizationLicenseRequest': new MerakiDashboardApi.UpdateOrganizationLicenseRequest() // UpdateOrganizationLicenseRequest | 
};
apiInstance.updateOrganizationLicense_0(organizationId, licenseId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **licenseId** | **String**|  | 
 **updateOrganizationLicenseRequest** | [**UpdateOrganizationLicenseRequest**](UpdateOrganizationLicenseRequest.md)|  | [optional] 

### Return type

[**GetOrganizationLicenses200ResponseInner**](GetOrganizationLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationLoginSecurity_0

> GetOrganizationLoginSecurity200Response updateOrganizationLoginSecurity_0(organizationId, opts)

Update the login security settings for an organization

Update the login security settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationLoginSecurityRequest': new MerakiDashboardApi.UpdateOrganizationLoginSecurityRequest() // UpdateOrganizationLoginSecurityRequest | 
};
apiInstance.updateOrganizationLoginSecurity_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationLoginSecurityRequest** | [**UpdateOrganizationLoginSecurityRequest**](UpdateOrganizationLoginSecurityRequest.md)|  | [optional] 

### Return type

[**GetOrganizationLoginSecurity200Response**](GetOrganizationLoginSecurity200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationPolicyObject_0

> Object updateOrganizationPolicyObject_0(organizationId, policyObjectId, opts)

Updates a Policy Object.

Updates a Policy Object.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectId = "policyObjectId_example"; // String | 
let opts = {
  'updateOrganizationPolicyObjectRequest': new MerakiDashboardApi.UpdateOrganizationPolicyObjectRequest() // UpdateOrganizationPolicyObjectRequest | 
};
apiInstance.updateOrganizationPolicyObject_0(organizationId, policyObjectId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **policyObjectId** | **String**|  | 
 **updateOrganizationPolicyObjectRequest** | [**UpdateOrganizationPolicyObjectRequest**](UpdateOrganizationPolicyObjectRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationPolicyObjectsGroup_0

> Object updateOrganizationPolicyObjectsGroup_0(organizationId, policyObjectGroupId, opts)

Updates a Policy Object Group.

Updates a Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectGroupId = "policyObjectGroupId_example"; // String | 
let opts = {
  'updateOrganizationPolicyObjectsGroupRequest': new MerakiDashboardApi.UpdateOrganizationPolicyObjectsGroupRequest() // UpdateOrganizationPolicyObjectsGroupRequest | 
};
apiInstance.updateOrganizationPolicyObjectsGroup_0(organizationId, policyObjectGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **policyObjectGroupId** | **String**|  | 
 **updateOrganizationPolicyObjectsGroupRequest** | [**UpdateOrganizationPolicyObjectsGroupRequest**](UpdateOrganizationPolicyObjectsGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationSamlIdp_0

> [GetOrganizationSamlIdps200ResponseInner] updateOrganizationSamlIdp_0(organizationId, idpId, opts)

Update a SAML IdP in your organization

Update a SAML IdP in your organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let idpId = "idpId_example"; // String | 
let opts = {
  'updateOrganizationSamlIdpRequest': new MerakiDashboardApi.UpdateOrganizationSamlIdpRequest() // UpdateOrganizationSamlIdpRequest | 
};
apiInstance.updateOrganizationSamlIdp_0(organizationId, idpId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **idpId** | **String**|  | 
 **updateOrganizationSamlIdpRequest** | [**UpdateOrganizationSamlIdpRequest**](UpdateOrganizationSamlIdpRequest.md)|  | [optional] 

### Return type

[**[GetOrganizationSamlIdps200ResponseInner]**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationSamlRole_0

> UpdateOrganizationSamlRole200Response updateOrganizationSamlRole_0(organizationId, samlRoleId, opts)

Update a SAML role

Update a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
let opts = {
  'updateOrganizationSamlRoleRequest': new MerakiDashboardApi.UpdateOrganizationSamlRoleRequest() // UpdateOrganizationSamlRoleRequest | 
};
apiInstance.updateOrganizationSamlRole_0(organizationId, samlRoleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **samlRoleId** | **String**|  | 
 **updateOrganizationSamlRoleRequest** | [**UpdateOrganizationSamlRoleRequest**](UpdateOrganizationSamlRoleRequest.md)|  | [optional] 

### Return type

[**UpdateOrganizationSamlRole200Response**](UpdateOrganizationSamlRole200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationSaml_0

> GetOrganizationSaml200Response updateOrganizationSaml_0(organizationId, opts)

Updates the SAML SSO enabled settings for an organization.

Updates the SAML SSO enabled settings for an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationSamlRequest': new MerakiDashboardApi.UpdateOrganizationSamlRequest() // UpdateOrganizationSamlRequest | 
};
apiInstance.updateOrganizationSaml_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationSamlRequest** | [**UpdateOrganizationSamlRequest**](UpdateOrganizationSamlRequest.md)|  | [optional] 

### Return type

[**GetOrganizationSaml200Response**](GetOrganizationSaml200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationSnmp_0

> Object updateOrganizationSnmp_0(organizationId, opts)

Update the SNMP settings for an organization

Update the SNMP settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationSnmpRequest': new MerakiDashboardApi.UpdateOrganizationSnmpRequest() // UpdateOrganizationSnmpRequest | 
};
apiInstance.updateOrganizationSnmp_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationSnmpRequest** | [**UpdateOrganizationSnmpRequest**](UpdateOrganizationSnmpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganization_0

> GetOrganizations200ResponseInner updateOrganization_0(organizationId, opts)

Update an organization

Update an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationRequest': new MerakiDashboardApi.UpdateOrganizationRequest() // UpdateOrganizationRequest | 
};
apiInstance.updateOrganization_0(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **updateOrganizationRequest** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)|  | [optional] 

### Return type

[**GetOrganizations200ResponseInner**](GetOrganizations200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vmxNetworkDevicesClaim_0

> Object vmxNetworkDevicesClaim_0(networkId, vmxNetworkDevicesClaimRequest)

Claim a vMX into a network

Claim a vMX into a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let vmxNetworkDevicesClaimRequest = new MerakiDashboardApi.VmxNetworkDevicesClaimRequest(); // VmxNetworkDevicesClaimRequest | 
apiInstance.vmxNetworkDevicesClaim_0(networkId, vmxNetworkDevicesClaimRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **vmxNetworkDevicesClaimRequest** | [**VmxNetworkDevicesClaimRequest**](VmxNetworkDevicesClaimRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wipeNetworkSmDevices_0

> WipeNetworkSmDevices200Response wipeNetworkSmDevices_0(networkId, opts)

Wipe a device

Wipe a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigureApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'wipeNetworkSmDevicesRequest': new MerakiDashboardApi.WipeNetworkSmDevicesRequest() // WipeNetworkSmDevicesRequest | 
};
apiInstance.wipeNetworkSmDevices_0(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **wipeNetworkSmDevicesRequest** | [**WipeNetworkSmDevicesRequest**](WipeNetworkSmDevicesRequest.md)|  | [optional] 

### Return type

[**WipeNetworkSmDevices200Response**](WipeNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

