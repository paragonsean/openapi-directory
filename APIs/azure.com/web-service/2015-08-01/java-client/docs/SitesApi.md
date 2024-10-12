# SitesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sitesAddSitePremierAddOn**](SitesApi.md#sitesAddSitePremierAddOn) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} |  |
| [**sitesAddSitePremierAddOnSlot**](SitesApi.md#sitesAddSitePremierAddOnSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} |  |
| [**sitesApplySlotConfigSlot**](SitesApi.md#sitesApplySlotConfigSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/applySlotConfig | Applies the configuration settings from the target slot onto the current slot |
| [**sitesApplySlotConfigToProduction**](SitesApi.md#sitesApplySlotConfigToProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/applySlotConfig | Applies the configuration settings from the target slot onto the current slot |
| [**sitesBackupSite**](SitesApi.md#sitesBackupSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backup | Creates web app backup |
| [**sitesBackupSiteSlot**](SitesApi.md#sitesBackupSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backup | Creates web app backup |
| [**sitesCreateDeployment**](SitesApi.md#sitesCreateDeployment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Create a deployment |
| [**sitesCreateDeploymentSlot**](SitesApi.md#sitesCreateDeploymentSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Create a deployment |
| [**sitesCreateInstanceDeployment**](SitesApi.md#sitesCreateInstanceDeployment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments/{id} | Create a deployment |
| [**sitesCreateInstanceDeploymentSlot**](SitesApi.md#sitesCreateInstanceDeploymentSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments/{id} | Create a deployment |
| [**sitesCreateOrUpdateSite**](SitesApi.md#sitesCreateOrUpdateSite) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Creates a new web app or modifies an existing web app. |
| [**sitesCreateOrUpdateSiteConfig**](SitesApi.md#sitesCreateOrUpdateSiteConfig) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Update the configuration of web app |
| [**sitesCreateOrUpdateSiteConfigSlot**](SitesApi.md#sitesCreateOrUpdateSiteConfigSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Update the configuration of web app |
| [**sitesCreateOrUpdateSiteHostNameBinding**](SitesApi.md#sitesCreateOrUpdateSiteHostNameBinding) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Creates a web app hostname binding |
| [**sitesCreateOrUpdateSiteHostNameBindingSlot**](SitesApi.md#sitesCreateOrUpdateSiteHostNameBindingSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Creates a web app hostname binding |
| [**sitesCreateOrUpdateSiteRelayServiceConnection**](SitesApi.md#sitesCreateOrUpdateSiteRelayServiceConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one. |
| [**sitesCreateOrUpdateSiteRelayServiceConnectionSlot**](SitesApi.md#sitesCreateOrUpdateSiteRelayServiceConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one. |
| [**sitesCreateOrUpdateSiteSlot**](SitesApi.md#sitesCreateOrUpdateSiteSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Creates a new web app or modifies an existing web app. |
| [**sitesCreateOrUpdateSiteSourceControl**](SitesApi.md#sitesCreateOrUpdateSiteSourceControl) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Update the source control configuration of web app |
| [**sitesCreateOrUpdateSiteSourceControlSlot**](SitesApi.md#sitesCreateOrUpdateSiteSourceControlSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Update the source control configuration of web app |
| [**sitesCreateOrUpdateSiteVNETConnection**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties. |
| [**sitesCreateOrUpdateSiteVNETConnectionGateway**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnectionGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway. |
| [**sitesCreateOrUpdateSiteVNETConnectionGatewaySlot**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnectionGatewaySlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway. |
| [**sitesCreateOrUpdateSiteVNETConnectionSlot**](SitesApi.md#sitesCreateOrUpdateSiteVNETConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties. |
| [**sitesDeleteBackup**](SitesApi.md#sitesDeleteBackup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId} | Deletes a backup from Azure Storage |
| [**sitesDeleteBackupSlot**](SitesApi.md#sitesDeleteBackupSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId} | Deletes a backup from Azure Storage |
| [**sitesDeleteDeployment**](SitesApi.md#sitesDeleteDeployment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Delete the deployment |
| [**sitesDeleteDeploymentSlot**](SitesApi.md#sitesDeleteDeploymentSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Delete the deployment |
| [**sitesDeleteInstanceDeployment**](SitesApi.md#sitesDeleteInstanceDeployment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments/{id} | Delete the deployment |
| [**sitesDeleteInstanceDeploymentSlot**](SitesApi.md#sitesDeleteInstanceDeploymentSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments/{id} | Delete the deployment |
| [**sitesDeleteSite**](SitesApi.md#sitesDeleteSite) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Deletes a web app |
| [**sitesDeleteSiteHostNameBinding**](SitesApi.md#sitesDeleteSiteHostNameBinding) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Deletes a host name binding |
| [**sitesDeleteSiteHostNameBindingSlot**](SitesApi.md#sitesDeleteSiteHostNameBindingSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Deletes a host name binding |
| [**sitesDeleteSitePremierAddOn**](SitesApi.md#sitesDeleteSitePremierAddOn) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} |  |
| [**sitesDeleteSitePremierAddOnSlot**](SitesApi.md#sitesDeleteSitePremierAddOnSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} |  |
| [**sitesDeleteSiteRelayServiceConnection**](SitesApi.md#sitesDeleteSiteRelayServiceConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Removes the association to a BizTalk Hybrid Connection, identified by its entity name. |
| [**sitesDeleteSiteRelayServiceConnectionSlot**](SitesApi.md#sitesDeleteSiteRelayServiceConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Removes the association to a BizTalk Hybrid Connection, identified by its entity name. |
| [**sitesDeleteSiteSlot**](SitesApi.md#sitesDeleteSiteSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Deletes a web app |
| [**sitesDeleteSiteSourceControl**](SitesApi.md#sitesDeleteSiteSourceControl) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Delete source control configuration of web app |
| [**sitesDeleteSiteSourceControlSlot**](SitesApi.md#sitesDeleteSiteSourceControlSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Delete source control configuration of web app |
| [**sitesDeleteSiteVNETConnection**](SitesApi.md#sitesDeleteSiteVNETConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Removes the specified Virtual Network Connection association from this web app. |
| [**sitesDeleteSiteVNETConnectionSlot**](SitesApi.md#sitesDeleteSiteVNETConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Removes the specified Virtual Network Connection association from this web app. |
| [**sitesDiscoverSiteRestore**](SitesApi.md#sitesDiscoverSiteRestore) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/discover | Discovers existing web app backups that can be restored |
| [**sitesDiscoverSiteRestoreSlot**](SitesApi.md#sitesDiscoverSiteRestoreSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/discover | Discovers existing web app backups that can be restored |
| [**sitesGenerateNewSitePublishingPassword**](SitesApi.md#sitesGenerateNewSitePublishingPassword) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/newpassword | Generates new random app publishing password |
| [**sitesGenerateNewSitePublishingPasswordSlot**](SitesApi.md#sitesGenerateNewSitePublishingPasswordSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/newpassword | Generates new random app publishing password |
| [**sitesGetDeletedSites**](SitesApi.md#sitesGetDeletedSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/deletedSites | Gets deleted web apps in subscription |
| [**sitesGetDeployment**](SitesApi.md#sitesGetDeployment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Get the deployment |
| [**sitesGetDeploymentSlot**](SitesApi.md#sitesGetDeploymentSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Get the deployment |
| [**sitesGetDeployments**](SitesApi.md#sitesGetDeployments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments | List deployments |
| [**sitesGetDeploymentsSlot**](SitesApi.md#sitesGetDeploymentsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments | List deployments |
| [**sitesGetInstanceDeployment**](SitesApi.md#sitesGetInstanceDeployment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments/{id} | Get the deployment |
| [**sitesGetInstanceDeploymentSlot**](SitesApi.md#sitesGetInstanceDeploymentSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments/{id} | Get the deployment |
| [**sitesGetInstanceDeployments**](SitesApi.md#sitesGetInstanceDeployments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/deployments | List deployments |
| [**sitesGetInstanceDeploymentsSlot**](SitesApi.md#sitesGetInstanceDeploymentsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/deployments | List deployments |
| [**sitesGetSite**](SitesApi.md#sitesGetSite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Get details of a web app |
| [**sitesGetSiteBackupConfiguration**](SitesApi.md#sitesGetSiteBackupConfiguration) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup/list | Gets the backup configuration for a web app |
| [**sitesGetSiteBackupConfigurationSlot**](SitesApi.md#sitesGetSiteBackupConfigurationSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup/list | Gets the backup configuration for a web app |
| [**sitesGetSiteBackupStatus**](SitesApi.md#sitesGetSiteBackupStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId} | Gets status of a web app backup that may be in progress. |
| [**sitesGetSiteBackupStatusSecrets**](SitesApi.md#sitesGetSiteBackupStatusSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId}/list | Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. |
| [**sitesGetSiteBackupStatusSecretsSlot**](SitesApi.md#sitesGetSiteBackupStatusSecretsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId}/list | Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. |
| [**sitesGetSiteBackupStatusSlot**](SitesApi.md#sitesGetSiteBackupStatusSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId} | Gets status of a web app backup that may be in progress. |
| [**sitesGetSiteConfig**](SitesApi.md#sitesGetSiteConfig) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Gets the configuration of the web app |
| [**sitesGetSiteConfigSlot**](SitesApi.md#sitesGetSiteConfigSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Gets the configuration of the web app |
| [**sitesGetSiteHostNameBinding**](SitesApi.md#sitesGetSiteHostNameBinding) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Get web app binding for a hostname |
| [**sitesGetSiteHostNameBindingSlot**](SitesApi.md#sitesGetSiteHostNameBindingSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Get web app binding for a hostname |
| [**sitesGetSiteHostNameBindings**](SitesApi.md#sitesGetSiteHostNameBindings) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings | Get web app hostname bindings |
| [**sitesGetSiteHostNameBindingsSlot**](SitesApi.md#sitesGetSiteHostNameBindingsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings | Get web app hostname bindings |
| [**sitesGetSiteInstanceIdentifiers**](SitesApi.md#sitesGetSiteInstanceIdentifiers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances | Gets all instance of a web app |
| [**sitesGetSiteInstanceIdentifiersSlot**](SitesApi.md#sitesGetSiteInstanceIdentifiersSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances | Gets all instance of a web app |
| [**sitesGetSiteLogsConfig**](SitesApi.md#sitesGetSiteLogsConfig) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/logs | Gets the web app logs configuration |
| [**sitesGetSiteLogsConfigSlot**](SitesApi.md#sitesGetSiteLogsConfigSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs | Gets the web app logs configuration |
| [**sitesGetSiteMetricDefinitions**](SitesApi.md#sitesGetSiteMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/metricdefinitions | Gets metric definitions for web app |
| [**sitesGetSiteMetricDefinitionsSlot**](SitesApi.md#sitesGetSiteMetricDefinitionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metricdefinitions | Gets metric definitions for web app |
| [**sitesGetSiteMetrics**](SitesApi.md#sitesGetSiteMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/metrics | Gets metrics for web app |
| [**sitesGetSiteMetricsSlot**](SitesApi.md#sitesGetSiteMetricsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metrics | Gets metrics for web app |
| [**sitesGetSiteNetworkFeatures**](SitesApi.md#sitesGetSiteNetworkFeatures) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkFeatures/{view} | Retrieves a view of all network features in use on this web app. |
| [**sitesGetSiteNetworkFeaturesSlot**](SitesApi.md#sitesGetSiteNetworkFeaturesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkFeatures/{view} | Retrieves a view of all network features in use on this web app. |
| [**sitesGetSiteOperation**](SitesApi.md#sitesGetSiteOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/operationresults/{operationId} | Gets the operation for a web app |
| [**sitesGetSiteOperationSlot**](SitesApi.md#sitesGetSiteOperationSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/operationresults/{operationId} | Gets the operation for a web app |
| [**sitesGetSitePremierAddOn**](SitesApi.md#sitesGetSitePremierAddOn) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} |  |
| [**sitesGetSitePremierAddOnSlot**](SitesApi.md#sitesGetSitePremierAddOnSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} |  |
| [**sitesGetSiteRelayServiceConnection**](SitesApi.md#sitesGetSiteRelayServiceConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Retrieves a BizTalk Hybrid Connection identified by its entity name. |
| [**sitesGetSiteRelayServiceConnectionSlot**](SitesApi.md#sitesGetSiteRelayServiceConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Retrieves a BizTalk Hybrid Connection identified by its entity name. |
| [**sitesGetSiteSlot**](SitesApi.md#sitesGetSiteSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Get details of a web app |
| [**sitesGetSiteSlots**](SitesApi.md#sitesGetSiteSlots) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots | Gets all the slots for a web apps |
| [**sitesGetSiteSnapshots**](SitesApi.md#sitesGetSiteSnapshots) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/snapshots | Returns all Snapshots to the user. |
| [**sitesGetSiteSnapshotsSlot**](SitesApi.md#sitesGetSiteSnapshotsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/snapshots | Returns all Snapshots to the user. |
| [**sitesGetSiteSourceControl**](SitesApi.md#sitesGetSiteSourceControl) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Get the source control configuration of web app |
| [**sitesGetSiteSourceControlSlot**](SitesApi.md#sitesGetSiteSourceControlSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Get the source control configuration of web app |
| [**sitesGetSiteUsages**](SitesApi.md#sitesGetSiteUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/usages | Gets the quota usage numbers for web app |
| [**sitesGetSiteUsagesSlot**](SitesApi.md#sitesGetSiteUsagesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/usages | Gets the quota usage numbers for web app |
| [**sitesGetSiteVNETConnection**](SitesApi.md#sitesGetSiteVNETConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Retrieves a specific Virtual Network Connection associated with this web app. |
| [**sitesGetSiteVNETConnectionSlot**](SitesApi.md#sitesGetSiteVNETConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Retrieves a specific Virtual Network Connection associated with this web app. |
| [**sitesGetSiteVNETConnections**](SitesApi.md#sitesGetSiteVNETConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections | Retrieves a list of all Virtual Network Connections associated with this web app. |
| [**sitesGetSiteVNETConnectionsSlot**](SitesApi.md#sitesGetSiteVNETConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections | Retrieves a list of all Virtual Network Connections associated with this web app. |
| [**sitesGetSiteVnetGateway**](SitesApi.md#sitesGetSiteVnetGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Retrieves a Virtual Network connection gateway associated with this web app and virtual network. |
| [**sitesGetSiteVnetGatewaySlot**](SitesApi.md#sitesGetSiteVnetGatewaySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Retrieves a Virtual Network connection gateway associated with this web app and virtual network. |
| [**sitesGetSites**](SitesApi.md#sitesGetSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites | Gets the web apps for a subscription in the specified resource group |
| [**sitesGetSlotConfigNames**](SitesApi.md#sitesGetSlotConfigNames) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames | Gets the names of application settings and connection string that remain with the slot during swap operation |
| [**sitesGetSlotsDifferencesFromProduction**](SitesApi.md#sitesGetSlotsDifferencesFromProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slotsdiffs | Get the difference in configuration settings between two web app slots |
| [**sitesGetSlotsDifferencesSlot**](SitesApi.md#sitesGetSlotsDifferencesSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsdiffs | Get the difference in configuration settings between two web app slots |
| [**sitesIsSiteCloneable**](SitesApi.md#sitesIsSiteCloneable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/iscloneable | Creates a new web app or modifies an existing web app. |
| [**sitesIsSiteCloneableSlot**](SitesApi.md#sitesIsSiteCloneableSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/iscloneable | Creates a new web app or modifies an existing web app. |
| [**sitesListSiteAppSettings**](SitesApi.md#sitesListSiteAppSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings/list | Gets the application settings of web app |
| [**sitesListSiteAppSettingsSlot**](SitesApi.md#sitesListSiteAppSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings/list | Gets the application settings of web app |
| [**sitesListSiteAuthSettings**](SitesApi.md#sitesListSiteAuthSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings/list | Gets the Authentication / Authorization settings associated with web app |
| [**sitesListSiteAuthSettingsSlot**](SitesApi.md#sitesListSiteAuthSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings/list | Gets the Authentication / Authorization settings associated with web app |
| [**sitesListSiteBackups**](SitesApi.md#sitesListSiteBackups) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups | Lists all available backups for web app |
| [**sitesListSiteBackupsSlot**](SitesApi.md#sitesListSiteBackupsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups | Lists all available backups for web app |
| [**sitesListSiteConnectionStrings**](SitesApi.md#sitesListSiteConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings/list | Gets the connection strings associated with web app |
| [**sitesListSiteConnectionStringsSlot**](SitesApi.md#sitesListSiteConnectionStringsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings/list | Gets the connection strings associated with web app |
| [**sitesListSiteMetadata**](SitesApi.md#sitesListSiteMetadata) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata/list | Gets the web app meta data. |
| [**sitesListSiteMetadataSlot**](SitesApi.md#sitesListSiteMetadataSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata/list | Gets the web app meta data. |
| [**sitesListSitePremierAddOns**](SitesApi.md#sitesListSitePremierAddOns) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons |  |
| [**sitesListSitePremierAddOnsSlot**](SitesApi.md#sitesListSitePremierAddOnsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons |  |
| [**sitesListSitePublishingCredentials**](SitesApi.md#sitesListSitePublishingCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/publishingcredentials/list | Gets the web app publishing credentials |
| [**sitesListSitePublishingCredentialsSlot**](SitesApi.md#sitesListSitePublishingCredentialsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/publishingcredentials/list | Gets the web app publishing credentials |
| [**sitesListSitePublishingProfileXml**](SitesApi.md#sitesListSitePublishingProfileXml) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publishxml | Gets the publishing profile for web app |
| [**sitesListSitePublishingProfileXmlSlot**](SitesApi.md#sitesListSitePublishingProfileXmlSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publishxml | Gets the publishing profile for web app |
| [**sitesListSiteRelayServiceConnections**](SitesApi.md#sitesListSiteRelayServiceConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection | Retrieves all BizTalk Hybrid Connections associated with this web app. |
| [**sitesListSiteRelayServiceConnectionsSlot**](SitesApi.md#sitesListSiteRelayServiceConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection | Retrieves all BizTalk Hybrid Connections associated with this web app. |
| [**sitesRecoverSite**](SitesApi.md#sitesRecoverSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/recover | Recovers a deleted web app |
| [**sitesRecoverSiteSlot**](SitesApi.md#sitesRecoverSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/recover | Recovers a deleted web app |
| [**sitesResetProductionSlotConfig**](SitesApi.md#sitesResetProductionSlotConfig) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resetSlotConfig | Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API |
| [**sitesResetSlotConfigSlot**](SitesApi.md#sitesResetSlotConfigSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resetSlotConfig | Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API |
| [**sitesRestartSite**](SitesApi.md#sitesRestartSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/restart | Restarts web app |
| [**sitesRestartSiteSlot**](SitesApi.md#sitesRestartSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restart | Restarts web app |
| [**sitesRestoreSite**](SitesApi.md#sitesRestoreSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId}/restore | Restores a web app |
| [**sitesRestoreSiteSlot**](SitesApi.md#sitesRestoreSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId}/restore | Restores a web app |
| [**sitesStartSite**](SitesApi.md#sitesStartSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/start | Starts web app |
| [**sitesStartSiteSlot**](SitesApi.md#sitesStartSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/start | Starts web app |
| [**sitesStopSite**](SitesApi.md#sitesStopSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/stop | Stops web app |
| [**sitesStopSiteSlot**](SitesApi.md#sitesStopSiteSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/stop | Stops web app |
| [**sitesSwapSlotWithProduction**](SitesApi.md#sitesSwapSlotWithProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slotsswap | Swaps web app slots |
| [**sitesSwapSlotsSlot**](SitesApi.md#sitesSwapSlotsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsswap | Swaps web app slots |
| [**sitesSyncSiteRepository**](SitesApi.md#sitesSyncSiteRepository) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sync |  |
| [**sitesSyncSiteRepositorySlot**](SitesApi.md#sitesSyncSiteRepositorySlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sync |  |
| [**sitesUpdateSiteAppSettings**](SitesApi.md#sitesUpdateSiteAppSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings | Updates the application settings of web app |
| [**sitesUpdateSiteAppSettingsSlot**](SitesApi.md#sitesUpdateSiteAppSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings | Updates the application settings of web app |
| [**sitesUpdateSiteAuthSettings**](SitesApi.md#sitesUpdateSiteAuthSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings | Updates the Authentication / Authorization settings associated with web app |
| [**sitesUpdateSiteAuthSettingsSlot**](SitesApi.md#sitesUpdateSiteAuthSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings | Updates the Authentication / Authorization settings associated with web app |
| [**sitesUpdateSiteBackupConfiguration**](SitesApi.md#sitesUpdateSiteBackupConfiguration) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup | Updates backup configuration of web app |
| [**sitesUpdateSiteBackupConfigurationSlot**](SitesApi.md#sitesUpdateSiteBackupConfigurationSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup | Updates backup configuration of web app |
| [**sitesUpdateSiteConfig**](SitesApi.md#sitesUpdateSiteConfig) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Update the configuration of web app |
| [**sitesUpdateSiteConfigSlot**](SitesApi.md#sitesUpdateSiteConfigSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Update the configuration of web app |
| [**sitesUpdateSiteConnectionStrings**](SitesApi.md#sitesUpdateSiteConnectionStrings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings | Updates the connection strings associated with web app |
| [**sitesUpdateSiteConnectionStringsSlot**](SitesApi.md#sitesUpdateSiteConnectionStringsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings | Updates the connection strings associated with web app |
| [**sitesUpdateSiteLogsConfig**](SitesApi.md#sitesUpdateSiteLogsConfig) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/logs | Updates the meta data for web app |
| [**sitesUpdateSiteLogsConfigSlot**](SitesApi.md#sitesUpdateSiteLogsConfigSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs | Updates the meta data for web app |
| [**sitesUpdateSiteMetadata**](SitesApi.md#sitesUpdateSiteMetadata) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata | Updates the meta data for web app |
| [**sitesUpdateSiteMetadataSlot**](SitesApi.md#sitesUpdateSiteMetadataSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata | Updates the meta data for web app |
| [**sitesUpdateSiteRelayServiceConnection**](SitesApi.md#sitesUpdateSiteRelayServiceConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one. |
| [**sitesUpdateSiteRelayServiceConnectionSlot**](SitesApi.md#sitesUpdateSiteRelayServiceConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Creates a new association to a BizTalk Hybrid Connection, or updates an existing one. |
| [**sitesUpdateSiteSourceControl**](SitesApi.md#sitesUpdateSiteSourceControl) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Update the source control configuration of web app |
| [**sitesUpdateSiteSourceControlSlot**](SitesApi.md#sitesUpdateSiteSourceControlSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Update the source control configuration of web app |
| [**sitesUpdateSiteVNETConnection**](SitesApi.md#sitesUpdateSiteVNETConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties. |
| [**sitesUpdateSiteVNETConnectionGateway**](SitesApi.md#sitesUpdateSiteVNETConnectionGateway) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway. |
| [**sitesUpdateSiteVNETConnectionGatewaySlot**](SitesApi.md#sitesUpdateSiteVNETConnectionGatewaySlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the Virtual Network Gateway. |
| [**sitesUpdateSiteVNETConnectionSlot**](SitesApi.md#sitesUpdateSiteVNETConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network Connection or updates it&#39;s properties. |
| [**sitesUpdateSlotConfigNames**](SitesApi.md#sitesUpdateSlotConfigNames) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames | Updates the names of application settings and connection string that remain with the slot during swap operation |


<a id="sitesAddSitePremierAddOn"></a>
# **sitesAddSitePremierAddOn**
> Object sitesAddSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String premierAddOnName = "premierAddOnName_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    PremierAddOnRequest premierAddOn = new PremierAddOnRequest(); // PremierAddOnRequest | 
    try {
      Object result = apiInstance.sitesAddSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesAddSitePremierAddOn");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **premierAddOnName** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **premierAddOn** | [**PremierAddOnRequest**](PremierAddOnRequest.md)|  | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesAddSitePremierAddOnSlot"></a>
# **sitesAddSitePremierAddOnSlot**
> Object sitesAddSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String premierAddOnName = "premierAddOnName_example"; // String | 
    String slot = "slot_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    PremierAddOnRequest premierAddOn = new PremierAddOnRequest(); // PremierAddOnRequest | 
    try {
      Object result = apiInstance.sitesAddSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesAddSitePremierAddOnSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **premierAddOnName** | **String**|  | |
| **slot** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **premierAddOn** | [**PremierAddOnRequest**](PremierAddOnRequest.md)|  | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesApplySlotConfigSlot"></a>
# **sitesApplySlotConfigSlot**
> Object sitesApplySlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Applies the configuration settings from the target slot onto the current slot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of the source slot. Settings from the target slot will be applied onto this slot
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSlotEntity slotSwapEntity = new CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name. Settings from that slot will be applied on the source slot
    try {
      Object result = apiInstance.sitesApplySlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesApplySlotConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of the source slot. Settings from the target slot will be applied onto this slot | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name. Settings from that slot will be applied on the source slot | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesApplySlotConfigToProduction"></a>
# **sitesApplySlotConfigToProduction**
> Object sitesApplySlotConfigToProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Applies the configuration settings from the target slot onto the current slot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSlotEntity slotSwapEntity = new CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name. Settings from that slot will be applied on the source slot
    try {
      Object result = apiInstance.sitesApplySlotConfigToProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesApplySlotConfigToProduction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name. Settings from that slot will be applied on the source slot | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesBackupSite"></a>
# **sitesBackupSite**
> BackupItem sitesBackupSite(resourceGroupName, name, subscriptionId, apiVersion, request)

Creates web app backup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    BackupRequest request = new BackupRequest(); // BackupRequest | Information on backup request
    try {
      BackupItem result = apiInstance.sitesBackupSite(resourceGroupName, name, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesBackupSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesBackupSiteSlot"></a>
# **sitesBackupSiteSlot**
> BackupItem sitesBackupSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Creates web app backup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    BackupRequest request = new BackupRequest(); // BackupRequest | Information on backup request
    try {
      BackupItem result = apiInstance.sitesBackupSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesBackupSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateDeployment"></a>
# **sitesCreateDeployment**
> Deployment sitesCreateDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, deployment)

Create a deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Deployment deployment = new Deployment(); // Deployment | Details of deployment
    try {
      Deployment result = apiInstance.sitesCreateDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, deployment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **deployment** | [**Deployment**](Deployment.md)| Details of deployment | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateDeploymentSlot"></a>
# **sitesCreateDeploymentSlot**
> Deployment sitesCreateDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, deployment)

Create a deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Deployment deployment = new Deployment(); // Deployment | Details of deployment
    try {
      Deployment result = apiInstance.sitesCreateDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, deployment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateDeploymentSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **deployment** | [**Deployment**](Deployment.md)| Details of deployment | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateInstanceDeployment"></a>
# **sitesCreateInstanceDeployment**
> Deployment sitesCreateInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion, deployment)

Create a deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Deployment deployment = new Deployment(); // Deployment | Details of deployment
    try {
      Deployment result = apiInstance.sitesCreateInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion, deployment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateInstanceDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **deployment** | [**Deployment**](Deployment.md)| Details of deployment | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateInstanceDeploymentSlot"></a>
# **sitesCreateInstanceDeploymentSlot**
> Deployment sitesCreateInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion, deployment)

Create a deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Deployment deployment = new Deployment(); // Deployment | Details of deployment
    try {
      Deployment result = apiInstance.sitesCreateInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion, deployment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateInstanceDeploymentSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **deployment** | [**Deployment**](Deployment.md)| Details of deployment | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSite"></a>
# **sitesCreateOrUpdateSite**
> Site sitesCreateOrUpdateSite(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope, skipDnsRegistration, skipCustomDomainVerification, forceDnsRegistration, ttlInSeconds)

Creates a new web app or modifies an existing web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Site siteEnvelope = new Site(); // Site | Details of web app if it exists already
    String skipDnsRegistration = "skipDnsRegistration_example"; // String | If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation
    String skipCustomDomainVerification = "skipCustomDomainVerification_example"; // String | If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    String forceDnsRegistration = "forceDnsRegistration_example"; // String | If true, web app hostname is force registered with DNS
    String ttlInSeconds = "ttlInSeconds_example"; // String | Time to live in seconds for web app's default domain name
    try {
      Site result = apiInstance.sitesCreateOrUpdateSite(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope, skipDnsRegistration, skipCustomDomainVerification, forceDnsRegistration, ttlInSeconds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteEnvelope** | [**Site**](Site.md)| Details of web app if it exists already | |
| **skipDnsRegistration** | **String**| If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation | [optional] |
| **skipCustomDomainVerification** | **String**| If true, custom (non *.azurewebsites.net) domains associated with web app are not verified. | [optional] |
| **forceDnsRegistration** | **String**| If true, web app hostname is force registered with DNS | [optional] |
| **ttlInSeconds** | **String**| Time to live in seconds for web app&#39;s default domain name | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Asynchronous operation in progress |  -  |

<a id="sitesCreateOrUpdateSiteConfig"></a>
# **sitesCreateOrUpdateSiteConfig**
> SiteConfig sitesCreateOrUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteConfig siteConfig = new SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
    try {
      SiteConfig result = apiInstance.sitesCreateOrUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | |

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteConfigSlot"></a>
# **sitesCreateOrUpdateSiteConfigSlot**
> SiteConfig sitesCreateOrUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteConfig siteConfig = new SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
    try {
      SiteConfig result = apiInstance.sitesCreateOrUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | |

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteHostNameBinding"></a>
# **sitesCreateOrUpdateSiteHostNameBinding**
> HostNameBinding sitesCreateOrUpdateSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, hostNameBinding)

Creates a web app hostname binding

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String hostName = "hostName_example"; // String | Name of host
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    HostNameBinding hostNameBinding = new HostNameBinding(); // HostNameBinding | Host name binding information
    try {
      HostNameBinding result = apiInstance.sitesCreateOrUpdateSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, hostNameBinding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteHostNameBinding");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **hostName** | **String**| Name of host | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **hostNameBinding** | [**HostNameBinding**](HostNameBinding.md)| Host name binding information | |

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteHostNameBindingSlot"></a>
# **sitesCreateOrUpdateSiteHostNameBindingSlot**
> HostNameBinding sitesCreateOrUpdateSiteHostNameBindingSlot(resourceGroupName, name, hostName, slot, subscriptionId, apiVersion, hostNameBinding)

Creates a web app hostname binding

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String hostName = "hostName_example"; // String | Name of host
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    HostNameBinding hostNameBinding = new HostNameBinding(); // HostNameBinding | Host name binding information
    try {
      HostNameBinding result = apiInstance.sitesCreateOrUpdateSiteHostNameBindingSlot(resourceGroupName, name, hostName, slot, subscriptionId, apiVersion, hostNameBinding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteHostNameBindingSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **hostName** | **String**| Name of host | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **hostNameBinding** | [**HostNameBinding**](HostNameBinding.md)| Host name binding information | |

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteRelayServiceConnection"></a>
# **sitesCreateOrUpdateSiteRelayServiceConnection**
> RelayServiceConnectionEntity sitesCreateOrUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RelayServiceConnectionEntity connectionEnvelope = new RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesCreateOrUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteRelayServiceConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteRelayServiceConnectionSlot"></a>
# **sitesCreateOrUpdateSiteRelayServiceConnectionSlot**
> RelayServiceConnectionEntity sitesCreateOrUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String slot = "slot_example"; // String | The name of the slot for the web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RelayServiceConnectionEntity connectionEnvelope = new RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesCreateOrUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteRelayServiceConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **slot** | **String**| The name of the slot for the web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteSlot"></a>
# **sitesCreateOrUpdateSiteSlot**
> Site sitesCreateOrUpdateSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope, skipDnsRegistration, skipCustomDomainVerification, forceDnsRegistration, ttlInSeconds)

Creates a new web app or modifies an existing web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Site siteEnvelope = new Site(); // Site | Details of web app if it exists already
    String skipDnsRegistration = "skipDnsRegistration_example"; // String | If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation
    String skipCustomDomainVerification = "skipCustomDomainVerification_example"; // String | If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    String forceDnsRegistration = "forceDnsRegistration_example"; // String | If true, web app hostname is force registered with DNS
    String ttlInSeconds = "ttlInSeconds_example"; // String | Time to live in seconds for web app's default domain name
    try {
      Site result = apiInstance.sitesCreateOrUpdateSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope, skipDnsRegistration, skipCustomDomainVerification, forceDnsRegistration, ttlInSeconds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteEnvelope** | [**Site**](Site.md)| Details of web app if it exists already | |
| **skipDnsRegistration** | **String**| If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation | [optional] |
| **skipCustomDomainVerification** | **String**| If true, custom (non *.azurewebsites.net) domains associated with web app are not verified. | [optional] |
| **forceDnsRegistration** | **String**| If true, web app hostname is force registered with DNS | [optional] |
| **ttlInSeconds** | **String**| Time to live in seconds for web app&#39;s default domain name | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Asynchronous operation in progress |  -  |

<a id="sitesCreateOrUpdateSiteSourceControl"></a>
# **sitesCreateOrUpdateSiteSourceControl**
> SiteSourceControl sitesCreateOrUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteSourceControl siteSourceControl = new SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
    try {
      SiteSourceControl result = apiInstance.sitesCreateOrUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteSourceControl");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | |

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="sitesCreateOrUpdateSiteSourceControlSlot"></a>
# **sitesCreateOrUpdateSiteSourceControlSlot**
> SiteSourceControl sitesCreateOrUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteSourceControl siteSourceControl = new SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
    try {
      SiteSourceControl result = apiInstance.sitesCreateOrUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteSourceControlSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | |

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="sitesCreateOrUpdateSiteVNETConnection"></a>
# **sitesCreateOrUpdateSiteVNETConnection**
> VnetInfo sitesCreateOrUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetInfo connectionEnvelope = new VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
    try {
      VnetInfo result = apiInstance.sitesCreateOrUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteVNETConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteVNETConnectionGateway"></a>
# **sitesCreateOrUpdateSiteVNETConnectionGateway**
> VnetGateway sitesCreateOrUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetGateway connectionEnvelope = new VnetGateway(); // VnetGateway | The properties to update this gateway with.
    try {
      VnetGateway result = apiInstance.sitesCreateOrUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteVNETConnectionGateway");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | |

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteVNETConnectionGatewaySlot"></a>
# **sitesCreateOrUpdateSiteVNETConnectionGatewaySlot**
> VnetGateway sitesCreateOrUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetGateway connectionEnvelope = new VnetGateway(); // VnetGateway | The properties to update this gateway with.
    try {
      VnetGateway result = apiInstance.sitesCreateOrUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteVNETConnectionGatewaySlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | |

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesCreateOrUpdateSiteVNETConnectionSlot"></a>
# **sitesCreateOrUpdateSiteVNETConnectionSlot**
> VnetInfo sitesCreateOrUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetInfo connectionEnvelope = new VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
    try {
      VnetInfo result = apiInstance.sitesCreateOrUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesCreateOrUpdateSiteVNETConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteBackup"></a>
# **sitesDeleteBackup**
> BackupItem sitesDeleteBackup(resourceGroupName, name, backupId, subscriptionId, apiVersion)

Deletes a backup from Azure Storage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupItem result = apiInstance.sitesDeleteBackup(resourceGroupName, name, backupId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteBackupSlot"></a>
# **sitesDeleteBackupSlot**
> BackupItem sitesDeleteBackupSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion)

Deletes a backup from Azure Storage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupItem result = apiInstance.sitesDeleteBackupSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteBackupSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteDeployment"></a>
# **sitesDeleteDeployment**
> Object sitesDeleteDeployment(resourceGroupName, name, id, subscriptionId, apiVersion)

Delete the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteDeployment(resourceGroupName, name, id, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteDeploymentSlot"></a>
# **sitesDeleteDeploymentSlot**
> Object sitesDeleteDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

Delete the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteDeploymentSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteInstanceDeployment"></a>
# **sitesDeleteInstanceDeployment**
> Object sitesDeleteInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion)

Delete the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteInstanceDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteInstanceDeploymentSlot"></a>
# **sitesDeleteInstanceDeploymentSlot**
> Object sitesDeleteInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion)

Delete the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteInstanceDeploymentSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSite"></a>
# **sitesDeleteSite**
> Object sitesDeleteSite(resourceGroupName, name, subscriptionId, apiVersion, deleteMetrics, deleteEmptyServerFarm, skipDnsRegistration, deleteAllSlots)

Deletes a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String deleteMetrics = "deleteMetrics_example"; // String | If true, web app metrics are also deleted
    String deleteEmptyServerFarm = "deleteEmptyServerFarm_example"; // String | If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted
    String skipDnsRegistration = "skipDnsRegistration_example"; // String | If true, DNS registration is skipped
    String deleteAllSlots = "deleteAllSlots_example"; // String | If true, all slots associated with web app are also deleted
    try {
      Object result = apiInstance.sitesDeleteSite(resourceGroupName, name, subscriptionId, apiVersion, deleteMetrics, deleteEmptyServerFarm, skipDnsRegistration, deleteAllSlots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **deleteMetrics** | **String**| If true, web app metrics are also deleted | [optional] |
| **deleteEmptyServerFarm** | **String**| If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted | [optional] |
| **skipDnsRegistration** | **String**| If true, DNS registration is skipped | [optional] |
| **deleteAllSlots** | **String**| If true, all slots associated with web app are also deleted | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteHostNameBinding"></a>
# **sitesDeleteSiteHostNameBinding**
> Object sitesDeleteSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion)

Deletes a host name binding

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String hostName = "hostName_example"; // String | Name of host
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteHostNameBinding");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **hostName** | **String**| Name of host | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteHostNameBindingSlot"></a>
# **sitesDeleteSiteHostNameBindingSlot**
> Object sitesDeleteSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion)

Deletes a host name binding

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String hostName = "hostName_example"; // String | Name of host
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteHostNameBindingSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **hostName** | **String**| Name of host | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSitePremierAddOn"></a>
# **sitesDeleteSitePremierAddOn**
> Object sitesDeleteSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String premierAddOnName = "premierAddOnName_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSitePremierAddOn");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **premierAddOnName** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSitePremierAddOnSlot"></a>
# **sitesDeleteSitePremierAddOnSlot**
> Object sitesDeleteSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String premierAddOnName = "premierAddOnName_example"; // String | 
    String slot = "slot_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSitePremierAddOnSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **premierAddOnName** | **String**|  | |
| **slot** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteRelayServiceConnection"></a>
# **sitesDeleteSiteRelayServiceConnection**
> Object sitesDeleteSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion)

Removes the association to a BizTalk Hybrid Connection, identified by its entity name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteRelayServiceConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteRelayServiceConnectionSlot"></a>
# **sitesDeleteSiteRelayServiceConnectionSlot**
> Object sitesDeleteSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion)

Removes the association to a BizTalk Hybrid Connection, identified by its entity name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String slot = "slot_example"; // String | The name of the slot for the web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteRelayServiceConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **slot** | **String**| The name of the slot for the web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteSlot"></a>
# **sitesDeleteSiteSlot**
> Object sitesDeleteSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, deleteMetrics, deleteEmptyServerFarm, skipDnsRegistration, deleteAllSlots)

Deletes a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String deleteMetrics = "deleteMetrics_example"; // String | If true, web app metrics are also deleted
    String deleteEmptyServerFarm = "deleteEmptyServerFarm_example"; // String | If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted
    String skipDnsRegistration = "skipDnsRegistration_example"; // String | If true, DNS registration is skipped
    String deleteAllSlots = "deleteAllSlots_example"; // String | If true, all slots associated with web app are also deleted
    try {
      Object result = apiInstance.sitesDeleteSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, deleteMetrics, deleteEmptyServerFarm, skipDnsRegistration, deleteAllSlots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **deleteMetrics** | **String**| If true, web app metrics are also deleted | [optional] |
| **deleteEmptyServerFarm** | **String**| If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted | [optional] |
| **skipDnsRegistration** | **String**| If true, DNS registration is skipped | [optional] |
| **deleteAllSlots** | **String**| If true, all slots associated with web app are also deleted | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteSourceControl"></a>
# **sitesDeleteSiteSourceControl**
> Object sitesDeleteSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion)

Delete source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteSourceControl");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteSourceControlSlot"></a>
# **sitesDeleteSiteSourceControlSlot**
> Object sitesDeleteSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Delete source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteSourceControlSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteVNETConnection"></a>
# **sitesDeleteSiteVNETConnection**
> Object sitesDeleteSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Removes the specified Virtual Network Connection association from this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteVNETConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDeleteSiteVNETConnectionSlot"></a>
# **sitesDeleteSiteVNETConnectionSlot**
> Object sitesDeleteSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion)

Removes the specified Virtual Network Connection association from this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesDeleteSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDeleteSiteVNETConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDiscoverSiteRestore"></a>
# **sitesDiscoverSiteRestore**
> RestoreRequest sitesDiscoverSiteRestore(resourceGroupName, name, subscriptionId, apiVersion, request)

Discovers existing web app backups that can be restored

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RestoreRequest request = new RestoreRequest(); // RestoreRequest | Information on restore request
    try {
      RestoreRequest result = apiInstance.sitesDiscoverSiteRestore(resourceGroupName, name, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDiscoverSiteRestore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | |

### Return type

[**RestoreRequest**](RestoreRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesDiscoverSiteRestoreSlot"></a>
# **sitesDiscoverSiteRestoreSlot**
> RestoreRequest sitesDiscoverSiteRestoreSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Discovers existing web app backups that can be restored

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RestoreRequest request = new RestoreRequest(); // RestoreRequest | Information on restore request
    try {
      RestoreRequest result = apiInstance.sitesDiscoverSiteRestoreSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesDiscoverSiteRestoreSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | |

### Return type

[**RestoreRequest**](RestoreRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGenerateNewSitePublishingPassword"></a>
# **sitesGenerateNewSitePublishingPassword**
> Object sitesGenerateNewSitePublishingPassword(resourceGroupName, name, subscriptionId, apiVersion)

Generates new random app publishing password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGenerateNewSitePublishingPassword(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGenerateNewSitePublishingPassword");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGenerateNewSitePublishingPasswordSlot"></a>
# **sitesGenerateNewSitePublishingPasswordSlot**
> Object sitesGenerateNewSitePublishingPasswordSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Generates new random app publishing password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGenerateNewSitePublishingPasswordSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGenerateNewSitePublishingPasswordSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetDeletedSites"></a>
# **sitesGetDeletedSites**
> DeletedSiteCollection sitesGetDeletedSites(resourceGroupName, subscriptionId, apiVersion, propertiesToInclude, includeSiteTypes)

Gets deleted web apps in subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Additional web app properties included in the response
    String includeSiteTypes = "includeSiteTypes_example"; // String | Types of apps included in the response
    try {
      DeletedSiteCollection result = apiInstance.sitesGetDeletedSites(resourceGroupName, subscriptionId, apiVersion, propertiesToInclude, includeSiteTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetDeletedSites");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] |
| **includeSiteTypes** | **String**| Types of apps included in the response | [optional] |

### Return type

[**DeletedSiteCollection**](DeletedSiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetDeployment"></a>
# **sitesGetDeployment**
> Deployment sitesGetDeployment(resourceGroupName, name, id, subscriptionId, apiVersion)

Get the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Deployment result = apiInstance.sitesGetDeployment(resourceGroupName, name, id, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetDeploymentSlot"></a>
# **sitesGetDeploymentSlot**
> Deployment sitesGetDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

Get the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Deployment result = apiInstance.sitesGetDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetDeploymentSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetDeployments"></a>
# **sitesGetDeployments**
> DeploymentCollection sitesGetDeployments(resourceGroupName, name, subscriptionId, apiVersion)

List deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeploymentCollection result = apiInstance.sitesGetDeployments(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetDeployments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetDeploymentsSlot"></a>
# **sitesGetDeploymentsSlot**
> DeploymentCollection sitesGetDeploymentsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeploymentCollection result = apiInstance.sitesGetDeploymentsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetDeploymentsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetInstanceDeployment"></a>
# **sitesGetInstanceDeployment**
> Deployment sitesGetInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion)

Get the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Deployment result = apiInstance.sitesGetInstanceDeployment(resourceGroupName, name, id, instanceId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetInstanceDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetInstanceDeploymentSlot"></a>
# **sitesGetInstanceDeploymentSlot**
> Deployment sitesGetInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion)

Get the deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String id = "id_example"; // String | Id of the deployment
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Deployment result = apiInstance.sitesGetInstanceDeploymentSlot(resourceGroupName, name, id, slot, instanceId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetInstanceDeploymentSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **id** | **String**| Id of the deployment | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetInstanceDeployments"></a>
# **sitesGetInstanceDeployments**
> DeploymentCollection sitesGetInstanceDeployments(resourceGroupName, name, instanceId, subscriptionId, apiVersion)

List deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeploymentCollection result = apiInstance.sitesGetInstanceDeployments(resourceGroupName, name, instanceId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetInstanceDeployments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetInstanceDeploymentsSlot"></a>
# **sitesGetInstanceDeploymentsSlot**
> DeploymentCollection sitesGetInstanceDeploymentsSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion)

List deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String instanceId = "instanceId_example"; // String | Id of web app instance
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeploymentCollection result = apiInstance.sitesGetInstanceDeploymentsSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetInstanceDeploymentsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **instanceId** | **String**| Id of web app instance | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSite"></a>
# **sitesGetSite**
> Site sitesGetSite(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude)

Get details of a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Additional web app properties included in the response
    try {
      Site result = apiInstance.sitesGetSite(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteBackupConfiguration"></a>
# **sitesGetSiteBackupConfiguration**
> BackupRequest sitesGetSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion)

Gets the backup configuration for a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupRequest result = apiInstance.sitesGetSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteBackupConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteBackupConfigurationSlot"></a>
# **sitesGetSiteBackupConfigurationSlot**
> BackupRequest sitesGetSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the backup configuration for a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupRequest result = apiInstance.sitesGetSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteBackupConfigurationSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteBackupStatus"></a>
# **sitesGetSiteBackupStatus**
> BackupItem sitesGetSiteBackupStatus(resourceGroupName, name, backupId, subscriptionId, apiVersion)

Gets status of a web app backup that may be in progress.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupItem result = apiInstance.sitesGetSiteBackupStatus(resourceGroupName, name, backupId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteBackupStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteBackupStatusSecrets"></a>
# **sitesGetSiteBackupStatusSecrets**
> BackupItem sitesGetSiteBackupStatusSecrets(resourceGroupName, name, backupId, subscriptionId, apiVersion, request)

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    BackupRequest request = new BackupRequest(); // BackupRequest | Information on backup request
    try {
      BackupItem result = apiInstance.sitesGetSiteBackupStatusSecrets(resourceGroupName, name, backupId, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteBackupStatusSecrets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteBackupStatusSecretsSlot"></a>
# **sitesGetSiteBackupStatusSecretsSlot**
> BackupItem sitesGetSiteBackupStatusSecretsSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request)

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    BackupRequest request = new BackupRequest(); // BackupRequest | Information on backup request
    try {
      BackupItem result = apiInstance.sitesGetSiteBackupStatusSecretsSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteBackupStatusSecretsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteBackupStatusSlot"></a>
# **sitesGetSiteBackupStatusSlot**
> BackupItem sitesGetSiteBackupStatusSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion)

Gets status of a web app backup that may be in progress.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupItem result = apiInstance.sitesGetSiteBackupStatusSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteBackupStatusSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteConfig"></a>
# **sitesGetSiteConfig**
> SiteConfig sitesGetSiteConfig(resourceGroupName, name, subscriptionId, apiVersion)

Gets the configuration of the web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteConfig result = apiInstance.sitesGetSiteConfig(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteConfigSlot"></a>
# **sitesGetSiteConfigSlot**
> SiteConfig sitesGetSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the configuration of the web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteConfig result = apiInstance.sitesGetSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteHostNameBinding"></a>
# **sitesGetSiteHostNameBinding**
> HostNameBinding sitesGetSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion)

Get web app binding for a hostname

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String hostName = "hostName_example"; // String | Name of host
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostNameBinding result = apiInstance.sitesGetSiteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteHostNameBinding");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **hostName** | **String**| Name of host | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteHostNameBindingSlot"></a>
# **sitesGetSiteHostNameBindingSlot**
> HostNameBinding sitesGetSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion)

Get web app binding for a hostname

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String hostName = "hostName_example"; // String | Name of host
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostNameBinding result = apiInstance.sitesGetSiteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteHostNameBindingSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **hostName** | **String**| Name of host | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteHostNameBindings"></a>
# **sitesGetSiteHostNameBindings**
> HostNameBindingCollection sitesGetSiteHostNameBindings(resourceGroupName, name, subscriptionId, apiVersion)

Get web app hostname bindings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostNameBindingCollection result = apiInstance.sitesGetSiteHostNameBindings(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteHostNameBindings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostNameBindingCollection**](HostNameBindingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteHostNameBindingsSlot"></a>
# **sitesGetSiteHostNameBindingsSlot**
> HostNameBindingCollection sitesGetSiteHostNameBindingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get web app hostname bindings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostNameBindingCollection result = apiInstance.sitesGetSiteHostNameBindingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteHostNameBindingsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostNameBindingCollection**](HostNameBindingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteInstanceIdentifiers"></a>
# **sitesGetSiteInstanceIdentifiers**
> SiteInstanceCollection sitesGetSiteInstanceIdentifiers(resourceGroupName, name, subscriptionId, apiVersion)

Gets all instance of a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteInstanceCollection result = apiInstance.sitesGetSiteInstanceIdentifiers(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteInstanceIdentifiers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteInstanceCollection**](SiteInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteInstanceIdentifiersSlot"></a>
# **sitesGetSiteInstanceIdentifiersSlot**
> SiteInstanceCollection sitesGetSiteInstanceIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets all instance of a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteInstanceCollection result = apiInstance.sitesGetSiteInstanceIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteInstanceIdentifiersSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteInstanceCollection**](SiteInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteLogsConfig"></a>
# **sitesGetSiteLogsConfig**
> SiteLogsConfig sitesGetSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion)

Gets the web app logs configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteLogsConfig result = apiInstance.sitesGetSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteLogsConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteLogsConfigSlot"></a>
# **sitesGetSiteLogsConfigSlot**
> SiteLogsConfig sitesGetSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the web app logs configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteLogsConfig result = apiInstance.sitesGetSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteLogsConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteMetricDefinitions"></a>
# **sitesGetSiteMetricDefinitions**
> MetricDefinitionCollection sitesGetSiteMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Gets metric definitions for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinitionCollection result = apiInstance.sitesGetSiteMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteMetricDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteMetricDefinitionsSlot"></a>
# **sitesGetSiteMetricDefinitionsSlot**
> MetricDefinitionCollection sitesGetSiteMetricDefinitionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets metric definitions for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinitionCollection result = apiInstance.sitesGetSiteMetricDefinitionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteMetricDefinitionsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteMetrics"></a>
# **sitesGetSiteMetrics**
> ResourceMetricCollection sitesGetSiteMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter)

Gets metrics for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | If true, metric details are included in response
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      ResourceMetricCollection result = apiInstance.sitesGetSiteMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| If true, metric details are included in response | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteMetricsSlot"></a>
# **sitesGetSiteMetricsSlot**
> ResourceMetricCollection sitesGetSiteMetricsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, details, $filter)

Gets metrics for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | If true, metric details are included in response
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      ResourceMetricCollection result = apiInstance.sitesGetSiteMetricsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteMetricsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| If true, metric details are included in response | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteNetworkFeatures"></a>
# **sitesGetSiteNetworkFeatures**
> NetworkFeatures sitesGetSiteNetworkFeatures(resourceGroupName, name, view, subscriptionId, apiVersion)

Retrieves a view of all network features in use on this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String view = "view_example"; // String | The type of view. This can either be \"summary\" or \"detailed\".
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      NetworkFeatures result = apiInstance.sitesGetSiteNetworkFeatures(resourceGroupName, name, view, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteNetworkFeatures");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **view** | **String**| The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**NetworkFeatures**](NetworkFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | The requested view does not exist. |  -  |

<a id="sitesGetSiteNetworkFeaturesSlot"></a>
# **sitesGetSiteNetworkFeaturesSlot**
> NetworkFeatures sitesGetSiteNetworkFeaturesSlot(resourceGroupName, name, view, slot, subscriptionId, apiVersion)

Retrieves a view of all network features in use on this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String view = "view_example"; // String | The type of view. This can either be \"summary\" or \"detailed\".
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      NetworkFeatures result = apiInstance.sitesGetSiteNetworkFeaturesSlot(resourceGroupName, name, view, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteNetworkFeaturesSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **view** | **String**| The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;. | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**NetworkFeatures**](NetworkFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | The requested view does not exist. |  -  |

<a id="sitesGetSiteOperation"></a>
# **sitesGetSiteOperation**
> Object sitesGetSiteOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets the operation for a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String operationId = "operationId_example"; // String | Id of an operation
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSiteOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteOperation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **operationId** | **String**| Id of an operation | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteOperationSlot"></a>
# **sitesGetSiteOperationSlot**
> Object sitesGetSiteOperationSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion)

Gets the operation for a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String operationId = "operationId_example"; // String | Id of an operation
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSiteOperationSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteOperationSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **operationId** | **String**| Id of an operation | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSitePremierAddOn"></a>
# **sitesGetSitePremierAddOn**
> Object sitesGetSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String premierAddOnName = "premierAddOnName_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSitePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSitePremierAddOn");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **premierAddOnName** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSitePremierAddOnSlot"></a>
# **sitesGetSitePremierAddOnSlot**
> Object sitesGetSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String premierAddOnName = "premierAddOnName_example"; // String | 
    String slot = "slot_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSitePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSitePremierAddOnSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **premierAddOnName** | **String**|  | |
| **slot** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteRelayServiceConnection"></a>
# **sitesGetSiteRelayServiceConnection**
> RelayServiceConnectionEntity sitesGetSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion)

Retrieves a BizTalk Hybrid Connection identified by its entity name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesGetSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteRelayServiceConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteRelayServiceConnectionSlot"></a>
# **sitesGetSiteRelayServiceConnectionSlot**
> RelayServiceConnectionEntity sitesGetSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion)

Retrieves a BizTalk Hybrid Connection identified by its entity name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String slot = "slot_example"; // String | The name of the slot for the web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesGetSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteRelayServiceConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **slot** | **String**| The name of the slot for the web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteSlot"></a>
# **sitesGetSiteSlot**
> Site sitesGetSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, propertiesToInclude)

Get details of a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Additional web app properties included in the response
    try {
      Site result = apiInstance.sitesGetSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, propertiesToInclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteSlots"></a>
# **sitesGetSiteSlots**
> SiteCollection sitesGetSiteSlots(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude)

Gets all the slots for a web apps

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | List of app properties to include in the response
    try {
      SiteCollection result = apiInstance.sitesGetSiteSlots(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteSlots");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| List of app properties to include in the response | [optional] |

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteSnapshots"></a>
# **sitesGetSiteSnapshots**
> Object sitesGetSiteSnapshots(resourceGroupName, name, subscriptionId, apiVersion)

Returns all Snapshots to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Webspace
    String name = "name_example"; // String | Website Name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSiteSnapshots(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteSnapshots");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Webspace | |
| **name** | **String**| Website Name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteSnapshotsSlot"></a>
# **sitesGetSiteSnapshotsSlot**
> Object sitesGetSiteSnapshotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Returns all Snapshots to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Webspace
    String name = "name_example"; // String | Website Name
    String slot = "slot_example"; // String | Website Slot
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSiteSnapshotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteSnapshotsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Webspace | |
| **name** | **String**| Website Name | |
| **slot** | **String**| Website Slot | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteSourceControl"></a>
# **sitesGetSiteSourceControl**
> SiteSourceControl sitesGetSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion)

Get the source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteSourceControl result = apiInstance.sitesGetSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteSourceControl");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteSourceControlSlot"></a>
# **sitesGetSiteSourceControlSlot**
> SiteSourceControl sitesGetSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get the source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteSourceControl result = apiInstance.sitesGetSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteSourceControlSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteUsages"></a>
# **sitesGetSiteUsages**
> CsmUsageQuotaCollection sitesGetSiteUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter)

Gets the quota usage numbers for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String $filter = "$filter_example"; // String | Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      CsmUsageQuotaCollection result = apiInstance.sitesGetSiteUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteUsages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **$filter** | **String**| Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**CsmUsageQuotaCollection**](CsmUsageQuotaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteUsagesSlot"></a>
# **sitesGetSiteUsagesSlot**
> CsmUsageQuotaCollection sitesGetSiteUsagesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, $filter)

Gets the quota usage numbers for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String $filter = "$filter_example"; // String | Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      CsmUsageQuotaCollection result = apiInstance.sitesGetSiteUsagesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteUsagesSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **$filter** | **String**| Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**CsmUsageQuotaCollection**](CsmUsageQuotaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteVNETConnection"></a>
# **sitesGetSiteVNETConnection**
> VnetInfo sitesGetSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Retrieves a specific Virtual Network Connection associated with this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      VnetInfo result = apiInstance.sitesGetSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteVNETConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteVNETConnectionSlot"></a>
# **sitesGetSiteVNETConnectionSlot**
> VnetInfo sitesGetSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion)

Retrieves a specific Virtual Network Connection associated with this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      VnetInfo result = apiInstance.sitesGetSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteVNETConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteVNETConnections"></a>
# **sitesGetSiteVNETConnections**
> List&lt;VnetInfo&gt; sitesGetSiteVNETConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieves a list of all Virtual Network Connections associated with this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<VnetInfo> result = apiInstance.sitesGetSiteVNETConnections(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteVNETConnections");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;VnetInfo&gt;**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteVNETConnectionsSlot"></a>
# **sitesGetSiteVNETConnectionsSlot**
> List&lt;VnetInfo&gt; sitesGetSiteVNETConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Retrieves a list of all Virtual Network Connections associated with this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<VnetInfo> result = apiInstance.sitesGetSiteVNETConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteVNETConnectionsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;VnetInfo&gt;**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSiteVnetGateway"></a>
# **sitesGetSiteVnetGateway**
> Object sitesGetSiteVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Retrieves a Virtual Network connection gateway associated with this web app and virtual network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSiteVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteVnetGateway");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Gateway does not exist. Only the \&quot;primary\&quot; gateway exists presently. |  -  |

<a id="sitesGetSiteVnetGatewaySlot"></a>
# **sitesGetSiteVnetGatewaySlot**
> Object sitesGetSiteVnetGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion)

Retrieves a Virtual Network connection gateway associated with this web app and virtual network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesGetSiteVnetGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSiteVnetGatewaySlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Gateway does not exist. Only the \&quot;primary\&quot; gateway exists presently. |  -  |

<a id="sitesGetSites"></a>
# **sitesGetSites**
> SiteCollection sitesGetSites(resourceGroupName, subscriptionId, apiVersion, propertiesToInclude, includeSiteTypes, includeSlots)

Gets the web apps for a subscription in the specified resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Additional web app properties included in the response
    String includeSiteTypes = "includeSiteTypes_example"; // String | Types of apps included in the response
    Boolean includeSlots = true; // Boolean | Whether or not to include deployments slots in results
    try {
      SiteCollection result = apiInstance.sitesGetSites(resourceGroupName, subscriptionId, apiVersion, propertiesToInclude, includeSiteTypes, includeSlots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSites");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Additional web app properties included in the response | [optional] |
| **includeSiteTypes** | **String**| Types of apps included in the response | [optional] |
| **includeSlots** | **Boolean**| Whether or not to include deployments slots in results | [optional] |

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSlotConfigNames"></a>
# **sitesGetSlotConfigNames**
> SlotConfigNamesResource sitesGetSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion)

Gets the names of application settings and connection string that remain with the slot during swap operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SlotConfigNamesResource result = apiInstance.sitesGetSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSlotConfigNames");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SlotConfigNamesResource**](SlotConfigNamesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSlotsDifferencesFromProduction"></a>
# **sitesGetSlotsDifferencesFromProduction**
> SlotDifferenceCollection sitesGetSlotsDifferencesFromProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Get the difference in configuration settings between two web app slots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSlotEntity slotSwapEntity = new CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
    try {
      SlotDifferenceCollection result = apiInstance.sitesGetSlotsDifferencesFromProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSlotsDifferencesFromProduction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | |

### Return type

[**SlotDifferenceCollection**](SlotDifferenceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesGetSlotsDifferencesSlot"></a>
# **sitesGetSlotsDifferencesSlot**
> SlotDifferenceCollection sitesGetSlotsDifferencesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Get the difference in configuration settings between two web app slots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of the source slot
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSlotEntity slotSwapEntity = new CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
    try {
      SlotDifferenceCollection result = apiInstance.sitesGetSlotsDifferencesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesGetSlotsDifferencesSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of the source slot | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | |

### Return type

[**SlotDifferenceCollection**](SlotDifferenceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesIsSiteCloneable"></a>
# **sitesIsSiteCloneable**
> SiteCloneability sitesIsSiteCloneable(resourceGroupName, name, subscriptionId, apiVersion)

Creates a new web app or modifies an existing web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteCloneability result = apiInstance.sitesIsSiteCloneable(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIsSiteCloneable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteCloneability**](SiteCloneability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesIsSiteCloneableSlot"></a>
# **sitesIsSiteCloneableSlot**
> SiteCloneability sitesIsSiteCloneableSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Creates a new web app or modifies an existing web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteCloneability result = apiInstance.sitesIsSiteCloneableSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIsSiteCloneableSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteCloneability**](SiteCloneability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteAppSettings"></a>
# **sitesListSiteAppSettings**
> StringDictionary sitesListSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the application settings of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      StringDictionary result = apiInstance.sitesListSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteAppSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteAppSettingsSlot"></a>
# **sitesListSiteAppSettingsSlot**
> StringDictionary sitesListSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the application settings of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      StringDictionary result = apiInstance.sitesListSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteAppSettingsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteAuthSettings"></a>
# **sitesListSiteAuthSettings**
> SiteAuthSettings sitesListSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the Authentication / Authorization settings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteAuthSettings result = apiInstance.sitesListSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteAuthSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteAuthSettingsSlot"></a>
# **sitesListSiteAuthSettingsSlot**
> SiteAuthSettings sitesListSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the Authentication / Authorization settings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteAuthSettings result = apiInstance.sitesListSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteAuthSettingsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteBackups"></a>
# **sitesListSiteBackups**
> BackupItemCollection sitesListSiteBackups(resourceGroupName, name, subscriptionId, apiVersion)

Lists all available backups for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupItemCollection result = apiInstance.sitesListSiteBackups(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteBackups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupItemCollection**](BackupItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteBackupsSlot"></a>
# **sitesListSiteBackupsSlot**
> BackupItemCollection sitesListSiteBackupsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Lists all available backups for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      BackupItemCollection result = apiInstance.sitesListSiteBackupsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteBackupsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**BackupItemCollection**](BackupItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteConnectionStrings"></a>
# **sitesListSiteConnectionStrings**
> ConnectionStringDictionary sitesListSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the connection strings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionStringDictionary result = apiInstance.sitesListSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteConnectionStrings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteConnectionStringsSlot"></a>
# **sitesListSiteConnectionStringsSlot**
> ConnectionStringDictionary sitesListSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the connection strings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionStringDictionary result = apiInstance.sitesListSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteConnectionStringsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteMetadata"></a>
# **sitesListSiteMetadata**
> StringDictionary sitesListSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion)

Gets the web app meta data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      StringDictionary result = apiInstance.sitesListSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteMetadata");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteMetadataSlot"></a>
# **sitesListSiteMetadataSlot**
> StringDictionary sitesListSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the web app meta data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      StringDictionary result = apiInstance.sitesListSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteMetadataSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSitePremierAddOns"></a>
# **sitesListSitePremierAddOns**
> Object sitesListSitePremierAddOns(resourceGroupName, name, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesListSitePremierAddOns(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSitePremierAddOns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSitePremierAddOnsSlot"></a>
# **sitesListSitePremierAddOnsSlot**
> Object sitesListSitePremierAddOnsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String slot = "slot_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesListSitePremierAddOnsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSitePremierAddOnsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **slot** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSitePublishingCredentials"></a>
# **sitesListSitePublishingCredentials**
> User sitesListSitePublishingCredentials(resourceGroupName, name, subscriptionId, apiVersion)

Gets the web app publishing credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      User result = apiInstance.sitesListSitePublishingCredentials(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSitePublishingCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSitePublishingCredentialsSlot"></a>
# **sitesListSitePublishingCredentialsSlot**
> User sitesListSitePublishingCredentialsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the web app publishing credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      User result = apiInstance.sitesListSitePublishingCredentialsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSitePublishingCredentialsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSitePublishingProfileXml"></a>
# **sitesListSitePublishingProfileXml**
> File sitesListSitePublishingProfileXml(resourceGroupName, name, subscriptionId, apiVersion, options)

Gets the publishing profile for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmPublishingProfileOptions options = new CsmPublishingProfileOptions(); // CsmPublishingProfileOptions | Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format=FileZilla3 for FileZilla FTP format.
    try {
      File result = apiInstance.sitesListSitePublishingProfileXml(resourceGroupName, name, subscriptionId, apiVersion, options);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSitePublishingProfileXml");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **options** | [**CsmPublishingProfileOptions**](CsmPublishingProfileOptions.md)| Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format&#x3D;FileZilla3 for FileZilla FTP format. | |

### Return type

[**File**](File.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSitePublishingProfileXmlSlot"></a>
# **sitesListSitePublishingProfileXmlSlot**
> File sitesListSitePublishingProfileXmlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, options)

Gets the publishing profile for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmPublishingProfileOptions options = new CsmPublishingProfileOptions(); // CsmPublishingProfileOptions | Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format=FileZilla3 for FileZilla FTP format.
    try {
      File result = apiInstance.sitesListSitePublishingProfileXmlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, options);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSitePublishingProfileXmlSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **options** | [**CsmPublishingProfileOptions**](CsmPublishingProfileOptions.md)| Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format&#x3D;FileZilla3 for FileZilla FTP format. | |

### Return type

[**File**](File.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteRelayServiceConnections"></a>
# **sitesListSiteRelayServiceConnections**
> RelayServiceConnectionEntity sitesListSiteRelayServiceConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieves all BizTalk Hybrid Connections associated with this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesListSiteRelayServiceConnections(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteRelayServiceConnections");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesListSiteRelayServiceConnectionsSlot"></a>
# **sitesListSiteRelayServiceConnectionsSlot**
> RelayServiceConnectionEntity sitesListSiteRelayServiceConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Retrieves all BizTalk Hybrid Connections associated with this web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String slot = "slot_example"; // String | The name of the slot for the web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesListSiteRelayServiceConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesListSiteRelayServiceConnectionsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **slot** | **String**| The name of the slot for the web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesRecoverSite"></a>
# **sitesRecoverSite**
> Site sitesRecoverSite(resourceGroupName, name, subscriptionId, apiVersion, recoveryEntity)

Recovers a deleted web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSiteRecoveryEntity recoveryEntity = new CsmSiteRecoveryEntity(); // CsmSiteRecoveryEntity | Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
    try {
      Site result = apiInstance.sitesRecoverSite(resourceGroupName, name, subscriptionId, apiVersion, recoveryEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesRecoverSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **recoveryEntity** | [**CsmSiteRecoveryEntity**](CsmSiteRecoveryEntity.md)| Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API. | |

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Asynchronous operation in progress |  -  |
| **404** | Web app not found |  -  |

<a id="sitesRecoverSiteSlot"></a>
# **sitesRecoverSiteSlot**
> Site sitesRecoverSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, recoveryEntity)

Recovers a deleted web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSiteRecoveryEntity recoveryEntity = new CsmSiteRecoveryEntity(); // CsmSiteRecoveryEntity | Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
    try {
      Site result = apiInstance.sitesRecoverSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, recoveryEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesRecoverSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **recoveryEntity** | [**CsmSiteRecoveryEntity**](CsmSiteRecoveryEntity.md)| Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API. | |

### Return type

[**Site**](Site.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Asynchronous operation in progress |  -  |
| **404** | Web app not found |  -  |

<a id="sitesResetProductionSlotConfig"></a>
# **sitesResetProductionSlotConfig**
> Object sitesResetProductionSlotConfig(resourceGroupName, name, subscriptionId, apiVersion)

Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesResetProductionSlotConfig(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesResetProductionSlotConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesResetSlotConfigSlot"></a>
# **sitesResetSlotConfigSlot**
> Object sitesResetSlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesResetSlotConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesResetSlotConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesRestartSite"></a>
# **sitesRestartSite**
> Object sitesRestartSite(resourceGroupName, name, subscriptionId, apiVersion, softRestart, synchronous)

Restarts web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean softRestart = true; // Boolean | Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app
    Boolean synchronous = true; // Boolean | If true then the API will block until the app has been restarted
    try {
      Object result = apiInstance.sitesRestartSite(resourceGroupName, name, subscriptionId, apiVersion, softRestart, synchronous);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesRestartSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **softRestart** | **Boolean**| Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app | [optional] |
| **synchronous** | **Boolean**| If true then the API will block until the app has been restarted | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesRestartSiteSlot"></a>
# **sitesRestartSiteSlot**
> Object sitesRestartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, softRestart, synchronous)

Restarts web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean softRestart = true; // Boolean | Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app
    Boolean synchronous = true; // Boolean | If true then the API will block until the app has been restarted
    try {
      Object result = apiInstance.sitesRestartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, softRestart, synchronous);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesRestartSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **softRestart** | **Boolean**| Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app | [optional] |
| **synchronous** | **Boolean**| If true then the API will block until the app has been restarted | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesRestoreSite"></a>
# **sitesRestoreSite**
> RestoreResponse sitesRestoreSite(resourceGroupName, name, backupId, subscriptionId, apiVersion, request)

Restores a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup to restore
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RestoreRequest request = new RestoreRequest(); // RestoreRequest | Information on restore request
    try {
      RestoreResponse result = apiInstance.sitesRestoreSite(resourceGroupName, name, backupId, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesRestoreSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup to restore | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | |

### Return type

[**RestoreResponse**](RestoreResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesRestoreSiteSlot"></a>
# **sitesRestoreSiteSlot**
> RestoreResponse sitesRestoreSiteSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request)

Restores a web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String backupId = "backupId_example"; // String | Id of backup to restore
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RestoreRequest request = new RestoreRequest(); // RestoreRequest | Information on restore request
    try {
      RestoreResponse result = apiInstance.sitesRestoreSiteSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesRestoreSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **backupId** | **String**| Id of backup to restore | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request | |

### Return type

[**RestoreResponse**](RestoreResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesStartSite"></a>
# **sitesStartSite**
> Object sitesStartSite(resourceGroupName, name, subscriptionId, apiVersion)

Starts web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesStartSite(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesStartSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesStartSiteSlot"></a>
# **sitesStartSiteSlot**
> Object sitesStartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Starts web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesStartSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesStartSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesStopSite"></a>
# **sitesStopSite**
> Object sitesStopSite(resourceGroupName, name, subscriptionId, apiVersion)

Stops web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesStopSite(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesStopSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesStopSiteSlot"></a>
# **sitesStopSiteSlot**
> Object sitesStopSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Stops web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesStopSiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesStopSiteSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesSwapSlotWithProduction"></a>
# **sitesSwapSlotWithProduction**
> Object sitesSwapSlotWithProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Swaps web app slots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSlotEntity slotSwapEntity = new CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
    try {
      Object result = apiInstance.sitesSwapSlotWithProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesSwapSlotWithProduction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Operation is in progress |  -  |

<a id="sitesSwapSlotsSlot"></a>
# **sitesSwapSlotsSlot**
> Object sitesSwapSlotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Swaps web app slots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of source slot for the swap
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmSlotEntity slotSwapEntity = new CsmSlotEntity(); // CsmSlotEntity | Request body that contains the target slot name
    try {
      Object result = apiInstance.sitesSwapSlotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesSwapSlotsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of source slot for the swap | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| Request body that contains the target slot name | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Operation is in progress |  -  |

<a id="sitesSyncSiteRepository"></a>
# **sitesSyncSiteRepository**
> Object sitesSyncSiteRepository(resourceGroupName, name, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesSyncSiteRepository(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesSyncSiteRepository");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesSyncSiteRepositorySlot"></a>
# **sitesSyncSiteRepositorySlot**
> Object sitesSyncSiteRepositorySlot(resourceGroupName, name, slot, subscriptionId, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String name = "name_example"; // String | 
    String slot = "slot_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.sitesSyncSiteRepositorySlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesSyncSiteRepositorySlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**|  | |
| **name** | **String**|  | |
| **slot** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteAppSettings"></a>
# **sitesUpdateSiteAppSettings**
> StringDictionary sitesUpdateSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion, appSettings)

Updates the application settings of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    StringDictionary appSettings = new StringDictionary(); // StringDictionary | Application settings of web app
    try {
      StringDictionary result = apiInstance.sitesUpdateSiteAppSettings(resourceGroupName, name, subscriptionId, apiVersion, appSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteAppSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **appSettings** | [**StringDictionary**](StringDictionary.md)| Application settings of web app | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteAppSettingsSlot"></a>
# **sitesUpdateSiteAppSettingsSlot**
> StringDictionary sitesUpdateSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, appSettings)

Updates the application settings of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    StringDictionary appSettings = new StringDictionary(); // StringDictionary | Application settings of web app
    try {
      StringDictionary result = apiInstance.sitesUpdateSiteAppSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, appSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteAppSettingsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **appSettings** | [**StringDictionary**](StringDictionary.md)| Application settings of web app | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteAuthSettings"></a>
# **sitesUpdateSiteAuthSettings**
> SiteAuthSettings sitesUpdateSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, siteAuthSettings)

Updates the Authentication / Authorization settings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteAuthSettings siteAuthSettings = new SiteAuthSettings(); // SiteAuthSettings | Auth settings associated with web app
    try {
      SiteAuthSettings result = apiInstance.sitesUpdateSiteAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, siteAuthSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteAuthSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteAuthSettings** | [**SiteAuthSettings**](SiteAuthSettings.md)| Auth settings associated with web app | |

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteAuthSettingsSlot"></a>
# **sitesUpdateSiteAuthSettingsSlot**
> SiteAuthSettings sitesUpdateSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteAuthSettings)

Updates the Authentication / Authorization settings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteAuthSettings siteAuthSettings = new SiteAuthSettings(); // SiteAuthSettings | Auth settings associated with web app
    try {
      SiteAuthSettings result = apiInstance.sitesUpdateSiteAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteAuthSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteAuthSettingsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteAuthSettings** | [**SiteAuthSettings**](SiteAuthSettings.md)| Auth settings associated with web app | |

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteBackupConfiguration"></a>
# **sitesUpdateSiteBackupConfiguration**
> BackupRequest sitesUpdateSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, request)

Updates backup configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    BackupRequest request = new BackupRequest(); // BackupRequest | Information on backup request
    try {
      BackupRequest result = apiInstance.sitesUpdateSiteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteBackupConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | |

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteBackupConfigurationSlot"></a>
# **sitesUpdateSiteBackupConfigurationSlot**
> BackupRequest sitesUpdateSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Updates backup configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    BackupRequest request = new BackupRequest(); // BackupRequest | Information on backup request
    try {
      BackupRequest result = apiInstance.sitesUpdateSiteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteBackupConfigurationSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request | |

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteConfig"></a>
# **sitesUpdateSiteConfig**
> SiteConfig sitesUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteConfig siteConfig = new SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
    try {
      SiteConfig result = apiInstance.sitesUpdateSiteConfig(resourceGroupName, name, subscriptionId, apiVersion, siteConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | |

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteConfigSlot"></a>
# **sitesUpdateSiteConfigSlot**
> SiteConfig sitesUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig)

Update the configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteConfig siteConfig = new SiteConfig(); // SiteConfig | Request body that contains the configuration setting for the web app
    try {
      SiteConfig result = apiInstance.sitesUpdateSiteConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteConfig** | [**SiteConfig**](SiteConfig.md)| Request body that contains the configuration setting for the web app | |

### Return type

[**SiteConfig**](SiteConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteConnectionStrings"></a>
# **sitesUpdateSiteConnectionStrings**
> ConnectionStringDictionary sitesUpdateSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, connectionStrings)

Updates the connection strings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    ConnectionStringDictionary connectionStrings = new ConnectionStringDictionary(); // ConnectionStringDictionary | Connection strings associated with web app
    try {
      ConnectionStringDictionary result = apiInstance.sitesUpdateSiteConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, connectionStrings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteConnectionStrings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionStrings** | [**ConnectionStringDictionary**](ConnectionStringDictionary.md)| Connection strings associated with web app | |

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteConnectionStringsSlot"></a>
# **sitesUpdateSiteConnectionStringsSlot**
> ConnectionStringDictionary sitesUpdateSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionStrings)

Updates the connection strings associated with web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    ConnectionStringDictionary connectionStrings = new ConnectionStringDictionary(); // ConnectionStringDictionary | Connection strings associated with web app
    try {
      ConnectionStringDictionary result = apiInstance.sitesUpdateSiteConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionStrings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteConnectionStringsSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionStrings** | [**ConnectionStringDictionary**](ConnectionStringDictionary.md)| Connection strings associated with web app | |

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteLogsConfig"></a>
# **sitesUpdateSiteLogsConfig**
> SiteLogsConfig sitesUpdateSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, siteLogsConfig)

Updates the meta data for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteLogsConfig siteLogsConfig = new SiteLogsConfig(); // SiteLogsConfig | Site logs configuration
    try {
      SiteLogsConfig result = apiInstance.sitesUpdateSiteLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, siteLogsConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteLogsConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteLogsConfig** | [**SiteLogsConfig**](SiteLogsConfig.md)| Site logs configuration | |

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteLogsConfigSlot"></a>
# **sitesUpdateSiteLogsConfigSlot**
> SiteLogsConfig sitesUpdateSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteLogsConfig)

Updates the meta data for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteLogsConfig siteLogsConfig = new SiteLogsConfig(); // SiteLogsConfig | Site logs configuration
    try {
      SiteLogsConfig result = apiInstance.sitesUpdateSiteLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteLogsConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteLogsConfigSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteLogsConfig** | [**SiteLogsConfig**](SiteLogsConfig.md)| Site logs configuration | |

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteMetadata"></a>
# **sitesUpdateSiteMetadata**
> StringDictionary sitesUpdateSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion, metadata)

Updates the meta data for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    StringDictionary metadata = new StringDictionary(); // StringDictionary | Meta data of web app
    try {
      StringDictionary result = apiInstance.sitesUpdateSiteMetadata(resourceGroupName, name, subscriptionId, apiVersion, metadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteMetadata");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **metadata** | [**StringDictionary**](StringDictionary.md)| Meta data of web app | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteMetadataSlot"></a>
# **sitesUpdateSiteMetadataSlot**
> StringDictionary sitesUpdateSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, metadata)

Updates the meta data for web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    StringDictionary metadata = new StringDictionary(); // StringDictionary | Meta data of web app
    try {
      StringDictionary result = apiInstance.sitesUpdateSiteMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, metadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteMetadataSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **metadata** | [**StringDictionary**](StringDictionary.md)| Meta data of web app | |

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteRelayServiceConnection"></a>
# **sitesUpdateSiteRelayServiceConnection**
> RelayServiceConnectionEntity sitesUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RelayServiceConnectionEntity connectionEnvelope = new RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesUpdateSiteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteRelayServiceConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteRelayServiceConnectionSlot"></a>
# **sitesUpdateSiteRelayServiceConnectionSlot**
> RelayServiceConnectionEntity sitesUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String entityName = "entityName_example"; // String | The name by which the Hybrid Connection is identified
    String slot = "slot_example"; // String | The name of the slot for the web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RelayServiceConnectionEntity connectionEnvelope = new RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | The details of the Hybrid Connection
    try {
      RelayServiceConnectionEntity result = apiInstance.sitesUpdateSiteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteRelayServiceConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **entityName** | **String**| The name by which the Hybrid Connection is identified | |
| **slot** | **String**| The name of the slot for the web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| The details of the Hybrid Connection | |

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteSourceControl"></a>
# **sitesUpdateSiteSourceControl**
> SiteSourceControl sitesUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteSourceControl siteSourceControl = new SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
    try {
      SiteSourceControl result = apiInstance.sitesUpdateSiteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteSourceControl");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | |

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteSourceControlSlot"></a>
# **sitesUpdateSiteSourceControlSlot**
> SiteSourceControl sitesUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl)

Update the source control configuration of web app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteSourceControl siteSourceControl = new SiteSourceControl(); // SiteSourceControl | Request body that contains the source control parameters
    try {
      SiteSourceControl result = apiInstance.sitesUpdateSiteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteSourceControlSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| Request body that contains the source control parameters | |

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteVNETConnection"></a>
# **sitesUpdateSiteVNETConnection**
> VnetInfo sitesUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetInfo connectionEnvelope = new VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
    try {
      VnetInfo result = apiInstance.sitesUpdateSiteVNETConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteVNETConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteVNETConnectionGateway"></a>
# **sitesUpdateSiteVNETConnectionGateway**
> VnetGateway sitesUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetGateway connectionEnvelope = new VnetGateway(); // VnetGateway | The properties to update this gateway with.
    try {
      VnetGateway result = apiInstance.sitesUpdateSiteVNETConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteVNETConnectionGateway");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | |

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteVNETConnectionGatewaySlot"></a>
# **sitesUpdateSiteVNETConnectionGatewaySlot**
> VnetGateway sitesUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Updates the Virtual Network Gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. The only gateway that exists presently is \"primary\"
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetGateway connectionEnvelope = new VnetGateway(); // VnetGateway | The properties to update this gateway with.
    try {
      VnetGateway result = apiInstance.sitesUpdateSiteVNETConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteVNETConnectionGatewaySlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **gatewayName** | **String**| The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot; | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The properties to update this gateway with. | |

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSiteVNETConnectionSlot"></a>
# **sitesUpdateSiteVNETConnectionSlot**
> VnetInfo sitesUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network Connection or updates it&#39;s properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String name = "name_example"; // String | The name of the web app
    String vnetName = "vnetName_example"; // String | The name of the Virtual Network
    String slot = "slot_example"; // String | The name of the slot for this web app.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetInfo connectionEnvelope = new VnetInfo(); // VnetInfo | The properties of this Virtual Network Connection
    try {
      VnetInfo result = apiInstance.sitesUpdateSiteVNETConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSiteVNETConnectionSlot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The resource group name | |
| **name** | **String**| The name of the web app | |
| **vnetName** | **String**| The name of the Virtual Network | |
| **slot** | **String**| The name of the slot for this web app. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetInfo**](VnetInfo.md)| The properties of this Virtual Network Connection | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sitesUpdateSlotConfigNames"></a>
# **sitesUpdateSlotConfigNames**
> SlotConfigNamesResource sitesUpdateSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion, slotConfigNames)

Updates the names of application settings and connection string that remain with the slot during swap operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    SlotConfigNamesResource slotConfigNames = new SlotConfigNamesResource(); // SlotConfigNamesResource | Request body containing the names of application settings and connection strings
    try {
      SlotConfigNamesResource result = apiInstance.sitesUpdateSlotConfigNames(resourceGroupName, name, subscriptionId, apiVersion, slotConfigNames);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesUpdateSlotConfigNames");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **slotConfigNames** | [**SlotConfigNamesResource**](SlotConfigNamesResource.md)| Request body containing the names of application settings and connection strings | |

### Return type

[**SlotConfigNamesResource**](SlotConfigNamesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

