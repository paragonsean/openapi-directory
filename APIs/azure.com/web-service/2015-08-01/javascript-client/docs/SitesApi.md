# WebSiteManagementClient.SitesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sitesAddSitePremierAddOn**](SitesApi.md#sitesAddSitePremierAddOn) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | 
[**sitesAddSitePremierAddOnSlot**](SitesApi.md#sitesAddSitePremierAddOnSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | 
[**sitesApplySlotConfigSlot**](SitesApi.md#sitesApplySlotConfigSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/applySlotConfig | Applies the configuration settings from the target slot onto the current slot
[**sitesApplySlotConfigToProduction**](SitesApi.md#sitesApplySlotConfigToProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/applySlotConfig | Applies the configuration settings from the target slot onto the current slot
[**sitesBackupSite**](SitesApi.md#sitesBackupSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backup | Creates web app backup
[**sitesBackupSiteSlot**](SitesApi.md#sitesBackupSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backup | Creates web app backup
[**sitesCreateDeployment**](SitesApi.md#sitesCreateDeployment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Create a deployment
[**sitesCreateDeploymentSlot**](SitesApi.md#sitesCreateDeploymentSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Create a deployment
[**sitesCreateInstanceDeployment**](SitesApi.md#sitesCreateInstanceDeployment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments/{id} | Create a deployment
[**sitesCreateInstanceDeploymentSlot**](SitesApi.md#sitesCreateInstanceDeploymentSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments/{id} | Create a deployment
[**sitesCreateOrUpdateSite**](SitesApi.md#sitesCreateOrUpdateSite) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Creates a new web app or modifies an existing web app.
[**sitesCreateOrUpdateSiteConfig**](SitesApi.md#sitesCreateOrUpdateSiteConfig) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Update the configuration of web app
[**sitesCreateOrUpdateSiteConfigSlot**](SitesApi.md#sitesCreateOrUpdateSiteConfigSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Update the configuration of web app
[**sitesCreateOrUpdateSiteHostNameBinding**](SitesApi.md#sitesCreateOrUpdateSiteHostNameBinding) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Creates a web app hostname binding
[**sitesCreateOrUpdateSiteHostNameBindingSlot**](SitesApi.md#sitesCreateOrUpdateSiteHostNameBindingSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Creates a web app hostname binding
[**sitesCreateOrUpdateSiteRelayServiceConnection**](SitesApi.md#sitesCreateOrUpdateSiteRelayServiceConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
[**sitesCreateOrUpdateSiteRelayServiceConnectionSlot**](SitesApi.md#sitesCreateOrUpdateSiteRelayServiceConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
[**sitesCreateOrUpdateSiteSlot**](SitesApi.md#sitesCreateOrUpdateSiteSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Creates a new web app or modifies an existing web app.
[**sitesCreateOrUpdateSiteSourceControl**](SitesApi.md#sitesCreateOrUpdateSiteSourceControl) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Update the source control configuration of web app
[**sitesCreateOrUpdateSiteSourceControlSlot**](SitesApi.md#sitesCreateOrUpdateSiteSourceControlSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Update the source control configuration of web app
[**sitesCreateOrUpdateSiteVNETConnection**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties.
[**sitesCreateOrUpdateSiteVNETConnectionGateway**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnectionGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway.
[**sitesCreateOrUpdateSiteVNETConnectionGatewaySlot**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnectionGatewaySlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway.
[**sitesCreateOrUpdateSiteVNETConnectionSlot**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties.
[**sitesDeleteBackup**](SitesApi.md#sitesDeleteBackup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId} | Deletes a backup from Azure Storage
[**sitesDeleteBackupSlot**](SitesApi.md#sitesDeleteBackupSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId} | Deletes a backup from Azure Storage
[**sitesDeleteDeployment**](SitesApi.md#sitesDeleteDeployment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Delete the deployment
[**sitesDeleteDeploymentSlot**](SitesApi.md#sitesDeleteDeploymentSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Delete the deployment
[**sitesDeleteInstanceDeployment**](SitesApi.md#sitesDeleteInstanceDeployment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments/{id} | Delete the deployment
[**sitesDeleteInstanceDeploymentSlot**](SitesApi.md#sitesDeleteInstanceDeploymentSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments/{id} | Delete the deployment
[**sitesDeleteSite**](SitesApi.md#sitesDeleteSite) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Deletes a web app
[**sitesDeleteSiteHostNameBinding**](SitesApi.md#sitesDeleteSiteHostNameBinding) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Deletes a host name binding
[**sitesDeleteSiteHostNameBindingSlot**](SitesApi.md#sitesDeleteSiteHostNameBindingSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Deletes a host name binding
[**sitesDeleteSitePremierAddOn**](SitesApi.md#sitesDeleteSitePremierAddOn) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | 
[**sitesDeleteSitePremierAddOnSlot**](SitesApi.md#sitesDeleteSitePremierAddOnSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | 
[**sitesDeleteSiteRelayServiceConnection**](SitesApi.md#sitesDeleteSiteRelayServiceConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Removes the association to a BizTalk Hybrid Connection, identified by its entity name.
[**sitesDeleteSiteRelayServiceConnectionSlot**](SitesApi.md#sitesDeleteSiteRelayServiceConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Removes the association to a BizTalk Hybrid Connection, identified by its entity name.
[**sitesDeleteSiteSlot**](SitesApi.md#sitesDeleteSiteSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Deletes a web app
[**sitesDeleteSiteSourceControl**](SitesApi.md#sitesDeleteSiteSourceControl) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Delete source control configuration of web app
[**sitesDeleteSiteSourceControlSlot**](SitesApi.md#sitesDeleteSiteSourceControlSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Delete source control configuration of web app
[**sitesDeleteSiteVNETConnection**](SitesApi.md#sitesDeleteSiteVNETConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Removes the specified Virtual Network Connection association from this web app.
[**sitesDeleteSiteVNETConnectionSlot**](SitesApi.md#sitesDeleteSiteVNETConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Removes the specified Virtual Network Connection association from this web app.
[**sitesDiscoverSiteRestore**](SitesApi.md#sitesDiscoverSiteRestore) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/discover | Discovers existing web app backups that can be restored
[**sitesDiscoverSiteRestoreSlot**](SitesApi.md#sitesDiscoverSiteRestoreSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/discover | Discovers existing web app backups that can be restored
[**sitesGenerateNewSitePublishingPassword**](SitesApi.md#sitesGenerateNewSitePublishingPassword) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/newpassword | Generates new random app publishing password
[**sitesGenerateNewSitePublishingPasswordSlot**](SitesApi.md#sitesGenerateNewSitePublishingPasswordSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/newpassword | Generates new random app publishing password
[**sitesGetDeletedSites**](SitesApi.md#sitesGetDeletedSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/deletedSites | Gets deleted web apps in subscription
[**sitesGetDeployment**](SitesApi.md#sitesGetDeployment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Get the deployment
[**sitesGetDeploymentSlot**](SitesApi.md#sitesGetDeploymentSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Get the deployment
[**sitesGetDeployments**](SitesApi.md#sitesGetDeployments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments | List deployments
[**sitesGetDeploymentsSlot**](SitesApi.md#sitesGetDeploymentsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments | List deployments
[**sitesGetInstanceDeployment**](SitesApi.md#sitesGetInstanceDeployment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments/{id} | Get the deployment
[**sitesGetInstanceDeploymentSlot**](SitesApi.md#sitesGetInstanceDeploymentSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments/{id} | Get the deployment
[**sitesGetInstanceDeployments**](SitesApi.md#sitesGetInstanceDeployments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments | List deployments
[**sitesGetInstanceDeploymentsSlot**](SitesApi.md#sitesGetInstanceDeploymentsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments | List deployments
[**sitesGetSite**](SitesApi.md#sitesGetSite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Get details of a web app
[**sitesGetSiteBackupConfiguration**](SitesApi.md#sitesGetSiteBackupConfiguration) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup/list | Gets the backup configuration for a web app
[**sitesGetSiteBackupConfigurationSlot**](SitesApi.md#sitesGetSiteBackupConfigurationSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup/list | Gets the backup configuration for a web app
[**sitesGetSiteBackupStatus**](SitesApi.md#sitesGetSiteBackupStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId} | Gets status of a web app backup that may be in progress.
[**sitesGetSiteBackupStatusSecrets**](SitesApi.md#sitesGetSiteBackupStatusSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId}/list | Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
[**sitesGetSiteBackupStatusSecretsSlot**](SitesApi.md#sitesGetSiteBackupStatusSecretsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId}/list | Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
[**sitesGetSiteBackupStatusSlot**](SitesApi.md#sitesGetSiteBackupStatusSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId} | Gets status of a web app backup that may be in progress.
[**sitesGetSiteConfig**](SitesApi.md#sitesGetSiteConfig) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Gets the configuration of the web app
[**sitesGetSiteConfigSlot**](SitesApi.md#sitesGetSiteConfigSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Gets the configuration of the web app
[**sitesGetSiteHostNameBinding**](SitesApi.md#sitesGetSiteHostNameBinding) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Get web app binding for a hostname
[**sitesGetSiteHostNameBindingSlot**](SitesApi.md#sitesGetSiteHostNameBindingSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Get web app binding for a hostname
[**sitesGetSiteHostNameBindings**](SitesApi.md#sitesGetSiteHostNameBindings) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings | Get web app hostname bindings
[**sitesGetSiteHostNameBindingsSlot**](SitesApi.md#sitesGetSiteHostNameBindingsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings | Get web app hostname bindings
[**sitesGetSiteInstanceIdentifiers**](SitesApi.md#sitesGetSiteInstanceIdentifiers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances | Gets all instance of a web app
[**sitesGetSiteInstanceIdentifiersSlot**](SitesApi.md#sitesGetSiteInstanceIdentifiersSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances | Gets all instance of a web app
[**sitesGetSiteLogsConfig**](SitesApi.md#sitesGetSiteLogsConfig) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/logs | Gets the web app logs configuration
[**sitesGetSiteLogsConfigSlot**](SitesApi.md#sitesGetSiteLogsConfigSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs | Gets the web app logs configuration
[**sitesGetSiteMetricDefinitions**](SitesApi.md#sitesGetSiteMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/metricdefinitions | Gets metric definitions for web app
[**sitesGetSiteMetricDefinitionsSlot**](SitesApi.md#sitesGetSiteMetricDefinitionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metricdefinitions | Gets metric definitions for web app
[**sitesGetSiteMetrics**](SitesApi.md#sitesGetSiteMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/metrics | Gets metrics for web app
[**sitesGetSiteMetricsSlot**](SitesApi.md#sitesGetSiteMetricsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metrics | Gets metrics for web app
[**sitesGetSiteNetworkFeatures**](SitesApi.md#sitesGetSiteNetworkFeatures) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkFeatures/{view} | Retrieves a view of all network features in use on this web app.
[**sitesGetSiteNetworkFeaturesSlot**](SitesApi.md#sitesGetSiteNetworkFeaturesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkFeatures/{view} | Retrieves a view of all network features in use on this web app.
[**sitesGetSiteOperation**](SitesApi.md#sitesGetSiteOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/operationresults/{operationId} | Gets the operation for a web app
[**sitesGetSiteOperationSlot**](SitesApi.md#sitesGetSiteOperationSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/operationresults/{operationId} | Gets the operation for a web app
[**sitesGetSitePremierAddOn**](SitesApi.md#sitesGetSitePremierAddOn) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | 
[**sitesGetSitePremierAddOnSlot**](SitesApi.md#sitesGetSitePremierAddOnSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | 
[**sitesGetSiteRelayServiceConnection**](SitesApi.md#sitesGetSiteRelayServiceConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Retrieves a BizTalk Hybrid Connection identified by its entity name.
[**sitesGetSiteRelayServiceConnectionSlot**](SitesApi.md#sitesGetSiteRelayServiceConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Retrieves a BizTalk Hybrid Connection identified by its entity name.
[**sitesGetSiteSlot**](SitesApi.md#sitesGetSiteSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Get details of a web app
[**sitesGetSiteSlots**](SitesApi.md#sitesGetSiteSlots) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots | Gets all the slots for a web apps
[**sitesGetSiteSnapshots**](SitesApi.md#sitesGetSiteSnapshots) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/snapshots | Returns all Snapshots to the user.
[**sitesGetSiteSnapshotsSlot**](SitesApi.md#sitesGetSiteSnapshotsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/snapshots | Returns all Snapshots to the user.
[**sitesGetSiteSourceControl**](SitesApi.md#sitesGetSiteSourceControl) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Get the source control configuration of web app
[**sitesGetSiteSourceControlSlot**](SitesApi.md#sitesGetSiteSourceControlSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Get the source control configuration of web app
[**sitesGetSiteUsages**](SitesApi.md#sitesGetSiteUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/usages | Gets the quota usage numbers for web app
[**sitesGetSiteUsagesSlot**](SitesApi.md#sitesGetSiteUsagesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/usages | Gets the quota usage numbers for web app
[**sitesGetSiteVNETConnection**](SitesApi.md#sitesGetSiteVNETConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Retrieves a specific Virtual Network Connection associated with this web app.
[**sitesGetSiteVNETConnectionSlot**](SitesApi.md#sitesGetSiteVNETConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Retrieves a specific Virtual Network Connection associated with this web app.
[**sitesGetSiteVNETConnections**](SitesApi.md#sitesGetSiteVNETConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections | Retrieves a list of all Virtual Network Connections associated with this web app.
[**sitesGetSiteVNETConnectionsSlot**](SitesApi.md#sitesGetSiteVNETConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections | Retrieves a list of all Virtual Network Connections associated with this web app.
[**sitesGetSiteVnetGateway**](SitesApi.md#sitesGetSiteVnetGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Retrieves a Virtual Network connection gateway associated with this web app and virtual network.
[**sitesGetSiteVnetGatewaySlot**](SitesApi.md#sitesGetSiteVnetGatewaySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Retrieves a Virtual Network connection gateway associated with this web app and virtual network.
[**sitesGetSites**](SitesApi.md#sitesGetSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites | Gets the web apps for a subscription in the specified resource group
[**sitesGetSlotConfigNames**](SitesApi.md#sitesGetSlotConfigNames) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames | Gets the names of application settings and connection string that remain with the slot during swap operation
[**sitesGetSlotsDifferencesFromProduction**](SitesApi.md#sitesGetSlotsDifferencesFromProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slotsdiffs | Get the difference in configuration settings between two web app slots
[**sitesGetSlotsDifferencesSlot**](SitesApi.md#sitesGetSlotsDifferencesSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsdiffs | Get the difference in configuration settings between two web app slots
[**sitesIsSiteCloneable**](SitesApi.md#sitesIsSiteCloneable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/iscloneable | Creates a new web app or modifies an existing web app.
[**sitesIsSiteCloneableSlot**](SitesApi.md#sitesIsSiteCloneableSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/iscloneable | Creates a new web app or modifies an existing web app.
[**sitesListSiteAppSettings**](SitesApi.md#sitesListSiteAppSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings/list | Gets the application settings of web app
[**sitesListSiteAppSettingsSlot**](SitesApi.md#sitesListSiteAppSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings/list | Gets the application settings of web app
[**sitesListSiteAuthSettings**](SitesApi.md#sitesListSiteAuthSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings/list | Gets the Authentication / Authorization settings associated with web app
[**sitesListSiteAuthSettingsSlot**](SitesApi.md#sitesListSiteAuthSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings/list | Gets the Authentication / Authorization settings associated with web app
[**sitesListSiteBackups**](SitesApi.md#sitesListSiteBackups) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups | Lists all available backups for web app
[**sitesListSiteBackupsSlot**](SitesApi.md#sitesListSiteBackupsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups | Lists all available backups for web app
[**sitesListSiteConnectionStrings**](SitesApi.md#sitesListSiteConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings/list | Gets the connection strings associated with web app
[**sitesListSiteConnectionStringsSlot**](SitesApi.md#sitesListSiteConnectionStringsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings/list | Gets the connection strings associated with web app
[**sitesListSiteMetadata**](SitesApi.md#sitesListSiteMetadata) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata/list | Gets the web app meta data.
[**sitesListSiteMetadataSlot**](SitesApi.md#sitesListSiteMetadataSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata/list | Gets the web app meta data.
[**sitesListSitePremierAddOns**](SitesApi.md#sitesListSitePremierAddOns) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons | 
[**sitesListSitePremierAddOnsSlot**](SitesApi.md#sitesListSitePremierAddOnsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons | 
[**sitesListSitePublishingCredentials**](SitesApi.md#sitesListSitePublishingCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/publishingcredentials/list | Gets the web app publishing credentials
[**sitesListSitePublishingCredentialsSlot**](SitesApi.md#sitesListSitePublishingCredentialsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/publishingcredentials/list | Gets the web app publishing credentials
[**sitesListSitePublishingProfileXml**](SitesApi.md#sitesListSitePublishingProfileXml) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publishxml | Gets the publishing profile for web app
[**sitesListSitePublishingProfileXmlSlot**](SitesApi.md#sitesListSitePublishingProfileXmlSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publishxml | Gets the publishing profile for web app
[**sitesListSiteRelayServiceConnections**](SitesApi.md#sitesListSiteRelayServiceConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection | Retrieves all BizTalk Hybrid Connections associated with this web app.
[**sitesListSiteRelayServiceConnectionsSlot**](SitesApi.md#sitesListSiteRelayServiceConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection | Retrieves all BizTalk Hybrid Connections associated with this web app.
[**sitesRecoverSite**](SitesApi.md#sitesRecoverSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/recover | Recovers a deleted web app
[**sitesRecoverSiteSlot**](SitesApi.md#sitesRecoverSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/recover | Recovers a deleted web app
[**sitesResetProductionSlotConfig**](SitesApi.md#sitesResetProductionSlotConfig) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resetSlotConfig | Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API
[**sitesResetSlotConfigSlot**](SitesApi.md#sitesResetSlotConfigSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resetSlotConfig | Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API
[**sitesRestartSite**](SitesApi.md#sitesRestartSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/restart | Restarts web app
[**sitesRestartSiteSlot**](SitesApi.md#sitesRestartSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restart | Restarts web app
[**sitesRestoreSite**](SitesApi.md#sitesRestoreSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId}/restore | Restores a web app
[**sitesRestoreSiteSlot**](SitesApi.md#sitesRestoreSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId}/restore | Restores a web app
[**sitesStartSite**](SitesApi.md#sitesStartSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/start | Starts web app
[**sitesStartSiteSlot**](SitesApi.md#sitesStartSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/start | Starts web app
[**sitesStopSite**](SitesApi.md#sitesStopSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/stop | Stops web app
[**sitesStopSiteSlot**](SitesApi.md#sitesStopSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/stop | Stops web app
[**sitesSwapSlotWithProduction**](SitesApi.md#sitesSwapSlotWithProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slotsswap | Swaps web app slots
[**sitesSwapSlotsSlot**](SitesApi.md#sitesSwapSlotsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsswap | Swaps web app slots
[**sitesSyncSiteRepository**](SitesApi.md#sitesSyncSiteRepository) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sync | 
[**sitesSyncSiteRepositorySlot**](SitesApi.md#sitesSyncSiteRepositorySlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sync | 
[**sitesUpdateSiteAppSettings**](SitesApi.md#sitesUpdateSiteAppSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings | Updates the application settings of web app
[**sitesUpdateSiteAppSettingsSlot**](SitesApi.md#sitesUpdateSiteAppSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings | Updates the application settings of web app
[**sitesUpdateSiteAuthSettings**](SitesApi.md#sitesUpdateSiteAuthSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings | Updates the Authentication / Authorization settings associated with web app
[**sitesUpdateSiteAuthSettingsSlot**](SitesApi.md#sitesUpdateSiteAuthSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings | Updates the Authentication / Authorization settings associated with web app
[**sitesUpdateSiteBackupConfiguration**](SitesApi.md#sitesUpdateSiteBackupConfiguration) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup | Updates backup configuration of web app
[**sitesUpdateSiteBackupConfigurationSlot**](SitesApi.md#sitesUpdateSiteBackupConfigurationSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup | Updates backup configuration of web app
[**sitesUpdateSiteConfig**](SitesApi.md#sitesUpdateSiteConfig) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Update the configuration of web app
[**sitesUpdateSiteConfigSlot**](SitesApi.md#sitesUpdateSiteConfigSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Update the configuration of web app
[**sitesUpdateSiteConnectionStrings**](SitesApi.md#sitesUpdateSiteConnectionStrings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings | Updates the connection strings associated with web app
[**sitesUpdateSiteConnectionStringsSlot**](SitesApi.md#sitesUpdateSiteConnectionStringsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings | Updates the connection strings associated with web app
[**sitesUpdateSiteLogsConfig**](SitesApi.md#sitesUpdateSiteLogsConfig) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/logs | Updates the meta data for web app
[**sitesUpdateSiteLogsConfigSlot**](SitesApi.md#sitesUpdateSiteLogsConfigSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs | Updates the meta data for web app
[**sitesUpdateSiteMetadata**](SitesApi.md#sitesUpdateSiteMetadata) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata | Updates the meta data for web app
[**sitesUpdateSiteMetadataSlot**](SitesApi.md#sitesUpdateSiteMetadataSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata | Updates the meta data for web app
[**sitesUpdateSiteRelayServiceConnection**](SitesApi.md#sitesUpdateSiteRelayServiceConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
[**sitesUpdateSiteRelayServiceConnectionSlot**](SitesApi.md#sitesUpdateSiteRelayServiceConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
[**sitesUpdateSiteSourceControl**](SitesApi.md#sitesUpdateSiteSourceControl) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Update the source control configuration of web app
[**sitesUpdateSiteSourceControlSlot**](SitesApi.md#sitesUpdateSiteSourceControlSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Update the source control configuration of web app
[**sitesUpdateSiteVNETConnection**](SitesApi.md#sitesUpdateSiteVNETConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties.
[**sitesUpdateSiteVNETConnectionGateway**](SitesApi.md#sitesUpdateSiteVNETConnectionGateway) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway.
[**sitesUpdateSiteVNETConnectionGatewaySlot**](SitesApi.md#sitesUpdateSiteVNETConnectionGatewaySlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway.
[**sitesUpdateSiteVNETConnectionSlot**](SitesApi.md#sitesUpdateSiteVNETConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties.
[**sitesUpdateSlotConfigNames**](SitesApi.md#sitesUpdateSlotConfigNames) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames | Updates the names of application settings and connection string that remain with the slot during swap operation



## sitesAddSitePremierAddOn

> Object sitesAddSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let premierAddOnName = "premierAddOnName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let premierAddOn = new WebSiteManagementClient.PremierAddOnRequest(); // PremierAddOnRequest | 
apiInstance.sitesAddSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **premierAddOnName** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **premierAddOn** | [**PremierAddOnRequest**](PremierAddOnRequest.md)|  | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesAddSitePremierAddOnSlot

> Object sitesAddSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let premierAddOnName = "premierAddOnName_example"; // String | 
let slot = "slot_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let premierAddOn = new WebSiteManagementClient.PremierAddOnRequest(); // PremierAddOnRequest | 
apiInstance.sitesAddSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **premierAddOnName** | **String**|  | 
 **slot** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **premierAddOn** | [**PremierAddOnRequest**](PremierAddOnRequest.md)|  | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesApplySlotConfigSlot

> Object sitesApplySlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Applies the configuration settings from the target slot onto the current slot

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of the source slot. Settings from the target slot will be applied onto this slot
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebSiteManagementClient.CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name. Settings from that slot will be applied on the source slot
apiInstance.sitesApplySlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of the source slot. Settings from the target slot will be applied onto this slot | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name. Settings from that slot will be applied on the source slot | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesApplySlotConfigToProduction

> Object sitesApplySlotConfigToProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Applies the configuration settings from the target slot onto the current slot

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebSiteManagementClient.CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name. Settings from that slot will be applied on the source slot
apiInstance.sitesApplySlotConfigToProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name. Settings from that slot will be applied on the source slot | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesBackupSite

> BackupItem sitesBackupSite(resourceGroupName, name, subscriptionId, apiVersion, request)

Creates web app backup

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.BackupRequest(); // BackupRequest | Information on backup request
apiInstance.sitesBackupSite(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesBackupSiteSlot

> BackupItem sitesBackupSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Creates web app backup

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.BackupRequest(); // BackupRequest | Information on backup request
apiInstance.sitesBackupSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateDeployment

> Deployment sitesCreateDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, deployment)

Create a deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let deployment = new WebSiteManagementClient.Deployment(); // Deployment | Details of deployment
apiInstance.sitesCreateDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, deployment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **deployment** | [**Deployment**](Deployment.md)| Details of deployment | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateDeploymentSlot

> Deployment sitesCreateDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, deployment)

Create a deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let deployment = new WebSiteManagementClient.Deployment(); // Deployment | Details of deployment
apiInstance.sitesCreateDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, deployment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **deployment** | [**Deployment**](Deployment.md)| Details of deployment | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateInstanceDeployment

> Deployment sitesCreateInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion, deployment)

Create a deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let deployment = new WebSiteManagementClient.Deployment(); // Deployment | Details of deployment
apiInstance.sitesCreateInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion, deployment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **deployment** | [**Deployment**](Deployment.md)| Details of deployment | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateInstanceDeploymentSlot

> Deployment sitesCreateInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion, deployment)

Create a deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let deployment = new WebSiteManagementClient.Deployment(); // Deployment | Details of deployment
apiInstance.sitesCreateInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion, deployment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **deployment** | [**Deployment**](Deployment.md)| Details of deployment | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSite

> Site sitesCreateOrUpdateSite(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope, opts)

Creates a new web app or modifies an existing web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteEnvelope = new WebSiteManagementClient.Site(); // Site | Details of web app if it exists already
let opts = {
  'skipDnsRegistration': "skipDnsRegistration_example", // String | If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation
  'skipCustomDomainVerification': "skipCustomDomainVerification_example", // String | If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
  'forceDnsRegistration': "forceDnsRegistration_example", // String | If true, web app hostname is force registered with DNS
  'ttlInSeconds': "ttlInSeconds_example" // String | Time to live in seconds for web app's default domain name
};
apiInstance.sitesCreateOrUpdateSite(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteEnvelope** | [**Site**](Site.md)| Details of web app if it exists already | 
 **skipDnsRegistration** | **String**| If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation | [optional] 
 **skipCustomDomainVerification** | **String**| If true, custom (non *.azurewebsites.net) domains associated with web app are not verified. | [optional] 
 **forceDnsRegistration** | **String**| If true, web app hostname is force registered with DNS | [optional] 
 **ttlInSeconds** | **String**| Time to live in seconds for web app&#39;s default domain name | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteConfig

> SiteConfig sitesCreateOrUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebSiteManagementClient.SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
apiInstance.sitesCreateOrUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | 

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteConfigSlot

> SiteConfig sitesCreateOrUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebSiteManagementClient.SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
apiInstance.sitesCreateOrUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | 

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteHostNameBinding

> HostNameBinding sitesCreateOrUpdateSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, hostNameBinding)

Creates a web app hostname binding

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let hostName = "hostName_example"; // String | Name of host
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let hostNameBinding = new WebSiteManagementClient.HostNameBinding(); // HostNameBinding | Host name binding information
apiInstance.sitesCreateOrUpdateSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, hostNameBinding, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **hostName** | **String**| Name of host | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **hostNameBinding** | [**HostNameBinding**](HostNameBinding.md)| Host name binding information | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteHostNameBindingSlot

> HostNameBinding sitesCreateOrUpdateSiteHostNameBindingSlot(resourceGroupName, name, hostName, slot, subscriptionId, apiVersion, hostNameBinding)

Creates a web app hostname binding

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let hostName = "hostName_example"; // String | Name of host
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let hostNameBinding = new WebSiteManagementClient.HostNameBinding(); // HostNameBinding | Host name binding information
apiInstance.sitesCreateOrUpdateSiteHostNameBindingSlot(resourceGroupName, name, hostName, slot, subscriptionId, apiVersion, hostNameBinding, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **hostName** | **String**| Name of host | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **hostNameBinding** | [**HostNameBinding**](HostNameBinding.md)| Host name binding information | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteRelayServiceConnection

> RelayServiceConnectionEntity sitesCreateOrUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
apiInstance.sitesCreateOrUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteRelayServiceConnectionSlot

> RelayServiceConnectionEntity sitesCreateOrUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
apiInstance.sitesCreateOrUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteSlot

> Site sitesCreateOrUpdateSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope, opts)

Creates a new web app or modifies an existing web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteEnvelope = new WebSiteManagementClient.Site(); // Site | Details of web app if it exists already
let opts = {
  'skipDnsRegistration': "skipDnsRegistration_example", // String | If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation
  'skipCustomDomainVerification': "skipCustomDomainVerification_example", // String | If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
  'forceDnsRegistration': "forceDnsRegistration_example", // String | If true, web app hostname is force registered with DNS
  'ttlInSeconds': "ttlInSeconds_example" // String | Time to live in seconds for web app's default domain name
};
apiInstance.sitesCreateOrUpdateSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteEnvelope** | [**Site**](Site.md)| Details of web app if it exists already | 
 **skipDnsRegistration** | **String**| If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation | [optional] 
 **skipCustomDomainVerification** | **String**| If true, custom (non *.azurewebsites.net) domains associated with web app are not verified. | [optional] 
 **forceDnsRegistration** | **String**| If true, web app hostname is force registered with DNS | [optional] 
 **ttlInSeconds** | **String**| Time to live in seconds for web app&#39;s default domain name | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteSourceControl

> SiteSourceControl sitesCreateOrUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebSiteManagementClient.SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
apiInstance.sitesCreateOrUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteSourceControlSlot

> SiteSourceControl sitesCreateOrUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebSiteManagementClient.SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
apiInstance.sitesCreateOrUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteVNETConnection

> VnetInfo sitesCreateOrUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
apiInstance.sitesCreateOrUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteVNETConnectionGateway

> VnetGateway sitesCreateOrUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetGateway(); // VnetGateway | The properties to update this gateway with.
apiInstance.sitesCreateOrUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | 

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteVNETConnectionGatewaySlot

> VnetGateway sitesCreateOrUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetGateway(); // VnetGateway | The properties to update this gateway with.
apiInstance.sitesCreateOrUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | 

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesCreateOrUpdateSiteVNETConnectionSlot

> VnetInfo sitesCreateOrUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
apiInstance.sitesCreateOrUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteBackup

> BackupItem sitesDeleteBackup(resourceGroupName, name, backupId, subscriptionId, apiVersion)

Deletes a backup from Azure Storage

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteBackup(resourceGroupName, name, backupId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteBackupSlot

> BackupItem sitesDeleteBackupSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion)

Deletes a backup from Azure Storage

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteBackupSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteDeployment

> Object sitesDeleteDeployment(resourceGroupName, name, id, subscriptionId, apiVersion)

Delete the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteDeploymentSlot

> Object sitesDeleteDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

Delete the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteInstanceDeployment

> Object sitesDeleteInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion)

Delete the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteInstanceDeploymentSlot

> Object sitesDeleteInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion)

Delete the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSite

> Object sitesDeleteSite(resourceGroupName, name, subscriptionId, apiVersion, opts)

Deletes a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'deleteMetrics': "deleteMetrics_example", // String | If true, web app metrics are also deleted
  'deleteEmptyServerFarm': "deleteEmptyServerFarm_example", // String | If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted
  'skipDnsRegistration': "skipDnsRegistration_example", // String | If true, DNS registration is skipped
  'deleteAllSlots': "deleteAllSlots_example" // String | If true, all slots associated with web app are also deleted
};
apiInstance.sitesDeleteSite(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **deleteMetrics** | **String**| If true, web app metrics are also deleted | [optional] 
 **deleteEmptyServerFarm** | **String**| If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted | [optional] 
 **skipDnsRegistration** | **String**| If true, DNS registration is skipped | [optional] 
 **deleteAllSlots** | **String**| If true, all slots associated with web app are also deleted | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteHostNameBinding

> Object sitesDeleteSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion)

Deletes a host name binding

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let hostName = "hostName_example"; // String | Name of host
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **hostName** | **String**| Name of host | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteHostNameBindingSlot

> Object sitesDeleteSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion)

Deletes a host name binding

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let hostName = "hostName_example"; // String | Name of host
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **hostName** | **String**| Name of host | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSitePremierAddOn

> Object sitesDeleteSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let premierAddOnName = "premierAddOnName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **premierAddOnName** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSitePremierAddOnSlot

> Object sitesDeleteSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let premierAddOnName = "premierAddOnName_example"; // String | 
let slot = "slot_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **premierAddOnName** | **String**|  | 
 **slot** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteRelayServiceConnection

> Object sitesDeleteSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion)

Removes the association to a BizTalk Hybrid Connection, identified by its entity name.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteRelayServiceConnectionSlot

> Object sitesDeleteSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion)

Removes the association to a BizTalk Hybrid Connection, identified by its entity name.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteSlot

> Object sitesDeleteSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Deletes a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'deleteMetrics': "deleteMetrics_example", // String | If true, web app metrics are also deleted
  'deleteEmptyServerFarm': "deleteEmptyServerFarm_example", // String | If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted
  'skipDnsRegistration': "skipDnsRegistration_example", // String | If true, DNS registration is skipped
  'deleteAllSlots': "deleteAllSlots_example" // String | If true, all slots associated with web app are also deleted
};
apiInstance.sitesDeleteSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **deleteMetrics** | **String**| If true, web app metrics are also deleted | [optional] 
 **deleteEmptyServerFarm** | **String**| If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted | [optional] 
 **skipDnsRegistration** | **String**| If true, DNS registration is skipped | [optional] 
 **deleteAllSlots** | **String**| If true, all slots associated with web app are also deleted | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteSourceControl

> Object sitesDeleteSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion)

Delete source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteSourceControlSlot

> Object sitesDeleteSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Delete source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteVNETConnection

> Object sitesDeleteSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Removes the specified Virtual Network Connection association from this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDeleteSiteVNETConnectionSlot

> Object sitesDeleteSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion)

Removes the specified Virtual Network Connection association from this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesDeleteSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDiscoverSiteRestore

> RestoreRequest sitesDiscoverSiteRestore(resourceGroupName, name, subscriptionId, apiVersion, request)

Discovers existing web app backups that can be restored

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.RestoreRequest(); // RestoreRequest | Information on restore request
apiInstance.sitesDiscoverSiteRestore(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | 

### Return type

[**RestoreRequest**](RestoreRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesDiscoverSiteRestoreSlot

> RestoreRequest sitesDiscoverSiteRestoreSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Discovers existing web app backups that can be restored

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.RestoreRequest(); // RestoreRequest | Information on restore request
apiInstance.sitesDiscoverSiteRestoreSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | 

### Return type

[**RestoreRequest**](RestoreRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGenerateNewSitePublishingPassword

> Object sitesGenerateNewSitePublishingPassword(resourceGroupName, name, subscriptionId, apiVersion)

Generates new random app publishing password

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGenerateNewSitePublishingPassword(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGenerateNewSitePublishingPasswordSlot

> Object sitesGenerateNewSitePublishingPasswordSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Generates new random app publishing password

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGenerateNewSitePublishingPasswordSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetDeletedSites

> DeletedSiteCollection sitesGetDeletedSites(resourceGroupName, subscriptionId, apiVersion, opts)

Gets deleted web apps in subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example", // String | Additional web app properties included in the response
  'includeSiteTypes': "includeSiteTypes_example" // String | Types of apps included in the response
};
apiInstance.sitesGetDeletedSites(resourceGroupName, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] 
 **includeSiteTypes** | **String**| Types of apps included in the response | [optional] 

### Return type

[**DeletedSiteCollection**](DeletedSiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetDeployment

> Deployment sitesGetDeployment(resourceGroupName, name, id, subscriptionId, apiVersion)

Get the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetDeploymentSlot

> Deployment sitesGetDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

Get the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetDeployments

> DeploymentCollection sitesGetDeployments(resourceGroupName, name, subscriptionId, apiVersion)

List deployments

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetDeployments(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetDeploymentsSlot

> DeploymentCollection sitesGetDeploymentsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List deployments

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetDeploymentsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetInstanceDeployment

> Deployment sitesGetInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion)

Get the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetInstanceDeploymentSlot

> Deployment sitesGetInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion)

Get the deployment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let id = "id_example"; // String | Id of the deployment
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **id** | **String**| Id of the deployment | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetInstanceDeployments

> DeploymentCollection sitesGetInstanceDeployments(resourceGroupName, name, instanceId, subscriptionId, apiVersion)

List deployments

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetInstanceDeployments(resourceGroupName, name, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetInstanceDeploymentsSlot

> DeploymentCollection sitesGetInstanceDeploymentsSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion)

List deployments

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | Id of web app instance
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetInstanceDeploymentsSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| Id of web app instance | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSite

> Site sitesGetSite(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get details of a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example" // String | Additional web app properties included in the response
};
apiInstance.sitesGetSite(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteBackupConfiguration

> BackupRequest sitesGetSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion)

Gets the backup configuration for a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteBackupConfigurationSlot

> BackupRequest sitesGetSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the backup configuration for a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteBackupStatus

> BackupItem sitesGetSiteBackupStatus(resourceGroupName, name, backupId, subscriptionId, apiVersion)

Gets status of a web app backup that may be in progress.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteBackupStatus(resourceGroupName, name, backupId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteBackupStatusSecrets

> BackupItem sitesGetSiteBackupStatusSecrets(resourceGroupName, name, backupId, subscriptionId, apiVersion, request)

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.BackupRequest(); // BackupRequest | Information on backup request
apiInstance.sitesGetSiteBackupStatusSecrets(resourceGroupName, name, backupId, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteBackupStatusSecretsSlot

> BackupItem sitesGetSiteBackupStatusSecretsSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request)

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.BackupRequest(); // BackupRequest | Information on backup request
apiInstance.sitesGetSiteBackupStatusSecretsSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteBackupStatusSlot

> BackupItem sitesGetSiteBackupStatusSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion)

Gets status of a web app backup that may be in progress.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteBackupStatusSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteConfig

> SiteConfig sitesGetSiteConfig(resourceGroupName, name, subscriptionId, apiVersion)

Gets the configuration of the web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteConfigSlot

> SiteConfig sitesGetSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the configuration of the web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteHostNameBinding

> HostNameBinding sitesGetSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion)

Get web app binding for a hostname

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let hostName = "hostName_example"; // String | Name of host
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **hostName** | **String**| Name of host | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteHostNameBindingSlot

> HostNameBinding sitesGetSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion)

Get web app binding for a hostname

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let hostName = "hostName_example"; // String | Name of host
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **hostName** | **String**| Name of host | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteHostNameBindings

> HostNameBindingCollection sitesGetSiteHostNameBindings(resourceGroupName, name, subscriptionId, apiVersion)

Get web app hostname bindings

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteHostNameBindings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBindingCollection**](HostNameBindingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteHostNameBindingsSlot

> HostNameBindingCollection sitesGetSiteHostNameBindingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get web app hostname bindings

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteHostNameBindingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBindingCollection**](HostNameBindingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteInstanceIdentifiers

> SiteInstanceCollection sitesGetSiteInstanceIdentifiers(resourceGroupName, name, subscriptionId, apiVersion)

Gets all instance of a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteInstanceIdentifiers(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteInstanceCollection**](SiteInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteInstanceIdentifiersSlot

> SiteInstanceCollection sitesGetSiteInstanceIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets all instance of a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteInstanceIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteInstanceCollection**](SiteInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteLogsConfig

> SiteLogsConfig sitesGetSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion)

Gets the web app logs configuration

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteLogsConfigSlot

> SiteLogsConfig sitesGetSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the web app logs configuration

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteMetricDefinitions

> MetricDefinitionCollection sitesGetSiteMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Gets metric definitions for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteMetricDefinitionsSlot

> MetricDefinitionCollection sitesGetSiteMetricDefinitionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets metric definitions for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteMetricDefinitionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteMetrics

> ResourceMetricCollection sitesGetSiteMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets metrics for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | If true, metric details are included in response
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.sitesGetSiteMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| If true, metric details are included in response | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteMetricsSlot

> ResourceMetricCollection sitesGetSiteMetricsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Gets metrics for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | If true, metric details are included in response
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.sitesGetSiteMetricsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| If true, metric details are included in response | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteNetworkFeatures

> NetworkFeatures sitesGetSiteNetworkFeatures(resourceGroupName, name, view, subscriptionId, apiVersion)

Retrieves a view of all network features in use on this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let view = "view_example"; // String | The type of view. This can either be \"summary\" or \"detailed\".
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteNetworkFeatures(resourceGroupName, name, view, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **view** | **String**| The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**NetworkFeatures**](NetworkFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteNetworkFeaturesSlot

> NetworkFeatures sitesGetSiteNetworkFeaturesSlot(resourceGroupName, name, view, slot, subscriptionId, apiVersion)

Retrieves a view of all network features in use on this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let view = "view_example"; // String | The type of view. This can either be \"summary\" or \"detailed\".
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteNetworkFeaturesSlot(resourceGroupName, name, view, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **view** | **String**| The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;. | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**NetworkFeatures**](NetworkFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteOperation

> Object sitesGetSiteOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets the operation for a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let operationId = "operationId_example"; // String | Id of an operation
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **operationId** | **String**| Id of an operation | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteOperationSlot

> Object sitesGetSiteOperationSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion)

Gets the operation for a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let operationId = "operationId_example"; // String | Id of an operation
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteOperationSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **operationId** | **String**| Id of an operation | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSitePremierAddOn

> Object sitesGetSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let premierAddOnName = "premierAddOnName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **premierAddOnName** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSitePremierAddOnSlot

> Object sitesGetSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let premierAddOnName = "premierAddOnName_example"; // String | 
let slot = "slot_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **premierAddOnName** | **String**|  | 
 **slot** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteRelayServiceConnection

> RelayServiceConnectionEntity sitesGetSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion)

Retrieves a BizTalk Hybrid Connection identified by its entity name.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteRelayServiceConnectionSlot

> RelayServiceConnectionEntity sitesGetSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion)

Retrieves a BizTalk Hybrid Connection identified by its entity name.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteSlot

> Site sitesGetSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Get details of a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example" // String | Additional web app properties included in the response
};
apiInstance.sitesGetSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteSlots

> SiteCollection sitesGetSiteSlots(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets all the slots for a web apps

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example" // String | List of app properties to include in the response
};
apiInstance.sitesGetSiteSlots(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| List of app properties to include in the response | [optional] 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteSnapshots

> Object sitesGetSiteSnapshots(resourceGroupName, name, subscriptionId, apiVersion)

Returns all Snapshots to the user.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Webspace
let name = "name_example"; // String | Website Name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteSnapshots(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Webspace | 
 **name** | **String**| Website Name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteSnapshotsSlot

> Object sitesGetSiteSnapshotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Returns all Snapshots to the user.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Webspace
let name = "name_example"; // String | Website Name
let slot = "slot_example"; // String | Website Slot
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteSnapshotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Webspace | 
 **name** | **String**| Website Name | 
 **slot** | **String**| Website Slot | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteSourceControl

> SiteSourceControl sitesGetSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion)

Get the source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteSourceControlSlot

> SiteSourceControl sitesGetSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get the source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteUsages

> CsmUsageQuotaCollection sitesGetSiteUsages(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets the quota usage numbers for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.sitesGetSiteUsages(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**CsmUsageQuotaCollection**](CsmUsageQuotaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteUsagesSlot

> CsmUsageQuotaCollection sitesGetSiteUsagesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Gets the quota usage numbers for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.sitesGetSiteUsagesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**CsmUsageQuotaCollection**](CsmUsageQuotaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSiteVNETConnection

> VnetInfo sitesGetSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Retrieves a specific Virtual Network Connection associated with this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteVNETConnectionSlot

> VnetInfo sitesGetSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion)

Retrieves a specific Virtual Network Connection associated with this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteVNETConnections

> [VnetInfo] sitesGetSiteVNETConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieves a list of all Virtual Network Connections associated with this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteVNETConnections(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[VnetInfo]**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteVNETConnectionsSlot

> [VnetInfo] sitesGetSiteVNETConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Retrieves a list of all Virtual Network Connections associated with this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteVNETConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[VnetInfo]**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteVnetGateway

> Object sitesGetSiteVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Retrieves a Virtual Network connection gateway associated with this web app and virtual network.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSiteVnetGatewaySlot

> Object sitesGetSiteVnetGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion)

Retrieves a Virtual Network connection gateway associated with this web app and virtual network.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSiteVnetGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSites

> SiteCollection sitesGetSites(resourceGroupName, subscriptionId, apiVersion, opts)

Gets the web apps for a subscription in the specified resource group

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example", // String | Additional web app properties included in the response
  'includeSiteTypes': "includeSiteTypes_example", // String | Types of apps included in the response
  'includeSlots': true // Boolean | Whether or not to include deployments slots in results
};
apiInstance.sitesGetSites(resourceGroupName, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] 
 **includeSiteTypes** | **String**| Types of apps included in the response | [optional] 
 **includeSlots** | **Boolean**| Whether or not to include deployments slots in results | [optional] 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesGetSlotConfigNames

> SlotConfigNamesResource sitesGetSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion)

Gets the names of application settings and connection string that remain with the slot during swap operation

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesGetSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SlotConfigNamesResource**](SlotConfigNamesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesGetSlotsDifferencesFromProduction

> SlotDifferenceCollection sitesGetSlotsDifferencesFromProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Get the difference in configuration settings between two web app slots

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebSiteManagementClient.CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
apiInstance.sitesGetSlotsDifferencesFromProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | 

### Return type

[**SlotDifferenceCollection**](SlotDifferenceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json


## sitesGetSlotsDifferencesSlot

> SlotDifferenceCollection sitesGetSlotsDifferencesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Get the difference in configuration settings between two web app slots

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of the source slot
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebSiteManagementClient.CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
apiInstance.sitesGetSlotsDifferencesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of the source slot | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | 

### Return type

[**SlotDifferenceCollection**](SlotDifferenceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json


## sitesIsSiteCloneable

> SiteCloneability sitesIsSiteCloneable(resourceGroupName, name, subscriptionId, apiVersion)

Creates a new web app or modifies an existing web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesIsSiteCloneable(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteCloneability**](SiteCloneability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesIsSiteCloneableSlot

> SiteCloneability sitesIsSiteCloneableSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Creates a new web app or modifies an existing web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesIsSiteCloneableSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteCloneability**](SiteCloneability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteAppSettings

> StringDictionary sitesListSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the application settings of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteAppSettingsSlot

> StringDictionary sitesListSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the application settings of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteAuthSettings

> SiteAuthSettings sitesListSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the Authentication / Authorization settings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteAuthSettingsSlot

> SiteAuthSettings sitesListSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the Authentication / Authorization settings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteBackups

> BackupItemCollection sitesListSiteBackups(resourceGroupName, name, subscriptionId, apiVersion)

Lists all available backups for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteBackups(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItemCollection**](BackupItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesListSiteBackupsSlot

> BackupItemCollection sitesListSiteBackupsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Lists all available backups for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteBackupsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItemCollection**](BackupItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## sitesListSiteConnectionStrings

> ConnectionStringDictionary sitesListSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the connection strings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteConnectionStringsSlot

> ConnectionStringDictionary sitesListSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the connection strings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteMetadata

> StringDictionary sitesListSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion)

Gets the web app meta data.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteMetadataSlot

> StringDictionary sitesListSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the web app meta data.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSitePremierAddOns

> Object sitesListSitePremierAddOns(resourceGroupName, name, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSitePremierAddOns(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSitePremierAddOnsSlot

> Object sitesListSitePremierAddOnsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let slot = "slot_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSitePremierAddOnsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **slot** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSitePublishingCredentials

> User sitesListSitePublishingCredentials(resourceGroupName, name, subscriptionId, apiVersion)

Gets the web app publishing credentials

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSitePublishingCredentials(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSitePublishingCredentialsSlot

> User sitesListSitePublishingCredentialsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the web app publishing credentials

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSitePublishingCredentialsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSitePublishingProfileXml

> File sitesListSitePublishingProfileXml(resourceGroupName, name, subscriptionId, apiVersion, options)

Gets the publishing profile for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let options = new WebSiteManagementClient.CsmPublishingProfileOptions(); // CsmPublishingProfileOptions | Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format=FileZilla3 for FileZilla FTP format.
apiInstance.sitesListSitePublishingProfileXml(resourceGroupName, name, subscriptionId, apiVersion, options, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **options** | [**CsmPublishingProfileOptions**](CsmPublishingProfileOptions.md)| Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format&#x3D;FileZilla3 for FileZilla FTP format. | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSitePublishingProfileXmlSlot

> File sitesListSitePublishingProfileXmlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, options)

Gets the publishing profile for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let options = new WebSiteManagementClient.CsmPublishingProfileOptions(); // CsmPublishingProfileOptions | Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format=FileZilla3 for FileZilla FTP format.
apiInstance.sitesListSitePublishingProfileXmlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, options, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **options** | [**CsmPublishingProfileOptions**](CsmPublishingProfileOptions.md)| Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format&#x3D;FileZilla3 for FileZilla FTP format. | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteRelayServiceConnections

> RelayServiceConnectionEntity sitesListSiteRelayServiceConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieves all BizTalk Hybrid Connections associated with this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteRelayServiceConnections(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesListSiteRelayServiceConnectionsSlot

> RelayServiceConnectionEntity sitesListSiteRelayServiceConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Retrieves all BizTalk Hybrid Connections associated with this web app.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesListSiteRelayServiceConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesRecoverSite

> Site sitesRecoverSite(resourceGroupName, name, subscriptionId, apiVersion, recoveryEntity)

Recovers a deleted web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let recoveryEntity = new WebSiteManagementClient.CsmSiteRecoveryEntity(); // CsmSiteRecoveryEntity | Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
apiInstance.sitesRecoverSite(resourceGroupName, name, subscriptionId, apiVersion, recoveryEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **recoveryEntity** | [**CsmSiteRecoveryEntity**](CsmSiteRecoveryEntity.md)| Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API. | 

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesRecoverSiteSlot

> Site sitesRecoverSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, recoveryEntity)

Recovers a deleted web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let recoveryEntity = new WebSiteManagementClient.CsmSiteRecoveryEntity(); // CsmSiteRecoveryEntity | Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
apiInstance.sitesRecoverSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, recoveryEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **recoveryEntity** | [**CsmSiteRecoveryEntity**](CsmSiteRecoveryEntity.md)| Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API. | 

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesResetProductionSlotConfig

> Object sitesResetProductionSlotConfig(resourceGroupName, name, subscriptionId, apiVersion)

Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesResetProductionSlotConfig(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesResetSlotConfigSlot

> Object sitesResetSlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesResetSlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesRestartSite

> Object sitesRestartSite(resourceGroupName, name, subscriptionId, apiVersion, opts)

Restarts web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'softRestart': true, // Boolean | Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app
  'synchronous': true // Boolean | If true then the API will block until the app has been restarted
};
apiInstance.sitesRestartSite(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **softRestart** | **Boolean**| Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app | [optional] 
 **synchronous** | **Boolean**| If true then the API will block until the app has been restarted | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesRestartSiteSlot

> Object sitesRestartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Restarts web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'softRestart': true, // Boolean | Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app
  'synchronous': true // Boolean | If true then the API will block until the app has been restarted
};
apiInstance.sitesRestartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **softRestart** | **Boolean**| Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app | [optional] 
 **synchronous** | **Boolean**| If true then the API will block until the app has been restarted | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesRestoreSite

> RestoreResponse sitesRestoreSite(resourceGroupName, name, backupId, subscriptionId, apiVersion, request)

Restores a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup to restore
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.RestoreRequest(); // RestoreRequest | Information on restore request
apiInstance.sitesRestoreSite(resourceGroupName, name, backupId, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup to restore | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | 

### Return type

[**RestoreResponse**](RestoreResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesRestoreSiteSlot

> RestoreResponse sitesRestoreSiteSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request)

Restores a web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let backupId = "backupId_example"; // String | Id of backup to restore
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.RestoreRequest(); // RestoreRequest | Information on restore request
apiInstance.sitesRestoreSiteSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **backupId** | **String**| Id of backup to restore | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | 

### Return type

[**RestoreResponse**](RestoreResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesStartSite

> Object sitesStartSite(resourceGroupName, name, subscriptionId, apiVersion)

Starts web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesStartSite(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesStartSiteSlot

> Object sitesStartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Starts web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesStartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesStopSite

> Object sitesStopSite(resourceGroupName, name, subscriptionId, apiVersion)

Stops web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesStopSite(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesStopSiteSlot

> Object sitesStopSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Stops web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesStopSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesSwapSlotWithProduction

> Object sitesSwapSlotWithProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Swaps web app slots

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebSiteManagementClient.CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
apiInstance.sitesSwapSlotWithProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesSwapSlotsSlot

> Object sitesSwapSlotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Swaps web app slots

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of source slot for the swap
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebSiteManagementClient.CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
apiInstance.sitesSwapSlotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of source slot for the swap | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesSyncSiteRepository

> Object sitesSyncSiteRepository(resourceGroupName, name, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesSyncSiteRepository(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesSyncSiteRepositorySlot

> Object sitesSyncSiteRepositorySlot(resourceGroupName, name, slot, subscriptionId, apiVersion)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let name = "name_example"; // String | 
let slot = "slot_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.sitesSyncSiteRepositorySlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**|  | 
 **name** | **String**|  | 
 **slot** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteAppSettings

> StringDictionary sitesUpdateSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion, appSettings)

Updates the application settings of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let appSettings = new WebSiteManagementClient.StringDictionary(); // StringDictionary | Application settings of web app
apiInstance.sitesUpdateSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion, appSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **appSettings** | [**StringDictionary**](StringDictionary.md)| Application settings of web app | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteAppSettingsSlot

> StringDictionary sitesUpdateSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, appSettings)

Updates the application settings of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let appSettings = new WebSiteManagementClient.StringDictionary(); // StringDictionary | Application settings of web app
apiInstance.sitesUpdateSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, appSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **appSettings** | [**StringDictionary**](StringDictionary.md)| Application settings of web app | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteAuthSettings

> SiteAuthSettings sitesUpdateSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, siteAuthSettings)

Updates the Authentication / Authorization settings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteAuthSettings = new WebSiteManagementClient.SiteAuthSettings(); // SiteAuthSettings | Auth settings associated with web app
apiInstance.sitesUpdateSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, siteAuthSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteAuthSettings** | [**SiteAuthSettings**](SiteAuthSettings.md)| Auth settings associated with web app | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteAuthSettingsSlot

> SiteAuthSettings sitesUpdateSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteAuthSettings)

Updates the Authentication / Authorization settings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteAuthSettings = new WebSiteManagementClient.SiteAuthSettings(); // SiteAuthSettings | Auth settings associated with web app
apiInstance.sitesUpdateSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteAuthSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteAuthSettings** | [**SiteAuthSettings**](SiteAuthSettings.md)| Auth settings associated with web app | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteBackupConfiguration

> BackupRequest sitesUpdateSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, request)

Updates backup configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.BackupRequest(); // BackupRequest | Information on backup request
apiInstance.sitesUpdateSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteBackupConfigurationSlot

> BackupRequest sitesUpdateSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Updates backup configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.BackupRequest(); // BackupRequest | Information on backup request
apiInstance.sitesUpdateSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteConfig

> SiteConfig sitesUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebSiteManagementClient.SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
apiInstance.sitesUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | 

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteConfigSlot

> SiteConfig sitesUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebSiteManagementClient.SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
apiInstance.sitesUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | 

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteConnectionStrings

> ConnectionStringDictionary sitesUpdateSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, connectionStrings)

Updates the connection strings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionStrings = new WebSiteManagementClient.ConnectionStringDictionary(); // ConnectionStringDictionary | Connection strings associated with web app
apiInstance.sitesUpdateSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, connectionStrings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionStrings** | [**ConnectionStringDictionary**](ConnectionStringDictionary.md)| Connection strings associated with web app | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteConnectionStringsSlot

> ConnectionStringDictionary sitesUpdateSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionStrings)

Updates the connection strings associated with web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionStrings = new WebSiteManagementClient.ConnectionStringDictionary(); // ConnectionStringDictionary | Connection strings associated with web app
apiInstance.sitesUpdateSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionStrings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionStrings** | [**ConnectionStringDictionary**](ConnectionStringDictionary.md)| Connection strings associated with web app | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteLogsConfig

> SiteLogsConfig sitesUpdateSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, siteLogsConfig)

Updates the meta data for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteLogsConfig = new WebSiteManagementClient.SiteLogsConfig(); // SiteLogsConfig | Site logs configuration
apiInstance.sitesUpdateSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, siteLogsConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteLogsConfig** | [**SiteLogsConfig**](SiteLogsConfig.md)| Site logs configuration | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteLogsConfigSlot

> SiteLogsConfig sitesUpdateSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteLogsConfig)

Updates the meta data for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteLogsConfig = new WebSiteManagementClient.SiteLogsConfig(); // SiteLogsConfig | Site logs configuration
apiInstance.sitesUpdateSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteLogsConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteLogsConfig** | [**SiteLogsConfig**](SiteLogsConfig.md)| Site logs configuration | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteMetadata

> StringDictionary sitesUpdateSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion, metadata)

Updates the meta data for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let metadata = new WebSiteManagementClient.StringDictionary(); // StringDictionary | Meta data of web app
apiInstance.sitesUpdateSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion, metadata, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **metadata** | [**StringDictionary**](StringDictionary.md)| Meta data of web app | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteMetadataSlot

> StringDictionary sitesUpdateSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, metadata)

Updates the meta data for web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let metadata = new WebSiteManagementClient.StringDictionary(); // StringDictionary | Meta data of web app
apiInstance.sitesUpdateSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, metadata, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **metadata** | [**StringDictionary**](StringDictionary.md)| Meta data of web app | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteRelayServiceConnection

> RelayServiceConnectionEntity sitesUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
apiInstance.sitesUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteRelayServiceConnectionSlot

> RelayServiceConnectionEntity sitesUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
apiInstance.sitesUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **entityName** | **String**| The name by which the Hybrid Connection is identified | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteSourceControl

> SiteSourceControl sitesUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebSiteManagementClient.SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
apiInstance.sitesUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteSourceControlSlot

> SiteSourceControl sitesUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebSiteManagementClient.SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
apiInstance.sitesUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteVNETConnection

> VnetInfo sitesUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
apiInstance.sitesUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteVNETConnectionGateway

> VnetGateway sitesUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetGateway(); // VnetGateway | The properties to update this gateway with.
apiInstance.sitesUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | 

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteVNETConnectionGatewaySlot

> VnetGateway sitesUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetGateway(); // VnetGateway | The properties to update this gateway with.
apiInstance.sitesUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | 

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSiteVNETConnectionSlot

> VnetInfo sitesUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let name = "name_example"; // String | The name of the web app
let vnetName = "vnetName_example"; // String | The name of the Virtual Network
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
apiInstance.sitesUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The resource group name | 
 **name** | **String**| The name of the web app | 
 **vnetName** | **String**| The name of the Virtual Network | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## sitesUpdateSlotConfigNames

> SlotConfigNamesResource sitesUpdateSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion, slotConfigNames)

Updates the names of application settings and connection string that remain with the slot during swap operation

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.SitesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let slotConfigNames = new WebSiteManagementClient.SlotConfigNamesResource(); // SlotConfigNamesResource | Request body containing the names of application settings and connection strings
apiInstance.sitesUpdateSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion, slotConfigNames, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **slotConfigNames** | [**SlotConfigNamesResource**](SlotConfigNamesResource.md)| Request body containing the names of application settings and connection strings | 

### Return type

[**SlotConfigNamesResource**](SlotConfigNamesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

